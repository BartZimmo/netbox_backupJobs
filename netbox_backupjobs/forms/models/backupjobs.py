from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelForm
from netbox_backupjobs.models import BackupJob
from utilities.forms.rendering import FieldSet
from ...choices import (
    BackupJobPlatformChoices,
    BackupJobStatusChoices,
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
)
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.utils import add_blank_choice
from utilities.forms.widgets import DateTimePicker

from ipam.models import IPAddress
from virtualization.models import VirtualMachine

__all__ = (
    'BackupJobForm',
)


class BackupJobForm(NetBoxModelForm):
    """
    Form for creating and editing BackupJob objects.
    """
    name = forms.CharField()
    status = forms.ChoiceField(
        choices=BackupJobStatusChoices,
        required=True,
    )
    jobtype = forms.CharField(
        required=False,
        label=_('Job Type'),
    )
    platform = forms.ChoiceField(
        choices=add_blank_choice(BackupJobPlatformChoices),
        required=False,
        label=_('Platform'),
    )
    job_creation_time = forms.DateTimeField(
        required=False,
        label=_('Job Creation Time'),
        widget=DateTimePicker(),
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
    target = forms.CharField(
        required=False,
        label=_('Target'),
    )
    virtual_machines = DynamicModelMultipleChoiceField(
        queryset=VirtualMachine.objects.all(),
        required=False,
        label="Virtual Machines",
        help_text='The virtual machines associated with this backup job',
    )

    # Advanced job settings
    Algorithm = forms.ChoiceField(
        choices=BackupJobAlgorithmChoices,
        required=True,
        label=_('Algorithm'),
    )
    EnableDeduplication = forms.ChoiceField(
        choices=BackupJobEnableDeduplicationChoices,
        required=True,
        label=_('Enable Deduplication'),
    )
    StorageEncryptionEnabled = forms.ChoiceField(
        choices=BackupJobStorageEncryptionEnabledChoices,
        required=True,
        label=_('Enable Storage Encryption'),
    )
    RetainDaysToKeep = forms.CharField(
        required=False,
        label=_('Retain Days to Keep'),
    )
    RetainCycles = forms.CharField(
        required=False,
        label=_('Retain Cycles'),
    )
    EnableDeletedVmDataRetention = forms.ChoiceField(
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        required=True,
        label=_('Enable Deleted VM Data Retention'),
    )
    RetainDaysToKeepDeletedVmData = forms.CharField(
        required=False,
        label=_('Retain Days to Keep Deleted VM Data'),
    )

    # Synthetic full backup settings
    TransformFullToSyntethic = forms.ChoiceField(
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        required=True,
        label=_('Transform Incremental to Synthetic Full'),
    )
    TransformToSyntheticFull = forms.ChoiceField(
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        required=True,
        label=_('Transform Reverse Incremental to Synthetic Full'),
    )
    TransformToSyntethicKind = forms.ChoiceField(
        choices=BackupJobSyntheticFullChoices,
        required=False,
        label=_('Synthetic Full Kind'),
    )
    TransformToSyntheticDays = forms.MultipleChoiceField(
        choices=BackupJobSyntheticFullDaysChoices,
        required=False,
        label=_('Synthetic Full Days of Week'),
    )
    SyntheticFullDayNumberInMonth = forms.ChoiceField(
        choices=BackupJobSyntheticFullWeekChoices,
        required=False,
        label=_('Synthetic Full Week of Month'),
    )
    SyntheticFullDayOfWeek = forms.ChoiceField(
        choices=BackupJobSyntheticFullDaysChoices,
        required=False,
        label=_('Synthetic Full Day of Week (Monthly)'),
    )
    TransformToSyntethicMonthly = forms.MultipleChoiceField(
        choices=BackupJobSyntheticFullMonthChoices,
        required=False,
        label=_('Synthetic Full Months'),
    )

    # Active full backup settings
    EnableFullBackup = forms.ChoiceField(
        choices=BackupJobEnableFullBackupChoices,
        required=True,
        label=_('Enable Active Full Backup'),
    )
    FullBackupScheduleKind = forms.ChoiceField(
        choices=BackupJobFullBackupScheduleKindChoices,
        required=False,
        label=_('Schedule Kind'),
    )
    FullBackupDays = forms.MultipleChoiceField(
        choices=BackupJobFullBackupDaysChoices,
        required=False,
        label=_('Days of Week'),
    )
    FullBackupDayNumberInMonth = forms.ChoiceField(
        choices=BackupJobFullBackupWeekChoices,
        required=False,
        label=_('Week of Month'),
    )
    FullBackupDayOfWeek = forms.ChoiceField(
        choices=BackupJobFullBackupDaysChoices,
        required=False,
        label=_('Day of Week (Monthly)'),
    )
    FullBackupMonths = forms.MultipleChoiceField(
        choices=BackupJobFullBackupMonthChoices,
        required=False,
        label=_('Months'),
    )

    # GFS retention settings
    EnableGFS = forms.ChoiceField(
        choices=BackupJobGFSEnableChoices,
        required=True,
        label=_('Enable GFS'),
    )
    WeeklyEnabled = forms.ChoiceField(
        choices=BackupJobGFSWeeklyEnabledChoices,
        required=True,
        label=_('Weekly Enabled'),
    )
    WeeklyKeepBackupsFor = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Weekly Keep (weeks)'),
    )
    WeeklyKeepBackupsOnDayOfWeek = forms.ChoiceField(
        choices=BackupJobGFSWeeklyDayChoices,
        required=False,
        label=_('Weekly Day'),
    )
    MonthlyEnabled = forms.ChoiceField(
        choices=BackupJobGFSMonthlyEnabledChoices,
        required=True,
        label=_('Monthly Enabled'),
    )
    MonthlyKeepBackupsFor = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Monthly Keep (months)'),
    )
    MonthlyKeepBackupsWeekOfMonth = forms.ChoiceField(
        choices=BackupJobGFSWeekOfMonthChoices,
        required=False,
        label=_('Monthly Week'),
    )
    YearlyEnabled = forms.ChoiceField(
        choices=BackupJobGFSYearlyEnabledChoices,
        required=True,
        label=_('Yearly Enabled'),
    )
    YearlyKeepBackupsFor = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Yearly Keep (years)'),
    )
    YearlyKeepBackupsOnMonthOfYear = forms.ChoiceField(
        choices=BackupJobGFSMonthOfYearChoices,
        required=False,
        label=_('Yearly Month'),
    )

    fieldsets = (
        FieldSet(
            'name', 'description', 'status', 'jobtype', 'platform', 'job_creation_time', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'tags',
            name=_('Backup Job'),
        ),
        FieldSet(
            'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled',
            'RetainDaysToKeep', 'RetainCycles',
            'EnableDeletedVmDataRetention', 'RetainDaysToKeepDeletedVmData',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'TransformFullToSyntethic', 'TransformToSyntheticFull',
            'TransformToSyntethicKind',
            'TransformToSyntheticDays',
            'SyntheticFullDayNumberInMonth', 'SyntheticFullDayOfWeek',
            'TransformToSyntethicMonthly',
            name=_('Synthetic Full Backup'),
        ),
        FieldSet(
            'EnableFullBackup', 'FullBackupScheduleKind',
            'FullBackupDays',
            'FullBackupDayNumberInMonth', 'FullBackupDayOfWeek',
            'FullBackupMonths',
            name=_('Active Full Backup'),
        ),
        FieldSet(
            'EnableGFS',
            'WeeklyEnabled', 'WeeklyKeepBackupsFor', 'WeeklyKeepBackupsOnDayOfWeek',
            'MonthlyEnabled', 'MonthlyKeepBackupsFor', 'MonthlyKeepBackupsWeekOfMonth',
            'YearlyEnabled', 'YearlyKeepBackupsFor', 'YearlyKeepBackupsOnMonthOfYear',
            name=_('GFS Retention'),
        ),
    )

    class Meta:
        model = BackupJob
        fields = [
            'name', 'status', 'jobtype', 'platform', 'job_creation_time', 'description', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'comments', 'tags',
            'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled',
            'RetainDaysToKeep', 'RetainCycles',
            'EnableDeletedVmDataRetention', 'RetainDaysToKeepDeletedVmData',
            'TransformFullToSyntethic', 'TransformToSyntheticFull',
            'TransformToSyntethicKind', 'TransformToSyntheticDays',
            'SyntheticFullDayNumberInMonth', 'SyntheticFullDayOfWeek',
            'TransformToSyntethicMonthly',
            'EnableFullBackup', 'FullBackupScheduleKind',
            'FullBackupDays', 'FullBackupDayNumberInMonth', 'FullBackupDayOfWeek',
            'FullBackupMonths',
            'EnableGFS',
            'WeeklyEnabled', 'WeeklyKeepBackupsFor', 'WeeklyKeepBackupsOnDayOfWeek',
            'MonthlyEnabled', 'MonthlyKeepBackupsFor', 'MonthlyKeepBackupsWeekOfMonth',
            'YearlyEnabled', 'YearlyKeepBackupsFor', 'YearlyKeepBackupsOnMonthOfYear',
        ]


