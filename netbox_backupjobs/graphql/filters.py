from datetime import datetime
from typing import TYPE_CHECKING, Annotated

import strawberry
import strawberry_django
from strawberry import ID
from strawberry_django import DatetimeFilterLookup, StrFilterLookup

from netbox.graphql.filters import NetBoxModelFilter

from netbox_backupjobs.models import BackupJob

if TYPE_CHECKING:
    from ipam.graphql.filters import IPAddressFilter
    from netbox.graphql.filter_lookups import IntegerLookup, StringArrayLookup
    from virtualization.graphql.filters import VirtualMachineFilter

    from .enums import (
        BackupJobPlatformEnum,
        BackupJobStatusEnum,
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
    RetainDaysToKeep: StrFilterLookup[str] | None = strawberry_django.filter_field()
    RetainCycles: StrFilterLookup[str] | None = strawberry_django.filter_field()
    EnableDeletedVmDataRetention: Annotated[
        'BackupJobEnableDeletedVmDataRetentionEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    RetainDaysToKeepDeletedVmData: StrFilterLookup[str] | None = strawberry_django.filter_field()

    # Synthetic full backup settings
    TransformFullToSyntethic: Annotated[
        'BackupJobEnableSyntheticFullForIncrementalEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    TransformToSyntheticFull: Annotated[
        'BackupJobEnableSyntheticFullForReverseIncrementalEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    TransformToSyntethicKind: Annotated[
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
    TransformToSyntethicMonthly: Annotated[
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
