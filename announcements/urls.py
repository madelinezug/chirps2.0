from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:announcement_id>/',views.detail,name='detail'),
    path('submit/',views.submit,name='submit'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('saved/',views.saved,name='saved'),
    path('review_tags/',views.approve_tag,name='approve_tag'),
    path('search_tags/',views.tag_search,name='search_tags'),
]
