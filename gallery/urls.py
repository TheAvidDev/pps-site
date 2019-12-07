from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contact/', views.contact, name='contact'),
    path('c/<uuid:category_id>', views.category, name='category'),
    path('g/<uuid:gallery_id>', views.gallery, name='gallery'),
    path('media/<uuid:category_id>/<uuid:gallery_id>/<file>', views.serve_gallery_image, name='serve_gallery_image'),
    path('media/<uuid:category_id>/<uuid:gallery_id>/thumbnails/<file>', views.serve_gallery_thumbnail, name='serve_gallery_thumbnail'),
    path('media/gallery_thumbnails/<file>', views.serve_thumbnail, name='serve_thumbnail')
]
