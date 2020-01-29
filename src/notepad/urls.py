from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from notes.views import note_list_view, finish_item, delete_item, not_finish_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', note_list_view, name="note_list"),
    path('finish-item/<id>', finish_item, name="finish-item"),
    path('not-finish-item/<id>', not_finish_item, name="not-finish-item"),
    path('delete-item/<id>', delete_item, name="delete-item"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

