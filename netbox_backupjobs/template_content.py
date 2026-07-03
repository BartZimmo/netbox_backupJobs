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


## ---------------------------------------- ##


template_extensions = (
    BackupJobTemplateExtension,
)
