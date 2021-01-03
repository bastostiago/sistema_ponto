from django.http import HttpResponse


def index(request):
    return HttpResponse("Esta é a pagina principal do registro de ponto")