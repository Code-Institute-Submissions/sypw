from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def holiday(request):
    """ a view to show 'book holiday' page"""

    return render(request, 'holiday/holiday.html')


def see_holiday(request):
    """ a view to see all holidays"""
    if request.method == "POST":
        message_name = str(request.POST['your-name'])
        message_phone = request.POST['your-phone']
        message_email = request.POST['your-email']
        dates = str([
            str(request.POST['start-date']),
            str(request.POST['end-date']),
        ])
        # end_date = request.POST['end-date']
        message = request.POST['message']
        content = " Phone: " + message_phone +  "  Message:  " + message +  " In dates: " + dates

        context = {
            'message_name': message_name,
            'message_phone': message_phone,
            'message_email': message_email,
            # 'start_date': start_date,
            # 'end_date': end_date,
            'dates': dates,
            'message': message,
            'content': content,
        }

        subject = message_name,
        body = content
        from_email = message_email


        # send an email function
        send_mail(
            subject,
            body,
            from_email,
            ['stan.kazovski@yahoo.com', settings.DEFAULT_FROM_EMAIL, ],
            fail_silently=False,)

        # send_mail(
        #     f"New message from {request.POST.get('message_name', 'message_email')}", # subject of the email, contains the user's email you can respond to
        #     request.POST.get('start_date', 'end_date', ), # body of the email
        #     settings.DEFAULT_FROM_EMAIL, # Some email you want all your messages to be from, e.g. contact@mysite.com
        #     ['myemail@gmail.com'] # where you want the contact email to be sent
        # )

        return render(request, 'holiday/see_holiday.html', context)

    else:
        return render(request, 'holiday/see_holiday.html')
