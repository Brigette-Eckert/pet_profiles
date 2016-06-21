from django.shortcuts import render, get_object_or_404

from profiles.models import Human, Pet


def profile_home(request):
    human = Human.objects.all()
    pet = Pet.objects.all()
    return render(request, "profiles/profile_list.html", {"human": human, "pet": pet})

#template not loading  anymore

def profile_detail(request, pk):
    #check if user is logged in, if so show, if not take to login/signup screen
    profile = get_object_or_404(Human, pk=pk)
    return render(request, "profiles/profile_detail.html", {"profile": profile})