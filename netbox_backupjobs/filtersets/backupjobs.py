import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from utilities.filters import MultiValueCharFilter
from utilities.filtersets import register_filterset

from netbox.filtersets import NetBoxModelFilterSet

from netbox_backupjobs.choices import (
    BackupJobPlatformChoices,
    BackupJobStatusChoices,
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
    Algorithm = django_filters.MultipleChoiceFilter(
        choices=BackupJobAlgorithmChoices,
        label=_('Algorithm'),
    )
    EnableDeduplication = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableDeduplicationChoices,
        label=_('Deduplication'),
    )
    StorageEncryptionEnabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobStorageEncryptionEnabledChoices,
        label=_('Storage Encryption'),
    )
    EnableDeletedVmDataRetention = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableDeletedVmDataRetentionChoices,
        label=_('Deleted VM Retention'),
    )

    # Synthetic full backup settings
    TransformFullToSyntethic = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableSyntheticFullForIncrementalChoices,
        label=_('Synthetic Full (Incremental)'),
    )
    TransformToSyntheticFull = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableSyntheticFullForReverseIncrementalChoices,
        label=_('Synthetic Full (Reverse Incr.)'),
    )
    TransformToSyntethicKind = django_filters.MultipleChoiceFilter(
        choices=BackupJobSyntheticFullChoices,
        label=_('Synthetic Full Kind'),
    )

    # Active full backup settings
    EnableFullBackup = django_filters.MultipleChoiceFilter(
        choices=BackupJobEnableFullBackupChoices,
        label=_('Active Full Backup'),
    )
    FullBackupScheduleKind = django_filters.MultipleChoiceFilter(
        choices=BackupJobFullBackupScheduleKindChoices,
        label=_('Full Backup Kind'),
    )

    # GFS retention settings
    EnableGFS = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSEnableChoices,
        label=_('GFS Enabled'),
    )
    WeeklyEnabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSWeeklyEnabledChoices,
        label=_('GFS Weekly'),
    )
    MonthlyEnabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSMonthlyEnabledChoices,
        label=_('GFS Monthly'),
    )
    YearlyEnabled = django_filters.MultipleChoiceFilter(
        choices=BackupJobGFSYearlyEnabledChoices,
        label=_('GFS Yearly'),
    )

    ## In the class Meta you can only add field names that are actual fields of the model.
    class Meta:
        model = BackupJob
        fields = {
            'id', 'name', 'target', 'jobtype', 'status', 'platform', 'job_creation_time', 'description', 'backup_server_name', 'backup_server_ip', 'virtual_machines', 'comments',
            'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled',
            'EnableDeletedVmDataRetention',
            'TransformFullToSyntethic', 'TransformToSyntheticFull', 'TransformToSyntethicKind',
            'EnableFullBackup', 'FullBackupScheduleKind',
            'EnableGFS', 'WeeklyEnabled', 'MonthlyEnabled', 'YearlyEnabled',
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