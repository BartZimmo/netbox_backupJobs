from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _


from netbox.models import NetBoxModel
from ipam.models import IPAddress
from virtualization.models import VirtualMachine
from netbox_backupjobs.choices import (
    BackupJobPlatformChoices,
    BackupJobStatusChoices,
    BackupJobResultChoices,
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
    BackupJobRunAutomaticallyChoices,
    BackupJobScheduleDailyEnabledChoices,
    BackupJobScheduleDailyKindChoices,
    BackupJobScheduleDaysChoices,
    BackupJobScheduleMonthlyEnabledChoices,
    BackupJobScheduleMonthlyDayOfWeekChoices,
    BackupJobScheduleMonthChoices,
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
    BackupJobScheduleDayOfMonthChoices,
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
    BackupJobScheduleHourChoices,
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


def default_schedule_daily_days():
    return [
        BackupJobScheduleDaysChoices.MONDAY,
        BackupJobScheduleDaysChoices.TUESDAY,
        BackupJobScheduleDaysChoices.WEDNESDAY,
        BackupJobScheduleDaysChoices.THURSDAY,
        BackupJobScheduleDaysChoices.FRIDAY,
        BackupJobScheduleDaysChoices.SATURDAY,
        BackupJobScheduleDaysChoices.SUNDAY,
    ]


def default_schedule_monthly_months():
    return [
        BackupJobScheduleMonthChoices.JANUARY,
        BackupJobScheduleMonthChoices.FEBRUARY,
        BackupJobScheduleMonthChoices.MARCH,
        BackupJobScheduleMonthChoices.APRIL,
        BackupJobScheduleMonthChoices.MAY,
        BackupJobScheduleMonthChoices.JUNE,
        BackupJobScheduleMonthChoices.JULY,
        BackupJobScheduleMonthChoices.AUGUST,
        BackupJobScheduleMonthChoices.SEPTEMBER,
        BackupJobScheduleMonthChoices.OCTOBER,
        BackupJobScheduleMonthChoices.NOVEMBER,
        BackupJobScheduleMonthChoices.DECEMBER,
    ]


def default_schedule_all_hours():
    return [str(h) for h in range(24)]


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
    last_backup_end_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Last Backup End Time',
        help_text='The date and time when the last backup job completed in the backup system',
    )
    last_backup_result = models.CharField(
        max_length=50,
        choices=BackupJobResultChoices,
        blank=True,
        verbose_name='Last Backup Result',
        help_text='The result of the last backup job',
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
    # Schedule Options
    #
    run_automatically = models.CharField(
        max_length=50,
        choices=BackupJobRunAutomaticallyChoices,
        default=BackupJobRunAutomaticallyChoices.FALSE,
        help_text='Whether the job runs automatically according to the schedule below',
    )
    schedule_daily_enabled = models.CharField(
        max_length=50,
        choices=BackupJobScheduleDailyEnabledChoices,
        default=BackupJobScheduleDailyEnabledChoices.FALSE,
        verbose_name='Daily Enabled',
        help_text='Enable the daily schedule for this job',
    )
    schedule_daily_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name='Daily Time',
        help_text='The time of day at which the daily schedule runs',
    )
    schedule_daily_kind = models.CharField(
        max_length=50,
        choices=BackupJobScheduleDailyKindChoices,
        default=BackupJobScheduleDailyKindChoices.EVERYDAY,
        blank=True,
        verbose_name='Daily Kind',
        help_text='Which days the daily schedule applies to',
    )
    schedule_daily_days = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobScheduleDaysChoices),
        default=default_schedule_daily_days,
        blank=True,
        verbose_name='Daily Days',
        help_text='The specific days of the week the daily schedule runs, when Daily Kind is Selected Days',
    )
    schedule_monthly_enabled = models.CharField(
        max_length=50,
        choices=BackupJobScheduleMonthlyEnabledChoices,
        default=BackupJobScheduleMonthlyEnabledChoices.FALSE,
        verbose_name='Monthly Enabled',
        help_text='Enable the monthly schedule for this job',
    )
    schedule_monthly_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name='Monthly Time',
        help_text='The time of day at which the monthly schedule runs',
    )
    schedule_monthly_day_number_in_month = models.CharField(
        max_length=50,
        choices=BackupJobScheduleMonthlyDayNumberInMonthChoices,
        default=BackupJobScheduleMonthlyDayNumberInMonthChoices.FIRST,
        blank=True,
        verbose_name='Monthly Day number of Month',
        help_text='The day of the month the monthly schedule runs',
    )
    schedule_monthly_day_of_week = models.CharField(
        max_length=50,
        choices=BackupJobScheduleMonthlyDayOfWeekChoices,
        default=BackupJobScheduleMonthlyDayOfWeekChoices.SATURDAY,
        blank=True,
        verbose_name='Monthly Day of Week',
        help_text='The day of the week the monthly schedule runs',
    )
    schedule_monthly_day_of_month = models.CharField(
        max_length=50,
        choices=BackupJobScheduleDayOfMonthChoices,
        default='1',
        blank=True,
        verbose_name='Monthly Day of Month',
        help_text='The day of the month the monthly schedule runs',
    )
    schedule_monthly_months = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobScheduleMonthChoices),
        default=default_schedule_monthly_months,
        blank=True,
        verbose_name='Monthly Months',
        help_text='The months the monthly schedule runs in',
    )
    schedule_periodically_enabled = models.CharField(
        max_length=50,
        choices=BackupJobPeriodicallyEnabledChoices,
        default=BackupJobPeriodicallyEnabledChoices.FALSE,
        verbose_name='Periodically Enabled',
        help_text='Enable the periodic (recurring interval) schedule for this job',
    )
    schedule_periodically_every = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        verbose_name='Periodically Every',
        help_text='The interval at which the job periodically runs, in units of Periodically Unit',
    )
    schedule_periodically_unit = models.CharField(
        max_length=50,
        choices=BackupJobPeriodicallyUnitChoices,
        default=BackupJobPeriodicallyUnitChoices.HOURS,
        blank=True,
        verbose_name='Periodically Unit',
        help_text='The unit of time used for the periodic schedule interval',
    )
    schedule_periodically_hour_offset_in_min = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(59)],
        verbose_name='Hour Offset (min)',
        help_text='Offset in minutes applied to the start of each hour block in the day schemas below (e.g. 15 shifts a block from 10:00-12:00 to 10:15-12:15)',
    )
    schedule_periodically_monday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupJobScheduleHourChoices),
        default=default_schedule_all_hours,
        blank=True,
        verbose_name='Monday Schema',
        help_text='Hours during which this job is allowed to run on Monday',
    )
    schedule_periodically_tuesday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupJobScheduleHourChoices),
        default=default_schedule_all_hours,
        blank=True,
        verbose_name='Tuesday Schema',
        help_text='Hours during which this job is allowed to run on Tuesday',
    )
    schedule_periodically_wednesday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupJobScheduleHourChoices),
        default=default_schedule_all_hours,
        blank=True,
        verbose_name='Wednesday Schema',
        help_text='Hours during which this job is allowed to run on Wednesday',
    )
    schedule_periodically_thursday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupJobScheduleHourChoices),
        default=default_schedule_all_hours,
        blank=True,
        verbose_name='Thursday Schema',
        help_text='Hours during which this job is allowed to run on Thursday',
    )
    schedule_periodically_friday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupJobScheduleHourChoices),
        default=default_schedule_all_hours,
        blank=True,
        verbose_name='Friday Schema',
        help_text='Hours during which this job is allowed to run on Friday',
    )
    schedule_periodically_saturday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupJobScheduleHourChoices),
        default=default_schedule_all_hours,
        blank=True,
        verbose_name='Saturday Schema',
        help_text='Hours during which this job is allowed to run on Saturday',
    )
    schedule_periodically_sunday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupJobScheduleHourChoices),
        default=default_schedule_all_hours,
        blank=True,
        verbose_name='Sunday Schema',
        help_text='Hours during which this job is allowed to run on Sunday',
    )
    after_job_enabled = models.CharField(
        max_length=50,
        choices=BackupJobAfterJobEnabledChoices,
        default=BackupJobAfterJobEnabledChoices.FALSE,
        verbose_name='After Job Enabled',
        help_text='Enable the after job schedule for this job',
    )
    after_job_name = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        related_name='preceding_jobs',
        null=True,
        blank=True,
        verbose_name='After Job',
        help_text='Veeam will wait for the selected job before starting this job',
    )

    #
    # Advanced job Settings
    #
    algorithm = models.CharField(
        max_length=50,
        choices=BackupJobAlgorithmChoices,
        default=BackupJobAlgorithmChoices.INCREMENTAL,
        help_text='The backup algorithm to use for this job',
    )
    enable_deduplication = models.CharField(
        max_length=50,
        choices=BackupJobEnableDeduplicationChoices,
        default=BackupJobEnableDeduplicationChoices.FALSE,
        help_text='Enable deduplication for this backup job',
    )
    storage_encryption_enabled = models.CharField(
        max_length=50,
        choices=BackupJobStorageEncryptionEnabledChoices,
        default=BackupJobStorageEncryptionEnabledChoices.FALSE,
        help_text='Enable storage encryption for this backup job',
    )
    retain_days_to_keep = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        help_text='The minimum number of days to retain backups for this job',
    )
    retain_cycles = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        help_text='The number of backup cycles veeam will retain for this job, this is auto calculated and also depends on synthetic full and active full backup settings',
    )
    enable_deleted_vm_data_retention = models.CharField(
        max_length=50,
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        default=BackupJobEnableDeletedVmDataRetentionChoices.FALSE,
        help_text='Enable retention of deleted VM data for this backup job',
    )
    retain_days_to_keep_deleted_vm_data = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        help_text='The number of days to retain deleted VM data for this backup job',
    )
    #
    # Synthetic Full Backup Settings
    #
    transform_full_to_synthetic = models.CharField(
        max_length=50,
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        default=BackupJobEnableSyntheticFullForIncrementalChoices.FALSE,
        help_text='Enable synthetic full backup for backup jobs that use incremental backup algorithm',
    )
    transform_to_synthetic_full = models.CharField(
        max_length=50,
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        default=BackupJobEnableSyntheticFullForReverseIncrementalChoices.FALSE,
        help_text='Enable synthetic full backup for backup jobs that use reverse incremental backup algorithm',
    )
    transform_to_synthetic_kind = models.CharField(
        max_length=50,
        choices=BackupJobSyntheticFullChoices,
        default=BackupJobSyntheticFullChoices.SYNTHETIC_FULL_DAILY,
        help_text='The kind of synthetic full backup to create for this job',
    )
    transform_to_synthetic_days = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobSyntheticFullDaysChoices),
        default=default_synthetic_days,
        blank=True,
        help_text='The days of the week to create synthetic full backups for this job',
    )
    synthetic_full_day_number_in_month = models.CharField(
        max_length=50,
        choices=BackupJobSyntheticFullWeekChoices,
        default=BackupJobSyntheticFullWeekChoices.FIRST,
        help_text='The week of the month to create synthetic full backups for this job',
    )
    synthetic_full_day_of_week = models.CharField(
        max_length=50,
        choices=BackupJobSyntheticFullDaysChoices,
        default=BackupJobSyntheticFullDaysChoices.SUNDAY,
        help_text='The day of the week to create synthetic full backups for this job',
    )
    transform_to_synthetic_monthly = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobSyntheticFullMonthChoices),
        default=default_synthetic_months,
        blank=True,
        help_text='The months to create synthetic full backups for this job',
    )
    #
    # Active Full Backup Settings
    #
    enable_full_backup = models.CharField(
        max_length=50,
        choices=BackupJobEnableFullBackupChoices,
        default=BackupJobEnableFullBackupChoices.FALSE,
        help_text='Enable active full backup for this job',
    )
    full_backup_schedule_kind = models.CharField(
        max_length=50,
        choices=BackupJobFullBackupScheduleKindChoices,
        default=BackupJobFullBackupScheduleKindChoices.DAILY,
        help_text='The schedule kind for active full backups',
    )
    full_backup_days = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobFullBackupDaysChoices),
        default=default_full_backup_days,
        blank=True,
        help_text='The days of the week to create active full backups for this job',
    )
    full_backup_day_number_in_month = models.CharField(
        max_length=50,
        choices=BackupJobFullBackupWeekChoices,
        default=BackupJobFullBackupWeekChoices.FIRST,
        help_text='The week of the month to create active full backups for this job',
    )
    full_backup_day_of_week = models.CharField(
        max_length=50,
        choices=BackupJobFullBackupDaysChoices,
        default=BackupJobFullBackupDaysChoices.SUNDAY,
        help_text='The day of the week to create active full backups (monthly)',
    )
    full_backup_months = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupJobFullBackupMonthChoices),
        default=default_full_backup_months,
        blank=True,
        help_text='The months to create active full backups for this job',
    )
    #
    # GFS Settings
    #
    enable_gfs = models.CharField(
        max_length=50,
        choices=BackupJobGFSEnableChoices,
        default=BackupJobGFSEnableChoices.FALSE,
        help_text='Enable GFS (Grandfather-Father-Son) retention policy for this job',
    )
    weekly_enabled = models.CharField(
        max_length=50,
        choices=BackupJobGFSWeeklyEnabledChoices,
        default=BackupJobGFSWeeklyEnabledChoices.FALSE,
        help_text='Enable weekly GFS restore points',
    )
    weekly_keep_backups_for = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        help_text='Number of weeks to keep weekly GFS restore points',
    )
    weekly_keep_backups_on_day_of_week = models.CharField(
        max_length=50,
        choices=BackupJobGFSWeeklyDayChoices,
        default=BackupJobGFSWeeklyDayChoices.SUNDAY,
        help_text='Day of the week to use as the weekly GFS restore point',
    )
    monthly_enabled = models.CharField(
        max_length=50,
        choices=BackupJobGFSMonthlyEnabledChoices,
        default=BackupJobGFSMonthlyEnabledChoices.FALSE,
        help_text='Enable monthly GFS restore points',
    )
    monthly_keep_backups_for = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        help_text='Number of months to keep monthly GFS restore points',
    )
    monthly_keep_backups_week_of_month = models.CharField(
        max_length=50,
        choices=BackupJobGFSWeekOfMonthChoices,
        default=BackupJobGFSWeekOfMonthChoices.FIRST,
        help_text='Week of the month to use as the monthly GFS restore point',
    )
    yearly_enabled = models.CharField(
        max_length=50,
        choices=BackupJobGFSYearlyEnabledChoices,
        default=BackupJobGFSYearlyEnabledChoices.FALSE,
        help_text='Enable yearly GFS restore points',
    )
    yearly_keep_backups_for = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        help_text='Number of years to keep yearly GFS restore points',
    )
    yearly_keep_backups_on_month_of_year = models.CharField(
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
        'algorithm', 'enable_deduplication', 'storage_encryption_enabled',
        'retain_days_to_keep', 'retain_cycles',
        'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
        'transform_full_to_synthetic', 'transform_to_synthetic_full', 'transform_to_synthetic_kind',
        'transform_to_synthetic_days', 'synthetic_full_day_number_in_month', 'synthetic_full_day_of_week',
        'transform_to_synthetic_monthly',
        'enable_full_backup', 'full_backup_schedule_kind',
        'full_backup_days', 'full_backup_day_number_in_month', 'full_backup_day_of_week', 'full_backup_months',
        'enable_gfs',
        'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
        'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
        'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
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

    def get_last_backup_result_color(self):
        return BackupJobResultChoices.colors.get(self.last_backup_result)

    def get_enable_deduplication_color(self):
        return BackupJobEnableDeduplicationChoices.colors.get(self.enable_deduplication)

    def get_storage_encryption_enabled_color(self):
        return BackupJobStorageEncryptionEnabledChoices.colors.get(self.storage_encryption_enabled)

    def get_enable_deleted_vm_data_retention_color(self):
        return BackupJobEnableDeletedVmDataRetentionChoices.colors.get(self.enable_deleted_vm_data_retention)

    def get_transform_full_to_synthetic_color(self):
        return BackupJobEnableSyntheticFullForIncrementalChoices.colors.get(self.transform_full_to_synthetic)

    def get_transform_to_synthetic_full_color(self):
        return BackupJobEnableSyntheticFullForReverseIncrementalChoices.colors.get(self.transform_to_synthetic_full)

    def get_enable_full_backup_color(self):
        return BackupJobEnableFullBackupChoices.colors.get(self.enable_full_backup)

    def get_full_backup_days_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobFullBackupDaysChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.full_backup_days) if self.full_backup_days else '—'

    def get_full_backup_months_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobFullBackupMonthChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.full_backup_months) if self.full_backup_months else '—'

    def get_enable_gfs_color(self):
        return BackupJobGFSEnableChoices.colors.get(self.enable_gfs)

    def get_weekly_enabled_color(self):
        return BackupJobGFSWeeklyEnabledChoices.colors.get(self.weekly_enabled)

    def get_monthly_enabled_color(self):
        return BackupJobGFSMonthlyEnabledChoices.colors.get(self.monthly_enabled)

    def get_yearly_enabled_color(self):
        return BackupJobGFSYearlyEnabledChoices.colors.get(self.yearly_enabled)

    def get_transform_to_synthetic_days_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobSyntheticFullDaysChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.transform_to_synthetic_days) if self.transform_to_synthetic_days else '—'

    def get_transform_to_synthetic_monthly_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobSyntheticFullMonthChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.transform_to_synthetic_monthly) if self.transform_to_synthetic_monthly else '—'

    def get_run_automatically_color(self):
        return BackupJobRunAutomaticallyChoices.colors.get(self.run_automatically)

    def get_schedule_daily_enabled_color(self):
        return BackupJobScheduleDailyEnabledChoices.colors.get(self.schedule_daily_enabled)

    def get_schedule_daily_days_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobScheduleDaysChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.schedule_daily_days) if self.schedule_daily_days else '—'

    def get_schedule_monthly_enabled_color(self):
        return BackupJobScheduleMonthlyEnabledChoices.colors.get(self.schedule_monthly_enabled)

    def get_schedule_monthly_months_display(self):
        labels = {c[0]: str(c[1]) for c in BackupJobScheduleMonthChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.schedule_monthly_months) if self.schedule_monthly_months else '—'

    def get_schedule_periodically_enabled_color(self):
        return BackupJobPeriodicallyEnabledChoices.colors.get(self.schedule_periodically_enabled)

    def _schedule_hour_schema_display(self, hours):
        if len(hours) == 24:
            return 'All Hours'
        if not hours:
            return 'No Hours'
        offset = self.schedule_periodically_hour_offset_in_min or 0
        ordered = sorted(int(h) for h in hours)
        ranges = []
        start = prev = ordered[0]
        for h in ordered[1:]:
            if h == prev + 1:
                prev = h
                continue
            ranges.append((start, prev))
            start = prev = h
        ranges.append((start, prev))

        def label(hour):
            return f'{hour % 24:02d}:{offset:02d}'

        parts = [f'{label(start)}-{label(end + 1)}' for start, end in ranges]
        return ', '.join(parts)

    def get_schedule_periodically_monday_schema_display(self):
        return self._schedule_hour_schema_display(self.schedule_periodically_monday_schema)

    def get_schedule_periodically_tuesday_schema_display(self):
        return self._schedule_hour_schema_display(self.schedule_periodically_tuesday_schema)

    def get_schedule_periodically_wednesday_schema_display(self):
        return self._schedule_hour_schema_display(self.schedule_periodically_wednesday_schema)

    def get_schedule_periodically_thursday_schema_display(self):
        return self._schedule_hour_schema_display(self.schedule_periodically_thursday_schema)

    def get_schedule_periodically_friday_schema_display(self):
        return self._schedule_hour_schema_display(self.schedule_periodically_friday_schema)

    def get_schedule_periodically_saturday_schema_display(self):
        return self._schedule_hour_schema_display(self.schedule_periodically_saturday_schema)

    def get_schedule_periodically_sunday_schema_display(self):
        return self._schedule_hour_schema_display(self.schedule_periodically_sunday_schema)

    def get_after_job_enabled_color(self):
        return BackupJobAfterJobEnabledChoices.colors.get(self.after_job_enabled)

