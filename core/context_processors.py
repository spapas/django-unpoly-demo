from django.conf import settings


def default_cp(request):

    return {
        "debug": settings.DEBUG,
        "up": request.up,

    }
