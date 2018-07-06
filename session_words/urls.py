from django.conf.urls import url, include#Don't forget to import include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.session_words_app.urls'))
]
