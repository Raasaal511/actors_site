from django.conf.urls.static import static
from django.urls import path, include

from actors.views import page_not_found
from coolsite import settings

from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('actors.urls')),


]

handler404 = page_not_found

if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))

    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
