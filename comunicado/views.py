from django.shortcuts import render


def comunicado(request):
    """ a view to show messages page"""

    return render(request, 'comunicado/comunicado.html')