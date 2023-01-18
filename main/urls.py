from django.urls import path
from .views import (
    index, news, updateView, deleteView,
    student,student_updateView,student_deleteView,
)

app_name = 'main'

urlpatterns = [
    path('index/', index, name='index'),
    path('news/<int:pk>/', news, name='news'),
    path('news/', news, name='news'),
    path('update/<int:id>/', updateView, name='update'),
    path('delete/<int:id>', deleteView, name='delete'),
    ###########################################
    path('student/', student, name='student'),
    path('student_update/<int:id>/', student_updateView, name='student_update'),
    path('student_delete/<int:id>', student_deleteView, name='student_delete'),
]