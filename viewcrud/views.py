from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone 
#models.py안의 pub_Date를 자동으로 받아오기 위해 그냥 유틸 가져오기
from .models import Blog
from .forms import NewBlog
#우리가 만든 함수들을 쓰기 위해 import해오기

def welcome(request):
    return render(request, 'viewcrud/index.html')
#welcome함수는 viewcrud의 index.html을 띄워주는 함수이다

def read(request):
    blogs = Blog.objects.all()
    #Blog안의 모든 객체 가져와서 보여줄거임! 는 blog 변수안에 담기
    return render(request, 'viewcrud/funccrud.html',{'blogs':blogs})
    #funccrud.html에 이 read함수의 내용을 담아 return 하겠다
    #{'blogs':blogs} : 사전형 객체
    #이제 viewcrud/funccrud.html만들자


def create(request):
    #새로운 데이터(블로그 글) 저장하는 역할 <-request가 post타입일 때!
    if request.method == 'POST':
        #입력된 블로그 글들을 저장해라
        form = NewBlog(request.POST) 
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    #글쓰기 페이지를 띄워주는 역할 <-request가 get타입일 때!
    else:
        #단순히 입력받을 수 있는 FORM을 띄워줘라
        form = NewBlog()
        return render(request, 'viewcrud/new.html',{'form':form})

def update(request, pk):
    #수정하고 싶은 특정 블로그글을 가져온다
    blog = get_object_or_404(Blog, pk=pk)
    #해당하는 블로그글의 번호에 맞는 입력공간을 가져온다
    #(어떻게 수정할지 입력할 공간이 있어야하니까)
    form = NewBlog(request.POST, instance=blog)
    #pk번째의 블로그글을 담은 instance(객체) 를 form에 입력한다
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'viewcrud/new.html', {'form':form})
    
def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    #삭제하고 싶은 특정 블로그글을 가져온다
    #Blog라는 모델에 해당하는 글인데, pk값은 pk이다.
    blog.delete()
    return redirect('home')
