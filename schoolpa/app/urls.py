from django.urls import path,include
from . import views
urlpatterns = [
  path('',views.home,name='home') ,
  path('studentspage/<int:pk>',views.students_page,name='students_page') ,
  path('showstudents',views.showstudents,name='showstudents') ,
  path('sendmsg',views.sendmsg,name='sendmsg') ,
  path('student_attendance',views.student_attendance,name='student_attendance') ,
  path('create_student',views.create_student,name='create_student') ,
  path('create_student_ajax',views.create_student_ajax,name='create_student_ajax') ,
  path('login/',views.login,name='login')
]
