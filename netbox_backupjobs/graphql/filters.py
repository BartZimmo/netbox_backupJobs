import strawberry
import strawberry_django

from typing import TYPE_CHECKING, Annotated

from strawberry import ID
from strawberry_django import FilterLookup

from netbox.graphql.filters import NetBoxModelFilter

from netbox_backupjobs.models import BackupJob

# if TYPE_CHECKING:
#     from ipam.graphql.filters import PrefixFilter
#     from netbox.graphql.filter_lookups import IntegerArrayLookup, IntegerLookup

#     from .enums import BackupJobStatusEnum

@strawberry_django.filter_type(BackupJob, lookups=True)
class BackupJobFilter(NetBoxModelFilter):
    pass