from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelForm
from netbox_backupjobs.models import BackupJob
from utilities.forms.rendering import FieldSet
from ...choices import (
    BackupJobPlatformChoices,
    BackupJobStatusChoices,
    BackupJobResultChoices,
    BackupJobAlgorithmChoices,
    BackupJobEnableDeduplicationChoices,
    BackupJobStorageEncryptionEnabledChoices,
    BackupJobEnableDeletedVmDataRetentionChoices,
    BackupJobEnableSyntheticFullForIncrementalChoices,
    BackupJobEnableSyntheticFullForReverseIncrementalChoices,
    BackupJobSyntheticFullChoices,
    BackupJobSyntheticFullDaysChoices,
    BackupJobSyntheticFullWeekChoices,
    BackupJobSyntheticFullMonthChoices,
    BackupJobEnableFullBackupChoices,
    BackupJobFullBackupScheduleKindChoices,
    BackupJobFullBackupDaysChoices,
    BackupJobFullBackupWeekChoices,
    BackupJobFullBackupMonthChoices,
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
    BackupJobScheduleDayOfMonthChoices,
    BackupJobScheduleMonthChoices,
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
    BackupJobScheduleHourChoices,
)
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.utils import add_blank_choice
from utilities.forms.widgets import DateTimePicker, TimePicker

from ipam.models import IPAddress
from virtualization.models import VirtualMachine

__all__ = (
    'BackupJobForm',
)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all' button (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})


class BackupJobForm(NetBoxModelForm):
    """
    Form for creating and editing BackupJob objects.
    """
    name = forms.CharField()
    status = forms.ChoiceField(
        choices=BackupJobStatusChoices,
        required=True,
    )
    jobtype = forms.CharField(
        required=False,
        label=_('Job Type'),
    )
    platform = forms.ChoiceField(
        choices=add_blank_choice(BackupJobPlatformChoices),
        required=False,
        label=_('Platform'),
    )
    job_creation_time = forms.DateTimeField(
        required=False,
        label=_('Job Creation Time'),
        widget=DateTimePicker(),
    )
    last_backup_end_time = forms.DateTimeField(
        required=False,
        label=_('Last Backup End Time'),
        widget=DateTimePicker(),
    )
    last_backup_result = forms.ChoiceField(
        choices=add_blank_choice(BackupJobResultChoices),
        required=False,
        label=_('Last Backup Result'),
    )
    description = forms.CharField(
        required=False,
    )
    backup_server_name = forms.CharField(
        required=False,
        label=_('Backup Server Name'),
        help_text=_(
            'Used only as a fallback. If the Backup Server IP is assigned to a device or virtual machine in '
            'NetBox, that name is shown instead.'
        ),
    )
    backup_server_ip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label=_('Backup Server IP'),
    )
    target = forms.CharField(
        required=False,
        label=_('Target'),
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label="Virtual Machines",
        help_text='The virtual machines associated with this backup job',
    )

    # Advanced job settings
    algorithm = forms.ChoiceField(
        choices=BackupJobAlgorithmChoices,
        required=True,
        label=_('Algorithm'),
    )
    enable_deduplication = forms.ChoiceField(
        choices=BackupJobEnableDeduplicationChoices,
        required=True,
        label=_('Enable Deduplication'),
    )
    storage_encryption_enabled = forms.ChoiceField(
        choices=BackupJobStorageEncryptionEnabledChoices,
        required=True,
        label=_('Enable Storage Encryption'),
    )
    retain_days_to_keep = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep'),
    )
    retain_cycles = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Cycles'),
    )
    enable_deleted_vm_data_retention = forms.ChoiceField(
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        required=True,
        label=_('Enable Deleted VM Data Retention'),
    )
    retain_days_to_keep_deleted_vm_data = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep Deleted VM Data'),
    )

    # Synthetic full backup settings
    transform_full_to_synthetic = forms.ChoiceField(
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        required=True,
        label=_('Transform Incremental to Synthetic Full'),
    )
    transform_to_synthetic_full = forms.ChoiceField(
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        required=True,
        label=_('Transform Reverse Incremental to Synthetic Full'),
    )
    transform_to_synthetic_kind = forms.ChoiceField(
        choices=BackupJobSyntheticFullChoices,
        required=False,
        label=_('Synthetic Full Kind'),
    )
    transform_to_synthetic_days = forms.MultipleChoiceField(
        choices=BackupJobSyntheticFullDaysChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Synthetic Full Days of Week'),
    )
    synthetic_full_day_number_in_month = forms.ChoiceField(
        choices=BackupJobSyntheticFullWeekChoices,
        required=False,
        label=_('Synthetic Full Week of Month'),
    )
    synthetic_full_day_of_week = forms.ChoiceField(
        choices=BackupJobSyntheticFullDaysChoices,
        required=False,
        label=_('Synthetic Full Day of Week (Monthly)'),
    )
    transform_to_synthetic_monthly = forms.MultipleChoiceField(
        choices=BackupJobSyntheticFullMonthChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Synthetic Full Months'),
    )

    # Active full backup settings
    enable_full_backup = forms.ChoiceField(
        choices=BackupJobEnableFullBackupChoices,
        required=True,
        label=_('Enable Active Full Backup'),
    )
    full_backup_schedule_kind = forms.ChoiceField(
        choices=BackupJobFullBackupScheduleKindChoices,
        required=False,
        label=_('Schedule Kind'),
    )
    full_backup_days = forms.MultipleChoiceField(
        choices=BackupJobFullBackupDaysChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Days of Week'),
    )
    full_backup_day_number_in_month = forms.ChoiceField(
        choices=BackupJobFullBackupWeekChoices,
        required=False,
        label=_('Week of Month'),
    )
    full_backup_day_of_week = forms.ChoiceField(
        choices=BackupJobFullBackupDaysChoices,
        required=False,
        label=_('Day of Week (Monthly)'),
    )
    full_backup_months = forms.MultipleChoiceField(
        choices=BackupJobFullBackupMonthChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Months'),
    )

    # GFS retention settings
    enable_gfs = forms.ChoiceField(
        choices=BackupJobGFSEnableChoices,
        required=True,
        label=_('Enable GFS'),
    )
    weekly_enabled = forms.ChoiceField(
        choices=BackupJobGFSWeeklyEnabledChoices,
        required=True,
        label=_('Weekly Enabled'),
    )
    weekly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Weekly Keep (weeks)'),
    )
    weekly_keep_backups_on_day_of_week = forms.ChoiceField(
        choices=BackupJobGFSWeeklyDayChoices,
        required=False,
        label=_('Weekly Day'),
    )
    monthly_enabled = forms.ChoiceField(
        choices=BackupJobGFSMonthlyEnabledChoices,
        required=True,
        label=_('Monthly Enabled'),
    )
    monthly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Monthly Keep (months)'),
    )
    monthly_keep_backups_week_of_month = forms.ChoiceField(
        choices=BackupJobGFSWeekOfMonthChoices,
        required=False,
        label=_('Monthly Week'),
    )
    yearly_enabled = forms.ChoiceField(
        choices=BackupJobGFSYearlyEnabledChoices,
        required=True,
        label=_('Yearly Enabled'),
    )
    yearly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Yearly Keep (years)'),
    )
    yearly_keep_backups_on_month_of_year = forms.ChoiceField(
        choices=BackupJobGFSMonthOfYearChoices,
        required=False,
        label=_('Yearly Month'),
    )

    # Schedule options
    run_automatically = forms.ChoiceField(
        choices=BackupJobRunAutomaticallyChoices,
        required=True,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.ChoiceField(
        choices=BackupJobScheduleDailyEnabledChoices,
        required=True,
        label=_('Daily Enabled'),
    )
    schedule_daily_time = forms.TimeField(
        required=False,
        label=_('Daily Time'),
        widget=TimePicker(),
    )
    schedule_daily_kind = forms.ChoiceField(
        choices=BackupJobScheduleDailyKindChoices,
        required=False,
        label=_('Daily Kind'),
    )
    schedule_daily_days = forms.MultipleChoiceField(
        choices=BackupJobScheduleDaysChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Daily Days'),
    )
    schedule_monthly_enabled = forms.ChoiceField(
        choices=BackupJobScheduleMonthlyEnabledChoices,
        required=True,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_time = forms.TimeField(
        required=False,
        label=_('Monthly Time'),
        widget=TimePicker(),
    )
    schedule_monthly_day_of_week = forms.ChoiceField(
        choices=BackupJobScheduleMonthlyDayOfWeekChoices,
        required=False,
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = forms.ChoiceField(
        choices=BackupJobScheduleMonthlyDayNumberInMonthChoices,
        required=False,
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = forms.ChoiceField(
        choices=BackupJobScheduleDayOfMonthChoices,
        required=False,
        label=_('Monthly Day of Month'),
    )
    schedule_monthly_months = forms.MultipleChoiceField(
        choices=BackupJobScheduleMonthChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Monthly Months'),
    )
    schedule_periodically_enabled = forms.ChoiceField(
        choices=BackupJobPeriodicallyEnabledChoices,
        required=True,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_every = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Periodically Every'),
    )
    schedule_periodically_unit = forms.ChoiceField(
        choices=BackupJobPeriodicallyUnitChoices,
        required=False,
        label=_('Periodically Unit'),
    )
    schedule_periodically_hour_offset_in_min = forms.IntegerField(
        required=False,
        min_value=0,
        max_value=59,
        label=_('Hour Offset (min)'),
        help_text=_('Offset in minutes applied to the start of each hour block in the day schemas below'),
    )
    schedule_periodically_monday_schema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Monday Schema'),
    )
    schedule_periodically_tuesday_schema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Tuesday Schema'),
    )
    schedule_periodically_wednesday_schema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Wednesday Schema'),
    )
    schedule_periodically_thursday_schema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Thursday Schema'),
    )
    schedule_periodically_friday_schema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Friday Schema'),
    )
    schedule_periodically_saturday_schema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Saturday Schema'),
    )
    schedule_periodically_sunday_schema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Sunday Schema'),
    )

    # After job
    after_job_enabled = forms.ChoiceField(
        choices=BackupJobAfterJobEnabledChoices,
        required=True,
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('After Job'),
    )

    fieldsets = (
        FieldSet(
            'name', 'description', 'status', 'jobtype', 'platform', 'job_creation_time', 'last_backup_end_time', 'last_backup_result', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'tags',
            name=_('Backup Job'),
        ),
        FieldSet(
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled',
            'retain_days_to_keep', 'retain_cycles',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'run_automatically',
            'schedule_daily_enabled', 'schedule_daily_time', 'schedule_daily_kind', 'schedule_daily_days',
            'schedule_monthly_enabled', 'schedule_monthly_time', 'schedule_monthly_day_of_week',
            'schedule_monthly_day_number_in_month', 'schedule_monthly_day_of_month', 'schedule_monthly_months',
            'schedule_periodically_enabled', 'schedule_periodically_every', 'schedule_periodically_unit',
            'schedule_periodically_hour_offset_in_min',
            'schedule_periodically_monday_schema', 'schedule_periodically_tuesday_schema',
            'schedule_periodically_wednesday_schema', 'schedule_periodically_thursday_schema',
            'schedule_periodically_friday_schema', 'schedule_periodically_saturday_schema',
            'schedule_periodically_sunday_schema',
            'after_job_enabled', 'after_job_name',
            name=_('Schedule Options'),
        ),
        FieldSet(
            'transform_full_to_synthetic', 'transform_to_synthetic_full',
            'transform_to_synthetic_kind',
            'transform_to_synthetic_days',
            'synthetic_full_day_number_in_month', 'synthetic_full_day_of_week',
            'transform_to_synthetic_monthly',
            name=_('Synthetic Full Backup'),
        ),
        FieldSet(
            'enable_full_backup', 'full_backup_schedule_kind',
            'full_backup_days',
            'full_backup_day_number_in_month', 'full_backup_day_of_week',
            'full_backup_months',
            name=_('Active Full Backup'),
        ),
        FieldSet(
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            name=_('GFS Retention'),
        ),
    )

    class Meta:
        model = BackupJob
        fields = [
            'name', 'status', 'jobtype', 'platform', 'job_creation_time', 'last_backup_end_time', 'last_backup_result', 'description', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'comments', 'tags',
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled',
            'retain_days_to_keep', 'retain_cycles',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            'transform_full_to_synthetic', 'transform_to_synthetic_full',
            'transform_to_synthetic_kind', 'transform_to_synthetic_days',
            'synthetic_full_day_number_in_month', 'synthetic_full_day_of_week',
            'transform_to_synthetic_monthly',
            'enable_full_backup', 'full_backup_schedule_kind',
            'full_backup_days', 'full_backup_day_number_in_month', 'full_backup_day_of_week',
            'full_backup_months',
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            'run_automatically',
            'schedule_daily_enabled', 'schedule_daily_time', 'schedule_daily_kind', 'schedule_daily_days',
            'schedule_monthly_enabled', 'schedule_monthly_time', 'schedule_monthly_day_of_week',
            'schedule_monthly_day_number_in_month', 'schedule_monthly_day_of_month', 'schedule_monthly_months',
            'schedule_periodically_enabled', 'schedule_periodically_every', 'schedule_periodically_unit',
            'schedule_periodically_hour_offset_in_min',
            'schedule_periodically_monday_schema', 'schedule_periodically_tuesday_schema',
            'schedule_periodically_wednesday_schema', 'schedule_periodically_thursday_schema',
            'schedule_periodically_friday_schema', 'schedule_periodically_saturday_schema',
            'schedule_periodically_sunday_schema',
            'after_job_enabled', 'after_job_name',
        ]


