from django.urls import path
from app1 import views
app_name='app1'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('sample/',views.sample,name='sample'),
]