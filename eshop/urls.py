from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


from products import urls as product_urls
from profiles import urls as profile_urls
from rating import urls as rating_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(product_urls, namespace="product")),
    path("", include(profile_urls, namespace="profile")),
    path("", include(rating_urls, namespace="rating")),
    re_path("", include('allauth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
