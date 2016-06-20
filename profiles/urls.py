from django.conf.urls import url

from . import views

urlpatterns = [
    # SINGULAR, the home route for the CURRENT user
    url(r'^$', views.profile_home, name="home"),
    # MULTIPLE, the profile page for ANY user
    url(r'^profiles(?P<pk>\d+)', views.profile_detail, name='detail'),
]


#where do I tell it to run the function from view-
# aka how does it know which function to run? aka how do I add profile_detail to view