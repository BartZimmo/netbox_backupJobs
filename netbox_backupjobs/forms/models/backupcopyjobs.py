from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelForm
from ipam.models import IPAddress
from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.models.backupcopyjobs import default_transfer_window_all_hours
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet
from utilities.forms.utils import add_blank_choice
from utilities.forms.widgets import DateTimePicker, TimePicker
from ...choices import (
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

__all__ = (
    'BackupCopyJobForm',
)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all' button (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})


class BackupCopyJobForm(NetBoxModelForm):
    """
    Form for creating and editing BackupCopyJob objects.
    """
    name = forms.CharField()
    status = forms.ChoiceField(
        choices=BackupCopyJobStatusChoices,
        required=True,
    )
    mode = forms.ChoiceField(
        choices=BackupCopyJobModeChoices,
        required=True,
        label=_('Copy Mode'),
    )
    data_transfer_mode = forms.ChoiceField(
        choices=BackupCopyJobDataTransferModeChoices,
        required=True,
        label=_('Data Transfer Mode'),
    )
    jobtype = forms.CharField(
        required=False,
        label=_('Job Type'),
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
    job_creation_time = forms.DateTimeField(
        required=False,
        label=_('Job Creation Time'),
        widget=DateTimePicker(),
    )
    last_backup_result = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobResultChoices),
        required=False,
        label=_('Last Backup Result'),
    )
    retain_days_to_keep = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep'),
    )
    target = forms.CharField(
        required=False,
        label=_('Target'),
    )
    backup_jobs = DynamicModelMultipleChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('Backup Jobs'),
        help_text=_('The backup job(s) that this copy job is associated with'),
    )

    # Advanced settings
    enable_deduplication = forms.ChoiceField(
        choices=BackupCopyJobEnableDeduplicationChoices,
        required=True,
        label=_('Enable Deduplication'),
    )
    storage_encryption_enabled = forms.ChoiceField(
        choices=BackupCopyJobStorageEncryptionEnabledChoices,
        required=True,
        label=_('Enable Storage Encryption'),
    )
    transaction_log_copy_enabled = forms.ChoiceField(
        choices=BackupCopyJobTransactionLogCopyEnabledChoices,
        required=True,
        label=_('Enable Transaction Log Copy'),
    )
    enable_deleted_vm_data_retention = forms.ChoiceField(
        choices=BackupCopyJobEnableDeletedVmDataRetentionChoices,
        required=True,
        label=_('Enable Deleted VM Data Retention'),
    )
    retain_days_to_keep_deleted_vm_data = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep Deleted VM Data'),
    )

    # GFS retention settings
    enable_gfs = forms.ChoiceField(
        choices=BackupCopyJobGFSEnableChoices,
        required=True,
        label=_('Enable GFS'),
    )
    weekly_enabled = forms.ChoiceField(
        choices=BackupCopyJobGFSWeeklyEnabledChoices,
        required=True,
        label=_('Weekly Enabled'),
    )
    weekly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Weekly Keep (weeks)'),
    )
    weekly_keep_backups_on_day_of_week = forms.ChoiceField(
        choices=BackupCopyJobGFSWeeklyDayChoices,
        required=False,
        label=_('Weekly Day'),
    )
    monthly_enabled = forms.ChoiceField(
        choices=BackupCopyJobGFSMonthlyEnabledChoices,
        required=True,
        label=_('Monthly Enabled'),
    )
    monthly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Monthly Keep (months)'),
    )
    monthly_keep_backups_week_of_month = forms.ChoiceField(
        choices=BackupCopyJobGFSWeekOfMonthChoices,
        required=False,
        label=_('Monthly Week'),
    )
    yearly_enabled = forms.ChoiceField(
        choices=BackupCopyJobGFSYearlyEnabledChoices,
        required=True,
        label=_('Yearly Enabled'),
    )
    yearly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Yearly Keep (years)'),
    )
    yearly_keep_backups_on_month_of_year = forms.ChoiceField(
        choices=BackupCopyJobGFSMonthOfYearChoices,
        required=False,
        label=_('Yearly Month'),
    )

    # Schedule options
    transfer_window = forms.ChoiceField(
        choices=BackupCopyJobTransferWindowChoices,
        required=True,
        label=_('Transfer Window'),
    )
    transfer_window_monday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Monday Schema'),
    )
    transfer_window_tuesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Tuesday Schema'),
    )
    transfer_window_wednesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Wednesday Schema'),
    )
    transfer_window_thursday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Thursday Schema'),
    )
    transfer_window_friday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Friday Schema'),
    )
    transfer_window_saturday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Saturday Schema'),
    )
    transfer_window_sunday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Sunday Schema'),
    )

    # Schedule options (used when mode is periodic)
    run_automatically = forms.ChoiceField(
        choices=BackupCopyJobRunAutomaticallyChoices,
        required=True,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.ChoiceField(
        choices=BackupCopyJobScheduleDailyEnabledChoices,
        required=True,
        label=_('Daily Enabled'),
    )
    schedule_daily_time = forms.TimeField(
        required=False,
        label=_('Daily Time'),
        widget=TimePicker(),
    )
    schedule_daily_kind = forms.ChoiceField(
        choices=BackupCopyJobScheduleDailyKindChoices,
        required=False,
        label=_('Daily Kind'),
    )
    schedule_daily_days = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleDaysChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Daily Days'),
    )
    schedule_monthly_enabled = forms.ChoiceField(
        choices=BackupCopyJobScheduleMonthlyEnabledChoices,
        required=True,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_time = forms.TimeField(
        required=False,
        label=_('Monthly Time'),
        widget=TimePicker(),
    )
    schedule_monthly_day_of_week = forms.ChoiceField(
        choices=BackupCopyJobScheduleMonthlyDayOfWeekChoices,
        required=False,
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = forms.ChoiceField(
        choices=BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
        required=False,
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = forms.ChoiceField(
        choices=BackupCopyJobScheduleDayOfMonthChoices,
        required=False,
        label=_('Monthly Day of Month'),
    )
    schedule_monthly_months = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleMonthChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Monthly Months'),
    )
    schedule_periodically_enabled = forms.ChoiceField(
        choices=BackupCopyJobPeriodicallyEnabledChoices,
        required=True,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_every = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Periodically Every'),
    )
    schedule_periodically_unit = forms.ChoiceField(
        choices=BackupCopyJobPeriodicallyUnitChoices,
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
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Monday Schema'),
    )
    schedule_periodically_tuesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Tuesday Schema'),
    )
    schedule_periodically_wednesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Wednesday Schema'),
    )
    schedule_periodically_thursday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Thursday Schema'),
    )
    schedule_periodically_friday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Friday Schema'),
    )
    schedule_periodically_saturday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Saturday Schema'),
    )
    schedule_periodically_sunday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        initial=default_transfer_window_all_hours,
        widget=select_all_widget(),
        label=_('Sunday Schema'),
    )
    after_job_enabled = forms.ChoiceField(
        choices=BackupCopyJobAfterJobEnabledChoices,
        required=True,
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelChoiceField(
        queryset=BackupCopyJob.objects.all(),
        required=False,
        label=_('After Job'),
    )

    fieldsets = (
        FieldSet(
            'name', 'description', 'status', 'mode', 'data_transfer_mode', 'jobtype', 'job_creation_time',
            'last_backup_result', 'backup_server_name', 'backup_server_ip', 'retain_days_to_keep', 'target',
            'backup_jobs', 'tags',
            name=_('Backup Copy Job'),
        ),
        FieldSet(
            'enable_deduplication', 'storage_encryption_enabled', 'transaction_log_copy_enabled',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            name=_('GFS Retention'),
        ),
        FieldSet(
            'transfer_window',
            'transfer_window_monday_schema', 'transfer_window_tuesday_schema', 'transfer_window_wednesday_schema',
            'transfer_window_thursday_schema', 'transfer_window_friday_schema', 'transfer_window_saturday_schema',
            'transfer_window_sunday_schema',
            name=_('Schedule Options when Copy Mode is Immediate'),
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
            name=_('Schedule Options when Copy Mode is Periodic'),
        ),
    )

    class Meta:
        model = BackupCopyJob
        fields = [
            'name', 'description', 'status', 'mode', 'data_transfer_mode', 'jobtype', 'job_creation_time',
            'last_backup_result', 'backup_server_name', 'backup_server_ip', 'retain_days_to_keep', 'target',
            'backup_jobs',
            'enable_deduplication', 'storage_encryption_enabled', 'transaction_log_copy_enabled',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            'transfer_window',
            'transfer_window_monday_schema', 'transfer_window_tuesday_schema', 'transfer_window_wednesday_schema',
            'transfer_window_thursday_schema', 'transfer_window_friday_schema', 'transfer_window_saturday_schema',
            'transfer_window_sunday_schema',
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
            'tags',
        ]
