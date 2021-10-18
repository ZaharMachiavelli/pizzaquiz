
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizes.urls', namespace='quizes'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)