
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import homepage.views
import news.views
urlpatterns = [
    path('', homepage.views.homepage, name="homepage"),
    path('news/', news.views.news, name="news"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
