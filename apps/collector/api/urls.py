from django.urls import path
from apps.collector.api.views import CollectionRequestView
from apps.collector.api.views import CollectionRequestView, CollectionAssignmentView

urlpatterns = [
    path('assignments/', CollectionRequestView.as_view()),
    path('assign/<int:pk>/', CollectionAssignmentView.as_view()),
]