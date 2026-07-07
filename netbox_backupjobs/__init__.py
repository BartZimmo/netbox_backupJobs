from netbox.plugins import PluginConfig
from django.urls import include, path
from .version import __version__

class NetboxBackupJobsConfig(PluginConfig):
    name = 'netbox_backupjobs'
    verbose_name = 'NetBox BackupJobs'
    version = __version__
    description = 'BackupJob trackings in NetBox'
    base_url = 'backupjobs'
    author = 'Bart Van der Biest'
    author_email = 'bart@zimmo.be'
    min_version = '4.6.0'
    default_settings = {
        'top_level_menu': True,
    }

    def ready(self):
        super().ready()

config = NetboxBackupJobsConfig