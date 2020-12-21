from django.shortcuts import render


def homePage(request):
    return render(request,'Home.html')


def AboutPage(request):
    return render(request,'AboutPage.html')