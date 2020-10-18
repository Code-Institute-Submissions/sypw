from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


@login_required
def holiday(request):
    """ a view to show 'book holiday' page"""

    return render(request, 'holiday/holiday.html')


def see_holiday(request):
    """ a view for the form to book holiday"""
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
        content = "  Message:  " + message + ". In dates: " + dates

        context = {
            'message_name': message_name,
            'message_phone': message_phone,
            'message_email': message_email,
            'dates': dates,
            'message': message,
            'content': content,
        }

        subject = message_name + " " + message_phone
        from_email = message_email

        # send an email function
        send_mail(
            subject,
            content,
            from_email,
            ['stan.kazovski@yahoo.com', settings.DEFAULT_FROM_EMAIL, ],
            fail_silently=False,)

        return render(request, 'holiday/see_holiday.html', context)

    else:
        return render(request, 'holiday/see_holiday.html')
