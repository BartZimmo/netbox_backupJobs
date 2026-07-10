from netbox.api.fields import SerializedPKRelatedField
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from ipam.api.serializers import IPAddressSerializer

from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.api.serializers.backupjobs import BackupJobSerializer


class BackupCopyJobSerializer(NetBoxModelSerializer):
    backup_jobs = SerializedPKRelatedField(
        queryset=BackupJob.objects.all(),
        serializer=BackupJobSerializer,
        nested=True,
        required=False,
        many=True,
    )
    backup_server_ip = IPAddressSerializer(
        nested=True,
        required=False,
        allow_null=True,
    )
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_backupjobs-api:backupcopyjob-detail')

    class Meta:
        model = BackupCopyJob
        fields = '__all__'
        brief_fields = (
            'id', 'url', 'display', 'name', 'status',
        )
