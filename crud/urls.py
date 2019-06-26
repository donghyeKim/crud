
from django.contrib import admin
from django.urls import path, include
import viewcrud.urls
import viewcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewcrud.views.welcome, name="welcome"),
    #url뒤에 아무것도 입력하지 않았을때(처음 실행했을 떄)
    #viewcrud안의 views안의 welcome을 실행시켜라~
    path('funccrud/', include(viewcrud.urls))
    
]
