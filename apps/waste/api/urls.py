from django.urls import path

from apps.waste.api.views import WasteCategoryView
urlpatterns = [
    path('', WasteCategoryView.as_view())
]