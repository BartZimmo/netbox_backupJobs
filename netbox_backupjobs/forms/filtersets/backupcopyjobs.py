__all__ = ('BackupCopyJobFilterForm',)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all' button (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})
from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms.fields import DynamicModelMultipleChoiceField, TagFilterField
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import DateTimePicker

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
    BackupCopyJobGFSMonthlyEnabledChoices,
    BackupCopyJobGFSYearlyEnabledChoices,
    BackupCopyJobDataTransferModeChoices,
    BackupCopyJobTransactionLogCopyEnabledChoices,
    BackupCopyJobTransferWindowChoices,
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
            'enable_gfs', 'weekly_enabled', 'monthly_enabled', 'yearly_enabled',
            name=_('GFS Retention'),
        ),
        FieldSet(
            'transfer_window',
            name=_('Schedule Options when Mode is Immediate'),
        ),
        FieldSet(
            'run_automatically', 'schedule_daily_enabled', 'schedule_daily_kind',
            'schedule_monthly_enabled', 'schedule_monthly_day_of_week', 'schedule_monthly_day_number_in_month',
            'schedule_monthly_day_of_month',
            'schedule_periodically_enabled', 'schedule_periodically_unit',
            'after_job_enabled', 'after_job_name',
            name=_('Schedule Options when Mode is Periodic'),
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
        widget=select_all_widget(),
        label='Status',
    )
    mode = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobModeChoices,
        widget=select_all_widget(),
        label=_('Copy Mode'),
    )
    data_transfer_mode = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobDataTransferModeChoices,
        widget=select_all_widget(),
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
        widget=select_all_widget(),
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
        widget=select_all_widget(),
        label=_('Deduplication'),
    )
    storage_encryption_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobStorageEncryptionEnabledChoices,
        widget=select_all_widget(),
        label=_('Storage Encryption'),
    )
    transaction_log_copy_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobTransactionLogCopyEnabledChoices,
        widget=select_all_widget(),
        label=_('Transaction Log Copy'),
    )
    enable_deleted_vm_data_retention = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobEnableDeletedVmDataRetentionChoices,
        widget=select_all_widget(),
        label=_('Deleted VM Retention'),
    )

    # GFS retention settings
    enable_gfs = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSEnableChoices,
        widget=select_all_widget(),
        label=_('GFS Enabled'),
    )
    weekly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSWeeklyEnabledChoices,
        widget=select_all_widget(),
        label=_('GFS Weekly'),
    )
    monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSMonthlyEnabledChoices,
        widget=select_all_widget(),
        label=_('GFS Monthly'),
    )
    yearly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobGFSYearlyEnabledChoices,
        widget=select_all_widget(),
        label=_('GFS Yearly'),
    )

    # Schedule options
    transfer_window = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobTransferWindowChoices,
        widget=select_all_widget(),
        label=_('Transfer Window'),
    )
    run_automatically = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobRunAutomaticallyChoices,
        widget=select_all_widget(),
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleDailyEnabledChoices,
        widget=select_all_widget(),
        label=_('Daily Enabled'),
    )
    schedule_daily_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleDailyKindChoices,
        widget=select_all_widget(),
        label=_('Daily Kind'),
    )
    schedule_monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobScheduleMonthlyEnabledChoices,
        widget=select_all_widget(),
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
        widget=select_all_widget(),
        label=_('Periodically Enabled'),
    )
    schedule_periodically_unit = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobPeriodicallyUnitChoices,
        widget=select_all_widget(),
        label=_('Periodically Unit'),
    )
    after_job_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupCopyJobAfterJobEnabledChoices,
        widget=select_all_widget(),
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelMultipleChoiceField(
        queryset=BackupCopyJob.objects.all(),
        required=False,
        label=_('After Job'),
    )
    tag = TagFilterField(BackupCopyJob)
