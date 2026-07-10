from django.core.exceptions import ValidationError
from django.test import TestCase

from netbox_backupjobs.models import BackupJob, BackupCopyJob
from netbox_backupjobs.models.backupjobs import default_schedule_all_hours


class TestBackupJobModel(TestCase):
    def test_minimal_job_saves_without_errors(self):
        job = BackupJob(name='Test Job')
        job.full_clean()
        job.save()
        self.assertEqual(job.pk is not None, True)

    def test_default_schedule_all_hours(self):
        hours = default_schedule_all_hours()
        self.assertEqual(hours, [str(h) for h in range(24)])
        self.assertEqual(len(hours), 24)

    def test_schedule_periodically_hour_offset_defaults_to_zero(self):
        job = BackupJob.objects.create(name='Offset Default Job')
        self.assertEqual(job.schedule_periodically_hour_offset_in_min, 0)

    def test_day_schema_defaults_to_all_hours(self):
        job = BackupJob.objects.create(name='Default Schema Job')
        self.assertEqual(
            job.get_schedule_periodically_monday_schema_display(),
            'All Hours',
        )

    def test_day_schema_empty_shows_no_hours(self):
        job = BackupJob.objects.create(
            name='No Hours Job',
            schedule_periodically_monday_schema=[],
        )
        self.assertEqual(
            job.get_schedule_periodically_monday_schema_display(),
            'No Hours',
        )

    def test_day_schema_merges_consecutive_hours_into_range(self):
        job = BackupJob.objects.create(
            name='Range Job',
            schedule_periodically_monday_schema=['8', '9', '10'],
        )
        self.assertEqual(
            job.get_schedule_periodically_monday_schema_display(),
            '08:00-11:00',
        )

    def test_day_schema_keeps_non_consecutive_hours_separate(self):
        job = BackupJob.objects.create(
            name='Split Job',
            schedule_periodically_monday_schema=['8', '9', '14'],
        )
        self.assertEqual(
            job.get_schedule_periodically_monday_schema_display(),
            '08:00-10:00, 14:00-15:00',
        )

    def test_day_schema_applies_hour_offset(self):
        job = BackupJob.objects.create(
            name='Offset Job',
            schedule_periodically_hour_offset_in_min=15,
            schedule_periodically_monday_schema=['10', '11'],
        )
        self.assertEqual(
            job.get_schedule_periodically_monday_schema_display(),
            '10:15-12:15',
        )


class TestBackupCopyJobModel(TestCase):
    def test_minimal_job_saves_without_errors(self):
        job = BackupCopyJob(name='Test Copy Job')
        job.full_clean()
        job.save()
        self.assertEqual(job.pk is not None, True)

    def test_status_defaults_to_enabled(self):
        job = BackupCopyJob.objects.create(name='Default Status Job')
        self.assertEqual(job.status, 'enabled')

    def test_retain_days_to_keep_rejects_zero(self):
        job = BackupCopyJob(name='Invalid Retain Job', retain_days_to_keep=0)
        with self.assertRaises(ValidationError):
            job.full_clean()
