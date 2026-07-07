__all__ = ('BackupJobFilterForm',)

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
            'LastBackupEndTime_after', 'LastBackupEndTime_before', 'LastBackupResult',
            'backup_server_name', 'backup_server_ip', 'target',
            'has_virtual_machines', 'has_powered_off_vms', 'virtual_machine', name=_('Backup Job'),
        ),
        FieldSet(
            'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled', 'EnableDeletedVmDataRetention',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'TransformFullToSynthetic', 'TransformToSyntheticFull', 'TransformToSyntheticKind',
            name=_('Synthetic Full Backup'),
        ),
        FieldSet(
            'EnableFullBackup', 'FullBackupScheduleKind',
            name=_('Active Full Backup'),
        ),
        FieldSet(
            'EnableGFS', 'WeeklyEnabled', 'MonthlyEnabled', 'YearlyEnabled',
            name=_('GFS Retention'),
        ),
        FieldSet(
            'RunAutomatically', 'ScheduleDailyEnabled', 'ScheduleDailyKind',
            'ScheduleMonthlyEnabled', 'ScheduleMonthlyDayOfWeek', 'ScheduleMonthlyDayNumberInMonth',
            'ScheduleMonthlyDayOfMonth',
            'SchedulePeriodicallyEnabled', 'SchedulePeriodicallyUnit',
            'AfterJobEnabled', 'AfterJobName',
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
        label=_('Job Creation Time After'),
        widget=DateTimePicker(),
    )
    job_creation_time_before = forms.DateTimeField(
        required=False,
        label=_('Job Creation Time Before'),
        widget=DateTimePicker(),
    )
    LastBackupEndTime_after = forms.DateTimeField(
        required=False,
        label=_('Last Backup End Time After'),
        widget=DateTimePicker(),
    )
    LastBackupEndTime_before = forms.DateTimeField(
        required=False,
        label=_('Last Backup End Time Before'),
        widget=DateTimePicker(),
    )
    LastBackupResult = forms.MultipleChoiceField(
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
    Algorithm = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobAlgorithmChoices,
        label=_('Algorithm'),
    )
    EnableDeduplication = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableDeduplicationChoices,
        label=_('Deduplication'),
    )
    StorageEncryptionEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobStorageEncryptionEnabledChoices,
        label=_('Storage Encryption'),
    )
    EnableDeletedVmDataRetention = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        label=_('Deleted VM Retention'),
    )

    # Synthetic full backup settings
    TransformFullToSynthetic = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        label=_('Synthetic Full (Incremental)'),
    )
    TransformToSyntheticFull = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        label=_('Synthetic Full (Reverse Incr.)'),
    )
    TransformToSyntheticKind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobSyntheticFullChoices,
        label=_('Synthetic Full Kind'),
    )

    # Active full backup settings
    EnableFullBackup = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobEnableFullBackupChoices,
        label=_('Active Full Backup'),
    )
    FullBackupScheduleKind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobFullBackupScheduleKindChoices,
        label=_('Full Backup Kind'),
    )

    # GFS retention settings
    EnableGFS = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSEnableChoices,
        label=_('GFS Enabled'),
    )
    WeeklyEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSWeeklyEnabledChoices,
        label=_('GFS Weekly'),
    )
    MonthlyEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSMonthlyEnabledChoices,
        label=_('GFS Monthly'),
    )
    YearlyEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobGFSYearlyEnabledChoices,
        label=_('GFS Yearly'),
    )

    # Schedule options
    RunAutomatically = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobRunAutomaticallyChoices,
        label=_('Run Automatically'),
    )
    ScheduleDailyEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDailyEnabledChoices,
        label=_('Daily Enabled'),
    )
    ScheduleDailyKind = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDailyKindChoices,
        label=_('Daily Kind'),
    )
    ScheduleMonthlyEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthlyEnabledChoices,
        label=_('Monthly Enabled'),
    )
    ScheduleMonthlyDayOfWeek = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthlyDayOfWeekChoices,
        label=_('Monthly Day of Week'),
    )
    ScheduleMonthlyDayNumberInMonth = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleMonthlyDayNumberInMonthChoices,
        label=_('Monthly Day number of Month'),
    )
    ScheduleMonthlyDayOfMonth = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobScheduleDayOfMonthChoices,
        label=_('Monthly Day of Month'),
    )
    SchedulePeriodicallyEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobPeriodicallyEnabledChoices,
        label=_('Periodically Enabled'),
    )
    SchedulePeriodicallyUnit = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobPeriodicallyUnitChoices,
        label=_('Periodically Unit'),
    )

    # After job
    AfterJobEnabled = forms.MultipleChoiceField(
        required=False,
        choices=BackupJobAfterJobEnabledChoices,
        label=_('After Job Enabled'),
    )
    AfterJobName = DynamicModelMultipleChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('After Job'),
    )