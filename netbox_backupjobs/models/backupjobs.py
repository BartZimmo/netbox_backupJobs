from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.forms import ValidationError
from django.urls import reverse
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _


from netbox.models import NetBoxModel, ChangeLoggedModel, NestedGroupModel
from virtualization.models import VirtualMachine
from netbox_backupjobs.choices import BackupJobStatusChoices


### ------------------------------------------------------- ###
### BackupJob Model
### ------------------------------------------------------- ###


class BackupJob(NetBoxModel):
    #
    # fields that identify backup jobs
    #
    name = models.CharField(
        help_text='Name of the backup job',
        max_length=255,
        verbose_name='Name',
    )
    status = models.CharField(
        max_length=50,
        choices= BackupJobStatusChoices,
        default= BackupJobStatusChoices.STATUS_ENABLED,
        help_text='Backup job status',
    )
    virtual_machines = models.ManyToManyField(
        VirtualMachine,
        related_name='backup_jobs',
        blank=True,
        help_text='The virtual machines associated with this backup job',
    )
    description = models.CharField(
        help_text='Description of the backup job',
        max_length=255,
        verbose_name='Description',
        null=True,
        blank=True
    )
    comments = models.TextField(
        blank=True,
        null=True,
        help_text='Additional comments about the backup job',
    )


    clone_fields = [
        'name', 'status', 'description', 'comments',
    ]
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'BackupJob'
        verbose_name_plural = 'BackupJobs'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='%(app_label)s_%(class)s_unique_name',
                violation_error_message=_("The BackupJob 'Name' must be unique.")
            ),
        ]

    def __str__(self):
        return self.name

    def get_status_color(self):
        return BackupJobStatusChoices.colors.get(self.status)
    