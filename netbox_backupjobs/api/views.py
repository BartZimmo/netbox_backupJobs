from netbox.api.viewsets import NetBoxModelViewSet

from netbox_backupjobs.models import BackupJob
from netbox_backupjobs.api.serializers.backupjobs import BackupJobSerializer
from netbox_backupjobs.filtersets.backupjobs import BackupJobFilterSet


class BackupJobViewSet(NetBoxModelViewSet):
    """API viewset for managing Backup Jobs"""
    queryset = BackupJob.objects.all()
    serializer_class = BackupJobSerializer
    filterset_class = BackupJobFilterSet
