from django.shortcuts import render


def holiday(request):
    """ a view to show holidays page"""

    return render(request, 'holiday/holiday.html')