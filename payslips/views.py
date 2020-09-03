from django.shortcuts import render


def payslips(request):
    """ a view to show payslips page"""

    return render(request, 'payslips/payslips.html')
