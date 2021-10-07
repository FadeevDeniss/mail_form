from django.urls import path, include
from mail.views import feedback, thanks, index, get_mail


urlpatterns = [
    path('', feedback),
    path('Thanks/', thanks),
    path('mail/', index),
    path('mail/<int:mail_id>/', get_mail)
]