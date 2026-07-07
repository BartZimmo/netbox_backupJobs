from netbox.api.fields import SerializedPKRelatedField
from netbox.api.serializers import NetBoxModelSerializer
from rest_framework import serializers

from ipam.api.serializers import IPAddressSerializer
from virtualization.api.serializers import VirtualMachineSerializer
from virtualization.models import VirtualMachine

from netbox_backupjobs.models import BackupJob

class BackupJobSerializer(NetBoxModelSerializer):
    virtual_machines = SerializedPKRelatedField(
        queryset=VirtualMachine.objects.all(),
        serializer=VirtualMachineSerializer,
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
        view_name='plugins-api:netbox_backupjobs-api:backupjob-detail')
    class Meta:
        model = BackupJob
        fields = '__all__'
        # These fields define what should be included when the serializer is used with nested=True.
        brief_fields = (
            'id', 'url', 'display', 'name', 'status',
        )