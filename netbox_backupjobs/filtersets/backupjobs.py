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
    BackupJobEnableFullBackupChoices,
    BackupJobFullBackupScheduleKindChoices,
    BackupJobGFSEnableChoices,
    BackupJobGFSWeeklyEnabledChoices,
    BackupJobGFSMonthlyEnabledChoices,
    BackupJobGFSYearlyEnabledChoices,
    BackupJobRunAutomaticallyChoices,
    BackupJobScheduleDailyEnabledChoices,
    BackupJobScheduleDailyKindChoices,
    BackupJobScheduleMonthlyEnabledChoices,
    BackupJobScheduleMonthlyDayOfWeekChoices,
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

    # Active full backup settings
    enable_full_backup = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableFullBackupChoices,
        label=_('Active Full Backup'),
    )
    full_backup_schedule_kind = django_filters.MultipleChoiceFilter(
        choices=BackupJobFullBackupScheduleKindChoices,
        label=_('Full Backup Kind'),
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
    schedule_periodically_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobPeriodicallyEnabledChoices,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_unit = django_filters.MultipleChoiceFilter(
        choices=BackupJobPeriodicallyUnitChoices,
        label=_('Periodically Unit'),
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
            'enable_full_backup', 'full_backup_schedule_kind',
            'enable_gfs', 'weekly_enabled', 'monthly_enabled', 'yearly_enabled',
            'run_automatically',
            'schedule_daily_enabled', 'schedule_daily_time', 'schedule_daily_kind',
            'schedule_monthly_enabled', 'schedule_monthly_time', 'schedule_monthly_day_of_week',
            'schedule_monthly_day_number_in_month', 'schedule_monthly_day_of_month',
            'schedule_periodically_enabled', 'schedule_periodically_every', 'schedule_periodically_unit',
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