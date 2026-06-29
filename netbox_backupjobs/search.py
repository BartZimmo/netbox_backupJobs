from netbox.search import SearchIndex, register_search

from netbox_backupjobs.models import BackupJob


@register_search
class BackupJobIndex(SearchIndex):
    model = BackupJob
    fields = (
         ('name', 100),
    )
    display_attrs = ('name',)