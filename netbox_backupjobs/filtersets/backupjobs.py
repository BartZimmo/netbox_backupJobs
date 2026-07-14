import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from utilities.filters import MultiValueCharFilter
from utilities.filtersets import register_filterset

from netbox.filtersets import NetBoxModelFilterSet

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
    BackupJobScheduleMonthChoices,
    BackupJobScheduleHourChoices,
    BackupJobPeriodicallyEnabledChoices,
    BackupJobPeriodicallyUnitChoices,
    BackupJobAfterJobEnabledChoices,
    BackupJobScheduleDayOfMonthChoices,
    BackupJobScheduleMonthlyDayNumberInMonthChoices,
)
from netbox_backupjobs.models import BackupJob

from ipam.models import IPAddress
from virtualization.models import VirtualMachine

@register_filterset
class BackupJobFilterSet(NetBoxModelFilterSet):
    name = MultiValueCharFilter(
        lookup_expr='iexact',
    )
    target = MultiValueCharFilter(
        lookup_expr='icontains',
    )
    jobtype = MultiValueCharFilter(
        lookup_expr='icontains',
        label=_('Job Type'),
    )
    backup_server_name = MultiValueCharFilter(
        lookup_expr='icontains',
        label=_('Backup Server Name'),
    )
    backup_server_ip = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.all(),
        label=_('Backup Server IP'),
    )
    status = django_filters.MultipleChoiceFilter(
        choices=BackupJobStatusChoices,
        label=_('Status'),
    )
    platform = django_filters.MultipleChoiceFilter(
        choices=BackupJobPlatformChoices,
        label=_('Platform'),
    )
    job_creation_time = django_filters.DateTimeFromToRangeFilter(
        label=_('Job Creation Time'),
    )
    last_backup_end_time = django_filters.DateTimeFromToRangeFilter(
        label=_('Last Backup End Time'),
    )
    last_backup_result = django_filters.MultipleChoiceFilter(
        choices=BackupJobResultChoices,
        label=_('Last Backup Result'),
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        field_name='virtual_machines',
        queryset=VirtualMachine.objects.all(),
        label="Virtual Machines",
        conjoined=False,
    )
    has_virtual_machines = django_filters.BooleanFilter(
        method='_has_virtual_machines',
        label=_('Has virtual machines'),
    )
    has_powered_off_vms = django_filters.BooleanFilter(
        method='_has_powered_off_vms',
        label=_('Has powered off virtual machines'),
    )

    # Advanced settings
    algorithm = django_filters.MultipleChoiceFilter(
        choices=BackupJobAlgorithmChoices,
        label=_('Algorithm'),
    )
    enable_deduplication = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableDeduplicationChoices,
        label=_('Deduplication'),
    )
    storage_encryption_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobStorageEncryptionEnabledChoices,
        label=_('Storage Encryption'),
    )
    enable_deleted_vm_data_retention = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        label=_('Deleted VM Retention'),
    )

    # Synthetic full backup settings
    transform_full_to_synthetic = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        label=_('Synthetic Full (Incremental)'),
    )
    transform_to_synthetic_full = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        label=_('Synthetic Full (Reverse Incr.)'),
    )
    transform_to_synthetic_kind = django_filters.MultipleChoiceFilter(
        choices=BackupJobSyntheticFullChoices,
        label=_('Synthetic Full Kind'),
    )
    transform_to_synthetic_days = django_filters.MultipleChoiceFilter(
        choices=BackupJobSyntheticFullDaysChoices,
        method='filter_transform_to_synthetic_days',
        label=_('Synthetic Full Days of Week'),
    )
    synthetic_full_day_number_in_month = django_filters.MultipleChoiceFilter(
        choices=BackupJobSyntheticFullWeekChoices,
        label=_('Synthetic Full Week of Month'),
    )
    synthetic_full_day_of_week = django_filters.MultipleChoiceFilter(
        choices=BackupJobSyntheticFullDaysChoices,
        label=_('Synthetic Full Day of Week (Monthly)'),
    )
    transform_to_synthetic_monthly = django_filters.MultipleChoiceFilter(
        choices=BackupJobSyntheticFullMonthChoices,
        method='filter_transform_to_synthetic_monthly',
        label=_('Synthetic Full Months'),
    )

    # Active full backup settings
    enable_full_backup = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableFullBackupChoices,
        label=_('Active Full Backup'),
    )
    full_backup_schedule_kind = django_filters.MultipleChoiceFilter(
        choices=BackupJobFullBackupScheduleKindChoices,
        label=_('Full Backup Kind'),
    )
    full_backup_days = django_filters.MultipleChoiceFilter(
        choices=BackupJobFullBackupDaysChoices,
        method='filter_full_backup_days',
        label=_('Full Backup Days'),
    )
    full_backup_day_number_in_month = django_filters.MultipleChoiceFilter(
        choices=BackupJobFullBackupWeekChoices,
        label=_('Full Backup Week of Month'),
    )
    full_backup_day_of_week = django_filters.MultipleChoiceFilter(
        choices=BackupJobFullBackupDaysChoices,
        label=_('Full Backup Day of Week (Monthly)'),
    )
    full_backup_months = django_filters.MultipleChoiceFilter(
        choices=BackupJobFullBackupMonthChoices,
        method='filter_full_backup_months',
        label=_('Full Backup Months'),
    )

    # GFS retention settings
    enable_gfs = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSEnableChoices,
        label=_('GFS Enabled'),
    )
    weekly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSWeeklyEnabledChoices,
        label=_('GFS Weekly'),
    )
    monthly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSMonthlyEnabledChoices,
        label=_('GFS Monthly'),
    )
    yearly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSYearlyEnabledChoices,
        label=_('GFS Yearly'),
    )
    weekly_keep_backups_on_day_of_week = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSWeeklyDayChoices,
        label=_('GFS Weekly Day'),
    )
    monthly_keep_backups_week_of_month = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSWeekOfMonthChoices,
        label=_('GFS Monthly Week'),
    )
    yearly_keep_backups_on_month_of_year = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSMonthOfYearChoices,
        label=_('GFS Yearly Month'),
    )

    # Schedule options
    run_automatically = django_filters.MultipleChoiceFilter(
        choices=BackupJobRunAutomaticallyChoices,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleDailyEnabledChoices,
        label=_('Daily Enabled'),
    )
    schedule_daily_kind = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleDailyKindChoices,
        label=_('Daily Kind'),
    )
    schedule_daily_days = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleDaysChoices,
        method='filter_schedule_daily_days',
        label=_('Daily Days'),
    )
    schedule_monthly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleMonthlyEnabledChoices,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_day_of_week = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleMonthlyDayOfWeekChoices,
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleMonthlyDayNumberInMonthChoices,
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleDayOfMonthChoices,
        label=_('Monthly Day of Month'),
    )
    schedule_monthly_months = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleMonthChoices,
        method='filter_schedule_monthly_months',
        label=_('Monthly Months'),
    )
    schedule_periodically_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobPeriodicallyEnabledChoices,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_unit = django_filters.MultipleChoiceFilter(
        choices=BackupJobPeriodicallyUnitChoices,
        label=_('Periodically Unit'),
    )
    schedule_periodically_monday_schema = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleHourChoices,
        method='filter_schedule_periodically_monday_schema',
        label=_('Monday Schema Hours'),
    )
    schedule_periodically_monday_between = django_filters.TimeRangeFilter(
        method='filter_schedule_periodically_monday_between',
        label=_('Monday Schema Between'),
    )
    schedule_periodically_tuesday_schema = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleHourChoices,
        method='filter_schedule_periodically_tuesday_schema',
        label=_('Tuesday Schema Hours'),
    )
    schedule_periodically_tuesday_between = django_filters.TimeRangeFilter(
        method='filter_schedule_periodically_tuesday_between',
        label=_('Tuesday Schema Between'),
    )
    schedule_periodically_wednesday_schema = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleHourChoices,
        method='filter_schedule_periodically_wednesday_schema',
        label=_('Wednesday Schema Hours'),
    )
    schedule_periodically_wednesday_between = django_filters.TimeRangeFilter(
        method='filter_schedule_periodically_wednesday_between',
        label=_('Wednesday Schema Between'),
    )
    schedule_periodically_thursday_schema = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleHourChoices,
        method='filter_schedule_periodically_thursday_schema',
        label=_('Thursday Schema Hours'),
    )
    schedule_periodically_thursday_between = django_filters.TimeRangeFilter(
        method='filter_schedule_periodically_thursday_between',
        label=_('Thursday Schema Between'),
    )
    schedule_periodically_friday_schema = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleHourChoices,
        method='filter_schedule_periodically_friday_schema',
        label=_('Friday Schema Hours'),
    )
    schedule_periodically_friday_between = django_filters.TimeRangeFilter(
        method='filter_schedule_periodically_friday_between',
        label=_('Friday Schema Between'),
    )
    schedule_periodically_saturday_schema = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleHourChoices,
        method='filter_schedule_periodically_saturday_schema',
        label=_('Saturday Schema Hours'),
    )
    schedule_periodically_saturday_between = django_filters.TimeRangeFilter(
        method='filter_schedule_periodically_saturday_between',
        label=_('Saturday Schema Between'),
    )
    schedule_periodically_sunday_schema = django_filters.MultipleChoiceFilter(
        choices=BackupJobScheduleHourChoices,
        method='filter_schedule_periodically_sunday_schema',
        label=_('Sunday Schema Hours'),
    )
    schedule_periodically_sunday_between = django_filters.TimeRangeFilter(
        method='filter_schedule_periodically_sunday_between',
        label=_('Sunday Schema Between'),
    )

    # After job
    after_job_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobAfterJobEnabledChoices,
        label=_('After Job Enabled'),
    )
    after_job_name = django_filters.ModelMultipleChoiceFilter(
        queryset=BackupJob.objects.all(),
        label=_('After Job'),
    )

    ## In the class Meta you can only add field names that are actual fields of the model.
    class Meta:
        model = BackupJob
        fields = {
            'id', 'name', 'target', 'jobtype', 'status', 'platform', 'job_creation_time', 'last_backup_end_time', 'last_backup_result', 'description', 'backup_server_name', 'backup_server_ip', 'virtual_machines', 'comments',
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled',
            'enable_deleted_vm_data_retention',
            'transform_full_to_synthetic', 'transform_to_synthetic_full', 'transform_to_synthetic_kind',
            'transform_to_synthetic_days', 'synthetic_full_day_number_in_month', 'synthetic_full_day_of_week',
            'transform_to_synthetic_monthly',
            'enable_full_backup', 'full_backup_schedule_kind',
            'full_backup_days', 'full_backup_day_number_in_month', 'full_backup_day_of_week', 'full_backup_months',
            'enable_gfs', 'weekly_enabled', 'monthly_enabled', 'yearly_enabled',
            'weekly_keep_backups_on_day_of_week', 'monthly_keep_backups_week_of_month',
            'yearly_keep_backups_on_month_of_year',
            'run_automatically',
            'schedule_daily_enabled', 'schedule_daily_time', 'schedule_daily_kind', 'schedule_daily_days',
            'schedule_monthly_enabled', 'schedule_monthly_time', 'schedule_monthly_day_of_week',
            'schedule_monthly_day_number_in_month', 'schedule_monthly_day_of_month', 'schedule_monthly_months',
            'schedule_periodically_enabled', 'schedule_periodically_every', 'schedule_periodically_unit',
            'schedule_periodically_monday_schema', 'schedule_periodically_tuesday_schema',
            'schedule_periodically_wednesday_schema', 'schedule_periodically_thursday_schema',
            'schedule_periodically_friday_schema', 'schedule_periodically_saturday_schema',
            'schedule_periodically_sunday_schema',
            'after_job_enabled', 'after_job_name',
        }

    ### Criteria for the Quick search box.
    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value)
        ).distinct()

    def _has_virtual_machines(self, queryset, name, value):
        if value:
            return queryset.exclude(virtual_machines__isnull=True).distinct()
        return queryset.filter(virtual_machines__isnull=True)

    def _has_powered_off_vms(self, queryset, name, value):
        if value:
            return queryset.filter(virtual_machines__status='offline').distinct()
        return queryset.exclude(virtual_machines__status='offline').distinct()

    def filter_full_backup_days(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(full_backup_days__overlap=list(value)).distinct()

    def filter_full_backup_months(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(full_backup_months__overlap=list(value)).distinct()

    def filter_transform_to_synthetic_days(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(transform_to_synthetic_days__overlap=list(value)).distinct()

    def filter_transform_to_synthetic_monthly(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(transform_to_synthetic_monthly__overlap=list(value)).distinct()

    def filter_schedule_daily_days(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_daily_days__overlap=list(value)).distinct()

    def filter_schedule_monthly_months(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_monthly_months__overlap=list(value)).distinct()

    def filter_schedule_periodically_monday_schema(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_periodically_monday_schema__overlap=list(value)).distinct()

    def filter_schedule_periodically_monday_between(self, queryset, name, value):
        if not value or (value.start is None and value.stop is None):
            return queryset
        start_hour = value.start.hour if value.start else 0
        end_hour = value.stop.hour if value.stop else 23
        if value.stop and value.stop.minute:
            end_hour += 1
        end_hour = min(end_hour, 24)
        if end_hour <= start_hour:
            return queryset.none()
        hours = [str(h) for h in range(start_hour, end_hour)]
        return queryset.filter(schedule_periodically_monday_schema__overlap=hours).distinct()

    def filter_schedule_periodically_tuesday_schema(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_periodically_tuesday_schema__overlap=list(value)).distinct()

    def filter_schedule_periodically_tuesday_between(self, queryset, name, value):
        if not value or (value.start is None and value.stop is None):
            return queryset
        start_hour = value.start.hour if value.start else 0
        end_hour = value.stop.hour if value.stop else 23
        if value.stop and value.stop.minute:
            end_hour += 1
        end_hour = min(end_hour, 24)
        if end_hour <= start_hour:
            return queryset.none()
        hours = [str(h) for h in range(start_hour, end_hour)]
        return queryset.filter(schedule_periodically_tuesday_schema__overlap=hours).distinct()

    def filter_schedule_periodically_wednesday_schema(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_periodically_wednesday_schema__overlap=list(value)).distinct()

    def filter_schedule_periodically_wednesday_between(self, queryset, name, value):
        if not value or (value.start is None and value.stop is None):
            return queryset
        start_hour = value.start.hour if value.start else 0
        end_hour = value.stop.hour if value.stop else 23
        if value.stop and value.stop.minute:
            end_hour += 1
        end_hour = min(end_hour, 24)
        if end_hour <= start_hour:
            return queryset.none()
        hours = [str(h) for h in range(start_hour, end_hour)]
        return queryset.filter(schedule_periodically_wednesday_schema__overlap=hours).distinct()

    def filter_schedule_periodically_thursday_schema(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_periodically_thursday_schema__overlap=list(value)).distinct()

    def filter_schedule_periodically_thursday_between(self, queryset, name, value):
        if not value or (value.start is None and value.stop is None):
            return queryset
        start_hour = value.start.hour if value.start else 0
        end_hour = value.stop.hour if value.stop else 23
        if value.stop and value.stop.minute:
            end_hour += 1
        end_hour = min(end_hour, 24)
        if end_hour <= start_hour:
            return queryset.none()
        hours = [str(h) for h in range(start_hour, end_hour)]
        return queryset.filter(schedule_periodically_thursday_schema__overlap=hours).distinct()

    def filter_schedule_periodically_friday_schema(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_periodically_friday_schema__overlap=list(value)).distinct()

    def filter_schedule_periodically_friday_between(self, queryset, name, value):
        if not value or (value.start is None and value.stop is None):
            return queryset
        start_hour = value.start.hour if value.start else 0
        end_hour = value.stop.hour if value.stop else 23
        if value.stop and value.stop.minute:
            end_hour += 1
        end_hour = min(end_hour, 24)
        if end_hour <= start_hour:
            return queryset.none()
        hours = [str(h) for h in range(start_hour, end_hour)]
        return queryset.filter(schedule_periodically_friday_schema__overlap=hours).distinct()

    def filter_schedule_periodically_saturday_schema(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_periodically_saturday_schema__overlap=list(value)).distinct()

    def filter_schedule_periodically_saturday_between(self, queryset, name, value):
        if not value or (value.start is None and value.stop is None):
            return queryset
        start_hour = value.start.hour if value.start else 0
        end_hour = value.stop.hour if value.stop else 23
        if value.stop and value.stop.minute:
            end_hour += 1
        end_hour = min(end_hour, 24)
        if end_hour <= start_hour:
            return queryset.none()
        hours = [str(h) for h in range(start_hour, end_hour)]
        return queryset.filter(schedule_periodically_saturday_schema__overlap=hours).distinct()

    def filter_schedule_periodically_sunday_schema(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(schedule_periodically_sunday_schema__overlap=list(value)).distinct()

    def filter_schedule_periodically_sunday_between(self, queryset, name, value):
        if not value or (value.start is None and value.stop is None):
            return queryset
        start_hour = value.start.hour if value.start else 0
        end_hour = value.stop.hour if value.stop else 23
        if value.stop and value.stop.minute:
            end_hour += 1
        end_hour = min(end_hour, 24)
        if end_hour <= start_hour:
            return queryset.none()
        hours = [str(h) for h in range(start_hour, end_hour)]
        return queryset.filter(schedule_periodically_sunday_schema__overlap=hours).distinct()
