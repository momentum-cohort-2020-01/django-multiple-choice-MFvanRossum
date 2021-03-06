"""snipit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile, name = 'profile'),
    path('snippets/library/', views.library, name='library'),
    path('user/<int:pk>', views.other_user, name = 'other-user'),
    path('accounts/', include('registration.backends.simple.urls'), name='login'),
    # path('accounts/', include('registration.backends.default.urls'), name = 'login'),
    path('snippets/new/', views.new_snippet, name = 'new-snippet'),
    path('snippets/edit/<int:pk>', views.edit_snippet, name='edit-snippet'),
    path('snippets/delete/<int:pk>', views.delete_snippet, name = 'delete-snippet'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
