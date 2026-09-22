from django.urls import path
from apps.address.api.views import address_list
from apps.address.api.views import address_list, add_address, address_update, address_delete
urlpatterns = [
    path('user',address_list),
    path('create',add_address),
    path('update/<int:id>',address_update),
    path('delete/<int:id>',address_delete),

]