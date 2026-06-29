from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from netbox_backupjobs.models import BackupJob

class BackupJobSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_backupjobs-api:backupjob-detail')
    class Meta:
        model = BackupJob
        fields = (
            'id', 'name', 'status', 'description', 'comments',
        )
        # These fields define what should be included when the serializer is used with nested=True.
        brief_fields = (
            'id', 'name', 'status',
        )