from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # ------------------------------------------------------------------
    path('superuser/', include('superadmin.urls')),
    path('user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('', include('accounts.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
