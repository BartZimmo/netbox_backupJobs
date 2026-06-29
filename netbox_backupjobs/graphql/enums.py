import strawberry

from netbox_backupjobs.choices import BackupJobStatusChoices


BackupJobStatusEnum = strawberry.enum(BackupJobStatusChoices.as_enum())