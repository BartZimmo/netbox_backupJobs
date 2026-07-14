from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.tables.backupjobs import BackupCopyJobBackupJobsTable
from netbox_backupjobs.tables.backupcopyjobs import BackupCopyJobTable
from netbox_backupjobs.forms.models import BackupCopyJobForm
from netbox_backupjobs.forms.filtersets import BackupCopyJobFilterForm
from netbox_backupjobs.forms.bulk_edit import BackupCopyJobBulkEditForm
from netbox_backupjobs.forms.bulk_import import BackupCopyJobImportForm
from netbox_backupjobs.filtersets import BackupCopyJobFilterSet


__all__ = (
    'BackupCopyJobView',
    'BackupCopyJobListView',
    'BackupCopyJobEditView',
    'BackupCopyJobDeleteView',
    'BackupCopyJobBulkEditView',
    'BackupCopyJobBulkImportView',
    'BackupCopyJobBulkDeleteView',
    'BackupCopyJobBackupJobsView',
)


#
# BackupCopyJobs
#

@register_model_view(BackupCopyJob)
class BackupCopyJobView(generic.ObjectView):
    """Display a single BackupCopyJob object."""
    queryset = BackupCopyJob.objects.all()

@register_model_view(BackupCopyJob, 'list', path='', detail=False)
class BackupCopyJobListView(generic.ObjectListView):
    """List all BackupCopyJob objects."""
    queryset = BackupCopyJob.objects.all()
    table = BackupCopyJobTable
    filterset = BackupCopyJobFilterSet
    filterset_form = BackupCopyJobFilterForm


@register_model_view(BackupCopyJob, 'add', detail=False)
@register_model_view(BackupCopyJob, 'edit')
class BackupCopyJobEditView(generic.ObjectEditView):
    """
    Create or edit a BackupCopyJob object.
    """
    queryset = BackupCopyJob.objects.all()
    form = BackupCopyJobForm


@register_model_view(BackupCopyJob, 'delete')
class BackupCopyJobDeleteView(generic.ObjectDeleteView):
    """
    Delete a BackupCopyJob object.
    """
    queryset = BackupCopyJob.objects.all()


@register_model_view(BackupCopyJob, 'backup_jobs')
class BackupCopyJobBackupJobsView(generic.ObjectChildrenView):
    queryset = BackupCopyJob.objects.all()
    child_model = BackupJob
    table = BackupCopyJobBackupJobsTable
    tab = ViewTab(
        label=_('Backup Jobs'),
        badge=lambda obj: obj.backup_jobs.count(),
        permission='netbox_backupjobs.view_backupjob',
        weight=510,
    )

    def get_children(self, request, parent):
        return parent.backup_jobs.restrict(request.user, 'view').annotate(
            virtual_machine_count=Count('virtual_machines', distinct=True),
        )


@register_model_view(BackupCopyJob, 'bulk_edit', detail=False)
class BackupCopyJobBulkEditView(generic.BulkEditView):
    """
    Bulk edit BackupCopyJob objects.
    """
    queryset = BackupCopyJob.objects.all()
    filterset = BackupCopyJobFilterSet
    table = BackupCopyJobTable
    form = BackupCopyJobBulkEditForm
    default_return_url = 'plugins:netbox_backupjobs:backupcopyjob_list'

    def post_save_operations(self, form, obj):
        super().post_save_operations(form, obj)
        if form.cleaned_data.get('add_backup_jobs', None):
            obj.backup_jobs.add(*form.cleaned_data['add_backup_jobs'])
        if form.cleaned_data.get('remove_backup_jobs', None):
            obj.backup_jobs.remove(*form.cleaned_data['remove_backup_jobs'])


@register_model_view(BackupCopyJob, 'bulk_import', detail=False)
class BackupCopyJobBulkImportView(generic.BulkImportView):
    """
    Bulk import BackupCopyJob objects.
    """
    queryset = BackupCopyJob.objects.all()
    model_form = BackupCopyJobImportForm


@register_model_view(BackupCopyJob, 'bulk_delete', path='delete', detail=False)
class BackupCopyJobBulkDeleteView(generic.BulkDeleteView):
    """
    Bulk delete BackupCopyJob objects.
    """
    queryset = BackupCopyJob.objects.all()
    table = BackupCopyJobTable
