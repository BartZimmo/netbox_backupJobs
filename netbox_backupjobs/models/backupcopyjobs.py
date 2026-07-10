from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.functions import Lower
from django.utils.translation import gettext_lazy as _

from netbox.models import NetBoxModel
from ipam.models import IPAddress
from netbox_backupjobs.choices import (
    BackupCopyJobStatusChoices,
    BackupCopyJobResultChoices,
    BackupCopyJobModeChoices,
    BackupCopyJobEnableDeduplicationChoices,
    BackupCopyJobStorageEncryptionEnabledChoices,
    BackupCopyJobEnableDeletedVmDataRetentionChoices,
    BackupCopyJobGFSEnableChoices,
    BackupCopyJobGFSWeeklyEnabledChoices,
    BackupCopyJobGFSWeeklyDayChoices,
    BackupCopyJobGFSMonthlyEnabledChoices,
    BackupCopyJobGFSWeekOfMonthChoices,
    BackupCopyJobGFSYearlyEnabledChoices,
    BackupCopyJobGFSMonthOfYearChoices,
    BackupCopyJobDataTransferModeChoices,
    BackupCopyJobTransactionLogCopyEnabledChoices,
    BackupCopyJobTransferWindowChoices,
    BackupCopyJobScheduleHourChoices,
    BackupCopyJobRunAutomaticallyChoices,
    BackupCopyJobScheduleDailyEnabledChoices,
    BackupCopyJobScheduleDailyKindChoices,
    BackupCopyJobScheduleDaysChoices,
    BackupCopyJobScheduleMonthlyEnabledChoices,
    BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
    BackupCopyJobScheduleMonthlyDayOfWeekChoices,
    BackupCopyJobScheduleDayOfMonthChoices,
    BackupCopyJobScheduleMonthChoices,
    BackupCopyJobPeriodicallyEnabledChoices,
    BackupCopyJobPeriodicallyUnitChoices,
    BackupCopyJobAfterJobEnabledChoices,
)


### ------------------------------------------------------- ###
### BackupCopyJob Model
### ------------------------------------------------------- ###

# Must be loaded before the class body so it's evaluated at runtime, not import time.
def default_transfer_window_all_hours():
    return [str(h) for h in range(24)]


def default_schedule_daily_days():
    return [
        BackupCopyJobScheduleDaysChoices.MONDAY,
        BackupCopyJobScheduleDaysChoices.TUESDAY,
        BackupCopyJobScheduleDaysChoices.WEDNESDAY,
        BackupCopyJobScheduleDaysChoices.THURSDAY,
        BackupCopyJobScheduleDaysChoices.FRIDAY,
        BackupCopyJobScheduleDaysChoices.SATURDAY,
        BackupCopyJobScheduleDaysChoices.SUNDAY,
    ]


def default_schedule_monthly_months():
    return [
        BackupCopyJobScheduleMonthChoices.JANUARY,
        BackupCopyJobScheduleMonthChoices.FEBRUARY,
        BackupCopyJobScheduleMonthChoices.MARCH,
        BackupCopyJobScheduleMonthChoices.APRIL,
        BackupCopyJobScheduleMonthChoices.MAY,
        BackupCopyJobScheduleMonthChoices.JUNE,
        BackupCopyJobScheduleMonthChoices.JULY,
        BackupCopyJobScheduleMonthChoices.AUGUST,
        BackupCopyJobScheduleMonthChoices.SEPTEMBER,
        BackupCopyJobScheduleMonthChoices.OCTOBER,
        BackupCopyJobScheduleMonthChoices.NOVEMBER,
        BackupCopyJobScheduleMonthChoices.DECEMBER,
    ]


class BackupCopyJob(NetBoxModel):
    name = models.CharField(
        help_text='Name of the backup copy job',
        max_length=255,
        verbose_name='Name',
    )
    jobtype = models.CharField(
        max_length=50,
        help_text='Type of the backup copy job. Example: Backup Copy, etc.',
        blank=True,
    )
    status = models.CharField(
        max_length=50,
        choices=BackupCopyJobStatusChoices,
        default=BackupCopyJobStatusChoices.STATUS_ENABLED,
        help_text='Backup copy job status',
    )
    mode = models.CharField(
        max_length=50,
        choices=BackupCopyJobModeChoices,
        default=BackupCopyJobModeChoices.IMMEDIATE,
        verbose_name='Copy Mode',
        help_text='Whether the backup copy job runs immediately or on a periodic schedule',
    )
    data_transfer_mode = models.CharField(
        max_length=50,
        choices=BackupCopyJobDataTransferModeChoices,
        default=BackupCopyJobDataTransferModeChoices.DIRECT,
        help_text='Whether data is transferred directly or through WAN accelerators',
    )
    description = models.CharField(
        help_text='Description of the backup copy job',
        max_length=255,
        verbose_name='Description',
        blank=True,
    )
    job_creation_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Job Creation Time',
        help_text='The date and time when the backup copy job was created in the backup system',
    )
    last_backup_result = models.CharField(
        max_length=50,
        choices=BackupCopyJobResultChoices,
        blank=True,
        verbose_name='Last Backup Result',
        help_text='The result of the last backup copy job',
    )
    retain_days_to_keep = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        help_text='The minimum number of days to retain backups for this job',
    )
    backup_server_name = models.CharField(
        blank=True,
        max_length=255,
        help_text='The backup server associated with this backup copy job',
    )
    backup_server_ip = models.ForeignKey(
        to=IPAddress,
        on_delete=models.SET_NULL,
        related_name='backup_copy_jobs',
        blank=True,
        null=True,
        verbose_name='Backup Server IP',
        help_text='The IP address of the backup server associated with this backup copy job',
    )
    target = models.CharField(
        help_text='Target of the backup copy job',
        max_length=255,
        verbose_name='Target',
        blank=True,
    )
    backup_jobs = models.ManyToManyField(
        to='netbox_backupjobs.BackupJob',
        related_name='copy_jobs',
        blank=True,
        help_text='The backup job(s) that this copy job is associated with',
    )
    #
    # Advanced job Settings
    #
    enable_deduplication = models.CharField(
        max_length=50,
        choices=BackupCopyJobEnableDeduplicationChoices,
        default=BackupCopyJobEnableDeduplicationChoices.FALSE,
        help_text='Enable deduplication for this backup copy job',
    )
    storage_encryption_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobStorageEncryptionEnabledChoices,
        default=BackupCopyJobStorageEncryptionEnabledChoices.FALSE,
        help_text='Enable storage encryption for this backup copy job',
    )
    transaction_log_copy_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobTransactionLogCopyEnabledChoices,
        default=BackupCopyJobTransactionLogCopyEnabledChoices.FALSE,
        help_text='Enable transaction log copy for this backup copy job',
    )
    enable_deleted_vm_data_retention = models.CharField(
        max_length=50,
        choices=BackupCopyJobEnableDeletedVmDataRetentionChoices,
        default=BackupCopyJobEnableDeletedVmDataRetentionChoices.FALSE,
        help_text='Enable retention of deleted VM data for this backup copy job',
    )
    retain_days_to_keep_deleted_vm_data = models.PositiveIntegerField(
        default=1,
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
        help_text='The number of days to retain deleted VM data for this backup copy job',
    )
    #
    # GFS Settings
    #
    enable_gfs = models.CharField(
        max_length=50,
        choices=BackupCopyJobGFSEnableChoices,
        default=BackupCopyJobGFSEnableChoices.FALSE,
        help_text='Enable GFS (Grandfather-Father-Son) retention policy for this job',
    )
    weekly_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobGFSWeeklyEnabledChoices,
        default=BackupCopyJobGFSWeeklyEnabledChoices.FALSE,
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
        choices=BackupCopyJobGFSWeeklyDayChoices,
        default=BackupCopyJobGFSWeeklyDayChoices.SUNDAY,
        help_text='Day of the week to use as the weekly GFS restore point',
    )
    monthly_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobGFSMonthlyEnabledChoices,
        default=BackupCopyJobGFSMonthlyEnabledChoices.FALSE,
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
        choices=BackupCopyJobGFSWeekOfMonthChoices,
        default=BackupCopyJobGFSWeekOfMonthChoices.FIRST,
        help_text='Week of the month to use as the monthly GFS restore point',
    )
    yearly_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobGFSYearlyEnabledChoices,
        default=BackupCopyJobGFSYearlyEnabledChoices.FALSE,
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
        choices=BackupCopyJobGFSMonthOfYearChoices,
        default=BackupCopyJobGFSMonthOfYearChoices.JANUARY,
        help_text='Month of the year to use as the yearly GFS restore point',
    )
    #
    # Schedule Options
    #
    transfer_window = models.CharField(
        max_length=50,
        choices=BackupCopyJobTransferWindowChoices,
        default=BackupCopyJobTransferWindowChoices.CONTINUOUSLY,
        help_text='Whether the transfer window runs continuously or on a per-day-of-week hour schedule',
    )
    transfer_window_monday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Monday Schema',
        help_text='Hours during which the transfer window is allowed to run on Monday',
    )
    transfer_window_tuesday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Tuesday Schema',
        help_text='Hours during which the transfer window is allowed to run on Tuesday',
    )
    transfer_window_wednesday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Wednesday Schema',
        help_text='Hours during which the transfer window is allowed to run on Wednesday',
    )
    transfer_window_thursday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Thursday Schema',
        help_text='Hours during which the transfer window is allowed to run on Thursday',
    )
    transfer_window_friday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Friday Schema',
        help_text='Hours during which the transfer window is allowed to run on Friday',
    )
    transfer_window_saturday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Saturday Schema',
        help_text='Hours during which the transfer window is allowed to run on Saturday',
    )
    transfer_window_sunday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Sunday Schema',
        help_text='Hours during which the transfer window is allowed to run on Sunday',
    )
    #
    # Schedule Options (used when mode is periodic)
    #
    run_automatically = models.CharField(
        max_length=50,
        choices=BackupCopyJobRunAutomaticallyChoices,
        default=BackupCopyJobRunAutomaticallyChoices.FALSE,
        help_text='Whether the job runs automatically according to the schedule below',
    )
    schedule_daily_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobScheduleDailyEnabledChoices,
        default=BackupCopyJobScheduleDailyEnabledChoices.FALSE,
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
        choices=BackupCopyJobScheduleDailyKindChoices,
        default=BackupCopyJobScheduleDailyKindChoices.EVERYDAY,
        blank=True,
        verbose_name='Daily Kind',
        help_text='Which days the daily schedule applies to',
    )
    schedule_daily_days = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupCopyJobScheduleDaysChoices),
        default=default_schedule_daily_days,
        blank=True,
        verbose_name='Daily Days',
        help_text='The specific days of the week the daily schedule runs, when Daily Kind is Selected Days',
    )
    schedule_monthly_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobScheduleMonthlyEnabledChoices,
        default=BackupCopyJobScheduleMonthlyEnabledChoices.FALSE,
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
        choices=BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
        default=BackupCopyJobScheduleMonthlyDayNumberInMonthChoices.FIRST,
        blank=True,
        verbose_name='Monthly Day number of Month',
        help_text='The day of the month the monthly schedule runs',
    )
    schedule_monthly_day_of_week = models.CharField(
        max_length=50,
        choices=BackupCopyJobScheduleMonthlyDayOfWeekChoices,
        default=BackupCopyJobScheduleMonthlyDayOfWeekChoices.SATURDAY,
        blank=True,
        verbose_name='Monthly Day of Week',
        help_text='The day of the week the monthly schedule runs',
    )
    schedule_monthly_day_of_month = models.CharField(
        max_length=50,
        choices=BackupCopyJobScheduleDayOfMonthChoices,
        default='1',
        blank=True,
        verbose_name='Monthly Day of Month',
        help_text='The day of the month the monthly schedule runs',
    )
    schedule_monthly_months = ArrayField(
        base_field=models.CharField(max_length=50, choices=BackupCopyJobScheduleMonthChoices),
        default=default_schedule_monthly_months,
        blank=True,
        verbose_name='Monthly Months',
        help_text='The months the monthly schedule runs in',
    )
    schedule_periodically_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobPeriodicallyEnabledChoices,
        default=BackupCopyJobPeriodicallyEnabledChoices.FALSE,
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
        choices=BackupCopyJobPeriodicallyUnitChoices,
        default=BackupCopyJobPeriodicallyUnitChoices.HOURS,
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
        help_text='Offset in minutes applied to the start of each hour block in the day schemas below',
    )
    schedule_periodically_monday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Monday Schema',
        help_text='Hours during which this job is allowed to run on Monday',
    )
    schedule_periodically_tuesday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Tuesday Schema',
        help_text='Hours during which this job is allowed to run on Tuesday',
    )
    schedule_periodically_wednesday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Wednesday Schema',
        help_text='Hours during which this job is allowed to run on Wednesday',
    )
    schedule_periodically_thursday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Thursday Schema',
        help_text='Hours during which this job is allowed to run on Thursday',
    )
    schedule_periodically_friday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Friday Schema',
        help_text='Hours during which this job is allowed to run on Friday',
    )
    schedule_periodically_saturday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Saturday Schema',
        help_text='Hours during which this job is allowed to run on Saturday',
    )
    schedule_periodically_sunday_schema = ArrayField(
        base_field=models.CharField(max_length=2, choices=BackupCopyJobScheduleHourChoices),
        default=default_transfer_window_all_hours,
        blank=True,
        verbose_name='Sunday Schema',
        help_text='Hours during which this job is allowed to run on Sunday',
    )
    after_job_enabled = models.CharField(
        max_length=50,
        choices=BackupCopyJobAfterJobEnabledChoices,
        default=BackupCopyJobAfterJobEnabledChoices.FALSE,
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

    class Meta:
        ordering = ('name',)
        verbose_name = 'BackupCopyJob'
        verbose_name_plural = 'Veeam BackupCopyJobs'
        constraints = [
            models.UniqueConstraint(
                Lower('name'),
                name='%(app_label)s_%(class)s_unique_name',
                violation_error_message=_("The BackupCopyJob 'Name' must be unique.")
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

    def get_status_color(self):
        return BackupCopyJobStatusChoices.colors.get(self.status)

    def get_last_backup_result_color(self):
        return BackupCopyJobResultChoices.colors.get(self.last_backup_result)

    def get_enable_deduplication_color(self):
        return BackupCopyJobEnableDeduplicationChoices.colors.get(self.enable_deduplication)

    def get_storage_encryption_enabled_color(self):
        return BackupCopyJobStorageEncryptionEnabledChoices.colors.get(self.storage_encryption_enabled)

    def get_transaction_log_copy_enabled_color(self):
        return BackupCopyJobTransactionLogCopyEnabledChoices.colors.get(self.transaction_log_copy_enabled)

    def get_enable_deleted_vm_data_retention_color(self):
        return BackupCopyJobEnableDeletedVmDataRetentionChoices.colors.get(self.enable_deleted_vm_data_retention)

    def get_enable_gfs_color(self):
        return BackupCopyJobGFSEnableChoices.colors.get(self.enable_gfs)

    def get_weekly_enabled_color(self):
        return BackupCopyJobGFSWeeklyEnabledChoices.colors.get(self.weekly_enabled)

    def get_monthly_enabled_color(self):
        return BackupCopyJobGFSMonthlyEnabledChoices.colors.get(self.monthly_enabled)

    def get_yearly_enabled_color(self):
        return BackupCopyJobGFSYearlyEnabledChoices.colors.get(self.yearly_enabled)

    def _hour_schema_display(self, hours, offset=0):
        if len(hours) == 24:
            return 'All Hours'
        if not hours:
            return 'No Hours'
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

    def get_transfer_window_monday_schema_display(self):
        return self._hour_schema_display(self.transfer_window_monday_schema)

    def get_transfer_window_tuesday_schema_display(self):
        return self._hour_schema_display(self.transfer_window_tuesday_schema)

    def get_transfer_window_wednesday_schema_display(self):
        return self._hour_schema_display(self.transfer_window_wednesday_schema)

    def get_transfer_window_thursday_schema_display(self):
        return self._hour_schema_display(self.transfer_window_thursday_schema)

    def get_transfer_window_friday_schema_display(self):
        return self._hour_schema_display(self.transfer_window_friday_schema)

    def get_transfer_window_saturday_schema_display(self):
        return self._hour_schema_display(self.transfer_window_saturday_schema)

    def get_transfer_window_sunday_schema_display(self):
        return self._hour_schema_display(self.transfer_window_sunday_schema)

    def get_run_automatically_color(self):
        return BackupCopyJobRunAutomaticallyChoices.colors.get(self.run_automatically)

    def get_schedule_daily_enabled_color(self):
        return BackupCopyJobScheduleDailyEnabledChoices.colors.get(self.schedule_daily_enabled)

    def get_schedule_daily_days_display(self):
        labels = {c[0]: str(c[1]) for c in BackupCopyJobScheduleDaysChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.schedule_daily_days) if self.schedule_daily_days else '—'

    def get_schedule_monthly_enabled_color(self):
        return BackupCopyJobScheduleMonthlyEnabledChoices.colors.get(self.schedule_monthly_enabled)

    def get_schedule_monthly_months_display(self):
        labels = {c[0]: str(c[1]) for c in BackupCopyJobScheduleMonthChoices.CHOICES}
        return ', '.join(labels.get(v, v) for v in self.schedule_monthly_months) if self.schedule_monthly_months else '—'

    def get_schedule_periodically_enabled_color(self):
        return BackupCopyJobPeriodicallyEnabledChoices.colors.get(self.schedule_periodically_enabled)

    def get_schedule_periodically_monday_schema_display(self):
        return self._hour_schema_display(
            self.schedule_periodically_monday_schema, self.schedule_periodically_hour_offset_in_min or 0
        )

    def get_schedule_periodically_tuesday_schema_display(self):
        return self._hour_schema_display(
            self.schedule_periodically_tuesday_schema, self.schedule_periodically_hour_offset_in_min or 0
        )

    def get_schedule_periodically_wednesday_schema_display(self):
        return self._hour_schema_display(
            self.schedule_periodically_wednesday_schema, self.schedule_periodically_hour_offset_in_min or 0
        )

    def get_schedule_periodically_thursday_schema_display(self):
        return self._hour_schema_display(
            self.schedule_periodically_thursday_schema, self.schedule_periodically_hour_offset_in_min or 0
        )

    def get_schedule_periodically_friday_schema_display(self):
        return self._hour_schema_display(
            self.schedule_periodically_friday_schema, self.schedule_periodically_hour_offset_in_min or 0
        )

    def get_schedule_periodically_saturday_schema_display(self):
        return self._hour_schema_display(
            self.schedule_periodically_saturday_schema, self.schedule_periodically_hour_offset_in_min or 0
        )

    def get_schedule_periodically_sunday_schema_display(self):
        return self._hour_schema_display(
            self.schedule_periodically_sunday_schema, self.schedule_periodically_hour_offset_in_min or 0
        )

    def get_after_job_enabled_color(self):
        return BackupCopyJobAfterJobEnabledChoices.colors.get(self.after_job_enabled)
