from django.urls import path

from apps.waste.api.views import WasteCategoryView, WasteUpdateDetailDeleteView
urlpatterns = [
    path('', WasteCategoryView.as_view()),
     path('category', WasteCategoryView.as_view()),
    path('category/<int:pk>', WasteUpdateDetailDeleteView.as_view())
]