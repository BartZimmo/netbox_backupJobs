__all__ = ('BackupJobFilterForm',)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all' button (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})
from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms import BOOLEAN_WITH_BLANK_CHOICES
from utilities.forms.fields import TagFilterField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet, InlineFields
from utilities.forms.widgets import DateTimePicker, TimePicker

from ipam.models import IPAddress

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
    BackupJobScheduleMonthChoices,
    BackupJobScheduleHourChoices,
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
    BackupJobScheduleDayOfMonthChoices,
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
)

from virtualization.models import VirtualMachine

class BackupJobFilterForm(NetBoxModelFilterSetForm):
    model = BackupJob
    fieldsets = (
        FieldSet(
            'q', 'name','description', 'status', 'jobtype', 'platform',
            InlineFields('job_creation_time_after', 'job_creation_time_before', label=_('Job Creation Time')),
            InlineFields('last_backup_end_time_after', 'last_backup_end_time_before', label=_('Last Backup End Time')),
            'last_backup_result',
            'backup_server_name', 'backup_server_ip', 'target',
            'has_virtual_machines', 'has_powered_off_vms', 'virtual_machine', name=_('Backup Job'),
        ),
        FieldSet(
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled', 'enable_deleted_vm_data_retention',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'run_automatically',
            name=_('Schedule Options: Run Automatically'),
        ),
        FieldSet(
            'schedule_daily_enabled', 'schedule_daily_kind', 'schedule_daily_days',
            name=_('Schedule Options: Daily'),
        ),
        FieldSet(
            'schedule_monthly_enabled', 'schedule_monthly_day_of_week', 'schedule_monthly_day_number_in_month',
            'schedule_monthly_day_of_month', 'schedule_monthly_months',
            name=_('Schedule Options: Monthly'),
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
            name=_('Schedule Options: Periodically'),
        ),
        FieldSet(
            'after_job_enabled', 'after_job_name',
            name=_('Schedule Options: After Job'),
        ),
        FieldSet(
            'transform_full_to_synthetic', 'transform_to_synthetic_full', 'transform_to_synthetic_kind',
            'transform_to_synthetic_days', 'synthetic_full_day_number_in_month', 'synthetic_full_day_of_week',
            'transform_to_synthetic_monthly',
            name=_('Synthetic Full Backup'),
        ),
        FieldSet(
            'enable_full_backup', 'full_backup_schedule_kind',
            'full_backup_days', 'full_backup_day_number_in_month', 'full_backup_day_of_week', 'full_backup_months',
            name=_('Active Full Backup'),
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
        choices=BackupJobStatusChoices,
        label='Status',
    )
    target = forms.CharField(
        required=False,
        label=_('Target'),
    )
    jobtype = forms.CharField(
        required=False,
        label=_('Job Type'),
    )
    platform = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobPlatformChoices,
        label=_('Platform'),
    )
    job_creation_time_after = forms.DateTimeField(
        required=False,
        label=_('Job Created after:'),
        widget=DateTimePicker(),
    )
    job_creation_time_before = forms.DateTimeField(
        required=False,
        label=_('Job Created before:'),
        widget=DateTimePicker(),
    )
    last_backup_end_time_after = forms.DateTimeField(
        required=False,
        label=_('Last Backup Ended after:'),
        widget=DateTimePicker(),
    )
    last_backup_end_time_before = forms.DateTimeField(
        required=False,
        label=_('Last Backup Ended before:'),
        widget=DateTimePicker(),
    )
    last_backup_result = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobResultChoices,
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
    virtual_machine = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        label="Virtual Machines Included",
        required=False,
    )
    has_virtual_machines = forms.NullBooleanField(
        required=False,
        label=_('Has Virtual Machines'),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    has_powered_off_vms = forms.NullBooleanField(
        required=False,
        label=_('Has Powered Off Virtual Machines'),
        widget=forms.Select(choices=BOOLEAN_WITH_BLANK_CHOICES),
    )
    tag = TagFilterField(BackupJob)

    # Advanced settings
    algorithm = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobAlgorithmChoices,
        label=_('Algorithm'),
    )
    enable_deduplication = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableDeduplicationChoices,
        label=_('Deduplication'),
    )
    storage_encryption_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobStorageEncryptionEnabledChoices,
        label=_('Storage Encryption'),
    )
    enable_deleted_vm_data_retention = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        label=_('Deleted VM Retention'),
    )

    # Synthetic full backup settings
    transform_full_to_synthetic = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        label=_('Synthetic Full (Incremental)'),
    )
    transform_to_synthetic_full = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        label=_('Synthetic Full (Reverse Incr.)'),
    )
    transform_to_synthetic_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobSyntheticFullChoices,
        label=_('Synthetic Full Kind'),
    )
    transform_to_synthetic_days = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobSyntheticFullDaysChoices,
        widget=select_all_widget(),
        label=_('Synthetic Full Days of Week'),
    )
    synthetic_full_day_number_in_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobSyntheticFullWeekChoices,
        widget=select_all_widget(),
        label=_('Synthetic Full Week of Month'),
    )
    synthetic_full_day_of_week = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobSyntheticFullDaysChoices,
        widget=select_all_widget(),
        label=_('Synthetic Full Day of Week (Monthly)'),
    )
    transform_to_synthetic_monthly = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobSyntheticFullMonthChoices,
        widget=select_all_widget(),
        label=_('Synthetic Full Months'),
    )

    # Active full backup settings
    enable_full_backup = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableFullBackupChoices,
        label=_('Active Full Backup'),
    )
    full_backup_schedule_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobFullBackupScheduleKindChoices,
        label=_('Full Backup Kind'),
    )
    full_backup_days = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobFullBackupDaysChoices,
        widget=select_all_widget(),
        label=_('Full Backup Days'),
    )
    full_backup_day_number_in_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobFullBackupWeekChoices,
        widget=select_all_widget(),
        label=_('Full Backup Week of Month'),
    )
    full_backup_day_of_week = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobFullBackupDaysChoices,
        widget=select_all_widget(),
        label=_('Full Backup Day of Week (Monthly)'),
    )
    full_backup_months = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobFullBackupMonthChoices,
        widget=select_all_widget(),
        label=_('Full Backup Months'),
    )

    # GFS retention settings
    enable_gfs = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSEnableChoices,
        label=_('GFS Enabled'),
    )
    weekly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSWeeklyEnabledChoices,
        label=_('GFS Weekly'),
    )
    monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSMonthlyEnabledChoices,
        label=_('GFS Monthly'),
    )
    yearly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSYearlyEnabledChoices,
        label=_('GFS Yearly'),
    )
    weekly_keep_backups_on_day_of_week = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSWeeklyDayChoices,
        widget=select_all_widget(),
        label=_('GFS Weekly Day'),
    )
    monthly_keep_backups_week_of_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSWeekOfMonthChoices,
        widget=select_all_widget(),
        label=_('GFS Monthly Week'),
    )
    yearly_keep_backups_on_month_of_year = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSMonthOfYearChoices,
        widget=select_all_widget(),
        label=_('GFS Yearly Month'),
    )

    # Schedule options
    run_automatically = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobRunAutomaticallyChoices,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDailyEnabledChoices,
        label=_('Daily Enabled'),
    )
    schedule_daily_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDailyKindChoices,
        label=_('Daily Kind'),
    )
    schedule_daily_days = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDaysChoices,
        widget=select_all_widget(),
        label=_('Daily Days'),
    )
    schedule_monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthlyEnabledChoices,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_day_of_week = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthlyDayOfWeekChoices,
        widget=select_all_widget(),
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthlyDayNumberInMonthChoices,
        widget=select_all_widget(),
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDayOfMonthChoices,
        widget=select_all_widget(),
        label=_('Monthly Day of Month'),
    )
    schedule_monthly_months = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthChoices,
        widget=select_all_widget(),
        label=_('Monthly Months'),
    )
    schedule_periodically_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobPeriodicallyEnabledChoices,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_unit = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobPeriodicallyUnitChoices,
        label=_('Periodically Unit'),
    )
    schedule_periodically_monday_schema = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleHourChoices,
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
        choices=BackupJobScheduleHourChoices,
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
        choices=BackupJobScheduleHourChoices,
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
        choices=BackupJobScheduleHourChoices,
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
        choices=BackupJobScheduleHourChoices,
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
        choices=BackupJobScheduleHourChoices,
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
        choices=BackupJobScheduleHourChoices,
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

    # After job
    after_job_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobAfterJobEnabledChoices,
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelMultipleChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('After Job'),
    )