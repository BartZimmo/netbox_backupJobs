__all__ = ('BackupJobFilterForm',)

from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms.fields import CommentField, TagFilterField
from utilities.forms.rendering import FieldSet

from netbox_backupjobs.models import BackupJob
from netbox_backupjobs.choices import BackupJobStatusChoices

class BackupJobFilterForm(NetBoxModelFilterSetForm):
    model = BackupJob
    fieldsets = (
        FieldSet('q', 'name', 'status', 'description', 'comments'),
        FieldSet('tag', name=_('Tags')),
    )
    q = forms.CharField(
        required=False,
        label='Search',
    )
    name = forms.CharField(
        required=False,
        label='Name',
    )
    status = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobStatusChoices,
        label='Status',
    )
    description = forms.CharField(
        required=False,
        label='Description',
    )
    comments = CommentField(
        required=False,
        label='Comments',
    )