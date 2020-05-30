from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('thanks/',views.ThankView.as_view(),name="thank_you"),
    path('test/',views.TestView.as_view(),name='test'),
    

]
