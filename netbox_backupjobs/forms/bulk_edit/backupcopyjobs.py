from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelBulkEditForm
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet, TabbedGroups
from utilities.forms.utils import add_blank_choice
from utilities.forms.widgets import DateTimePicker, TimePicker

from ipam.models import IPAddress

from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.choices import (
    BackupCopyJobStatusChoices,
    BackupCopyJobResultChoices,
    BackupCopyJobModeChoices,
    BackupCopyJobDataTransferModeChoices,
    BackupCopyJobEnableDeduplicationChoices,
    BackupCopyJobStorageEncryptionEnabledChoices,
    BackupCopyJobTransactionLogCopyEnabledChoices,
    BackupCopyJobEnableDeletedVmDataRetentionChoices,
    BackupCopyJobGFSEnableChoices,
    BackupCopyJobGFSWeeklyEnabledChoices,
    BackupCopyJobGFSWeeklyDayChoices,
    BackupCopyJobGFSMonthlyEnabledChoices,
    BackupCopyJobGFSWeekOfMonthChoices,
    BackupCopyJobGFSYearlyEnabledChoices,
    BackupCopyJobGFSMonthOfYearChoices,
    BackupCopyJobTransferWindowChoices,
    BackupCopyJobScheduleHourChoices,
    BackupCopyJobRunAutomaticallyChoices,
    BackupCopyJobScheduleDailyEnabledChoices,
    BackupCopyJobScheduleDailyKindChoices,
    BackupCopyJobScheduleDaysChoices,
    BackupCopyJobScheduleMonthlyEnabledChoices,
    BackupCopyJobScheduleMonthlyDayOfWeekChoices,
    BackupCopyJobScheduleDayOfMonthChoices,
    BackupCopyJobScheduleMonthChoices,
    BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
    BackupCopyJobPeriodicallyEnabledChoices,
    BackupCopyJobPeriodicallyUnitChoices,
    BackupCopyJobAfterJobEnabledChoices,
)

__all__ = (
    'BackupCopyJobBulkEditForm',
)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all'/'Clear' button pair (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})


class BackupCopyJobBulkEditForm(NetBoxModelBulkEditForm):
    """
    Form for bulk editing BackupCopyJob objects.
    """
    jobtype = forms.CharField(
        required=False,
        label=_('Job Type'),
    )
    status = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobStatusChoices),
        required=False,
        label=_('Status'),
    )
    mode = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobModeChoices),
        required=False,
        label=_('Copy Mode'),
    )
    data_transfer_mode = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobDataTransferModeChoices),
        required=False,
        label=_('Data Transfer Mode'),
    )
    description = forms.CharField(
        required=False,
        label=_('Description'),
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
    backup_server_name = forms.CharField(
        required=False,
        label=_('Backup Server Name'),
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
    add_backup_jobs = DynamicModelMultipleChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('Add Backup Jobs'),
    )
    remove_backup_jobs = DynamicModelMultipleChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('Remove Backup Jobs'),
    )

    # Advanced settings
    enable_deduplication = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobEnableDeduplicationChoices),
        required=False,
        label=_('Enable Deduplication'),
    )
    storage_encryption_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobStorageEncryptionEnabledChoices),
        required=False,
        label=_('Enable Storage Encryption'),
    )
    transaction_log_copy_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobTransactionLogCopyEnabledChoices),
        required=False,
        label=_('Enable Transaction Log Copy'),
    )
    enable_deleted_vm_data_retention = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobEnableDeletedVmDataRetentionChoices),
        required=False,
        label=_('Enable Deleted VM Data Retention'),
    )
    retain_days_to_keep_deleted_vm_data = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep Deleted VM Data'),
    )

    # GFS retention settings
    enable_gfs = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobGFSEnableChoices),
        required=False,
        label=_('Enable GFS'),
    )
    weekly_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobGFSWeeklyEnabledChoices),
        required=False,
        label=_('Weekly Enabled'),
    )
    weekly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Weekly Keep (weeks)'),
    )
    weekly_keep_backups_on_day_of_week = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobGFSWeeklyDayChoices),
        required=False,
        label=_('Weekly Day'),
    )
    monthly_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobGFSMonthlyEnabledChoices),
        required=False,
        label=_('Monthly Enabled'),
    )
    monthly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Monthly Keep (months)'),
    )
    monthly_keep_backups_week_of_month = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobGFSWeekOfMonthChoices),
        required=False,
        label=_('Monthly Week'),
    )
    yearly_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobGFSYearlyEnabledChoices),
        required=False,
        label=_('Yearly Enabled'),
    )
    yearly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Yearly Keep (years)'),
    )
    yearly_keep_backups_on_month_of_year = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobGFSMonthOfYearChoices),
        required=False,
        label=_('Yearly Month'),
    )

    # Schedule options when mode is immediate
    transfer_window = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobTransferWindowChoices),
        required=False,
        label=_('Transfer Window'),
    )
    transfer_window_monday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Monday Schema'),
    )
    transfer_window_tuesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Tuesday Schema'),
    )
    transfer_window_wednesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Wednesday Schema'),
    )
    transfer_window_thursday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Thursday Schema'),
    )
    transfer_window_friday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Friday Schema'),
    )
    transfer_window_saturday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Saturday Schema'),
    )
    transfer_window_sunday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Sunday Schema'),
    )

    # Schedule options when mode is periodic
    run_automatically = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobRunAutomaticallyChoices),
        required=False,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobScheduleDailyEnabledChoices),
        required=False,
        label=_('Daily Enabled'),
    )
    schedule_daily_time = forms.TimeField(
        required=False,
        label=_('Daily Time'),
        widget=TimePicker(),
    )
    schedule_daily_kind = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobScheduleDailyKindChoices),
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
        choices=add_blank_choice(BackupCopyJobScheduleMonthlyEnabledChoices),
        required=False,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_time = forms.TimeField(
        required=False,
        label=_('Monthly Time'),
        widget=TimePicker(),
    )
    schedule_monthly_day_of_week = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobScheduleMonthlyDayOfWeekChoices),
        required=False,
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobScheduleMonthlyDayNumberInMonthChoices),
        required=False,
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobScheduleDayOfMonthChoices),
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
        choices=add_blank_choice(BackupCopyJobPeriodicallyEnabledChoices),
        required=False,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_every = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Periodically Every'),
    )
    schedule_periodically_unit = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobPeriodicallyUnitChoices),
        required=False,
        label=_('Periodically Unit'),
    )
    schedule_periodically_hour_offset_in_min = forms.IntegerField(
        required=False,
        min_value=0,
        max_value=59,
        label=_('Hour Offset (min)'),
    )
    schedule_periodically_monday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Monday Schema'),
    )
    schedule_periodically_tuesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Tuesday Schema'),
    )
    schedule_periodically_wednesday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Wednesday Schema'),
    )
    schedule_periodically_thursday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Thursday Schema'),
    )
    schedule_periodically_friday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Friday Schema'),
    )
    schedule_periodically_saturday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Saturday Schema'),
    )
    schedule_periodically_sunday_schema = forms.MultipleChoiceField(
        choices=BackupCopyJobScheduleHourChoices,
        required=False,
        widget=select_all_widget(),
        label=_('Sunday Schema'),
    )
    after_job_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupCopyJobAfterJobEnabledChoices),
        required=False,
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelChoiceField(
        queryset=BackupCopyJob.objects.all(),
        required=False,
        label=_('After Job'),
    )

    model = BackupCopyJob
    fieldsets = (
        FieldSet(
            'jobtype', 'status', 'mode', 'data_transfer_mode', 'description',
            'job_creation_time', 'last_backup_result',
            'retain_days_to_keep', 'backup_server_name', 'backup_server_ip', 'target',
            name=_('Backup Copy Job'),
        ),
        FieldSet(
            TabbedGroups(
                FieldSet('add_backup_jobs', name=_('Add')),
                FieldSet('remove_backup_jobs', name=_('Remove')),
            ),
            name=_('Backup Jobs'),
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
            name=_('Schedule Options when Mode is Immediate'),
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
            name=_('Schedule Options when Mode is Periodic'),
        ),
    )
    nullable_fields = [
        'description', 'job_creation_time', 'backup_server_name', 'backup_server_ip', 'target',
        'retain_days_to_keep', 'retain_days_to_keep_deleted_vm_data',
        'weekly_keep_backups_for', 'monthly_keep_backups_for', 'yearly_keep_backups_for',
        'schedule_daily_time', 'schedule_monthly_time',
        'schedule_periodically_every', 'schedule_periodically_hour_offset_in_min',
        'after_job_name',
    ]
