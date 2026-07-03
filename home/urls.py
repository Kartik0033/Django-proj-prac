from django.urls import path
from home.views import home,contact,DynamicResponse,thankyou

urlpatterns = [
    path('',home),
    path('contact/', contact ),
    path('dynamic/<number>',DynamicResponse),
    path('thankyou/',thankyou)
]