from django.urls import path
from .views import MovieApiView,MovieDetail


urlpatterns = [

    path('',MovieApiView.as_view()),
    path('<int:pk>/',MovieDetail.as_view()),
]
