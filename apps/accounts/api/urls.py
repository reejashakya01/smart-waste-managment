from django.urls import path
from apps.accounts.api.views import user_list

urlpatterns = [
    path('list/', user_list, name='user-list'),
]