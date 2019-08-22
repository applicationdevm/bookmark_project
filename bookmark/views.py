from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

#def bookmarkList(request):
    #object_list = Bookmark.objects.all
    #return render(request,"bookmark/bookmark_list.html",{'object': object})

class BookmarkList(ListView):
    model = Bookmark

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name','url','description']
    success_url = reverse_lazy('bookmark_list')

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['description']
    success_url = reverse_lazy('bookmark_list')

class BookmarkDelete(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark_list')
    template_name_suffix = "_delete"
    #template_name = 'bookmark/bookmark delete.html'


# 앱/모델명_list.html을 랜더링하겠다.
# 앱/모델명_form.html을 랜더링하겠다.
# 앱/모델명_detail.html을 랜더링하겠다.
# 앱/모델명_confirm_delete.html을 랜더링하겠다.

#만약에 뷰애서 출력할 모델 데이터가 있다면
#단일 객체를 보여줘야하는 경우 : object
#복수 객체를 보야줘야하는 경우 : object_list
# Create your views here.
