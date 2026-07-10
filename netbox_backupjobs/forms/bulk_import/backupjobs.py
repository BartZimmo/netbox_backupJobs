from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelImportForm
from utilities.forms.fields import CSVChoiceField, CSVModelChoiceField, CSVModelMultipleChoiceField

from ipam.models import IPAddress
from virtualization.models import VirtualMachine

from netbox_backupjobs.models import BackupJob
from netbox_backupjobs.choices import (
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
    BackupJobEnableFullBackupChoices,
    BackupJobFullBackupScheduleKindChoices,
    BackupJobFullBackupWeekChoices,
    BackupJobFullBackupDaysChoices,
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
    BackupJobScheduleMonthlyEnabledChoices,
    BackupJobScheduleMonthlyDayOfWeekChoices,
    BackupJobScheduleDayOfMonthChoices,
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
)

__all__ = (
    'BackupJobImportForm',
)


class BackupJobImportForm(NetBoxModelImportForm):
    """
    Form for bulk importing BackupJob objects via CSV/JSON/YAML.

    Covers the same practical subset of fields as BackupJobBulkEditForm - the per-day/hour
    schedule arrays (e.g. 'Monday Schema') are not included here; set those afterwards via the
    regular edit page or bulk edit.
    """
    name = forms.CharField(
        label=_('Name'),
        required=True,
        help_text=_('Name of the backup job'),
    )
    jobtype = forms.CharField(
        label=_('Job Type'),
        required=False,
    )
    platform = CSVChoiceField(
        label=_('Platform'),
        choices=BackupJobPlatformChoices,
        required=False,
    )
    status = CSVChoiceField(
        label=_('Status'),
        choices=BackupJobStatusChoices,
        required=False,
        help_text=_('Defaults to Enabled'),
    )
    description = forms.CharField(
        label=_('Description'),
        required=False,
    )
    job_creation_time = forms.DateTimeField(
        label=_('Job Creation Time'),
        required=False,
    )
    last_backup_end_time = forms.DateTimeField(
        label=_('Last Backup End Time'),
        required=False,
    )
    last_backup_result = CSVChoiceField(
        label=_('Last Backup Result'),
        choices=BackupJobResultChoices,
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
    virtual_machines = CSVModelMultipleChoiceField(
        label=_('Virtual Machines'),
        queryset=VirtualMachine.objects.all(),
        to_field_name='name',
        required=False,
        help_text=_('Virtual machine names separated by commas, encased with double quotes (e.g. "vm1,vm2")'),
    )

    # Advanced job settings
    algorithm = CSVChoiceField(
        label=_('Algorithm'),
        choices=BackupJobAlgorithmChoices,
        required=False,
        help_text=_('Defaults to Incremental'),
    )
    enable_deduplication = CSVChoiceField(
        label=_('Enable Deduplication'),
        choices=BackupJobEnableDeduplicationChoices,
        required=False,
    )
    storage_encryption_enabled = CSVChoiceField(
        label=_('Enable Storage Encryption'),
        choices=BackupJobStorageEncryptionEnabledChoices,
        required=False,
    )
    retain_days_to_keep = forms.IntegerField(
        label=_('Retain Days to Keep'),
        required=False,
    )
    retain_cycles = forms.IntegerField(
        label=_('Retain Cycles'),
        required=False,
    )
    enable_deleted_vm_data_retention = CSVChoiceField(
        label=_('Enable Deleted VM Data Retention'),
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        required=False,
    )
    retain_days_to_keep_deleted_vm_data = forms.IntegerField(
        label=_('Retain Days to Keep Deleted VM Data'),
        required=False,
    )

    # Synthetic full backup settings
    transform_full_to_synthetic = CSVChoiceField(
        label=_('Transform Incremental to Synthetic Full'),
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        required=False,
    )
    transform_to_synthetic_full = CSVChoiceField(
        label=_('Transform Reverse Incremental to Synthetic Full'),
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        required=False,
    )
    transform_to_synthetic_kind = CSVChoiceField(
        label=_('Synthetic Full Kind'),
        choices=BackupJobSyntheticFullChoices,
        required=False,
    )
    synthetic_full_day_number_in_month = CSVChoiceField(
        label=_('Synthetic Full Week of Month'),
        choices=BackupJobSyntheticFullWeekChoices,
        required=False,
    )
    synthetic_full_day_of_week = CSVChoiceField(
        label=_('Synthetic Full Day of Week (Monthly)'),
        choices=BackupJobSyntheticFullDaysChoices,
        required=False,
    )

    # Active full backup settings
    enable_full_backup = CSVChoiceField(
        label=_('Enable Active Full Backup'),
        choices=BackupJobEnableFullBackupChoices,
        required=False,
    )
    full_backup_schedule_kind = CSVChoiceField(
        label=_('Schedule Kind'),
        choices=BackupJobFullBackupScheduleKindChoices,
        required=False,
    )
    full_backup_day_number_in_month = CSVChoiceField(
        label=_('Week of Month'),
        choices=BackupJobFullBackupWeekChoices,
        required=False,
    )
    full_backup_day_of_week = CSVChoiceField(
        label=_('Day of Week (Monthly)'),
        choices=BackupJobFullBackupDaysChoices,
        required=False,
    )

    # GFS retention settings
    enable_gfs = CSVChoiceField(
        label=_('Enable GFS'),
        choices=BackupJobGFSEnableChoices,
        required=False,
    )
    weekly_enabled = CSVChoiceField(
        label=_('Weekly Enabled'),
        choices=BackupJobGFSWeeklyEnabledChoices,
        required=False,
    )
    weekly_keep_backups_for = forms.IntegerField(
        label=_('Weekly Keep (weeks)'),
        required=False,
    )
    weekly_keep_backups_on_day_of_week = CSVChoiceField(
        label=_('Weekly Day'),
        choices=BackupJobGFSWeeklyDayChoices,
        required=False,
    )
    monthly_enabled = CSVChoiceField(
        label=_('Monthly Enabled'),
        choices=BackupJobGFSMonthlyEnabledChoices,
        required=False,
    )
    monthly_keep_backups_for = forms.IntegerField(
        label=_('Monthly Keep (months)'),
        required=False,
    )
    monthly_keep_backups_week_of_month = CSVChoiceField(
        label=_('Monthly Week'),
        choices=BackupJobGFSWeekOfMonthChoices,
        required=False,
    )
    yearly_enabled = CSVChoiceField(
        label=_('Yearly Enabled'),
        choices=BackupJobGFSYearlyEnabledChoices,
        required=False,
    )
    yearly_keep_backups_for = forms.IntegerField(
        label=_('Yearly Keep (years)'),
        required=False,
    )
    yearly_keep_backups_on_month_of_year = CSVChoiceField(
        label=_('Yearly Month'),
        choices=BackupJobGFSMonthOfYearChoices,
        required=False,
    )

    # Schedule options
    run_automatically = CSVChoiceField(
        label=_('Run Automatically'),
        choices=BackupJobRunAutomaticallyChoices,
        required=False,
    )
    schedule_daily_enabled = CSVChoiceField(
        label=_('Daily Enabled'),
        choices=BackupJobScheduleDailyEnabledChoices,
        required=False,
    )
    schedule_daily_time = forms.TimeField(
        label=_('Daily Time'),
        required=False,
    )
    schedule_daily_kind = CSVChoiceField(
        label=_('Daily Kind'),
        choices=BackupJobScheduleDailyKindChoices,
        required=False,
    )
    schedule_monthly_enabled = CSVChoiceField(
        label=_('Monthly Enabled'),
        choices=BackupJobScheduleMonthlyEnabledChoices,
        required=False,
    )
    schedule_monthly_time = forms.TimeField(
        label=_('Monthly Time'),
        required=False,
    )
    schedule_monthly_day_of_week = CSVChoiceField(
        label=_('Monthly Day of Week'),
        choices=BackupJobScheduleMonthlyDayOfWeekChoices,
        required=False,
    )
    schedule_monthly_day_number_in_month = CSVChoiceField(
        label=_('Monthly Day number of Month'),
        choices=BackupJobScheduleMonthlyDayNumberInMonthChoices,
        required=False,
    )
    schedule_monthly_day_of_month = CSVChoiceField(
        label=_('Monthly Day of Month'),
        choices=BackupJobScheduleDayOfMonthChoices,
        required=False,
    )
    schedule_periodically_enabled = CSVChoiceField(
        label=_('Periodically Enabled'),
        choices=BackupJobPeriodicallyEnabledChoices,
        required=False,
    )
    schedule_periodically_every = forms.IntegerField(
        label=_('Periodically Every'),
        required=False,
    )
    schedule_periodically_unit = CSVChoiceField(
        label=_('Periodically Unit'),
        choices=BackupJobPeriodicallyUnitChoices,
        required=False,
    )
    schedule_periodically_hour_offset_in_min = forms.IntegerField(
        label=_('Hour Offset (min)'),
        required=False,
    )
    after_job_enabled = CSVChoiceField(
        label=_('After Job Enabled'),
        choices=BackupJobAfterJobEnabledChoices,
        required=False,
    )
    after_job_name = CSVModelChoiceField(
        label=_('After Job'),
        queryset=BackupJob.objects.all(),
        to_field_name='name',
        required=False,
    )
    comments = forms.CharField(
        label=_('Comments'),
        required=False,
    )

    class Meta:
        model = BackupJob
        fields = [
            'name', 'jobtype', 'platform', 'status', 'description',
            'job_creation_time', 'last_backup_end_time', 'last_backup_result',
            'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines',
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled',
            'retain_days_to_keep', 'retain_cycles',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            'transform_full_to_synthetic', 'transform_to_synthetic_full', 'transform_to_synthetic_kind',
            'synthetic_full_day_number_in_month', 'synthetic_full_day_of_week',
            'enable_full_backup', 'full_backup_schedule_kind',
            'full_backup_day_number_in_month', 'full_backup_day_of_week',
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            'run_automatically',
            'schedule_daily_enabled', 'schedule_daily_time', 'schedule_daily_kind',
            'schedule_monthly_enabled', 'schedule_monthly_time', 'schedule_monthly_day_of_week',
            'schedule_monthly_day_number_in_month', 'schedule_monthly_day_of_month',
            'schedule_periodically_enabled', 'schedule_periodically_every', 'schedule_periodically_unit',
            'schedule_periodically_hour_offset_in_min',
            'after_job_enabled', 'after_job_name',
            'comments', 'tags',
        ]
