from django.templatetags.static import static
from django.utils.safestring import mark_safe

from netbox.plugins import PluginTemplateExtension


class BackupJobsSelectAllExtension(PluginTemplateExtension):
    """
    Adds "Select all" / "Clear" buttons to the hour/day/month schedule multi-select fields
    (see static/netbox_backupjobs/selectall.js).
    """
    def head(self):
        return mark_safe(f'<script src="{static("netbox_backupjobs/selectall.js")}"></script>')


## ---------------------------------------- ##


template_extensions = (
    BackupJobsSelectAllExtension,
)
