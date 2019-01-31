from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from cushion_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    path('btre/', include('btre_pages.urls')),
    path('btre/listings', include('btre_listings.urls')),
    path('btre/accounts', include('btre_accounts.urls')),
    path('btre/contacts', include('btre_contacts.urls')),

    path('cushion/shop/', include('cushion_shop.urls')),
    path('cushion/cart/', include('cushion_cart.urls')),
    path('cushion/search/', include('cushion_search.urls')),
    path('cushion/order/', include('cushion_order.urls')),

    path('account/create', views.signupView, name='signup'),
    path('account/login', views.signinView, name='signin'),
    path('account/logout/', views.signoutView, name='signout'),

    path('sloth/', include ('sloth_shop.urls')),
    path('sloth/cart', include('sloth_cart.urls')),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
