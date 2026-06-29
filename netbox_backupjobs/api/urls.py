from netbox.api.routers import NetBoxRouter
from django.urls import path, include
from netbox_backupjobs.api.views import BackupJobViewSet

app_name = 'netbox_backupjobs'

router = NetBoxRouter()
router.register('backupjobs', BackupJobViewSet)


urlpatterns = [
    path('', include(router.urls)),
]