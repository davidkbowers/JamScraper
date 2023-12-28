from django.http import HttpResponse


def health_check(request):
    # just return anything with status code 200
    return HttpResponse("OK", status=200)
