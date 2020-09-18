from django.shortcuts import render


def holiday(request):
    """ a view to show 'book holiday' page"""

    return render(request, 'holiday/holiday.html')

def see_holiday(request):
    """ a view to see all holidays"""

    return render(request, 'holiday/see_holiday.html')
