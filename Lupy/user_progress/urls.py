from django.urls import path
from . import views

app_name = "user_progress"

urlpatterns = [
    path('', views.home, name='home'),
    path('add_skills/', views.add_skills, name='add_skills'),
    path('remove_skills/<int:id>', views.remove_skills, name='remove_skills'),
    path('edit_skills/<int:id>', views.edit_skills, name='edit_skills')

]