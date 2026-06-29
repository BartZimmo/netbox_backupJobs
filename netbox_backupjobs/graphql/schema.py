import strawberry
import strawberry_django

from .types import BackupJobType

@strawberry.type(name='Query')
class NetBoxBackupJobQuery:
    backup_job: BackupJobType = strawberry_django.field()
    backup_job_list: list[BackupJobType] = strawberry_django.field()