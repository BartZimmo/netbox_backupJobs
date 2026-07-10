from utilities.choices import ChoiceSet
from django.utils.translation import gettext_lazy as _


#
# BackupJob
#

class BackupJobPlatformChoices(ChoiceSet):
    key = 'BackupJob.platform'

    VMWARE = 'vmware'
    HYPER_V = 'hyper-v'
    OBJECT_STORAGE = 'object-storage'

    CHOICES = [
        (VMWARE, _('VMware')),
        (HYPER_V, _('Hyper-V')),
        (OBJECT_STORAGE, _('Object Storage')),
    ]

class BackupJobStatusChoices(ChoiceSet):
    key = 'BackupJob.status'

    STATUS_ENABLED = 'enabled'
    STATUS_DISABLED = 'disabled'
    STATUS_ORPHANED = 'orphaned'


    CHOICES = [
        (STATUS_ENABLED, _('Enabled'), 'green'),
        (STATUS_DISABLED, _('Disabled'), 'blue'),
        (STATUS_ORPHANED, _('Orphaned'), 'yellow'),   
    ]

class BackupJobResultChoices(ChoiceSet):
    key = 'BackupJob.last_backup_result'

    SUCCESS = 'success'
    WARNING = 'warning'
    FAILED = 'failed'

    CHOICES = [
        (SUCCESS, _('Success'), 'green'),
        (WARNING, _('Warning'), 'yellow'),
        (FAILED, _('Failed'), 'red'),
    ]

class BackupJobAlgorithmChoices(ChoiceSet):
    key = 'BackupJob.algorithm'

    INCREMENTAL = 'incremental'
    REVERSE_INCREMENTAL = 'reverse incremental'

    CHOICES = [
        (INCREMENTAL, _('Incremental')),
        (REVERSE_INCREMENTAL, _('Reverse Incremental')),
    ]

class BackupJobStorageEncryptionEnabledChoices(ChoiceSet):
    key = 'BackupJob.storage_encryption_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]

class BackupJobEnableDeduplicationChoices(ChoiceSet):
    key = 'BackupJob.enable_deduplication'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]

class BackupJobEnableDeletedVmDataRetentionChoices(ChoiceSet):
    key = 'BackupJob.enable_deleted_vm_data_retention'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]

class BackupJobEnableFullBackupChoices(ChoiceSet):
    key = 'BackupJob.enable_full_backup'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupJobEnableSyntheticFullForIncrementalChoices(ChoiceSet):
    key = 'BackupJob.enable_synthetic_full_for_incremental'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]

class BackupJobEnableSyntheticFullForReverseIncrementalChoices(ChoiceSet):
    key = 'BackupJob.enable_synthetic_full_for_reverse_incremental'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]

class BackupJobSyntheticFullChoices(ChoiceSet):
    key = 'BackupJob.synthetic_full'

    SYNTHETIC_FULL_DAILY = 'daily'
    SYNTHETIC_FULL_MONTHLY = 'monthly'

    CHOICES = [
        (SYNTHETIC_FULL_DAILY, _('Daily')),
        (SYNTHETIC_FULL_MONTHLY, _('Monthly')),
    ]

class BackupJobSyntheticFullDaysChoices(ChoiceSet):
    key = 'BackupJob.synthetic_full_days'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday'), 'green'),
        (TUESDAY, _('Tuesday'), 'blue'),
        (WEDNESDAY, _('Wednesday'), 'orange'),
        (THURSDAY, _('Thursday'), 'purple'),
        (FRIDAY, _('Friday'), 'red'),
        (SATURDAY, _('Saturday'), 'yellow'),
        (SUNDAY, _('Sunday'), 'gray'),
    ]

class BackupJobSyntheticFullWeekChoices(ChoiceSet):
    key = 'BackupJob.synthetic_full_week'

    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    LAST = 'last'

    CHOICES = [
        (FIRST, _('First'), 'green'),
        (SECOND, _('Second'), 'blue'),
        (THIRD, _('Third'), 'orange'),
        (FOURTH, _('Fourth'), 'purple'),
        (LAST, _('Last'), 'red'),
    ]


class BackupJobSyntheticFullMonthChoices(ChoiceSet):
    key = 'BackupJob.synthetic_full_month'

    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'

    CHOICES = [
        (JANUARY, _('January')),
        (FEBRUARY, _('February')),
        (MARCH, _('March')),
        (APRIL, _('April')),
        (MAY, _('May')),
        (JUNE, _('June')),
        (JULY, _('July')),
        (AUGUST, _('August')),
        (SEPTEMBER, _('September')),
        (OCTOBER, _('October')),
        (NOVEMBER, _('November')),
        (DECEMBER, _('December')),
    ]


class BackupJobFullBackupScheduleKindChoices(ChoiceSet):
    key = 'BackupJob.full_backup_schedule_kind'

    DAILY = 'daily'
    MONTHLY = 'monthly'

    CHOICES = [
        (DAILY, _('Daily')),
        (MONTHLY, _('Monthly')),
    ]


class BackupJobFullBackupDaysChoices(ChoiceSet):
    key = 'BackupJob.full_backup_days'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday'), 'green'),
        (TUESDAY, _('Tuesday'), 'blue'),
        (WEDNESDAY, _('Wednesday'), 'orange'),
        (THURSDAY, _('Thursday'), 'purple'),
        (FRIDAY, _('Friday'), 'red'),
        (SATURDAY, _('Saturday'), 'yellow'),
        (SUNDAY, _('Sunday'), 'gray'),
    ]


class BackupJobFullBackupWeekChoices(ChoiceSet):
    key = 'BackupJob.full_backup_week'

    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    LAST = 'last'

    CHOICES = [
        (FIRST, _('First'), 'green'),
        (SECOND, _('Second'), 'blue'),
        (THIRD, _('Third'), 'orange'),
        (FOURTH, _('Fourth'), 'purple'),
        (LAST, _('Last'), 'red'),
    ]


class BackupJobFullBackupMonthChoices(ChoiceSet):
    key = 'BackupJob.full_backup_month'

    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'

    CHOICES = [
        (JANUARY, _('January')),
        (FEBRUARY, _('February')),
        (MARCH, _('March')),
        (APRIL, _('April')),
        (MAY, _('May')),
        (JUNE, _('June')),
        (JULY, _('July')),
        (AUGUST, _('August')),
        (SEPTEMBER, _('September')),
        (OCTOBER, _('October')),
        (NOVEMBER, _('November')),
        (DECEMBER, _('December')),
    ]


class BackupJobGFSEnableChoices(ChoiceSet):
    key = 'BackupJob.gfs_enable'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupJobGFSWeeklyEnabledChoices(ChoiceSet):
    key = 'BackupJob.gfs_weekly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]


class BackupJobGFSWeeklyDayChoices(ChoiceSet):
    key = 'BackupJob.gfs_weekly_day'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
        (SUNDAY, _('Sunday')),
    ]


class BackupJobGFSMonthlyEnabledChoices(ChoiceSet):
    key = 'BackupJob.gfs_monthly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]


class BackupJobGFSWeekOfMonthChoices(ChoiceSet):
    key = 'BackupJob.gfs_week_of_month'

    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    LAST = 'last'

    CHOICES = [
        (FIRST, _('First')),
        (SECOND, _('Second')),
        (THIRD, _('Third')),
        (FOURTH, _('Fourth')),
        (LAST, _('Last')),
    ]


class BackupJobGFSYearlyEnabledChoices(ChoiceSet):
    key = 'BackupJob.gfs_yearly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]


class BackupJobGFSMonthOfYearChoices(ChoiceSet):
    key = 'BackupJob.gfs_month_of_year'

    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'

    CHOICES = [
        (JANUARY, _('January')),
        (FEBRUARY, _('February')),
        (MARCH, _('March')),
        (APRIL, _('April')),
        (MAY, _('May')),
        (JUNE, _('June')),
        (JULY, _('July')),
        (AUGUST, _('August')),
        (SEPTEMBER, _('September')),
        (OCTOBER, _('October')),
        (NOVEMBER, _('November')),
        (DECEMBER, _('December')),
    ]


#
# BackupJob Schedule Options
#

class BackupJobRunAutomaticallyChoices(ChoiceSet):
    key = 'BackupJob.run_automatically'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]

#--- Daily Schedule Options ---#

class BackupJobScheduleDailyEnabledChoices(ChoiceSet):
    key = 'BackupJob.schedule_daily_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupJobScheduleDailyKindChoices(ChoiceSet):
    key = 'BackupJob.schedule_daily_kind'

    EVERYDAY = 'everyday'
    WEEKDAYS = 'weekdays'
    SELECTED_DAYS = 'selected days'

    CHOICES = [
        (EVERYDAY, _('Everyday')),
        (WEEKDAYS, _('Weekdays')),
        (SELECTED_DAYS, _('Selected Days')),
    ]


class BackupJobScheduleDaysChoices(ChoiceSet):
    key = 'BackupJob.schedule_days'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday'), 'green'),
        (TUESDAY, _('Tuesday'), 'blue'),
        (WEDNESDAY, _('Wednesday'), 'orange'),
        (THURSDAY, _('Thursday'), 'purple'),
        (FRIDAY, _('Friday'), 'red'),
        (SATURDAY, _('Saturday'), 'yellow'),
        (SUNDAY, _('Sunday'), 'gray'),
    ]

#--- Monthly Schedule Options ---#

class BackupJobScheduleMonthlyEnabledChoices(ChoiceSet):
    key = 'BackupJob.schedule_monthly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]

class BackupJobScheduleMonthlyDayNumberInMonthChoices(ChoiceSet):
    key = 'BackupJob.schedule_monthly_day_number_in_month'

    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    LAST = 'last'
    THIS_DAY = 'this day'

    CHOICES = [
        (FIRST, _('First'), 'green'),
        (SECOND, _('Second'), 'blue'),
        (THIRD, _('Third'), 'orange'),
        (FOURTH, _('Fourth'), 'purple'),
        (LAST, _('Last'), 'red'),
        (THIS_DAY, _('This Day'), 'gray'),
    ]

class BackupJobScheduleMonthlyDayOfWeekChoices(ChoiceSet):
    key = 'BackupJob.schedule_monthly_day_of_week'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday'), 'green'),
        (TUESDAY, _('Tuesday'), 'blue'),
        (WEDNESDAY, _('Wednesday'), 'orange'),
        (THURSDAY, _('Thursday'), 'purple'),
        (FRIDAY, _('Friday'), 'red'),
        (SATURDAY, _('Saturday'), 'yellow'),
        (SUNDAY, _('Sunday'), 'gray'),
    ]

class BackupJobScheduleDayOfMonthChoices(ChoiceSet):
    key = 'BackupJob.schedule_day_of_month'

    LAST = 'last'

    CHOICES = [
        (LAST, _('Last'), 'yellow'),
        *[(str(i), str(i)) for i in range(1, 32)],  # Choices from 1 to 31
    ]


class BackupJobScheduleMonthChoices(ChoiceSet):
    key = 'BackupJob.schedule_month'

    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'

    CHOICES = [
        (JANUARY, _('January')),
        (FEBRUARY, _('February')),
        (MARCH, _('March')),
        (APRIL, _('April')),
        (MAY, _('May')),
        (JUNE, _('June')),
        (JULY, _('July')),
        (AUGUST, _('August')),
        (SEPTEMBER, _('September')),
        (OCTOBER, _('October')),
        (NOVEMBER, _('November')),
        (DECEMBER, _('December')),
    ]


class BackupJobPeriodicallyEnabledChoices(ChoiceSet):
    key = 'BackupJob.periodically_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupJobPeriodicallyUnitChoices(ChoiceSet):
    key = 'BackupJob.periodically_unit'

    MINUTES = 'minutes'
    HOURS = 'hours'
    CONTINUOUSLY = 'continuously'

    CHOICES = [
        (MINUTES, _('Minutes')),
        (HOURS, _('Hours')),
        (CONTINUOUSLY, _('Continuously')),
    ]


class BackupJobAfterJobEnabledChoices(ChoiceSet):
    key = 'BackupJob.after_job_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupJobScheduleHourChoices(ChoiceSet):
    key = 'BackupJob.schedule_hour'

    CHOICES = [(str(h), f'{h:02d}:00') for h in range(24)]


#
# BackupCopyJob
#


class BackupCopyJobStatusChoices(ChoiceSet):
    key = 'BackupCopyJob.status'

    STATUS_ENABLED = 'enabled'
    STATUS_DISABLED = 'disabled'
    STATUS_ORPHANED = 'orphaned'

    CHOICES = [
        (STATUS_ENABLED, _('Enabled'), 'green'),
        (STATUS_DISABLED, _('Disabled'), 'blue'),
        (STATUS_ORPHANED, _('Orphaned'), 'yellow'),
    ]


class BackupCopyJobResultChoices(ChoiceSet):
    key = 'BackupCopyJob.last_backup_result'

    SUCCESS = 'success'
    WARNING = 'warning'
    FAILED = 'failed'

    CHOICES = [
        (SUCCESS, _('Success'), 'green'),
        (WARNING, _('Warning'), 'yellow'),
        (FAILED, _('Failed'), 'red'),
    ]


class BackupCopyJobModeChoices(ChoiceSet):
    key = 'BackupCopyJob.mode'

    IMMEDIATE = 'immediate'
    PERIODIC = 'periodic'

    CHOICES = [
        (IMMEDIATE, _('Immediate (mirroring)')),
        (PERIODIC, _('Periodic (pruning)')),
    ]


class BackupCopyJobEnableDeduplicationChoices(ChoiceSet):
    key = 'BackupCopyJob.enable_deduplication'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobStorageEncryptionEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.storage_encryption_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobEnableDeletedVmDataRetentionChoices(ChoiceSet):
    key = 'BackupCopyJob.enable_deleted_vm_data_retention'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]


class BackupCopyJobGFSEnableChoices(ChoiceSet):
    key = 'BackupCopyJob.gfs_enable'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobGFSWeeklyEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.gfs_weekly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]


class BackupCopyJobGFSWeeklyDayChoices(ChoiceSet):
    key = 'BackupCopyJob.gfs_weekly_day'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday')),
        (TUESDAY, _('Tuesday')),
        (WEDNESDAY, _('Wednesday')),
        (THURSDAY, _('Thursday')),
        (FRIDAY, _('Friday')),
        (SATURDAY, _('Saturday')),
        (SUNDAY, _('Sunday')),
    ]


class BackupCopyJobGFSMonthlyEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.gfs_monthly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]


class BackupCopyJobGFSWeekOfMonthChoices(ChoiceSet):
    key = 'BackupCopyJob.gfs_week_of_month'

    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    LAST = 'last'

    CHOICES = [
        (FIRST, _('First')),
        (SECOND, _('Second')),
        (THIRD, _('Third')),
        (FOURTH, _('Fourth')),
        (LAST, _('Last')),
    ]


class BackupCopyJobGFSYearlyEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.gfs_yearly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'blue'),
    ]


class BackupCopyJobGFSMonthOfYearChoices(ChoiceSet):
    key = 'BackupCopyJob.gfs_month_of_year'

    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'

    CHOICES = [
        (JANUARY, _('January')),
        (FEBRUARY, _('February')),
        (MARCH, _('March')),
        (APRIL, _('April')),
        (MAY, _('May')),
        (JUNE, _('June')),
        (JULY, _('July')),
        (AUGUST, _('August')),
        (SEPTEMBER, _('September')),
        (OCTOBER, _('October')),
        (NOVEMBER, _('November')),
        (DECEMBER, _('December')),
    ]


class BackupCopyJobDataTransferModeChoices(ChoiceSet):
    key = 'BackupCopyJob.data_transfer_mode'

    DIRECT = 'direct'
    THROUGH_WAN_ACCELERATORS = 'through_wan_accelerators'

    CHOICES = [
        (DIRECT, _('Direct')),
        (THROUGH_WAN_ACCELERATORS, _('Through WAN Accelerators')),
    ]


class BackupCopyJobTransactionLogCopyEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.transaction_log_copy_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobTransferWindowChoices(ChoiceSet):
    key = 'BackupCopyJob.transfer_window'

    CONTINUOUSLY = 'continuously'
    BY_SCHEMA = 'by_schema'

    CHOICES = [
        (CONTINUOUSLY, _('Continuously')),
        (BY_SCHEMA, _('By Schema')),
    ]


class BackupCopyJobScheduleHourChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_hour'

    CHOICES = [(str(h), f'{h:02d}:00') for h in range(24)]


class BackupCopyJobRunAutomaticallyChoices(ChoiceSet):
    key = 'BackupCopyJob.run_automatically'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobScheduleDailyEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_daily_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobScheduleDailyKindChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_daily_kind'

    EVERYDAY = 'everyday'
    WEEKDAYS = 'weekdays'
    SELECTED_DAYS = 'selected days'

    CHOICES = [
        (EVERYDAY, _('Everyday')),
        (WEEKDAYS, _('Weekdays')),
        (SELECTED_DAYS, _('Selected Days')),
    ]


class BackupCopyJobScheduleDaysChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_days'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday'), 'green'),
        (TUESDAY, _('Tuesday'), 'blue'),
        (WEDNESDAY, _('Wednesday'), 'orange'),
        (THURSDAY, _('Thursday'), 'purple'),
        (FRIDAY, _('Friday'), 'red'),
        (SATURDAY, _('Saturday'), 'yellow'),
        (SUNDAY, _('Sunday'), 'gray'),
    ]


class BackupCopyJobScheduleMonthlyEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_monthly_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobScheduleMonthlyDayNumberInMonthChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_monthly_day_number_in_month'

    FIRST = 'first'
    SECOND = 'second'
    THIRD = 'third'
    FOURTH = 'fourth'
    LAST = 'last'
    THIS_DAY = 'this day'

    CHOICES = [
        (FIRST, _('First'), 'green'),
        (SECOND, _('Second'), 'blue'),
        (THIRD, _('Third'), 'orange'),
        (FOURTH, _('Fourth'), 'purple'),
        (LAST, _('Last'), 'red'),
        (THIS_DAY, _('This Day'), 'gray'),
    ]


class BackupCopyJobScheduleMonthlyDayOfWeekChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_monthly_day_of_week'

    MONDAY = 'monday'
    TUESDAY = 'tuesday'
    WEDNESDAY = 'wednesday'
    THURSDAY = 'thursday'
    FRIDAY = 'friday'
    SATURDAY = 'saturday'
    SUNDAY = 'sunday'

    CHOICES = [
        (MONDAY, _('Monday'), 'green'),
        (TUESDAY, _('Tuesday'), 'blue'),
        (WEDNESDAY, _('Wednesday'), 'orange'),
        (THURSDAY, _('Thursday'), 'purple'),
        (FRIDAY, _('Friday'), 'red'),
        (SATURDAY, _('Saturday'), 'yellow'),
        (SUNDAY, _('Sunday'), 'gray'),
    ]


class BackupCopyJobScheduleDayOfMonthChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_day_of_month'

    LAST = 'last'

    CHOICES = [
        (LAST, _('Last'), 'yellow'),
        *[(str(i), str(i)) for i in range(1, 32)],  # Choices from 1 to 31
    ]


class BackupCopyJobScheduleMonthChoices(ChoiceSet):
    key = 'BackupCopyJob.schedule_month'

    JANUARY = 'january'
    FEBRUARY = 'february'
    MARCH = 'march'
    APRIL = 'april'
    MAY = 'may'
    JUNE = 'june'
    JULY = 'july'
    AUGUST = 'august'
    SEPTEMBER = 'september'
    OCTOBER = 'october'
    NOVEMBER = 'november'
    DECEMBER = 'december'

    CHOICES = [
        (JANUARY, _('January')),
        (FEBRUARY, _('February')),
        (MARCH, _('March')),
        (APRIL, _('April')),
        (MAY, _('May')),
        (JUNE, _('June')),
        (JULY, _('July')),
        (AUGUST, _('August')),
        (SEPTEMBER, _('September')),
        (OCTOBER, _('October')),
        (NOVEMBER, _('November')),
        (DECEMBER, _('December')),
    ]


class BackupCopyJobPeriodicallyEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.periodically_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]


class BackupCopyJobPeriodicallyUnitChoices(ChoiceSet):
    key = 'BackupCopyJob.periodically_unit'

    MINUTES = 'minutes'
    HOURS = 'hours'
    CONTINUOUSLY = 'continuously'

    CHOICES = [
        (MINUTES, _('Minutes')),
        (HOURS, _('Hours')),
        (CONTINUOUSLY, _('Continuously')),
    ]


class BackupCopyJobAfterJobEnabledChoices(ChoiceSet):
    key = 'BackupCopyJob.after_job_enabled'

    TRUE = 'true'
    FALSE = 'false'

    CHOICES = [
        (TRUE, _('Enabled'), 'green'),
        (FALSE, _('Disabled'), 'red'),
    ]
