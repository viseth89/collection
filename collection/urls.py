from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('btre/', include('btre_pages.urls')),
    path('btre/listings', include('btre_listings.urls')),
    path('btre/accounts', include('btre_accounts.urls')),
    path('btre/contacts', include('btre_contacts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
