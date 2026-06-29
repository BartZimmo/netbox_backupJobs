import django_filters
from django.db.models import Q
from django.utils.translation import gettext as _

from utilities.filters import MultiValueCharFilter
from utilities.filtersets import register_filterset

from netbox.filtersets import NetBoxModelFilterSet

from netbox_backupjobs.choices import BackupJobStatusChoices
from netbox_backupjobs.models import BackupJob

from virtualization.models import VirtualMachine

@register_filterset
class BackupJobFilterSet(NetBoxModelFilterSet):
    name = MultiValueCharFilter(
        lookup_expr='iexact',
    )
    status = django_filters.MultipleChoiceFilter(
        choices=BackupJobStatusChoices,
        label=_('Status'),
    )
    virtual_machine = django_filters.ModelMultipleChoiceFilter(
        field_name='virtual_machines',
        queryset=VirtualMachine.objects.all(),
        label="Virtual Machines",
        conjoined=False,
    )

    ## In the class Meta you can only add field names that are actual fields of the model.
    class Meta:
        model = BackupJob
        fields = {
            'id', 'name', 'status', 'description', 'virtual_machines', 'comments',
        }

    ### Criteria for the Quick search box.
    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value)
        ).distinct()