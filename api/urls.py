from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path(
         'v2/foods/<int:pk>/', views.FoodDetail.as_view()),
    path(
        'v2/foods/',views.FoodList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)