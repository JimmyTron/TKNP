from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header ="TKNP STUDENTS CLEARANCE PORTAL"
admin.site.index_title ="Clearance Portal"
admin.site.site_title ="Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
]

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""