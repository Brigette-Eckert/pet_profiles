from django.shortcuts import render, get_object_or_404

from profiles.models import Human


def profile_home(request):
    return render(request, "profiles/profile_list.html", {"profile": {}})


def profile_detail(request, pk):
    # check if the user is logged in. user is in "request.user"
    # profile = Human.objects.get(user=request.user)
    profile = get_object_or_404(Human, pk=pk)
    return render(request, "profiles/profile_detail.html", {"profile": {}})

