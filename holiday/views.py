from django.shortcuts import render
from django.core.mail import send_mail


def holiday(request):
    """ a view to show 'book holiday' page"""

    return render(request, 'holiday/holiday.html')


def see_holiday(request):
    """ a view to see all holidays"""
    if request.method == "POST":
        message_name = request.POST['your-name']
        message_phone = request.POST['your-phone']
        message_email = request.POST['your-email']
        start_date = request.POST['start-date']
        end_date = request.POST['end-date']
        message = request.POST['message']

        # send an email function
        send_mail(
            message_name,
            message_phone,
            message_email,
            message,
            start_date,
            end_date,
            ["stan.kazovsky@yahoo.com"]
        )

        return render(request, 'holiday/see_holiday.html', {})
    else:
        return render(request, 'holiday/see_holiday.html')
