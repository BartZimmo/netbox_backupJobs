__all__ = ('BackupCopyJobFilterForm',)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all' button (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})
from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelMultipleChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet, InlineFields
from utilities.forms.widgets import DateTimePicker, TimePicker

from ipam.models import IPAddress

from netbox_backupjobs.models import BackupJob, BackupCopyJob
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
    BackupCopyJobScheduleMonthlyEnabledChoices,
    BackupCopyJobScheduleMonthlyDayOfWeekChoices,
    BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
    BackupCopyJobScheduleDayOfMonthChoices,
    BackupCopyJobPeriodicallyEnabledChoices,
    BackupCopyJobPeriodicallyUnitChoices,
    BackupCopyJobAfterJobEnabledChoices,
)


class BackupCopyJobFilterForm(NetBoxModelFilterSetForm):
    model = BackupCopyJob
    fieldsets = (
        FieldSet(
            'q', 'name', 'description', 'status', 'mode', 'data_transfer_mode', 'jobtype',
            'job_creation_time_after', 'job_creation_time_before', 'last_backup_result',
            'backup_server_name', 'backup_server_ip', 'target', 'backup_job',
            name=_('Backup Copy Job'),
        ),
        FieldSet(
            'enable_deduplication', 'storage_encryption_enabled', 'transaction_log_copy_enabled',
            'enable_deleted_vm_data_retention',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'enable_gfs',
            name=_('GFS Retention: Enabled'),
        ),
        FieldSet(
            'weekly_enabled', 'weekly_keep_backups_on_day_of_week',
            name=_('GFS Retention: Weekly'),
        ),
        FieldSet(
            'monthly_enabled', 'monthly_keep_backups_week_of_month',
            name=_('GFS Retention: Monthly'),
        ),
        FieldSet(
            'yearly_enabled', 'yearly_keep_backups_on_month_of_year',
            name=_('GFS Retention: Yearly'),
        ),
        FieldSet(
            'transfer_window',
            'transfer_window_monday_schema',
            InlineFields('transfer_window_monday_between_after', 'transfer_window_monday_between_before', label=_('Monday Schema Between')),
            'transfer_window_tuesday_schema',
            InlineFields('transfer_window_tuesday_between_after', 'transfer_window_tuesday_between_before', label=_('Tuesday Schema Between')),
            'transfer_window_wednesday_schema',
            InlineFields('transfer_window_wednesday_between_after', 'transfer_window_wednesday_between_before', label=_('Wednesday Schema Between')),
            'transfer_window_thursday_schema',
            InlineFields('transfer_window_thursday_between_after', 'transfer_window_thursday_between_before', label=_('Thursday Schema Between')),
            'transfer_window_friday_schema',
            InlineFields('transfer_window_friday_between_after', 'transfer_window_friday_between_before', label=_('Friday Schema Between')),
            'transfer_window_saturday_schema',
            InlineFields('transfer_window_saturday_between_after', 'transfer_window_saturday_between_before', label=_('Saturday Schema Between')),
            'transfer_window_sunday_schema',
            InlineFields('transfer_window_sunday_between_after', 'transfer_window_sunday_between_before', label=_('Sunday Schema Between')),
            name=_('Schedule Options when Mode is Immediate'),
        ),
        FieldSet(
            'run_automatically',
            name=_('Periodic Schedule: Run Automatically'),
        ),
        FieldSet(
            'schedule_daily_enabled', 'schedule_daily_kind',
            name=_('Periodic Schedule: Daily'),
        ),
        FieldSet(
            'schedule_monthly_enabled', 'schedule_monthly_day_of_week', 'schedule_monthly_day_number_in_month',
            'schedule_monthly_day_of_month',
            name=_('Periodic Schedule: Monthly'),
        ),
        FieldSet(
            'schedule_periodically_enabled', 'schedule_periodically_unit',
            'schedule_periodically_monday_schema',
            InlineFields('schedule_periodically_monday_between_after', 'schedule_periodically_monday_between_before', label=_('Monday Schema Between')),
            'schedule_periodically_tuesday_schema',
            InlineFields('schedule_periodically_tuesday_between_after', 'schedule_periodically_tuesday_between_before', label=_('Tuesday Schema Between')),
            'schedule_periodically_wednesday_schema',
            InlineFields('schedule_periodically_wednesday_between_after', 'schedule_periodically_wednesday_between_before', label=_('Wednesday Schema Between')),
            'schedule_periodically_thursday_schema',
            InlineFields('schedule_periodically_thursday_between_after', 'schedule_periodically_thursday_between_before', label=_('Thursday Schema Between')),
            'schedule_periodically_friday_schema',
            InlineFields('schedule_periodically_friday_between_after', 'schedule_periodically_friday_between_before', label=_('Friday Schema Between')),
            'schedule_periodically_saturday_schema',
            InlineFields('schedule_periodically_saturday_between_after', 'schedule_periodically_saturday_between_before', label=_('Saturday Schema Between')),
            'schedule_periodically_sunday_schema',
            InlineFields('schedule_periodically_sunday_between_after', 'schedule_periodically_sunday_between_before', label=_('Sunday Schema Between')),
            name=_('Periodic Schedule: Periodically'),
        ),
        FieldSet(
            'after_job_enabled', 'after_job_name',
            name=_('Periodic Schedule: After Job'),
        ),
        FieldSet('tag', name=_('Tags')),
    )
    q = forms.CharField(
        required=False,
        label='Search',
    )
    name = forms.CharField(
        required=False,
        label='Name',
    )
    status = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobStatusChoices,
        label='Status',
    )
    mode = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobModeChoices,
        label=_('Copy Mode'),
    )
    data_transfer_mode = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobDataTransferModeChoices,
        label=_('Data Transfer Mode'),
    )
    target = forms.CharField(
        required=False,
        label=_('Target'),
    )
    jobtype = forms.CharField(
        required=False,
        label=_('Job Type'),
    )
    job_creation_time_after = forms.DateTimeField(
        required=False,
        label=_('Job Creation Time After'),
        widget=DateTimePicker(),
    )
    job_creation_time_before = forms.DateTimeField(
        required=False,
        label=_('Job Creation Time Before'),
        widget=DateTimePicker(),
    )
    last_backup_result = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobResultChoices,
        label=_('Last Backup Result'),
    )
    description = forms.CharField(
        required=False,
        label='Description',
    )
    backup_server_name = forms.CharField(
        required=False,
        label=_('Backup Server Name'),
    )
    backup_server_ip = DynamicModelMultipleChoiceField(
        queryset=IPAddress.objects.all(),
        required=False,
        label=_('Backup Server IP'),
    )
    backup_job = DynamicModelMultipleChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('Backup Jobs'),
    )

    # Advanced settings
    enable_deduplication = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobEnableDeduplicationChoices,
        label=_('Deduplication'),
    )
    storage_encryption_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobStorageEncryptionEnabledChoices,
        label=_('Storage Encryption'),
    )
    transaction_log_copy_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobTransactionLogCopyEnabledChoices,
        label=_('Transaction Log Copy'),
    )
    enable_deleted_vm_data_retention = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobEnableDeletedVmDataRetentionChoices,
        label=_('Deleted VM Retention'),
    )

    # GFS retention settings
    enable_gfs = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSEnableChoices,
        label=_('GFS Enabled'),
    )
    weekly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSWeeklyEnabledChoices,
        label=_('GFS Weekly'),
    )
    monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSMonthlyEnabledChoices,
        label=_('GFS Monthly'),
    )
    yearly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSYearlyEnabledChoices,
        label=_('GFS Yearly'),
    )
    weekly_keep_backups_on_day_of_week = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSWeeklyDayChoices,
        widget=select_all_widget(),
        label=_('GFS Weekly Day'),
    )
    monthly_keep_backups_week_of_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSWeekOfMonthChoices,
        widget=select_all_widget(),
        label=_('GFS Monthly Week'),
    )
    yearly_keep_backups_on_month_of_year = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSMonthOfYearChoices,
        widget=select_all_widget(),
        label=_('GFS Yearly Month'),
    )

    # Schedule options
    transfer_window = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobTransferWindowChoices,
        label=_('Transfer Window'),
    )
    transfer_window_monday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Monday Schema Hours'),
    )
    transfer_window_monday_between_after = forms.TimeField(
        required=False,
        label=_('Monday after:'),
        widget=TimePicker(),
    )
    transfer_window_monday_between_before = forms.TimeField(
        required=False,
        label=_('Monday before:'),
        widget=TimePicker(),
    )
    transfer_window_tuesday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Tuesday Schema Hours'),
    )
    transfer_window_tuesday_between_after = forms.TimeField(
        required=False,
        label=_('Tuesday after:'),
        widget=TimePicker(),
    )
    transfer_window_tuesday_between_before = forms.TimeField(
        required=False,
        label=_('Tuesday before:'),
        widget=TimePicker(),
    )
    transfer_window_wednesday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Wednesday Schema Hours'),
    )
    transfer_window_wednesday_between_after = forms.TimeField(
        required=False,
        label=_('Wednesday after:'),
        widget=TimePicker(),
    )
    transfer_window_wednesday_between_before = forms.TimeField(
        required=False,
        label=_('Wednesday before:'),
        widget=TimePicker(),
    )
    transfer_window_thursday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Thursday Schema Hours'),
    )
    transfer_window_thursday_between_after = forms.TimeField(
        required=False,
        label=_('Thursday after:'),
        widget=TimePicker(),
    )
    transfer_window_thursday_between_before = forms.TimeField(
        required=False,
        label=_('Thursday before:'),
        widget=TimePicker(),
    )
    transfer_window_friday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Friday Schema Hours'),
    )
    transfer_window_friday_between_after = forms.TimeField(
        required=False,
        label=_('Friday after:'),
        widget=TimePicker(),
    )
    transfer_window_friday_between_before = forms.TimeField(
        required=False,
        label=_('Friday before:'),
        widget=TimePicker(),
    )
    transfer_window_saturday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Saturday Schema Hours'),
    )
    transfer_window_saturday_between_after = forms.TimeField(
        required=False,
        label=_('Saturday after:'),
        widget=TimePicker(),
    )
    transfer_window_saturday_between_before = forms.TimeField(
        required=False,
        label=_('Saturday before:'),
        widget=TimePicker(),
    )
    transfer_window_sunday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Sunday Schema Hours'),
    )
    transfer_window_sunday_between_after = forms.TimeField(
        required=False,
        label=_('Sunday after:'),
        widget=TimePicker(),
    )
    transfer_window_sunday_between_before = forms.TimeField(
        required=False,
        label=_('Sunday before:'),
        widget=TimePicker(),
    )
    run_automatically = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobRunAutomaticallyChoices,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleDailyEnabledChoices,
        label=_('Daily Enabled'),
    )
    schedule_daily_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleDailyKindChoices,
        label=_('Daily Kind'),
    )
    schedule_monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleMonthlyEnabledChoices,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_day_of_week = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleMonthlyDayOfWeekChoices,
        widget=select_all_widget(),
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
        widget=select_all_widget(),
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleDayOfMonthChoices,
        widget=select_all_widget(),
        label=_('Monthly Day of Month'),
    )
    schedule_periodically_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobPeriodicallyEnabledChoices,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_unit = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobPeriodicallyUnitChoices,
        label=_('Periodically Unit'),
    )
    schedule_periodically_monday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Monday Schema Hours'),
    )
    schedule_periodically_monday_between_after = forms.TimeField(
        required=False,
        label=_('Monday after:'),
        widget=TimePicker(),
    )
    schedule_periodically_monday_between_before = forms.TimeField(
        required=False,
        label=_('Monday before:'),
        widget=TimePicker(),
    )
    schedule_periodically_tuesday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Tuesday Schema Hours'),
    )
    schedule_periodically_tuesday_between_after = forms.TimeField(
        required=False,
        label=_('Tuesday after:'),
        widget=TimePicker(),
    )
    schedule_periodically_tuesday_between_before = forms.TimeField(
        required=False,
        label=_('Tuesday before:'),
        widget=TimePicker(),
    )
    schedule_periodically_wednesday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Wednesday Schema Hours'),
    )
    schedule_periodically_wednesday_between_after = forms.TimeField(
        required=False,
        label=_('Wednesday after:'),
        widget=TimePicker(),
    )
    schedule_periodically_wednesday_between_before = forms.TimeField(
        required=False,
        label=_('Wednesday before:'),
        widget=TimePicker(),
    )
    schedule_periodically_thursday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Thursday Schema Hours'),
    )
    schedule_periodically_thursday_between_after = forms.TimeField(
        required=False,
        label=_('Thursday after:'),
        widget=TimePicker(),
    )
    schedule_periodically_thursday_between_before = forms.TimeField(
        required=False,
        label=_('Thursday before:'),
        widget=TimePicker(),
    )
    schedule_periodically_friday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Friday Schema Hours'),
    )
    schedule_periodically_friday_between_after = forms.TimeField(
        required=False,
        label=_('Friday after:'),
        widget=TimePicker(),
    )
    schedule_periodically_friday_between_before = forms.TimeField(
        required=False,
        label=_('Friday before:'),
        widget=TimePicker(),
    )
    schedule_periodically_saturday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Saturday Schema Hours'),
    )
    schedule_periodically_saturday_between_after = forms.TimeField(
        required=False,
        label=_('Saturday after:'),
        widget=TimePicker(),
    )
    schedule_periodically_saturday_between_before = forms.TimeField(
        required=False,
        label=_('Saturday before:'),
        widget=TimePicker(),
    )
    schedule_periodically_sunday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleHourChoices,
        widget=select_all_widget(),
        label=_('Sunday Schema Hours'),
    )
    schedule_periodically_sunday_between_after = forms.TimeField(
        required=False,
        label=_('Sunday after:'),
        widget=TimePicker(),
    )
    schedule_periodically_sunday_between_before = forms.TimeField(
        required=False,
        label=_('Sunday before:'),
        widget=TimePicker(),
    )
    after_job_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobAfterJobEnabledChoices,
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelMultipleChoiceField(
        queryset=BackupCopyJob.objects.all(),
        required=False,
        label=_('After Job'),
    )
    tag = TagFilterField(BackupCopyJob)
