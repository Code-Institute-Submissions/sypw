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
            'message_name', [
                'message_phone',
                'message',
                'start_date',
                'end_date',
            ],
            'message_email',
            ["stan.kazovsky@yahoo.com"],
            fail_silently=True,
        )

        context = {
            'message_name': message_name,
            'message_phone': message_phone,
            'message_email': message_email,
            'start_date': start_date,
            'end_date': end_date,
            'message': message,
        }

        return render(request, 'holiday/see_holiday.html', context)

    else:
        return render(request, 'holiday/see_holiday.html')
