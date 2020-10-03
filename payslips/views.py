from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def payslips(request):
    """ a view to show payslips page"""

    return render(request, 'payslips/payslips.html')
