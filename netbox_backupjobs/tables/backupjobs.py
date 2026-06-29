import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from utilities.tables import register_table_column
from virtualization.tables import VirtualMachineTable
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
    virtual_machines = columns.ManyToManyColumn(
        verbose_name="Virtual Machines",
        linkify_item=True,
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
            'pk', 'name', 'status', 'description', 'virtual_machines',
        )


# ========================
# virtualization model table columns
# ========================

### Add Backupjob column to Virtual Machine tables.
backupjob_column = columns.ManyToManyColumn(
    verbose_name=_('Backup Jobs'),
    linkify_item=True,
)

register_table_column(backupjob_column, 'backup_jobs', VirtualMachineTable)