from django.urls import path,include
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.base,name='base' ),
    path('home/',views.home,name='home' ),
    path('products/',views.products,name='Products' ),
    path('services/',views.services,name='Services' ),
    path('blogs/',views.blogs,name='Blogs' ),
    path('blogs/<blogs_id>',views.blogs_pages,name='Blogs_pages' ),
    path('interior/',views.interior,name='Interior' ),
    path('exterior/',views.exterior,name='Exterior' ),
    path('base_paint/',views.base_paint,name='Base_paint' ),
    path('choose_color/',views.choose_color,name='Choose_color' ),

    # path('about_us/',views.about_us,name='about_us' ),
    path('contact_us/',views.contact_us,name='Contact_us' ),
    # path('login/',views.Login,name='login' ),
    path('form/',views.form,name='Form' ),
    path('putty_services/',views.putty_services),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)