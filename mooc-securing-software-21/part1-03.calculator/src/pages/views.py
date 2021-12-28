from django.http import HttpResponse

# Create your views here.


def get_arguments(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    return (first, second)


def addPageView(request):
    (first, second) = get_arguments(request)
    return HttpResponse(str(first + second))


def multiplyPageView(request):
    (first, second) = get_arguments(request)
    return HttpResponse(str(first * second))
