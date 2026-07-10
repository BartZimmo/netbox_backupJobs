from netbox.api.viewsets import NetBoxModelViewSet

from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.api.serializers.backupjobs import BackupJobSerializer
from netbox_backupjobs.api.serializers.backupcopyjobs import BackupCopyJobSerializer
from netbox_backupjobs.filtersets.backupjobs import BackupJobFilterSet
from netbox_backupjobs.filtersets.backupcopyjobs import BackupCopyJobFilterSet


class BackupJobViewSet(NetBoxModelViewSet):
    """API viewset for managing Backup Jobs"""
    queryset = BackupJob.objects.all()
    serializer_class = BackupJobSerializer
    filterset_class = BackupJobFilterSet


class BackupCopyJobViewSet(NetBoxModelViewSet):
    """API viewset for managing Backup Copy Jobs"""
    queryset = BackupCopyJob.objects.all()
    serializer_class = BackupCopyJobSerializer
    filterset_class = BackupCopyJobFilterSet
