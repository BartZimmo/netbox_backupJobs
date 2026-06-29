from django.utils.translation import gettext_lazy as _

from netbox.views import generic
from utilities.views import register_model_view

from netbox_backupjobs.models import BackupJob
from netbox_backupjobs.tables.backupjobs import BackupJobTable
from netbox_backupjobs.forms.models import BackupJobForm
from netbox_backupjobs.forms.filtersets import BackupJobFilterForm
from netbox_backupjobs.filtersets import BackupJobFilterSet



__all__ = (
    'BackupJobView',
    'BackupJobListView',
    'BackupJobEditView',
    'BackupJobDeleteView',
    'BackupJobBulkDeleteView',
)


#
# BackupJobs
#

@register_model_view(BackupJob)
class BackupJobView(generic.ObjectView):
    """Display a single BackupJob object."""
    queryset = BackupJob.objects.all()

@register_model_view(BackupJob, 'list', path='', detail=False)
class BackupJobListView(generic.ObjectListView):
    """List all BackupJob objects."""
    queryset = BackupJob.objects.all()
    table = BackupJobTable
    filterset = BackupJobFilterSet
    filterset_form = BackupJobFilterForm



@register_model_view(BackupJob, 'add', detail=False)
@register_model_view(BackupJob, 'edit')
class BackupJobEditView(generic.ObjectEditView):
    """
    Create or edit a BackupJob object.
    """
    queryset = BackupJob.objects.all()
    form = BackupJobForm


@register_model_view(BackupJob, 'delete')
class BackupJobDeleteView(generic.ObjectDeleteView):
    """
    Delete a BackupJob object.
    """
    queryset = BackupJob.objects.all()


@register_model_view(BackupJob, 'bulk_delete', path='delete', detail=False)
class BackupJobBulkDeleteView(generic.BulkDeleteView):
    """
    Bulk delete BackupJob objects.
    """
    queryset = BackupJob.objects.all()
    table = BackupJobTable
