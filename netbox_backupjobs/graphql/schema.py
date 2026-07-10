import strawberry
import strawberry_django

from .types import BackupJobType, BackupCopyJobType

@strawberry.type(name='Query')
class NetBoxBackupJobQuery:
    backup_job: BackupJobType = strawberry_django.field()
    backup_job_list: list[BackupJobType] = strawberry_django.field()
    backup_copy_job: BackupCopyJobType = strawberry_django.field()
    backup_copy_job_list: list[BackupCopyJobType] = strawberry_django.field()