from datetime import datetime, time
from typing import TYPE_CHECKING, Annotated

import strawberry
import strawberry_django
from strawberry import ID
from strawberry_django import DatetimeFilterLookup, StrFilterLookup, TimeFilterLookup

from netbox.graphql.filters import NetBoxModelFilter

from netbox_backupjobs.models import BackupJob, BackupCopyJob

if TYPE_CHECKING:
    from ipam.graphql.filters import IPAddressFilter
    from netbox.graphql.filter_lookups import IntegerLookup, StringArrayLookup
    from virtualization.graphql.filters import VirtualMachineFilter

    from .enums import (
        BackupCopyJobStatusEnum,
        BackupCopyJobResultEnum,
        BackupCopyJobModeEnum,
        BackupCopyJobEnableDeduplicationEnum,
        BackupCopyJobStorageEncryptionEnabledEnum,
        BackupCopyJobEnableDeletedVmDataRetentionEnum,
        BackupCopyJobGFSEnableEnum,
        BackupCopyJobGFSWeeklyEnabledEnum,
        BackupCopyJobGFSWeeklyDayEnum,
        BackupCopyJobGFSMonthlyEnabledEnum,
        BackupCopyJobGFSWeekOfMonthEnum,
        BackupCopyJobGFSYearlyEnabledEnum,
        BackupCopyJobGFSMonthOfYearEnum,
        BackupCopyJobDataTransferModeEnum,
        BackupCopyJobTransactionLogCopyEnabledEnum,
        BackupCopyJobTransferWindowEnum,
        BackupCopyJobRunAutomaticallyEnum,
        BackupCopyJobScheduleDailyEnabledEnum,
        BackupCopyJobScheduleDailyKindEnum,
        BackupCopyJobScheduleMonthlyEnabledEnum,
        BackupCopyJobScheduleMonthlyDayOfWeekEnum,
        BackupCopyJobScheduleMonthlyDayNumberInMonthEnum,
        BackupCopyJobPeriodicallyEnabledEnum,
        BackupCopyJobPeriodicallyUnitEnum,
        BackupCopyJobAfterJobEnabledEnum,
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
    last_backup_end_time: DatetimeFilterLookup[datetime] | None = strawberry_django.filter_field()
    last_backup_result: Annotated['BackupJobResultEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    backup_server_name: StrFilterLookup[str] | None = strawberry_django.filter_field()
    backup_server_ip: Annotated['IPAddressFilter', strawberry.lazy('ipam.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    backup_server_ip_id: ID | None = strawberry_django.filter_field()
    target: StrFilterLookup[str] | None = strawberry_django.filter_field()

    # Advanced settings
    algorithm: Annotated['BackupJobAlgorithmEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    enable_deduplication: Annotated[
        'BackupJobEnableDeduplicationEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    storage_encryption_enabled: Annotated[
        'BackupJobStorageEncryptionEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    retain_days_to_keep: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    retain_cycles: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    enable_deleted_vm_data_retention: Annotated[
        'BackupJobEnableDeletedVmDataRetentionEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    retain_days_to_keep_deleted_vm_data: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )

    # Synthetic full backup settings
    transform_full_to_synthetic: Annotated[
        'BackupJobEnableSyntheticFullForIncrementalEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    transform_to_synthetic_full: Annotated[
        'BackupJobEnableSyntheticFullForReverseIncrementalEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    transform_to_synthetic_kind: Annotated[
        'BackupJobSyntheticFullEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    transform_to_synthetic_days: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    synthetic_full_day_number_in_month: Annotated[
        'BackupJobSyntheticFullWeekEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    synthetic_full_day_of_week: Annotated[
        'BackupJobSyntheticFullDaysEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    transform_to_synthetic_monthly: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()

    # Active full backup settings
    enable_full_backup: Annotated[
        'BackupJobEnableFullBackupEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    full_backup_schedule_kind: Annotated[
        'BackupJobFullBackupScheduleKindEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    full_backup_days: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    full_backup_day_number_in_month: Annotated[
        'BackupJobFullBackupWeekEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    full_backup_day_of_week: Annotated[
        'BackupJobFullBackupDaysEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    full_backup_months: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )

    # GFS retention settings
    enable_gfs: Annotated['BackupJobGFSEnableEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    weekly_enabled: Annotated[
        'BackupJobGFSWeeklyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    weekly_keep_backups_for: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    weekly_keep_backups_on_day_of_week: Annotated[
        'BackupJobGFSWeeklyDayEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    monthly_enabled: Annotated[
        'BackupJobGFSMonthlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    monthly_keep_backups_for: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    monthly_keep_backups_week_of_month: Annotated[
        'BackupJobGFSWeekOfMonthEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    yearly_enabled: Annotated[
        'BackupJobGFSYearlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    yearly_keep_backups_for: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    yearly_keep_backups_on_month_of_year: Annotated[
        'BackupJobGFSMonthOfYearEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()

    comments: StrFilterLookup[str] | None = strawberry_django.filter_field()

    # Schedule options
    run_automatically: Annotated[
        'BackupJobRunAutomaticallyEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_daily_enabled: Annotated[
        'BackupJobScheduleDailyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_daily_time: TimeFilterLookup[time] | None = strawberry_django.filter_field()
    schedule_daily_kind: Annotated[
        'BackupJobScheduleDailyKindEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_daily_days: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    schedule_monthly_enabled: Annotated[
        'BackupJobScheduleMonthlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_monthly_time: TimeFilterLookup[time] | None = strawberry_django.filter_field()
    schedule_monthly_day_number_in_month: Annotated[
        'BackupJobScheduleMonthlyDayNumberInMonthEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_monthly_day_of_week: Annotated[
        'BackupJobScheduleMonthlyDayOfWeekEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    # Note: values are '1'-'31' plus 'last'; can't be a GraphQL enum since enum values may not start with a digit.
    schedule_monthly_day_of_month: StrFilterLookup[str] | None = strawberry_django.filter_field()
    schedule_monthly_months: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    schedule_periodically_enabled: Annotated[
        'BackupJobPeriodicallyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_every: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    schedule_periodically_unit: Annotated[
        'BackupJobPeriodicallyUnitEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_hour_offset_in_min: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    # Note: values are '0'-'23'; can't be a GraphQL enum since enum values may not start with a digit.
    schedule_periodically_monday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_tuesday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_wednesday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_thursday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_friday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_saturday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_sunday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()

    # After job
    after_job_enabled: Annotated[
        'BackupJobAfterJobEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    after_job_name: Annotated['BackupJobFilter', strawberry.lazy('netbox_backupjobs.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    after_job_name_id: ID | None = strawberry_django.filter_field()


@strawberry_django.filter_type(BackupCopyJob, lookups=True)
class BackupCopyJobFilter(NetBoxModelFilter):
    name: StrFilterLookup[str] | None = strawberry_django.filter_field()
    jobtype: StrFilterLookup[str] | None = strawberry_django.filter_field()
    status: Annotated['BackupCopyJobStatusEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    mode: Annotated['BackupCopyJobModeEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    data_transfer_mode: Annotated[
        'BackupCopyJobDataTransferModeEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    description: StrFilterLookup[str] | None = strawberry_django.filter_field()
    job_creation_time: DatetimeFilterLookup[datetime] | None = strawberry_django.filter_field()
    last_backup_result: Annotated[
        'BackupCopyJobResultEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    backup_server_name: StrFilterLookup[str] | None = strawberry_django.filter_field()
    backup_server_ip: Annotated['IPAddressFilter', strawberry.lazy('ipam.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    backup_server_ip_id: ID | None = strawberry_django.filter_field()
    retain_days_to_keep: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    target: StrFilterLookup[str] | None = strawberry_django.filter_field()
    backup_jobs: Annotated['BackupJobFilter', strawberry.lazy('netbox_backupjobs.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )

    # Advanced settings
    enable_deduplication: Annotated[
        'BackupCopyJobEnableDeduplicationEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    storage_encryption_enabled: Annotated[
        'BackupCopyJobStorageEncryptionEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    transaction_log_copy_enabled: Annotated[
        'BackupCopyJobTransactionLogCopyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    enable_deleted_vm_data_retention: Annotated[
        'BackupCopyJobEnableDeletedVmDataRetentionEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    retain_days_to_keep_deleted_vm_data: Annotated[
        'IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()

    # GFS retention settings
    enable_gfs: Annotated['BackupCopyJobGFSEnableEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')] | None = (
        strawberry_django.filter_field()
    )
    weekly_enabled: Annotated[
        'BackupCopyJobGFSWeeklyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    weekly_keep_backups_for: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    weekly_keep_backups_on_day_of_week: Annotated[
        'BackupCopyJobGFSWeeklyDayEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    monthly_enabled: Annotated[
        'BackupCopyJobGFSMonthlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    monthly_keep_backups_for: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    monthly_keep_backups_week_of_month: Annotated[
        'BackupCopyJobGFSWeekOfMonthEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    yearly_enabled: Annotated[
        'BackupCopyJobGFSYearlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    yearly_keep_backups_for: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    yearly_keep_backups_on_month_of_year: Annotated[
        'BackupCopyJobGFSMonthOfYearEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()

    # Schedule options
    transfer_window: Annotated[
        'BackupCopyJobTransferWindowEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    # Note: values are '0'-'23'; can't be a GraphQL enum since enum values may not start with a digit.
    transfer_window_monday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    transfer_window_tuesday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    transfer_window_wednesday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    transfer_window_thursday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    transfer_window_friday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    transfer_window_saturday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    transfer_window_sunday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    run_automatically: Annotated[
        'BackupCopyJobRunAutomaticallyEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_daily_enabled: Annotated[
        'BackupCopyJobScheduleDailyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_daily_time: TimeFilterLookup[time] | None = strawberry_django.filter_field()
    schedule_daily_kind: Annotated[
        'BackupCopyJobScheduleDailyKindEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_daily_days: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    schedule_monthly_enabled: Annotated[
        'BackupCopyJobScheduleMonthlyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_monthly_time: TimeFilterLookup[time] | None = strawberry_django.filter_field()
    schedule_monthly_day_number_in_month: Annotated[
        'BackupCopyJobScheduleMonthlyDayNumberInMonthEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_monthly_day_of_week: Annotated[
        'BackupCopyJobScheduleMonthlyDayOfWeekEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    # Note: values are '1'-'31' plus 'last'; can't be a GraphQL enum since enum values may not start with a digit.
    schedule_monthly_day_of_month: StrFilterLookup[str] | None = strawberry_django.filter_field()
    schedule_monthly_months: Annotated['StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    schedule_periodically_enabled: Annotated[
        'BackupCopyJobPeriodicallyEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_every: Annotated['IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')] | None = (
        strawberry_django.filter_field()
    )
    schedule_periodically_unit: Annotated[
        'BackupCopyJobPeriodicallyUnitEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_hour_offset_in_min: Annotated[
        'IntegerLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    # Note: values are '0'-'23'; can't be a GraphQL enum since enum values may not start with a digit.
    schedule_periodically_monday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_tuesday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_wednesday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_thursday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_friday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_saturday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()
    schedule_periodically_sunday_schema: Annotated[
        'StringArrayLookup', strawberry.lazy('netbox.graphql.filter_lookups')
    ] | None = strawberry_django.filter_field()

    # After job
    after_job_enabled: Annotated[
        'BackupCopyJobAfterJobEnabledEnum', strawberry.lazy('netbox_backupjobs.graphql.enums')
    ] | None = strawberry_django.filter_field()
    after_job_name: Annotated['BackupCopyJobFilter', strawberry.lazy('netbox_backupjobs.graphql.filters')] | None = (
        strawberry_django.filter_field()
    )
    after_job_name_id: ID | None = strawberry_django.filter_field()
