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
    

    CHOICES = [
        (STATUS_ENABLED, _('Enabled'), 'green'),
        (STATUS_DISABLED, _('Disabled'), 'blue'),        
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
