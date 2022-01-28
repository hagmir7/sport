
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts.urls import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
     path('summernote/', include('django_summernote.urls')),
    path('', index, name='home' )
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)