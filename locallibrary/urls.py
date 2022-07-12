from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from catalog import views as catalog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    # path('', catalog_views.),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)