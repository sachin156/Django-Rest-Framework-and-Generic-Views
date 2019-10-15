from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('languages',views.LanguageView)
router.register('Paradigm',views.ParadigmView)
router.register('Programmer',views.ProgrammerView)

urlpatterns = [
    path('',include(router.urls))
]
