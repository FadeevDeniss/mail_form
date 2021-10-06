from django.urls import path, include
from mail.views import feedback, thanks, index


urlpatterns = [
    path('', feedback),
    path('Thanks/', thanks),
    path('mail/', index)
]