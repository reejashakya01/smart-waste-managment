from django.urls import path
from apps.waste_collection.api.views import UserCollectionRequestView


urlpatterns = [
    path(
        "collection-requests/",
        UserCollectionRequestView.as_view(),
        name="user-collection-requests",
    ),
]