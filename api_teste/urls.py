
from django.contrib import admin
from django.urls import path, include
from django.urls import SeuModeloListCreateView

urlpatterns = [
    path('api/seu-modelo/', SeuModeloListCreateView.as_view(), name='seu-modelo-list-create'),
    path('admin/', admin.site.urls),
    path('api/', include('test_api.urls')),
]
