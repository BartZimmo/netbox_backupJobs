from typing import TYPE_CHECKING, Annotated

import strawberry
import strawberry_django
from netbox.graphql.types import NetBoxObjectType

from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.graphql.filters import BackupJobFilter, BackupCopyJobFilter

@strawberry_django.type(BackupJob, fields='__all__', filters=BackupJobFilter)
class BackupJobType(NetBoxObjectType):
    pass

@strawberry_django.type(BackupCopyJob, fields='__all__', filters=BackupCopyJobFilter)
class BackupCopyJobType(NetBoxObjectType):
    pass