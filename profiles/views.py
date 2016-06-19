from django.shortcuts import render, get_object_or_404

from profiles.models import Human


def profile_home(request):
    # check if the user is logged in. user is in "request.user"
    # profile = Human.objects.get(user=request.user) # need to set the pk to the current user pk
    return render(request, "profiles/profile_detail.html", {"profile": {}})


def profile_display(request, pk):
    profile = get_object_or_404(Human, pk=pk)
    return None # return a new template, profile_display, send it "profile" in a kwarg

