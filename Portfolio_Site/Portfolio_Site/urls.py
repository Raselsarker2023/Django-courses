from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),  
    path('accounts/', include('accounts.urls')),  
    path('firstapp/', include('firstapp.urls')),  
    path('blog/', include('blog.urls')),
    path('projects/', include('projects.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
