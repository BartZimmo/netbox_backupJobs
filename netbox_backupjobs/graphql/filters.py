from datetime import datetime, time
from typing import TYPE_CHECKING, Annotated

import strawberry
import strawberry_django
from strawberry import ID
from strawberry_django import DatetimeFilterLookup, StrFilterLookup, TimeFilterLookup

from netbox.graphql.filters import NetBoxModelFilter

from netbox_backupjobs.models import BackupJob

if TYPE_CHECKING:
    from ipam.graphql.filters import IPAddressFilter
    from netbox.graphql.filter_lookups import IntegerLookup, StringArrayLookup
    from virtualization.graphql.filters import VirtualMachineFilter

    from .enums import (
        BackupJobPlatformEnum,
        BackupJobStatusEnum,
        BackupJobResultEnum,
        BackupJobAlgorithmEnum,
        BackupJobStorageEncryptionEnabledEnum,
        BackupJobEnableDeduplicationEnum,
        BackupJobEnableDeletedVmDataRetentionEnum,
        BackupJobEnableFullBackupEnum,
        BackupJobEnableSyntheticFullForIncrementalEnum,
        BackupJobEnableSyntheticFullForReverseIncrementalEnum,
        BackupJobSyntheticFullEnum,
        BackupJobSyntheticFullDaysEnum,
        BackupJobSyntheticFullWeekEnum,
        BackupJobFullBackupScheduleKindEnum,
        BackupJobFullBackupWeekEnum,
        BackupJobFullBackupDaysEnum,
        BackupJobGFSEnableEnum,
        BackupJobGFSWeeklyEnabledEnum,
        BackupJobGFSWeeklyDayEnum,
        BackupJobGFSMonthlyEnabledEnum,
        BackupJobGFSWeekOfMonthEnum,
        BackupJobGFSYearlyEnabledEnum,
        BackupJobGFSMonthOfYearEnum,
        BackupJobRunAutomaticallyEnum,
        BackupJobScheduleDailyEnabledEnum,
        BackupJobScheduleDailyKindEnum,
        BackupJobScheduleMonthlyEnabledEnum,
        BackupJobScheduleMonthlyDayOfWeekEnum,
        BackupJobPeriodicallyEnabledEnum,
        BackupJobPeriodicallyUnitEnum,
        BackupJobAfterJobEnabledEnum,
        BackupJobScheduleMonthlyDayNumberInMonthEnum,
    )


@strawberry_django.filter_type(BackupJob, lookups=True)
class BackupJobFilter(NetBoxModelFilter):
    name: StrFilterLookup[str] | None = strawberry_django.filter_field()
    jobtype: StrFilterLookup[str] | None = strawberry_django.filter_field()
    platform: Annotated['BackupJobPlatformEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    status: Annotated['BackupJobStatusEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    virtual_machines: Annotated['VirtualMachineFilter', strawberry.lazy('virtualization.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    description: StrFilterLookup[str] | None = strawberry_django.filter_field()
    job_creation_time: DatetimeFilterLookup[datetime] | None = strawberry_django.filter_field()
    LastBackupEndTime: DatetimeFilterLookup[datetime] | None = strawberry_django.filter_field()
    LastBackupResult: Annotated['BackupJobResultEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    backup_server_name: StrFilterLookup[str] | None = strawberry_django.filter_field()
    backup_server_ip: Annotated['IPAddressFilter', strawberry.lazy('ipam.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    backup_server_ip_id: ID | None = strawberry_django.filter_field()
    target: StrFilterLookup[str] | None = strawberry_django.filter_field()

    # Advanced settings
    Algorithm: Annotated['BackupJobAlgorithmEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    EnableDeduplication: Annotated[
        'BackupJobEnableDeduplicationEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    StorageEncryptionEnabled: Annotated[
        'BackupJobStorageEncryptionEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    RetainDaysToKeep: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    RetainCycles: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    EnableDeletedVmDataRetention: Annotated[
        'BackupJobEnableDeletedVmDataRetentionEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    RetainDaysToKeepDeletedVmData: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )

    # Synthetic full backup settings
    TransformFullToSynthetic: Annotated[
        'BackupJobEnableSyntheticFullForIncrementalEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    TransformToSyntheticFull: Annotated[
        'BackupJobEnableSyntheticFullForReverseIncrementalEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    TransformToSyntheticKind: Annotated[
        'BackupJobSyntheticFullEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    TransformToSyntheticDays: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    SyntheticFullDayNumberInMonth: Annotated[
        'BackupJobSyntheticFullWeekEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    SyntheticFullDayOfWeek: Annotated[
        'BackupJobSyntheticFullDaysEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    TransformToSyntheticMonthly: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()

    # Active full backup settings
    EnableFullBackup: Annotated[
        'BackupJobEnableFullBackupEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    FullBackupScheduleKind: Annotated[
        'BackupJobFullBackupScheduleKindEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    FullBackupDays: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    FullBackupDayNumberInMonth: Annotated[
        'BackupJobFullBackupWeekEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    FullBackupDayOfWeek: Annotated[
        'BackupJobFullBackupDaysEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    FullBackupMonths: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )

    # GFS retention settings
    EnableGFS: Annotated['BackupJobGFSEnableEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    WeeklyEnabled: Annotated[
        'BackupJobGFSWeeklyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    WeeklyKeepBackupsFor: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    WeeklyKeepBackupsOnDayOfWeek: Annotated[
        'BackupJobGFSWeeklyDayEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    MonthlyEnabled: Annotated[
        'BackupJobGFSMonthlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    MonthlyKeepBackupsFor: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    MonthlyKeepBackupsWeekOfMonth: Annotated[
        'BackupJobGFSWeekOfMonthEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    YearlyEnabled: Annotated[
        'BackupJobGFSYearlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    YearlyKeepBackupsFor: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    YearlyKeepBackupsOnMonthOfYear: Annotated[
        'BackupJobGFSMonthOfYearEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()

    comments: StrFilterLookup[str] | None = strawberry_django.filter_field()

    # Schedule options
    RunAutomatically: Annotated[
        'BackupJobRunAutomaticallyEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    ScheduleDailyEnabled: Annotated[
        'BackupJobScheduleDailyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    ScheduleDailyTime: TimeFilterLookup[time] | None = strawberry_django.filter_field()
    ScheduleDailyKind: Annotated[
        'BackupJobScheduleDailyKindEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    ScheduleDailyDays: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    ScheduleMonthlyEnabled: Annotated[
        'BackupJobScheduleMonthlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    ScheduleMonthlyTime: TimeFilterLookup[time] | None = strawberry_django.filter_field()
    ScheduleMonthlyDayNumberInMonth: Annotated[
        'BackupJobScheduleMonthlyDayNumberInMonthEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    ScheduleMonthlyDayOfWeek: Annotated[
        'BackupJobScheduleMonthlyDayOfWeekEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    # Note: values are '1'-'31' plus 'last'; can't be a GraphQL enum since enum values may not start with a digit.
    ScheduleMonthlyDayOfMonth: StrFilterLookup[str] | None = strawberry_django.filter_field()
    ScheduleMonthlyMonths: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    SchedulePeriodicallyEnabled: Annotated[
        'BackupJobPeriodicallyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallyEvery: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    SchedulePeriodicallyUnit: Annotated[
        'BackupJobPeriodicallyUnitEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallyHourOffsetInMin: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    # Note: values are '0'-'23'; can't be a GraphQL enum since enum values may not start with a digit.
    SchedulePeriodicallyMondaySchema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallyTuesdaySchema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallyWednesdaySchema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallyThursdaySchema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallyFridaySchema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallySaturdaySchema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    SchedulePeriodicallySundaySchema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()

    # After job
    AfterJobEnabled: Annotated[
        'BackupJobAfterJobEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    AfterJobName: Annotated['BackupJobFilter', strawberry.lazy('netbox_backupjobs.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    AfterJobName_id: ID | None = strawberry_django.filter_field()
