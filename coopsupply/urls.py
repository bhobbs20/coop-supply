from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('store/', include('store.urls')),
    path('search/', include('searchstore.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
