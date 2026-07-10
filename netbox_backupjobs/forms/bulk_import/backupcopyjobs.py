from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelImportForm
from utilities.forms.fields import CSVChoiceField, CSVModelChoiceField, CSVModelMultipleChoiceField

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
    BackupCopyJobRunAutomaticallyChoices,
    BackupCopyJobScheduleDailyEnabledChoices,
    BackupCopyJobScheduleDailyKindChoices,
    BackupCopyJobScheduleMonthlyEnabledChoices,
    BackupCopyJobScheduleMonthlyDayOfWeekChoices,
    BackupCopyJobScheduleDayOfMonthChoices,
    BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
    BackupCopyJobPeriodicallyEnabledChoices,
    BackupCopyJobPeriodicallyUnitChoices,
    BackupCopyJobAfterJobEnabledChoices,
)

__all__ = (
    'BackupCopyJobImportForm',
)


class BackupCopyJobImportForm(NetBoxModelImportForm):
    """
    Form for bulk importing BackupCopyJob objects via CSV/JSON/YAML.

    Covers the same practical subset of fields as BackupCopyJobBulkEditForm - the per-day/hour
    schedule arrays (e.g. 'Monday Schema') are not included here; set those afterwards via the
    regular edit page or bulk edit.
    """
    name = forms.CharField(
        label=_('Name'),
        required=True,
        help_text=_('Name of the backup copy job'),
    )
    jobtype = forms.CharField(
        label=_('Job Type'),
        required=False,
    )
    status = CSVChoiceField(
        label=_('Status'),
        choices=BackupCopyJobStatusChoices,
        required=False,
        help_text=_('Defaults to Enabled'),
    )
    mode = CSVChoiceField(
        label=_('Copy Mode'),
        choices=BackupCopyJobModeChoices,
        required=False,
        help_text=_('Defaults to Immediate (mirroring)'),
    )
    data_transfer_mode = CSVChoiceField(
        label=_('Data Transfer Mode'),
        choices=BackupCopyJobDataTransferModeChoices,
        required=False,
        help_text=_('Defaults to Direct'),
    )
    description = forms.CharField(
        label=_('Description'),
        required=False,
    )
    job_creation_time = forms.DateTimeField(
        label=_('Job Creation Time'),
        required=False,
    )
    last_backup_result = CSVChoiceField(
        label=_('Last Backup Result'),
        choices=BackupCopyJobResultChoices,
        required=False,
    )
    retain_days_to_keep = forms.IntegerField(
        label=_('Retain Days to Keep'),
        required=False,
    )
    backup_server_name = forms.CharField(
        label=_('Backup Server Name'),
        required=False,
    )
    backup_server_ip = CSVModelChoiceField(
        label=_('Backup Server IP'),
        queryset=IPAddress.objects.all(),
        to_field_name='address',
        required=False,
        help_text=_('IP address of the backup server, e.g. 192.0.2.1/24'),
    )
    target = forms.CharField(
        label=_('Target'),
        required=False,
    )
    backup_jobs = CSVModelMultipleChoiceField(
        label=_('Backup Jobs'),
        queryset=BackupJob.objects.all(),
        to_field_name='name',
        required=False,
        help_text=_('Backup job names separated by commas, encased with double quotes (e.g. "job1,job2")'),
    )

    # Advanced settings
    enable_deduplication = CSVChoiceField(
        label=_('Enable Deduplication'),
        choices=BackupCopyJobEnableDeduplicationChoices,
        required=False,
    )
    storage_encryption_enabled = CSVChoiceField(
        label=_('Enable Storage Encryption'),
        choices=BackupCopyJobStorageEncryptionEnabledChoices,
        required=False,
    )
    transaction_log_copy_enabled = CSVChoiceField(
        label=_('Enable Transaction Log Copy'),
        choices=BackupCopyJobTransactionLogCopyEnabledChoices,
        required=False,
    )
    enable_deleted_vm_data_retention = CSVChoiceField(
        label=_('Enable Deleted VM Data Retention'),
        choices=BackupCopyJobEnableDeletedVmDataRetentionChoices,
        required=False,
    )
    retain_days_to_keep_deleted_vm_data = forms.IntegerField(
        label=_('Retain Days to Keep Deleted VM Data'),
        required=False,
    )

    # GFS retention settings
    enable_gfs = CSVChoiceField(
        label=_('Enable GFS'),
        choices=BackupCopyJobGFSEnableChoices,
        required=False,
    )
    weekly_enabled = CSVChoiceField(
        label=_('Weekly Enabled'),
        choices=BackupCopyJobGFSWeeklyEnabledChoices,
        required=False,
    )
    weekly_keep_backups_for = forms.IntegerField(
        label=_('Weekly Keep (weeks)'),
        required=False,
    )
    weekly_keep_backups_on_day_of_week = CSVChoiceField(
        label=_('Weekly Day'),
        choices=BackupCopyJobGFSWeeklyDayChoices,
        required=False,
    )
    monthly_enabled = CSVChoiceField(
        label=_('Monthly Enabled'),
        choices=BackupCopyJobGFSMonthlyEnabledChoices,
        required=False,
    )
    monthly_keep_backups_for = forms.IntegerField(
        label=_('Monthly Keep (months)'),
        required=False,
    )
    monthly_keep_backups_week_of_month = CSVChoiceField(
        label=_('Monthly Week'),
        choices=BackupCopyJobGFSWeekOfMonthChoices,
        required=False,
    )
    yearly_enabled = CSVChoiceField(
        label=_('Yearly Enabled'),
        choices=BackupCopyJobGFSYearlyEnabledChoices,
        required=False,
    )
    yearly_keep_backups_for = forms.IntegerField(
        label=_('Yearly Keep (years)'),
        required=False,
    )
    yearly_keep_backups_on_month_of_year = CSVChoiceField(
        label=_('Yearly Month'),
        choices=BackupCopyJobGFSMonthOfYearChoices,
        required=False,
    )

    # Schedule options when mode is immediate
    transfer_window = CSVChoiceField(
        label=_('Transfer Window'),
        choices=BackupCopyJobTransferWindowChoices,
        required=False,
        help_text=_('Defaults to Continuously'),
    )

    # Schedule options when mode is periodic
    run_automatically = CSVChoiceField(
        label=_('Run Automatically'),
        choices=BackupCopyJobRunAutomaticallyChoices,
        required=False,
    )
    schedule_daily_enabled = CSVChoiceField(
        label=_('Daily Enabled'),
        choices=BackupCopyJobScheduleDailyEnabledChoices,
        required=False,
    )
    schedule_daily_time = forms.TimeField(
        label=_('Daily Time'),
        required=False,
    )
    schedule_daily_kind = CSVChoiceField(
        label=_('Daily Kind'),
        choices=BackupCopyJobScheduleDailyKindChoices,
        required=False,
    )
    schedule_monthly_enabled = CSVChoiceField(
        label=_('Monthly Enabled'),
        choices=BackupCopyJobScheduleMonthlyEnabledChoices,
        required=False,
    )
    schedule_monthly_time = forms.TimeField(
        label=_('Monthly Time'),
        required=False,
    )
    schedule_monthly_day_of_week = CSVChoiceField(
        label=_('Monthly Day of Week'),
        choices=BackupCopyJobScheduleMonthlyDayOfWeekChoices,
        required=False,
    )
    schedule_monthly_day_number_in_month = CSVChoiceField(
        label=_('Monthly Day number of Month'),
        choices=BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
        required=False,
    )
    schedule_monthly_day_of_month = CSVChoiceField(
        label=_('Monthly Day of Month'),
        choices=BackupCopyJobScheduleDayOfMonthChoices,
        required=False,
    )
    schedule_periodically_enabled = CSVChoiceField(
        label=_('Periodically Enabled'),
        choices=BackupCopyJobPeriodicallyEnabledChoices,
        required=False,
    )
    schedule_periodically_every = forms.IntegerField(
        label=_('Periodically Every'),
        required=False,
    )
    schedule_periodically_unit = CSVChoiceField(
        label=_('Periodically Unit'),
        choices=BackupCopyJobPeriodicallyUnitChoices,
        required=False,
    )
    schedule_periodically_hour_offset_in_min = forms.IntegerField(
        label=_('Hour Offset (min)'),
        required=False,
    )
    after_job_enabled = CSVChoiceField(
        label=_('After Job Enabled'),
        choices=BackupCopyJobAfterJobEnabledChoices,
        required=False,
    )
    after_job_name = CSVModelChoiceField(
        label=_('After Job'),
        queryset=BackupCopyJob.objects.all(),
        to_field_name='name',
        required=False,
    )

    class Meta:
        model = BackupCopyJob
        fields = [
            'name', 'jobtype', 'status', 'mode', 'data_transfer_mode', 'description',
            'job_creation_time', 'last_backup_result',
            'retain_days_to_keep', 'backup_server_name', 'backup_server_ip', 'target', 'backup_jobs',
            'enable_deduplication', 'storage_encryption_enabled', 'transaction_log_copy_enabled',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            'transfer_window',
            'run_automatically',
            'schedule_daily_enabled', 'schedule_daily_time', 'schedule_daily_kind',
            'schedule_monthly_enabled', 'schedule_monthly_time', 'schedule_monthly_day_of_week',
            'schedule_monthly_day_number_in_month', 'schedule_monthly_day_of_month',
            'schedule_periodically_enabled', 'schedule_periodically_every', 'schedule_periodically_unit',
            'schedule_periodically_hour_offset_in_min',
            'after_job_enabled', 'after_job_name',
            'tags',
        ]
