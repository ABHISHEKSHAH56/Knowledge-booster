from django.urls import path
from . import views


urlpatterns = [
        path('', views.new),
        path('tag/<slug:tag_slug>/', views.new, name='new_by_tag'),
        path('<int:id>/<slug:slug>/', views.detail , name='detail'),
        path('search', views.post_search, name='post_search'),
        path('suscriber', views.suscriber),
        path('add',views.addcom),
        path('about',views.index),
        path('contact', views.contct),

        
         
]
