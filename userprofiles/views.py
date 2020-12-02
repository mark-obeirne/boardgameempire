from django.shortcuts import render


def profile(request):
    """ Display the user's profile """
    return render(request, "userprofiles/profile.html")