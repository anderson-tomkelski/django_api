from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contents import views

urlpatterns = [
    path('contents/', views.ContentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
