from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelForm
from netbox_backupjobs.models import BackupJob
from utilities.forms.rendering import FieldSet
from ...choices import (BackupJobStatusChoices)
from utilities.forms.fields import CommentField, DynamicModelMultipleChoiceField

from virtualization.models import VirtualMachine

__all__ = (
    'BackupJobForm',
)


class BackupJobForm(NetBoxModelForm):
    """
    Form for creating and editing BackupJob objects.
    """
    name = forms.CharField()
    status = forms.ChoiceField(
        choices=BackupJobStatusChoices,
        required=True,
    )
    description = forms.CharField(
        required=False,
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label="Virtual Machine",
        help_text='The virtual machine associated with this backup job',
    )

    fieldsets = (
        FieldSet(
            'name', 'status', 'description', 'virtual_machines', 'tags',
            name=_('Backup Job')
        ),
    )

    class Meta:
        model = BackupJob
        fields = [
            'name', 'status', 'description', 'virtual_machines', 'comments', 'tags',
        ]
