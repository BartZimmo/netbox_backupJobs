from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelForm
from netbox_backupjobs.models import BackupJob
from utilities.forms.rendering import FieldSet
from ...choices import (BackupJobStatusChoices)
from utilities.forms.fields import CommentField

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

    

    fieldsets = (
        FieldSet(
            'name', 'status', 'description', 'tags',
            name=_('Backup Job')
        ),
    )

    class Meta:
        model = BackupJob
        fields = [
            'name', 'status', 'description', 'comments', 'tags',
        ]
