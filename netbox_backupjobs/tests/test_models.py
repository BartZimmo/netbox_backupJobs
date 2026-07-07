from django.test import TestCase

from netbox_backupjobs.models import BackupJob
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
        self.assertEqual(job.SchedulePeriodicallyHourOffsetInMin, 0)

    def test_day_schema_defaults_to_all_hours(self):
        job = BackupJob.objects.create(name='Default Schema Job')
        self.assertEqual(
            job.get_SchedulePeriodicallyMondaySchema_display(),
            'All Hours',
        )

    def test_day_schema_empty_shows_no_hours(self):
        job = BackupJob.objects.create(
            name='No Hours Job',
            SchedulePeriodicallyMondaySchema=[],
        )
        self.assertEqual(
            job.get_SchedulePeriodicallyMondaySchema_display(),
            'No Hours',
        )

    def test_day_schema_merges_consecutive_hours_into_range(self):
        job = BackupJob.objects.create(
            name='Range Job',
            SchedulePeriodicallyMondaySchema=['8', '9', '10'],
        )
        self.assertEqual(
            job.get_SchedulePeriodicallyMondaySchema_display(),
            '08:00-11:00',
        )

    def test_day_schema_keeps_non_consecutive_hours_separate(self):
        job = BackupJob.objects.create(
            name='Split Job',
            SchedulePeriodicallyMondaySchema=['8', '9', '14'],
        )
        self.assertEqual(
            job.get_SchedulePeriodicallyMondaySchema_display(),
            '08:00-10:00, 14:00-15:00',
        )

    def test_day_schema_applies_hour_offset(self):
        job = BackupJob.objects.create(
            name='Offset Job',
            SchedulePeriodicallyHourOffsetInMin=15,
            SchedulePeriodicallyMondaySchema=['10', '11'],
        )
        self.assertEqual(
            job.get_SchedulePeriodicallyMondaySchema_display(),
            '10:15-12:15',
        )
