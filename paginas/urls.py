from django.urls import path
from .views import TrabalhoPageView, ListadeEventosPageView, ONGsDeAnimaisPageView, ONGsDeAnimaisPedroIIPageView, oqEPageView, voluntariadoPageView
urlpatterns = [

    path('', TrabalhoPageView.as_view() , name ='trabalho'),
    path('/ListadeEventos/', ListadeEventosPageView.as_view() , name ='ListadeEventos'),
    path('/ONGsDeAnimais/', ONGsDeAnimaisPageView.as_view() , name ='ONGsDeAnimais'),
    path('/ONGsDeAnimaisPedroII/', ONGsDeAnimaisPedroIIPageView.as_view() , name ='ONGsDeAnimaisPedroII'),
    path('/oqE/', oqEPageView.as_view() , name ='oqE'),
    path('/voluntariado/', voluntariadoPageView.as_view() , name ='voluntariado'),

]