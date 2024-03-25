from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello World");

def say_hello_html(request):
    return render(request, "playground/hello.html", context={'name': '지우야','greeting':'안녀엉~'});
def say_bye_html(request):
    context = {
        'singer': '데이식스',
        'title' : '해와 달 처럼',
    }
    return render(request, "playground/bye.html", context = context);

