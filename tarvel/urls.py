from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Ice Cream Center"
admin.site.site_title = "gyats_icecream"
admin.site.index_title = " welcome to gyats Ice Cream"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls'))
]
