from django.urls import path
from apps.collector.api.views import CollectionRequestView

urlpatterns = [
    path('assignments/', CollectionRequestView.as_view()),
]