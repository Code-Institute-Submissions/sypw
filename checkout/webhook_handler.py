from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle an unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        order_exist = False
        try:
            order = Order.objects.get(
                full_name__iexact=billing_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=billing_details.phone,
                postcode__iexact=billing_details.postcode,
                street_address1__iexact=billing_details.line1,
                street_address2__iexact=billing_details.line2,
                town_or_city__iexact=billing_details.city,
                county__iexact=billing_details.state,
                country__iexact=billing_details.country,
                grand_total=grand_total
            )
            order_exist = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    postcode=billing_details.postcode,
                    street_address1=billing_details.line1,
                    street_address2=billing_details.line2,
                    town_or_city=billing_details.city,
                    county=billing_details.state,
                    country=billing_details.country,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR {e}',
                        status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Success! Order already in database!',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


    # def send_confirmation_email(self, order):
    #     """Sent the user confirmation email"""
    #     client_email = order.email
    #     subject = render_to_string(
    #         'checkout/confirmation_emails/confirmation_email_subject.txt',
    #         {'order': order})
    #     body = render_to_string(
    #         'checkout/confirmation_emails/confirmation_email_body.txt',
    #         {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    #     send_mail(
    #         subject,
    #         body,
    #         settings.DEFAULT_FROM_EMAIL,
    #         [client_email]
    #     )
