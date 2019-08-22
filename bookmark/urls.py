from django.urls import path,include

#url - 주소(정규표현식으로 주소를 표현),뷰
#path - 주소(기존 정규표현식을 간단히 표현할수 있게 해주는 컨버터),뷰
#re_path - 주소(정규표현식으로 주소를 표현)
# 뷰는 함수형,클래스형 두종류로 만들수 있음.
# 결국은 장고에서는 모든 뷰는 함수형으로 동작하게 되어있다.
from .views import BookmarkList,BookmarkCreate,BookmarkUpdate,BookmarkDelete
#r"update/(?P<pk>\d+"
urlpatterns =[
    path("delete/<int:pk>",BookmarkDelete.as_view(),name = 'bookmark_delete'),
    path("update/<int:pk>",BookmarkUpdate.as_view(),name = 'bookmark_update'),
    path('write/',BookmarkCreate.as_view(),name = 'bookmark_create'),
    path('',BookmarkList.as_view(),name = 'bookmark_list'),

]