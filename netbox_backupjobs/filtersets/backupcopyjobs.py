import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from utilities.filters import MultiValueCharFilter
from utilities.filtersets import register_filterset

from netbox.filtersets import NetBoxModelFilterSet

from ipam.models import IPAddress

from netbox_backupjobs.choices import (
    BackupCopyJobStatusChoices,
    BackupCopyJobResultChoices,
    BackupCopyJobModeChoices,
    BackupCopyJobEnableDeduplicationChoices,
    BackupCopyJobStorageEncryptionEnabledChoices,
    BackupCopyJobEnableDeletedVmDataRetentionChoices,
    BackupCopyJobGFSEnableChoices,
    BackupCopyJobGFSWeeklyEnabledChoices,
    BackupCopyJobGFSMonthlyEnabledChoices,
    BackupCopyJobGFSYearlyEnabledChoices,
    BackupCopyJobDataTransferModeChoices,
    BackupCopyJobTransactionLogCopyEnabledChoices,
    BackupCopyJobTransferWindowChoices,
    BackupCopyJobRunAutomaticallyChoices,
    BackupCopyJobScheduleDailyEnabledChoices,
    BackupCopyJobScheduleDailyKindChoices,
    BackupCopyJobScheduleMonthlyEnabledChoices,
    BackupCopyJobScheduleMonthlyDayOfWeekChoices,
    BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
    BackupCopyJobScheduleDayOfMonthChoices,
    BackupCopyJobPeriodicallyEnabledChoices,
    BackupCopyJobPeriodicallyUnitChoices,
    BackupCopyJobAfterJobEnabledChoices,
)
from netbox_backupjobs.models import BackupJob, BackupCopyJob


@register_filterset
class BackupCopyJobFilterSet(NetBoxModelFilterSet):
    name = MultiValueCharFilter(
        lookup_expr='iexact',
    )
    target = MultiValueCharFilter(
        lookup_expr='icontains',
    )
    backup_server_name = MultiValueCharFilter(
        lookup_expr='icontains',
        label=_('Backup Server Name'),
    )
    backup_server_ip = django_filters.ModelMultipleChoiceFilter(
        queryset=IPAddress.objects.all(),
        label=_('Backup Server IP'),
    )
    jobtype = MultiValueCharFilter(
        lookup_expr='icontains',
        label=_('Job Type'),
    )
    status = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobStatusChoices,
        label=_('Status'),
    )
    mode = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobModeChoices,
        label=_('Copy Mode'),
    )
    data_transfer_mode = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobDataTransferModeChoices,
        label=_('Data Transfer Mode'),
    )
    job_creation_time = django_filters.DateTimeFromToRangeFilter(
        label=_('Job Creation Time'),
    )
    last_backup_result = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobResultChoices,
        label=_('Last Backup Result'),
    )
    backup_job = django_filters.ModelMultipleChoiceFilter(
        field_name='backup_jobs',
        queryset=BackupJob.objects.all(),
        label=_('Backup Jobs'),
        conjoined=False,
    )

    # Advanced settings
    enable_deduplication = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobEnableDeduplicationChoices,
        label=_('Deduplication'),
    )
    storage_encryption_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobStorageEncryptionEnabledChoices,
        label=_('Storage Encryption'),
    )
    transaction_log_copy_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobTransactionLogCopyEnabledChoices,
        label=_('Transaction Log Copy'),
    )
    enable_deleted_vm_data_retention = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobEnableDeletedVmDataRetentionChoices,
        label=_('Deleted VM Retention'),
    )

    # GFS retention settings
    enable_gfs = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobGFSEnableChoices,
        label=_('GFS Enabled'),
    )
    weekly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobGFSWeeklyEnabledChoices,
        label=_('GFS Weekly'),
    )
    monthly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobGFSMonthlyEnabledChoices,
        label=_('GFS Monthly'),
    )
    yearly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobGFSYearlyEnabledChoices,
        label=_('GFS Yearly'),
    )

    # Schedule options
    transfer_window = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobTransferWindowChoices,
        label=_('Transfer Window'),
    )
    run_automatically = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobRunAutomaticallyChoices,
        label=_('Run Automatically'),
    )
    schedule_daily_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobScheduleDailyEnabledChoices,
        label=_('Daily Enabled'),
    )
    schedule_daily_kind = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobScheduleDailyKindChoices,
        label=_('Daily Kind'),
    )
    schedule_monthly_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobScheduleMonthlyEnabledChoices,
        label=_('Monthly Enabled'),
    )
    schedule_monthly_day_of_week = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobScheduleMonthlyDayOfWeekChoices,
        label=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobScheduleMonthlyDayNumberInMonthChoices,
        label=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobScheduleDayOfMonthChoices,
        label=_('Monthly Day of Month'),
    )
    schedule_periodically_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobPeriodicallyEnabledChoices,
        label=_('Periodically Enabled'),
    )
    schedule_periodically_unit = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobPeriodicallyUnitChoices,
        label=_('Periodically Unit'),
    )
    after_job_enabled = django_filters.MultipleChoiceFilter(
        choices=BackupCopyJobAfterJobEnabledChoices,
        label=_('After Job Enabled'),
    )
    after_job_name = django_filters.ModelMultipleChoiceFilter(
        queryset=BackupCopyJob.objects.all(),
        label=_('After Job'),
    )

    ## In the class Meta you can only add field names that are actual fields of the model.
    class Meta:
        model = BackupCopyJob
        fields = {
            'id', 'name', 'target', 'jobtype', 'status', 'mode', 'data_transfer_mode', 'job_creation_time',
            'last_backup_result', 'description', 'backup_server_name', 'backup_server_ip', 'backup_jobs',
            'enable_deduplication', 'storage_encryption_enabled', 'transaction_log_copy_enabled',
            'enable_deleted_vm_data_retention',
            'enable_gfs', 'weekly_enabled', 'monthly_enabled', 'yearly_enabled',
            'transfer_window',
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
