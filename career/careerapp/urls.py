from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^grades/', views.EnterGrades.as_view(), name='enter_grades'),
    #url(r'^programmes/*$', views.dislay_programmes, name='programmes'),
    url(r'^interests/', views.ChooseInterests.as_view(), name='career_interests'),
    url(r'^self_assessment/', views.self_assessment, name='self_assessment')
]
