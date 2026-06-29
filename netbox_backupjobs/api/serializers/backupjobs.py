from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from virtualization.api.serializers import (
    VirtualMachineSerializer,
    ClusterSerializer,
)

from netbox_backupjobs.models import BackupJob

class BackupJobSerializer(NetBoxModelSerializer):
    virtual_machines = VirtualMachineSerializer(nested=True, many=True, required=False)
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_backupjobs-api:backupjob-detail')
    class Meta:
        model = BackupJob
        fields = '__all__'
        # These fields define what should be included when the serializer is used with nested=True.
        brief_fields = (
            'id', 'name', 'status',
        )