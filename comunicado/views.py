from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def comunicado(request):
    """ a view to show messages page"""

    return render(request, 'comunicado/comunicado.html')