from django.urls import path
from . import views

urlpatterns=[
    path('', views.read, name="home"),
    path('newblog/', views.create, name='newblog'),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
]

#기본 프로젝트의 urls에서 이 url을 include 받으니
#예를 들어서 funccrud/newblog/하면 create함수가 뜬당.
# read,create,update,delete는 views 에 정의해뒀음
#이제 models.py ㄱㄱ (model=데이터 형식 정의)