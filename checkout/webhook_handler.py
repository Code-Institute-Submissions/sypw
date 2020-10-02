from django.http import HttpResponse


class StripeWH_Handler:
    """This one will handle webhooks from stripe"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle all unexpected events"""
        return HttpResponse(
            content=f'Unhandled webhook recived: {event["type"]}',
            status=200)

    def handle_payment_event_succeeded(self, event):
        """ Handle all payment succeeded events"""
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)

    def handle_payment_event_failed(self, event):
        """ Handle all failed payment events"""
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)

    