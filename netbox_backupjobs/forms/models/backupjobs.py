from django import forms
from django.utils.translation import gettext_lazy as _

from netbox.forms import NetBoxModelForm
from netbox_backupjobs.models import BackupJob
from utilities.forms.rendering import FieldSet
from ...choices import (
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
    BackupJobScheduleDayOfMonthChoices,
    BackupJobScheduleMonthChoices,
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
    BackupJobScheduleHourChoices,
)
from utilities.forms.fields import DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms.utils import add_blank_choice
from utilities.forms.widgets import DateTimePicker, TimePicker

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
    LastBackupEndTime = forms.DateTimeField(
        required=False,
        label=_('Last Backup End Time'),
        widget=DateTimePicker(),
    )
    LastBackupResult = forms.ChoiceField(
        choices=add_blank_choice(BackupJobResultChoices),
        required=False,
        label=_('Last Backup Result'),
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
    RetainDaysToKeep = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep'),
    )
    RetainCycles = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Cycles'),
    )
    EnableDeletedVmDataRetention = forms.ChoiceField(
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        required=True,
        label=_('Enable Deleted VM Data Retention'),
    )
    RetainDaysToKeepDeletedVmData = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Retain Days to Keep Deleted VM Data'),
    )

    # Synthetic full backup settings
    TransformFullToSynthetic = forms.ChoiceField(
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        required=True,
        label=_('Transform Incremental to Synthetic Full'),
    )
    TransformToSyntheticFull = forms.ChoiceField(
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        required=True,
        label=_('Transform Reverse Incremental to Synthetic Full'),
    )
    TransformToSyntheticKind = forms.ChoiceField(
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
    TransformToSyntheticMonthly = forms.MultipleChoiceField(
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

    # Schedule options
    RunAutomatically = forms.ChoiceField(
        choices=BackupJobRunAutomaticallyChoices,
        required=True,
        label=_('Run Automatically'),
    )
    ScheduleDailyEnabled = forms.ChoiceField(
        choices=BackupJobScheduleDailyEnabledChoices,
        required=True,
        label=_('Daily Enabled'),
    )
    ScheduleDailyTime = forms.TimeField(
        required=False,
        label=_('Daily Time'),
        widget=TimePicker(),
    )
    ScheduleDailyKind = forms.ChoiceField(
        choices=BackupJobScheduleDailyKindChoices,
        required=False,
        label=_('Daily Kind'),
    )
    ScheduleDailyDays = forms.MultipleChoiceField(
        choices=BackupJobScheduleDaysChoices,
        required=False,
        label=_('Daily Days'),
    )
    ScheduleMonthlyEnabled = forms.ChoiceField(
        choices=BackupJobScheduleMonthlyEnabledChoices,
        required=True,
        label=_('Monthly Enabled'),
    )
    ScheduleMonthlyTime = forms.TimeField(
        required=False,
        label=_('Monthly Time'),
        widget=TimePicker(),
    )
    ScheduleMonthlyDayOfWeek = forms.ChoiceField(
        choices=BackupJobScheduleMonthlyDayOfWeekChoices,
        required=False,
        label=_('Monthly Day of Week'),
    )
    ScheduleMonthlyDayNumberInMonth = forms.ChoiceField(
        choices=BackupJobScheduleMonthlyDayNumberInMonthChoices,
        required=False,
        label=_('Monthly Day number of Month'),
    )
    ScheduleMonthlyDayOfMonth = forms.ChoiceField(
        choices=BackupJobScheduleDayOfMonthChoices,
        required=False,
        label=_('Monthly Day of Month'),
    )
    ScheduleMonthlyMonths = forms.MultipleChoiceField(
        choices=BackupJobScheduleMonthChoices,
        required=False,
        label=_('Monthly Months'),
    )
    SchedulePeriodicallyEnabled = forms.ChoiceField(
        choices=BackupJobPeriodicallyEnabledChoices,
        required=True,
        label=_('Periodically Enabled'),
    )
    SchedulePeriodicallyEvery = forms.IntegerField(
        required=False,
        min_value=1,
        label=_('Periodically Every'),
    )
    SchedulePeriodicallyUnit = forms.ChoiceField(
        choices=BackupJobPeriodicallyUnitChoices,
        required=False,
        label=_('Periodically Unit'),
    )
    SchedulePeriodicallyHourOffsetInMin = forms.IntegerField(
        required=False,
        min_value=0,
        max_value=59,
        label=_('Hour Offset (min)'),
        help_text=_('Offset in minutes applied to the start of each hour block in the day schemas below'),
    )
    SchedulePeriodicallyMondaySchema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        label=_('Monday Schema'),
    )
    SchedulePeriodicallyTuesdaySchema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        label=_('Tuesday Schema'),
    )
    SchedulePeriodicallyWednesdaySchema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        label=_('Wednesday Schema'),
    )
    SchedulePeriodicallyThursdaySchema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        label=_('Thursday Schema'),
    )
    SchedulePeriodicallyFridaySchema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        label=_('Friday Schema'),
    )
    SchedulePeriodicallySaturdaySchema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        label=_('Saturday Schema'),
    )
    SchedulePeriodicallySundaySchema = forms.MultipleChoiceField(
        choices=BackupJobScheduleHourChoices,
        required=False,
        label=_('Sunday Schema'),
    )

    # After job
    AfterJobEnabled = forms.ChoiceField(
        choices=BackupJobAfterJobEnabledChoices,
        required=True,
        label=_('After Job Enabled'),
    )
    AfterJobName = DynamicModelChoiceField(
        queryset=BackupJob.objects.all(),
        required=False,
        label=_('After Job'),
    )

    fieldsets = (
        FieldSet(
            'name', 'description', 'status', 'jobtype', 'platform', 'job_creation_time', 'LastBackupEndTime', 'LastBackupResult', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'tags',
            name=_('Backup Job'),
        ),
        FieldSet(
            'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled',
            'RetainDaysToKeep', 'RetainCycles',
            'EnableDeletedVmDataRetention', 'RetainDaysToKeepDeletedVmData',
            name=_('Advanced Settings'),
        ),
        FieldSet(
            'TransformFullToSynthetic', 'TransformToSyntheticFull',
            'TransformToSyntheticKind',
            'TransformToSyntheticDays',
            'SyntheticFullDayNumberInMonth', 'SyntheticFullDayOfWeek',
            'TransformToSyntheticMonthly',
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
        FieldSet(
            'RunAutomatically',
            'ScheduleDailyEnabled', 'ScheduleDailyTime', 'ScheduleDailyKind', 'ScheduleDailyDays',
            'ScheduleMonthlyEnabled', 'ScheduleMonthlyTime', 'ScheduleMonthlyDayOfWeek',
            'ScheduleMonthlyDayNumberInMonth', 'ScheduleMonthlyDayOfMonth', 'ScheduleMonthlyMonths',
            'SchedulePeriodicallyEnabled', 'SchedulePeriodicallyEvery', 'SchedulePeriodicallyUnit',
            'SchedulePeriodicallyHourOffsetInMin',
            'SchedulePeriodicallyMondaySchema', 'SchedulePeriodicallyTuesdaySchema',
            'SchedulePeriodicallyWednesdaySchema', 'SchedulePeriodicallyThursdaySchema',
            'SchedulePeriodicallyFridaySchema', 'SchedulePeriodicallySaturdaySchema',
            'SchedulePeriodicallySundaySchema',
            'AfterJobEnabled', 'AfterJobName',
            name=_('Schedule Options'),
        ),
    )

    class Meta:
        model = BackupJob
        fields = [
            'name', 'status', 'jobtype', 'platform', 'job_creation_time', 'LastBackupEndTime', 'LastBackupResult', 'description', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'comments', 'tags',
            'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled',
            'RetainDaysToKeep', 'RetainCycles',
            'EnableDeletedVmDataRetention', 'RetainDaysToKeepDeletedVmData',
            'TransformFullToSynthetic', 'TransformToSyntheticFull',
            'TransformToSyntheticKind', 'TransformToSyntheticDays',
            'SyntheticFullDayNumberInMonth', 'SyntheticFullDayOfWeek',
            'TransformToSyntheticMonthly',
            'EnableFullBackup', 'FullBackupScheduleKind',
            'FullBackupDays', 'FullBackupDayNumberInMonth', 'FullBackupDayOfWeek',
            'FullBackupMonths',
            'EnableGFS',
            'WeeklyEnabled', 'WeeklyKeepBackupsFor', 'WeeklyKeepBackupsOnDayOfWeek',
            'MonthlyEnabled', 'MonthlyKeepBackupsFor', 'MonthlyKeepBackupsWeekOfMonth',
            'YearlyEnabled', 'YearlyKeepBackupsFor', 'YearlyKeepBackupsOnMonthOfYear',
            'RunAutomatically',
            'ScheduleDailyEnabled', 'ScheduleDailyTime', 'ScheduleDailyKind', 'ScheduleDailyDays',
            'ScheduleMonthlyEnabled', 'ScheduleMonthlyTime', 'ScheduleMonthlyDayOfWeek',
            'ScheduleMonthlyDayNumberInMonth', 'ScheduleMonthlyDayOfMonth', 'ScheduleMonthlyMonths',
            'SchedulePeriodicallyEnabled', 'SchedulePeriodicallyEvery', 'SchedulePeriodicallyUnit',
            'SchedulePeriodicallyHourOffsetInMin',
            'SchedulePeriodicallyMondaySchema', 'SchedulePeriodicallyTuesdaySchema',
            'SchedulePeriodicallyWednesdaySchema', 'SchedulePeriodicallyThursdaySchema',
            'SchedulePeriodicallyFridaySchema', 'SchedulePeriodicallySaturdaySchema',
            'SchedulePeriodicallySundaySchema',
            'AfterJobEnabled', 'AfterJobName',
        ]


