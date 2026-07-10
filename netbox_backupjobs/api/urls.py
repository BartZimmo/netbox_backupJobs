from netbox.api.routers import NetBoxRouter
from django.urls import path, include
from netbox_backupjobs.api.views import BackupJobViewSet, BackupCopyJobViewSet

app_name = 'netbox_backupjobs'

router = NetBoxRouter()
router.register('backupjobs', BackupJobViewSet)
router.register('backupcopyjobs', BackupCopyJobViewSet)


urlpatterns = [
    path('', include(router.urls)),
]