from django.urls import path
from . import views

urlpatterns=[
    path ('api/groups/', views.groups, name='groups'),
    path ('api/groups/<int:id>', views.group, name='group'),
]