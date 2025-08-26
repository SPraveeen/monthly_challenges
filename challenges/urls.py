from django.urls import path
from .import views

urlpatterns = [
    path('<int:month>',views.monthyly_challenges_by_number),
    path('<str:month>',views.monthly_challenges)
]

