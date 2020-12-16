from django.shortcuts import render


def about_us(request):
    return render(request, "about/about.html")


def loyalty(request):
    return render(request, "about/loyalty.html")


def returns(request):
    return render(request, "about/returns.html")
