__all__ = ('BackupJobFilterForm',)


def select_all_widget():
    """A SelectMultiple widget with a 'Select all' button (see selectall.js)."""
    return forms.SelectMultiple(attrs={'class': 'netbox-backupjobs-select-all'})
from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelFilterSetForm
from utilities.forms import BOOLEAN_WITH_BLANK_CHOICES
from utilities.forms.fields import TagFilterField, DynamicModelMultipleChoiceField
from utilities.forms.rendering import FieldSet
from utilities.forms.widgets import DateTimePicker

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
    BackupJobEnableFullBackupChoices,
    BackupJobFullBackupScheduleKindChoices,
    BackupJobGFSEnableChoices,
    BackupJobGFSWeeklyEnabledChoices,
    BackupJobGFSMonthlyEnabledChoices,
    BackupJobGFSYearlyEnabledChoices,
    BackupJobRunAutomaticallyChoices,
    BackupJobScheduleDailyEnabledChoices,
    BackupJobScheduleDailyKindChoices,
    BackupJobScheduleMonthlyEnabledChoices,
    BackupJobScheduleMonthlyDayOfWeekChoices,
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
            'q', 'name','description', 'status', 'jobtype', 'platform', 'job_creation_time_after', 'job_creation_time_before',
            'last_backup_end_time_after', 'last_backup_end_time_before', 'last_backup_result',
            'backup_server_name', 'backup_server_ip', 'target',
            'has_virtual_machines', 'has_powered_off_vms', 'virtual_machine', name=_('Backup Job'),
        ),
        FieldSet(
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled', 'enable_deleted_vm_data_retention',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'transform_full_to_synthetic', 'transform_to_synthetic_full', 'transform_to_synthetic_kind',
            name=_('Synthetic Full Backup'),
        ),
        FieldSet(
            'enable_full_backup', 'full_backup_schedule_kind',
            name=_('Active Full Backup'),
        ),
        FieldSet(
            'enable_gfs', 'weekly_enabled', 'monthly_enabled', 'yearly_enabled',
            name=_('GFS Retention'),
        ),
        FieldSet(
            'run_automatically', 'schedule_daily_enabled', 'schedule_daily_kind',
            'schedule_monthly_enabled', 'schedule_monthly_day_of_week', 'schedule_monthly_day_number_in_month',
            'schedule_monthly_day_of_month',
            'schedule_periodically_enabled', 'schedule_periodically_unit',
            'after_job_enabled', 'after_job_name',
            name=_('Schedule Options'),
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
        widget=select_all_widget(),
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
        widget=select_all_widget(),
        label=_('Platform'),
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
    last_backup_end_time_after = forms.DateTimeField(
        required=False,
        label=_('Last Backup End Time After'),
        widget=DateTimePicker(),
    )
    last_backup_end_time_before = forms.DateTimeField(
        required=False,
        label=_('Last Backup End Time Before'),
        widget=DateTimePicker(),
    )
    last_backup_result = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobResultChoices,
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
        widget=select_all_widget(),
        label=_('Algorithm'),
    )
    enable_deduplication = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableDeduplicationChoices,
        widget=select_all_widget(),
        label=_('Deduplication'),
    )
    storage_encryption_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobStorageEncryptionEnabledChoices,
        widget=select_all_widget(),
        label=_('Storage Encryption'),
    )
    enable_deleted_vm_data_retention = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        widget=select_all_widget(),
        label=_('Deleted VM Retention'),
    )

    # Synthetic full backup settings
    transform_full_to_synthetic = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        widget=select_all_widget(),
        label=_('Synthetic Full (Incremental)'),
    )
    transform_to_synthetic_full = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        widget=select_all_widget(),
        label=_('Synthetic Full (Reverse Incr.)'),
    )
    transform_to_synthetic_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobSyntheticFullChoices,
        widget=select_all_widget(),
        label=_('Synthetic Full Kind'),
    )

    # Active full backup settings
    enable_full_backup = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableFullBackupChoices,
        widget=select_all_widget(),
        label=_('Active Full Backup'),
    )
    full_backup_schedule_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobFullBackupScheduleKindChoices,
        widget=select_all_widget(),
        label=_('Full Backup Kind'),
    )

    # GFS retention settings
    enable_gfs = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSEnableChoices,
        widget=select_all_widget(),
        label=_('GFS Enabled'),
    )
    weekly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSWeeklyEnabledChoices,
        widget=select_all_widget(),
        label=_('GFS Weekly'),
    )
    monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSMonthlyEnabledChoices,
        widget=select_all_widget(),
        label=_('GFS Monthly'),
    )
    yearly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSYearlyEnabledChoices,
        widget=select_all_widget(),
        label=_('GFS Yearly'),
    )

    # Schedule options
    run_automatically = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobRunAutomaticallyChoices,
        widget=select_all_widget(),
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDailyEnabledChoices,
        widget=select_all_widget(),
        label=_('Daily Enabled'),
    )
    schedule_daily_kind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDailyKindChoices,
        widget=select_all_widget(),
        label=_('Daily Kind'),
    )
    schedule_monthly_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthlyEnabledChoices,
        widget=select_all_widget(),
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
    schedule_periodically_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobPeriodicallyEnabledChoices,
        widget=select_all_widget(),
        label=_('Periodically Enabled'),
    )
    schedule_periodically_unit = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobPeriodicallyUnitChoices,
        widget=select_all_widget(),
        label=_('Periodically Unit'),
    )

    # After job
    after_job_enabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobAfterJobEnabledChoices,
        widget=select_all_widget(),
        label=_('After Job Enabled'),
    )
    after_job_name = DynamicModelMultipleChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('After Job'),
    )