from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelBulkEditForm
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet, TabbedGroups
from utilities.forms.utils import add_blank_choice
from utilities.forms.widgets import DateTimePicker, TimePicker

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
    BackupJobSyntheticFullMonthChoices,
    BackupJobEnableFullBackupChoices,
    BackupJobFullBackupScheduleKindChoices,
    BackupJobFullBackupWeekChoices,
    BackupJobFullBackupDaysChoices,
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
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
    BackupJobScheduleHourChoices,
)

__all__ = (
    'BackupJobBulkEditForm',
)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all'/'Clear' button pair (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})


class BackupJobBulkEditForm(NetBoxModelBulkEditForm):
    """
    Form for bulk editing BackupJob objects.
    """
    jobtype = forms.CharField(
        required=False,
        label=_('Job Type'),
    )
    platform = forms.ChoiceField(
        choices=add_blank_choice(BackupJobPlatformChoices),
        required=False,
        label=_('Platform'),
    )
    status = forms.ChoiceField(
        choices=add_blank_choice(BackupJobStatusChoices),
        required=False,
        label=_('Status'),
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
    add_virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label=_('Add Virtual Machines'),
    )
    remove_virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label=_('Remove Virtual Machines'),
    )

    # Advanced job settings
    algorithm = forms.ChoiceField(
        choices=add_blank_choice(BackupJobAlgorithmChoices),
        required=False,
        label=_('Algorithm'),
    )
    enable_deduplication = forms.ChoiceField(
        choices=add_blank_choice(BackupJobEnableDeduplicationChoices),
        required=False,
        label=_('Enable Deduplication'),
    )
    storage_encryption_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupJobStorageEncryptionEnabledChoices),
        required=False,
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
        choices=add_blank_choice(BackupJobEnableDeletedVmDataRetentionChoices),
        required=False,
        label=_('Enable Deleted VM Data Retention'),
    )
    retain_days_to_keep_deleted_vm_data = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep Deleted VM Data'),
    )

    # Synthetic full backup settings
    transform_full_to_synthetic = forms.ChoiceField(
        choices=add_blank_choice(BackupJobEnableSyntheticFullForIncrementalChoices),
        required=False,
        label=_('Transform Incremental to Synthetic Full'),
    )
    transform_to_synthetic_full = forms.ChoiceField(
        choices=add_blank_choice(BackupJobEnableSyntheticFullForReverseIncrementalChoices),
        required=False,
        label=_('Transform Reverse Incremental to Synthetic Full'),
    )
    transform_to_synthetic_kind = forms.ChoiceField(
        choices=add_blank_choice(BackupJobSyntheticFullChoices),
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
        choices=add_blank_choice(BackupJobSyntheticFullWeekChoices),
        required=False,
        label=_('Synthetic Full Week of Month'),
    )
    synthetic_full_day_of_week = forms.ChoiceField(
        choices=add_blank_choice(BackupJobSyntheticFullDaysChoices),
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
        choices=add_blank_choice(BackupJobEnableFullBackupChoices),
        required=False,
        label=_('Enable Active Full Backup'),
    )
    full_backup_schedule_kind = forms.ChoiceField(
        choices=add_blank_choice(BackupJobFullBackupScheduleKindChoices),
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
        choices=add_blank_choice(BackupJobFullBackupWeekChoices),
        required=False,
        label=_('Week of Month'),
    )
    full_backup_day_of_week = forms.ChoiceField(
        choices=add_blank_choice(BackupJobFullBackupDaysChoices),
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
        choices=add_blank_choice(BackupJobGFSEnableChoices),
        required=False,
        label=_('Enable GFS'),
    )
    weekly_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupJobGFSWeeklyEnabledChoices),
        required=False,
        label=_('Weekly Enabled'),
    )
    weekly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Weekly Keep (weeks)'),
    )
    weekly_keep_backups_on_day_of_week = forms.ChoiceField(
        choices=add_blank_choice(BackupJobGFSWeeklyDayChoices),
        required=False,
        label=_('Weekly Day'),
    )
    monthly_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupJobGFSMonthlyEnabledChoices),
        required=False,
        label=_('Monthly Enabled'),
    )
    monthly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Monthly Keep (months)'),
    )
    monthly_keep_backups_week_of_month = forms.ChoiceField(
        choices=add_blank_choice(BackupJobGFSWeekOfMonthChoices),
        required=False,
        label=_('Monthly Week'),
    )
    yearly_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupJobGFSYearlyEnabledChoices),
        required=False,
        label=_('Yearly Enabled'),
    )
    yearly_keep_backups_for = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Yearly Keep (years)'),
    )
    yearly_keep_backups_on_month_of_year = forms.ChoiceField(
        choices=add_blank_choice(BackupJobGFSMonthOfYearChoices),
        required=False,
        label=_('Yearly Month'),
    )

    # Schedule options
    run_automatically = forms.ChoiceField(
        choices=add_blank_choice(BackupJobRunAutomaticallyChoices),
        required=False,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupJobScheduleDailyEnabledChoices),
        required=False,
        label=_('Daily Enabled'),
    )
    schedule_daily_time = forms.TimeField(
        required=False,
        label=_('Daily Time'),
        widget=TimePicker(),
    )
    schedule_daily_kind = forms.ChoiceField(
        choices=add_blank_choice(BackupJobScheduleDailyKindChoices),
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
        choices=add_blank_choice(BackupJobScheduleMonthlyEnabledChoices),
        required=False,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_time = forms.TimeField(
        required=False,
        label=_('Monthly Time'),
        widget=TimePicker(),
    )
    schedule_monthly_day_of_week = forms.ChoiceField(
        choices=add_blank_choice(BackupJobScheduleMonthlyDayOfWeekChoices),
        required=False,
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = forms.ChoiceField(
        choices=add_blank_choice(BackupJobScheduleMonthlyDayNumberInMonthChoices),
        required=False,
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = forms.ChoiceField(
        choices=add_blank_choice(BackupJobScheduleDayOfMonthChoices),
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
        choices=add_blank_choice(BackupJobPeriodicallyEnabledChoices),
        required=False,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_every = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Periodically Every'),
    )
    schedule_periodically_unit = forms.ChoiceField(
        choices=add_blank_choice(BackupJobPeriodicallyUnitChoices),
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
    after_job_enabled = forms.ChoiceField(
        choices=add_blank_choice(BackupJobAfterJobEnabledChoices),
        required=False,
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('After Job'),
    )
    comments = CommentField()

    model = BackupJob
    fieldsets = (
        FieldSet(
            'jobtype', 'platform', 'status', 'description',
            'job_creation_time', 'last_backup_end_time', 'last_backup_result',
            'backup_server_name', 'backup_server_ip', 'target',
            name=_('Backup Job'),
        ),
        FieldSet(
            TabbedGroups(
                FieldSet('add_virtual_machines', name=_('Add')),
                FieldSet('remove_virtual_machines', name=_('Remove')),
            ),
            name=_('Virtual Machines'),
        ),
        FieldSet(
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled',
            'retain_days_to_keep', 'retain_cycles',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'transform_full_to_synthetic', 'transform_to_synthetic_full', 'transform_to_synthetic_kind',
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
    )
    nullable_fields = [
        'description', 'job_creation_time', 'last_backup_end_time',
        'backup_server_name', 'backup_server_ip', 'target',
        'retain_days_to_keep', 'retain_cycles', 'retain_days_to_keep_deleted_vm_data',
        'weekly_keep_backups_for', 'monthly_keep_backups_for', 'yearly_keep_backups_for',
        'schedule_daily_time', 'schedule_monthly_time',
        'schedule_periodically_every', 'schedule_periodically_hour_offset_in_min',
        'after_job_name', 'comments',
    ]
