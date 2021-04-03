from django.urls import path
from app2 import views
app_name='app2'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('index/',views.index,name='index'),
    path('sample/',views.sample,name='sample'),
]