from django.db.models import Count
from django.utils.translation import gettext_lazy as _

from netbox.views import generic
from utilities.views import ViewTab, register_model_view

from virtualization.models import VirtualMachine
from virtualization.tables import VirtualMachineTable

from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.tables.backupjobs import BackupJobTable
from netbox_backupjobs.tables.backupcopyjobs import BackupCopyJobTable
from netbox_backupjobs.forms.models import BackupJobForm
from netbox_backupjobs.forms.filtersets import BackupJobFilterForm
from netbox_backupjobs.forms.bulk_edit import BackupJobBulkEditForm
from netbox_backupjobs.forms.bulk_import import BackupJobImportForm
from netbox_backupjobs.filtersets import BackupJobFilterSet



__all__ = (
    'BackupJobView',
    'BackupJobListView',
    'BackupJobEditView',
    'BackupJobDeleteView',
    'BackupJobBulkEditView',
    'BackupJobBulkImportView',
    'BackupJobBulkDeleteView',
    'BackupJobVirtualMachinesView',
    'BackupJobCopyJobsView',
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
    queryset = BackupJob.objects.annotate(
        virtual_machine_count=Count('virtual_machines', distinct=True),
    )
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


@register_model_view(BackupJob, 'virtual_machines')
class BackupJobVirtualMachinesView(generic.ObjectChildrenView):
    queryset = BackupJob.objects.all()
    child_model = VirtualMachine
    table = VirtualMachineTable
    tab = ViewTab(
        label=_('Virtual Machines'),
        badge=lambda obj: obj.virtual_machines.count(),
        permission='virtualization.view_virtualmachine',
        weight=500,
    )

    def get_children(self, request, parent):
        return parent.virtual_machines.restrict(request.user, 'view').all()


@register_model_view(BackupJob, 'copy_jobs')
class BackupJobCopyJobsView(generic.ObjectChildrenView):
    queryset = BackupJob.objects.all()
    child_model = BackupCopyJob
    table = BackupCopyJobTable
    tab = ViewTab(
        label=_('Backup Copy Jobs'),
        badge=lambda obj: obj.copy_jobs.count(),
        permission='netbox_backupjobs.view_backupcopyjob',
        weight=510,
    )

    def get_children(self, request, parent):
        return parent.copy_jobs.restrict(request.user, 'view').all()


@register_model_view(BackupJob, 'bulk_edit', detail=False)
class BackupJobBulkEditView(generic.BulkEditView):
    """
    Bulk edit BackupJob objects.
    """
    queryset = BackupJob.objects.all()
    filterset = BackupJobFilterSet
    table = BackupJobTable
    form = BackupJobBulkEditForm
    default_return_url = 'plugins:netbox_backupjobs:backupjob_list'

    def post_save_operations(self, form, obj):
        super().post_save_operations(form, obj)
        if form.cleaned_data.get('add_virtual_machines', None):
            obj.virtual_machines.add(*form.cleaned_data['add_virtual_machines'])
        if form.cleaned_data.get('remove_virtual_machines', None):
            obj.virtual_machines.remove(*form.cleaned_data['remove_virtual_machines'])


@register_model_view(BackupJob, 'bulk_import', detail=False)
class BackupJobBulkImportView(generic.BulkImportView):
    """
    Bulk import BackupJob objects.
    """
    queryset = BackupJob.objects.all()
    model_form = BackupJobImportForm


@register_model_view(BackupJob, 'bulk_delete', path='delete', detail=False)
class BackupJobBulkDeleteView(generic.BulkDeleteView):
    """
    Bulk delete BackupJob objects.
    """
    queryset = BackupJob.objects.all()
    table = BackupJobTable
