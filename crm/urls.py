from django.contrib import admin
from django.urls import path, include  # 👈 include is important

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),  # 👈 this tells Django to use your app’s urls
]
