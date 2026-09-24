from django.urls import path

from apps.waste.api.views import WasteCategoryView, WasteUpdateDetailDeleteView
from apps.waste.api.views import WasteCategoryCreateView, WasteCategoryDeleteView   

urlpatterns = [
    path('', WasteCategoryView.as_view()),
     path('category', WasteCategoryView.as_view()),
     path('category/<int:pk>', WasteUpdateDetailDeleteView.as_view()),
     path( 'category/create/', WasteCategoryCreateView.as_view()),
     path('category/<int:pk>/delete/',WasteCategoryDeleteView.as_view()),
     
]