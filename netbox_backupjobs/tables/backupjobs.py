import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from netbox_backupjobs.models import BackupJob

__all__ = (
    'BackupJobTable',
)


class BackupJobTable(NetBoxTable):
    """
    Table for displaying BackupJob objects in list views.
    """
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True
    )
    status = columns.ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    description = tables.Column(
        verbose_name=_('Description'),
    )
    comments = tables.Column(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='plugins:netbox_backupjobs:backupjob_list'
    )

    class Meta(NetBoxTable.Meta):
        model = BackupJob
        fields = (
            'pk', 'id', 'name', 'status', 'description', 'comments', 
            'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = (
            'pk', 'name', 'status', 'description',
        )
