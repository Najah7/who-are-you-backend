
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 管理者 or 開発者用 
    path("admin/", admin.site.urls),
    # 認証用
    path('', include('djoser.urls.authtoken'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)