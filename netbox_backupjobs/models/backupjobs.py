from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _


from netbox.models import NetBoxModel
from ipam.models import IPAddress
from virtualization.models import VirtualMachine
from netbox_backupjobs.choices import (
    BackupJobPlatformChoices,
    BackupJobStatusChoices,
    BackupJobEnableDeduplicationChoices,
    BackupJobStorageEncryptionEnabledChoices,
    BackupJobEnableDeletedVmDataRetentionChoices,
    BackupJobAlgorithmChoices,
    BackupJobEnableFullBackupChoices,
    BackupJobFullBackupScheduleKindChoices,
    BackupJobFullBackupDaysChoices,
    BackupJobFullBackupWeekChoices,
    BackupJobFullBackupMonthChoices,
    BackupJobEnableSyntheticFullForIncrementalChoices,
    BackupJobEnableSyntheticFullForReverseIncrementalChoices,
    BackupJobSyntheticFullChoices,
    BackupJobSyntheticFullDaysChoices,
    BackupJobSyntheticFullWeekChoices,
    BackupJobSyntheticFullMonthChoices,
    BackupJobGFSEnableChoices,
    BackupJobGFSWeeklyEnabledChoices,
    BackupJobGFSWeeklyDayChoices,
    BackupJobGFSMonthlyEnabledChoices,
    BackupJobGFSWeekOfMonthChoices,
    BackupJobGFSYearlyEnabledChoices,
    BackupJobGFSMonthOfYearChoices,
)


### ------------------------------------------------------- ###
### BackupJob Model
### ------------------------------------------------------- ###

# These defaults must be loaded before the class definition, otherwise the default will be evaluated at import time and not at runtime.
# This is important for the ArrayField fields, as they require a callable to be passed as the default value.

def default_synthetic_days():
    return [BackupJobSyntheticFullDaysChoices.SATURDAY]


def default_full_backup_days():
    return [BackupJobFullBackupDaysChoices.SATURDAY]


def default_full_backup_months():
    return [
        BackupJobFullBackupMonthChoices.JANUARY,
        BackupJobFullBackupMonthChoices.FEBRUARY,
        BackupJobFullBackupMonthChoices.MARCH,
        BackupJobFullBackupMonthChoices.APRIL,
        BackupJobFullBackupMonthChoices.MAY,
        BackupJobFullBackupMonthChoices.JUNE,
        BackupJobFullBackupMonthChoices.JULY,
        BackupJobFullBackupMonthChoices.AUGUST,
        BackupJobFullBackupMonthChoices.SEPTEMBER,
        BackupJobFullBackupMonthChoices.OCTOBER,
        BackupJobFullBackupMonthChoices.NOVEMBER,
        BackupJobFullBackupMonthChoices.DECEMBER,
    ]


def default_synthetic_months():
    return [
        BackupJobSyntheticFullMonthChoices.JANUARY,
        BackupJobSyntheticFullMonthChoices.FEBRUARY,
        BackupJobSyntheticFullMonthChoices.MARCH,
        BackupJobSyntheticFullMonthChoices.APRIL,
        BackupJobSyntheticFullMonthChoices.MAY,
        BackupJobSyntheticFullMonthChoices.JUNE,
        BackupJobSyntheticFullMonthChoices.JULY,
        BackupJobSyntheticFullMonthChoices.AUGUST,
        BackupJobSyntheticFullMonthChoices.SEPTEMBER,
        BackupJobSyntheticFullMonthChoices.OCTOBER,
        BackupJobSyntheticFullMonthChoices.NOVEMBER,
        BackupJobSyntheticFullMonthChoices.DECEMBER,
    ]


class BackupJob(NetBoxModel):
    #
    # fields that identify backup jobs
    #
    name = models.CharField(
        help_text='Name of the backup job',
        max_length=255,
        verbose_name='Name',
    )
    jobtype = models.CharField(
        max_length=50,
        help_text='Type of the backup job. Example: Backup, Replication, etc.',
        blank=True,
    )
    platform = models.CharField(
        max_length=50,
        choices=BackupJobPlatformChoices,
        blank=True,
        help_text='Platform of the backup job. Example: VMware, Hyper-V, etc.',
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
        blank=True
    )
    job_creation_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Job Creation Time',
        help_text='The date and time when the backup job was created in the backup system',
    )
    backup_server_name = models.CharField(
        blank=True,
        max_length=255,
        help_text='The backup server associated with this backup job',
    )
    backup_server_ip = models.ForeignKey(
        to=IPAddress,
        on_delete=models.SET_NULL,
        related_name='backup_jobs',
        blank=True,
        null=True,
        verbose_name='Backup Server IP',
        help_text='The IP address of the backup server associated with this backup job',
    )
    target = models.CharField(
        help_text='Target of the backup job',
        max_length=255,
        verbose_name='Target',
        blank=True
    )

    #
    # Advanced job Settings
    #
    Algorithm = models.CharField(
        max_length=50,
        choices=BackupJobAlgorithmChoices,
        default=BackupJobAlgorithmChoices.INCREMENTAL,
        help_text='The backup algorithm to use for this job',
    )
    EnableDeduplication = models.CharField(
        max_length=50,
        choices=BackupJobEnableDeduplicationChoices,
        default=BackupJobEnableDeduplicationChoices.FALSE,
        help_text='Enable deduplication for this backup job',
    )
    StorageEncryptionEnabled = models.CharField(
        max_length=50,
        choices=BackupJobStorageEncryptionEnabledChoices,
        default=BackupJobStorageEncryptionEnabledChoices.FALSE,
        help_text='Enable storage encryption for this backup job',
    )
    RetainDaysToKeep = models.CharField(
        max_length=50,
        blank=True,
        help_text='The minimum number of days to retain backups for this job',
    )
    RetainCycles = models.CharField(
        max_length=50,
        blank=True,
        help_text='The number of backup cycles veeam will retain for this job, this is auto calculated and also depends on synthetic full and active full backup settings',
    )
    EnableDeletedVmDataRetention = models.CharField(
        max_length=50,
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        default=BackupJobEnableDeletedVmDataRetentionChoices.FALSE,
        help_text='Enable retention of deleted VM data for this backup job',
    )
    RetainDaysToKeepDeletedVmData = models.CharField(
        max_length=50,
        blank=True,
        help_text='The number of days to retain deleted VM data for this backup job',
    )
    #
    # Synthetic Full Backup Settings
    #
    TransformFullToSyntethic = models.CharField(
        max_length=50,
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        default=BackupJobEnableSyntheticFullForIncrementalChoices.FALSE,
        help_text='Enable synthetic full backup for backup jobs that use incremental backup algorithm',
    )
    TransformToSyntheticFull = models.CharField(
        max_length=50,
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        default=BackupJobEnableSyntheticFullForReverseIncrementalChoices.FALSE,
        help_text='Enable synthetic full backup for backup jobs that use reverse incremental backup algorithm',
    )
    TransformToSyntethicKind = models.CharField(
        max_length=50,
        choices=BackupJobSyntheticFullChoices,
        default=BackupJobSyntheticFullChoices.SYNTHETIC_FULL_DAILY,
        help_text='The kind of synthetic full backup to create for this job',
    )
    TransformToSyntheticDays = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobSyntheticFullDaysChoices),
        default=default_synthetic_days,
        blank=True,
        help_text='The days of the week to create synthetic full backups for this job',
    )
    SyntheticFullDayNumberInMonth = models.CharField(
        max_length=50,
        choices=BackupJobSyntheticFullWeekChoices,
        default=BackupJobSyntheticFullWeekChoices.FIRST,
        help_text='The week of the month to create synthetic full backups for this job',
    )
    SyntheticFullDayOfWeek = models.CharField(
        max_length=50,
        choices=BackupJobSyntheticFullDaysChoices,
        default=BackupJobSyntheticFullDaysChoices.SUNDAY,
        help_text='The day of the week to create synthetic full backups for this job',
    )
    TransformToSyntethicMonthly = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobSyntheticFullMonthChoices),
        default=default_synthetic_months,
        blank=True,
        help_text='The months to create synthetic full backups for this job',
    )
    #
    # Active Full Backup Settings
    #
    EnableFullBackup = models.CharField(
        max_length=50,
        choices=BackupJobEnableFullBackupChoices,
        default=BackupJobEnableFullBackupChoices.FALSE,
        help_text='Enable active full backup for this job',
    )
    FullBackupScheduleKind = models.CharField(
        max_length=50,
        choices=BackupJobFullBackupScheduleKindChoices,
        default=BackupJobFullBackupScheduleKindChoices.DAILY,
        help_text='The schedule kind for active full backups',
    )
    FullBackupDays = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobFullBackupDaysChoices),
        default=default_full_backup_days,
        blank=True,
        help_text='The days of the week to create active full backups for this job',
    )
    FullBackupDayNumberInMonth = models.CharField(
        max_length=50,
        choices=BackupJobFullBackupWeekChoices,
        default=BackupJobFullBackupWeekChoices.FIRST,
        help_text='The week of the month to create active full backups for this job',
    )
    FullBackupDayOfWeek = models.CharField(
        max_length=50,
        choices=BackupJobFullBackupDaysChoices,
        default=BackupJobFullBackupDaysChoices.SUNDAY,
        help_text='The day of the week to create active full backups (monthly)',
    )
    FullBackupMonths = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobFullBackupMonthChoices),
        default=default_full_backup_months,
        blank=True,
        help_text='The months to create active full backups for this job',
    )
    #
    # GFS Settings
    #
    EnableGFS = models.CharField(
        max_length=50,
        choices=BackupJobGFSEnableChoices,
        default=BackupJobGFSEnableChoices.FALSE,
        help_text='Enable GFS (Grandfather-Father-Son) retention policy for this job',
    )
    WeeklyEnabled = models.CharField(
        max_length=50,
        choices=BackupJobGFSWeeklyEnabledChoices,
        default=BackupJobGFSWeeklyEnabledChoices.FALSE,
        help_text='Enable weekly GFS restore points',
    )
    WeeklyKeepBackupsFor = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        help_text='Number of weeks to keep weekly GFS restore points',
    )
    WeeklyKeepBackupsOnDayOfWeek = models.CharField(
        max_length=50,
        choices=BackupJobGFSWeeklyDayChoices,
        default=BackupJobGFSWeeklyDayChoices.SUNDAY,
        help_text='Day of the week to use as the weekly GFS restore point',
    )
    MonthlyEnabled = models.CharField(
        max_length=50,
        choices=BackupJobGFSMonthlyEnabledChoices,
        default=BackupJobGFSMonthlyEnabledChoices.FALSE,
        help_text='Enable monthly GFS restore points',
    )
    MonthlyKeepBackupsFor = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        help_text='Number of months to keep monthly GFS restore points',
    )
    MonthlyKeepBackupsWeekOfMonth = models.CharField(
        max_length=50,
        choices=BackupJobGFSWeekOfMonthChoices,
        default=BackupJobGFSWeekOfMonthChoices.FIRST,
        help_text='Week of the month to use as the monthly GFS restore point',
    )
    YearlyEnabled = models.CharField(
        max_length=50,
        choices=BackupJobGFSYearlyEnabledChoices,
        default=BackupJobGFSYearlyEnabledChoices.FALSE,
        help_text='Enable yearly GFS restore points',
    )
    YearlyKeepBackupsFor = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        help_text='Number of years to keep yearly GFS restore points',
    )
    YearlyKeepBackupsOnMonthOfYear = models.CharField(
        max_length=50,
        choices=BackupJobGFSMonthOfYearChoices,
        default=BackupJobGFSMonthOfYearChoices.JANUARY,
        help_text='Month of the year to use as the yearly GFS restore point',
    )


    comments = models.TextField(
        blank=True,
        help_text='Additional comments about the backup job',
    )



    clone_fields = [
        'name', 'jobtype', 'platform', 'status', 'virtual_machines', 'description',
        'backup_server_name', 'backup_server_ip',
        'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled',
        'RetainDaysToKeep', 'RetainCycles',
        'EnableDeletedVmDataRetention', 'RetainDaysToKeepDeletedVmData',
        'TransformFullToSyntethic', 'TransformToSyntheticFull', 'TransformToSyntethicKind',
        'TransformToSyntheticDays', 'SyntheticFullDayNumberInMonth', 'SyntheticFullDayOfWeek',
        'TransformToSyntethicMonthly',
        'EnableFullBackup', 'FullBackupScheduleKind',
        'FullBackupDays', 'FullBackupDayNumberInMonth', 'FullBackupDayOfWeek', 'FullBackupMonths',
        'EnableGFS',
        'WeeklyEnabled', 'WeeklyKeepBackupsFor', 'WeeklyKeepBackupsOnDayOfWeek',
        'MonthlyEnabled', 'MonthlyKeepBackupsFor', 'MonthlyKeepBackupsWeekOfMonth',
        'YearlyEnabled', 'YearlyKeepBackupsFor', 'YearlyKeepBackupsOnMonthOfYear',
        'comments',
    ]
    

    class Meta:
        ordering = ('name',)
        verbose_name = 'BackupJob'
        verbose_name_plural = 'Veeam BackupJobs'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='%(app_label)s_%(class)s_unique_name',
                violation_error_message=_("The BackupJob 'Name' must be unique.")
            ),
        ]

    def __str__(self):
        return self.name

    @property
    def backup_server_display(self):
        """
        If backup_server_ip is assigned to a device/VM interface, return that device/VM.
        Otherwise fall back to the manually entered backup_server_name.
        """
        if self.backup_server_ip and self.backup_server_ip.assigned_object:
            parent = getattr(self.backup_server_ip.assigned_object, 'parent_object', None)
            if parent:
                return parent
        return self.backup_server_name

    @property
    def virtual_machine_names(self):
        return ', '.join(self.virtual_machines.values_list('name', flat=True))

    def get_status_color(self):
        return BackupJobStatusChoices.colors.get(self.status)

    def get_EnableDeduplication_color(self):
        return BackupJobEnableDeduplicationChoices.colors.get(self.EnableDeduplication)

    def get_StorageEncryptionEnabled_color(self):
        return BackupJobStorageEncryptionEnabledChoices.colors.get(self.StorageEncryptionEnabled)

    def get_EnableDeletedVmDataRetention_color(self):
        return BackupJobEnableDeletedVmDataRetentionChoices.colors.get(self.EnableDeletedVmDataRetention)

    def get_TransformFullToSyntethic_color(self):
        return BackupJobEnableSyntheticFullForIncrementalChoices.colors.get(self.TransformFullToSyntethic)

    def get_TransformToSyntheticFull_color(self):
        return BackupJobEnableSyntheticFullForReverseIncrementalChoices.colors.get(self.TransformToSyntheticFull)

    def get_EnableFullBackup_color(self):
        return BackupJobEnableFullBackupChoices.colors.get(self.EnableFullBackup)

    def get_FullBackupDays_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobFullBackupDaysChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.FullBackupDays) if self.FullBackupDays else '—'

    def get_FullBackupMonths_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobFullBackupMonthChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.FullBackupMonths) if self.FullBackupMonths else '—'

    def get_EnableGFS_color(self):
        return BackupJobGFSEnableChoices.colors.get(self.EnableGFS)

    def get_WeeklyEnabled_color(self):
        return BackupJobGFSWeeklyEnabledChoices.colors.get(self.WeeklyEnabled)

    def get_MonthlyEnabled_color(self):
        return BackupJobGFSMonthlyEnabledChoices.colors.get(self.MonthlyEnabled)

    def get_YearlyEnabled_color(self):
        return BackupJobGFSYearlyEnabledChoices.colors.get(self.YearlyEnabled)

    def get_TransformToSyntheticDays_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobSyntheticFullDaysChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.TransformToSyntheticDays) if self.TransformToSyntheticDays else '—'

    def get_TransformToSyntethicMonthly_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobSyntheticFullMonthChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.TransformToSyntethicMonthly) if self.TransformToSyntethicMonthly else '—'

    