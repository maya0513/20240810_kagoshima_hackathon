from django.urls import path
from .views import index, tab1, tab2, tab3, register_data
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('tab1/', tab1, name='tab1'),
    path('register_data/', register_data, name='register_data'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
