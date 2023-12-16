from django.urls import path
from . import views


#http://127.0.0.1:8000

urlpatterns=[
  path('', views.index, name='index'),
  path('project', views.project, name='project'),
  path('about', views.about, name='about'),
  path('galeri', views.galeri, name='galeri'),
  path('call', views.call, name='call'),
  path('iletisim', views.iletisim, name='iletisim'),
  path('duyuru', views.duyuru, name='duyuru'),
  path('login', views.login, name='login'),
  path('signin', views.signin, name='signin'),
  path('curlingtr', views.curlingtr, name='curlingtr'),
  path('sportstr', views.sportstr, name='sportstr'),
  path('duyuru1', views.duyuru1, name='duyuru1'),
 
  
]

# urlpatterns=[
#   path('', views.index, name='index'),
#   path('about', views.about, name='about'),
# ]