import strawberry

from netbox_backupjobs.choices import (
    BackupJobPlatformChoices,
    BackupJobStatusChoices,
    BackupJobResultChoices,
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
