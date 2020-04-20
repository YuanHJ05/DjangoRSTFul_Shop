"""mxshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path, include

# 配置媒体文件夹
from django.views.static import serve
from django.conf import settings

# 配置ckeditor
from django.conf import settings
from django.conf.urls.static import static

# 配置xadmin

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('xadmin/', xadmin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('goods/', include('goods.urls', namespace='goods')),
    path('trade/', include('trade.urls', namespace='trade')),

    # 配置媒体文件的路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # 配置ckeditor图片上传路径，固定写法
    path('ckeditor', include('ckeditor_uploader.urls')),

]
# 开发环境这样写，部署的时候不这样写
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
