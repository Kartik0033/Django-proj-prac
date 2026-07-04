from django.urls import path
from home.views import home,contact,DynamicResponse,thankyou,search

urlpatterns = [
    path('',home),
    path('contact/', contact ),
    path('dynamic/<number>',DynamicResponse),
    path('thankyou/',thankyou),
    path("search/", search)
]