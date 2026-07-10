from django.templatetags.static import static
from django.utils.safestring import mark_safe

from netbox.plugins import PluginTemplateExtension

from netbox_backupjobs.models import BackupJob


class BackupJobTemplateExtension(PluginTemplateExtension):
    models = ['virtualization.virtualmachine']

    def right_page(self):
        vm = self.context.get('object')
        backup_jobs = BackupJob.objects.filter(virtual_machines=vm).order_by('name')
        return self.render('netbox_backupjobs/inc/backupjob_info.html', extra_context={
            'backup_jobs': backup_jobs,
        })


class BackupJobsSelectAllExtension(PluginTemplateExtension):
    """
    Adds "Select all" / "Clear" buttons to the hour/day/month schedule multi-select fields
    (see static/netbox_backupjobs/selectall.js).
    """
    def head(self):
        return mark_safe(f'<script src="{static("netbox_backupjobs/selectall.js")}"></script>')


## ---------------------------------------- ##


template_extensions = (
    BackupJobTemplateExtension,
    BackupJobsSelectAllExtension,
)
