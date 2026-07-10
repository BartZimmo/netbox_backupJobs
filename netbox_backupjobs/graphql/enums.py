import strawberry

from netbox_backupjobs.choices import (
    BackupJobPlatformChoices,
    BackupJobStatusChoices,
    BackupJobResultChoices,
    BackupCopyJobStatusChoices,
    BackupCopyJobResultChoices,
    BackupCopyJobModeChoices,
    BackupCopyJobEnableDeduplicationChoices,
    BackupCopyJobStorageEncryptionEnabledChoices,
    BackupCopyJobEnableDeletedVmDataRetentionChoices,
    BackupCopyJobGFSEnableChoices,
    BackupCopyJobGFSWeeklyEnabledChoices,
    BackupCopyJobGFSWeeklyDayChoices,
    BackupCopyJobGFSMonthlyEnabledChoices,
    BackupCopyJobGFSWeekOfMonthChoices,
    BackupCopyJobGFSYearlyEnabledChoices,
    BackupCopyJobGFSMonthOfYearChoices,
    BackupCopyJobDataTransferModeChoices,
    BackupCopyJobTransactionLogCopyEnabledChoices,
    BackupCopyJobTransferWindowChoices,
    BackupCopyJobRunAutomaticallyChoices,
    BackupCopyJobScheduleDailyEnabledChoices,
    BackupCopyJobScheduleDailyKindChoices,
    BackupCopyJobScheduleMonthlyEnabledChoices,
    BackupCopyJobScheduleMonthlyDayOfWeekChoices,
    BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
    BackupCopyJobPeriodicallyEnabledChoices,
    BackupCopyJobPeriodicallyUnitChoices,
    BackupCopyJobAfterJobEnabledChoices,
    BackupJobAlgorithmChoices,
    BackupJobStorageEncryptionEnabledChoices,
    BackupJobEnableDeduplicationChoices,
    BackupJobEnableDeletedVmDataRetentionChoices,
    BackupJobEnableFullBackupChoices,
    BackupJobEnableSyntheticFullForIncrementalChoices,
    BackupJobEnableSyntheticFullForReverseIncrementalChoices,
    BackupJobSyntheticFullChoices,
    BackupJobSyntheticFullDaysChoices,
    BackupJobSyntheticFullWeekChoices,
    BackupJobFullBackupScheduleKindChoices,
    BackupJobFullBackupDaysChoices,
    BackupJobFullBackupWeekChoices,
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
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
)


BackupJobPlatformEnum = strawberry.enum(BackupJobPlatformChoices.as_enum())
BackupJobStatusEnum = strawberry.enum(BackupJobStatusChoices.as_enum())
BackupJobResultEnum = strawberry.enum(BackupJobResultChoices.as_enum())
BackupJobAlgorithmEnum = strawberry.enum(BackupJobAlgorithmChoices.as_enum())
BackupJobStorageEncryptionEnabledEnum = strawberry.enum(BackupJobStorageEncryptionEnabledChoices.as_enum())
BackupJobEnableDeduplicationEnum = strawberry.enum(BackupJobEnableDeduplicationChoices.as_enum())
BackupJobEnableDeletedVmDataRetentionEnum = strawberry.enum(BackupJobEnableDeletedVmDataRetentionChoices.as_enum())
BackupJobEnableFullBackupEnum = strawberry.enum(BackupJobEnableFullBackupChoices.as_enum())
BackupJobEnableSyntheticFullForIncrementalEnum = strawberry.enum(
    BackupJobEnableSyntheticFullForIncrementalChoices.as_enum()
)
BackupJobEnableSyntheticFullForReverseIncrementalEnum = strawberry.enum(
    BackupJobEnableSyntheticFullForReverseIncrementalChoices.as_enum()
)
BackupJobSyntheticFullEnum = strawberry.enum(BackupJobSyntheticFullChoices.as_enum())
BackupJobSyntheticFullDaysEnum = strawberry.enum(BackupJobSyntheticFullDaysChoices.as_enum())
BackupJobSyntheticFullWeekEnum = strawberry.enum(BackupJobSyntheticFullWeekChoices.as_enum())
BackupJobFullBackupScheduleKindEnum = strawberry.enum(BackupJobFullBackupScheduleKindChoices.as_enum())
BackupJobFullBackupDaysEnum = strawberry.enum(BackupJobFullBackupDaysChoices.as_enum())
BackupJobFullBackupWeekEnum = strawberry.enum(BackupJobFullBackupWeekChoices.as_enum())
BackupJobGFSEnableEnum = strawberry.enum(BackupJobGFSEnableChoices.as_enum())
BackupJobGFSWeeklyEnabledEnum = strawberry.enum(BackupJobGFSWeeklyEnabledChoices.as_enum())
BackupJobGFSWeeklyDayEnum = strawberry.enum(BackupJobGFSWeeklyDayChoices.as_enum())
BackupJobGFSMonthlyEnabledEnum = strawberry.enum(BackupJobGFSMonthlyEnabledChoices.as_enum())
BackupJobGFSWeekOfMonthEnum = strawberry.enum(BackupJobGFSWeekOfMonthChoices.as_enum())
BackupJobGFSYearlyEnabledEnum = strawberry.enum(BackupJobGFSYearlyEnabledChoices.as_enum())
BackupJobGFSMonthOfYearEnum = strawberry.enum(BackupJobGFSMonthOfYearChoices.as_enum())
BackupJobRunAutomaticallyEnum = strawberry.enum(BackupJobRunAutomaticallyChoices.as_enum())
BackupJobScheduleDailyEnabledEnum = strawberry.enum(BackupJobScheduleDailyEnabledChoices.as_enum())
BackupJobScheduleDailyKindEnum = strawberry.enum(BackupJobScheduleDailyKindChoices.as_enum())
BackupJobScheduleMonthlyEnabledEnum = strawberry.enum(BackupJobScheduleMonthlyEnabledChoices.as_enum())
BackupJobScheduleMonthlyDayOfWeekEnum = strawberry.enum(BackupJobScheduleMonthlyDayOfWeekChoices.as_enum())
BackupJobPeriodicallyEnabledEnum = strawberry.enum(BackupJobPeriodicallyEnabledChoices.as_enum())
BackupJobPeriodicallyUnitEnum = strawberry.enum(BackupJobPeriodicallyUnitChoices.as_enum())
BackupJobAfterJobEnabledEnum = strawberry.enum(BackupJobAfterJobEnabledChoices.as_enum())
BackupJobScheduleMonthlyDayNumberInMonthEnum = strawberry.enum(BackupJobScheduleMonthlyDayNumberInMonthChoices.as_enum())

BackupCopyJobStatusEnum = strawberry.enum(BackupCopyJobStatusChoices.as_enum())
BackupCopyJobResultEnum = strawberry.enum(BackupCopyJobResultChoices.as_enum())
BackupCopyJobModeEnum = strawberry.enum(BackupCopyJobModeChoices.as_enum())
BackupCopyJobEnableDeduplicationEnum = strawberry.enum(BackupCopyJobEnableDeduplicationChoices.as_enum())
BackupCopyJobStorageEncryptionEnabledEnum = strawberry.enum(BackupCopyJobStorageEncryptionEnabledChoices.as_enum())
BackupCopyJobEnableDeletedVmDataRetentionEnum = strawberry.enum(
    BackupCopyJobEnableDeletedVmDataRetentionChoices.as_enum()
)
BackupCopyJobGFSEnableEnum = strawberry.enum(BackupCopyJobGFSEnableChoices.as_enum())
BackupCopyJobGFSWeeklyEnabledEnum = strawberry.enum(BackupCopyJobGFSWeeklyEnabledChoices.as_enum())
BackupCopyJobGFSWeeklyDayEnum = strawberry.enum(BackupCopyJobGFSWeeklyDayChoices.as_enum())
BackupCopyJobGFSMonthlyEnabledEnum = strawberry.enum(BackupCopyJobGFSMonthlyEnabledChoices.as_enum())
BackupCopyJobGFSWeekOfMonthEnum = strawberry.enum(BackupCopyJobGFSWeekOfMonthChoices.as_enum())
BackupCopyJobGFSYearlyEnabledEnum = strawberry.enum(BackupCopyJobGFSYearlyEnabledChoices.as_enum())
BackupCopyJobGFSMonthOfYearEnum = strawberry.enum(BackupCopyJobGFSMonthOfYearChoices.as_enum())
BackupCopyJobDataTransferModeEnum = strawberry.enum(BackupCopyJobDataTransferModeChoices.as_enum())
BackupCopyJobTransactionLogCopyEnabledEnum = strawberry.enum(BackupCopyJobTransactionLogCopyEnabledChoices.as_enum())
BackupCopyJobTransferWindowEnum = strawberry.enum(BackupCopyJobTransferWindowChoices.as_enum())
# Note: BackupCopyJobScheduleHourChoices values are '0'-'23'; can't be a GraphQL enum since
# enum values may not start with a digit. Use StringArrayLookup in filters.py instead.
BackupCopyJobRunAutomaticallyEnum = strawberry.enum(BackupCopyJobRunAutomaticallyChoices.as_enum())
BackupCopyJobScheduleDailyEnabledEnum = strawberry.enum(BackupCopyJobScheduleDailyEnabledChoices.as_enum())
BackupCopyJobScheduleDailyKindEnum = strawberry.enum(BackupCopyJobScheduleDailyKindChoices.as_enum())
BackupCopyJobScheduleMonthlyEnabledEnum = strawberry.enum(BackupCopyJobScheduleMonthlyEnabledChoices.as_enum())
BackupCopyJobScheduleMonthlyDayOfWeekEnum = strawberry.enum(BackupCopyJobScheduleMonthlyDayOfWeekChoices.as_enum())
BackupCopyJobScheduleMonthlyDayNumberInMonthEnum = strawberry.enum(
    BackupCopyJobScheduleMonthlyDayNumberInMonthChoices.as_enum()
)
BackupCopyJobPeriodicallyEnabledEnum = strawberry.enum(BackupCopyJobPeriodicallyEnabledChoices.as_enum())
BackupCopyJobPeriodicallyUnitEnum = strawberry.enum(BackupCopyJobPeriodicallyUnitChoices.as_enum())
BackupCopyJobAfterJobEnabledEnum = strawberry.enum(BackupCopyJobAfterJobEnabledChoices.as_enum())
# Note: BackupCopyJobScheduleDayOfMonthChoices values are '1'-'31' plus 'last'; can't be a GraphQL
# enum since enum values may not start with a digit. Use StrFilterLookup in filters.py instead.
