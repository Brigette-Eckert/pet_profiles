from django.shortcuts import render, get_object_or_404

from profiles.models import Human, Pet


def profile_home(request):
    profiles = Human.objects.all()
    return render(request, "profiles/profile_list.html", {"profiles": {profiles}})


def profile_detail(request, pk):
    # check if the user is logged in. user is in "request.user"
    human = Human.objects.get(user=request.user)
    profile = get_object_or_404(Human, pk=pk)#add cat 404 error
    return render(request, "profiles/profile_detail.html", {"profile": {profile}})

# need to pass in models- in the dicts- so it can find class.atrribute