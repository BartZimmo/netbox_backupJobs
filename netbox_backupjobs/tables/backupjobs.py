import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from utilities.tables import register_table_column
from virtualization.tables import VirtualMachineTable
from netbox_backupjobs.models import BackupJob

__all__ = (
    'BackupJobTable',
)


class BackupJobTable(NetBoxTable):
    """
    Table for displaying BackupJob objects in list views.
    """
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True,
    )
    status = columns.ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    jobtype = tables.Column(
        verbose_name=_('Job Type'),
    )
    platform = tables.Column(
        verbose_name=_('Platform'),
    )
    job_creation_time = tables.DateTimeColumn(
        verbose_name=_('Job Creation Time'),
        format='Y-m-d H:i',
    )
    LastBackupEndTime = tables.DateTimeColumn(
        verbose_name=_('Last Backup End Time'),
        format='Y-m-d H:i',
    )
    LastBackupResult = columns.ChoiceFieldColumn(
        verbose_name=_('Last Backup Result'),
    )
    description = tables.Column(
        verbose_name=_('Description'),
    )
    backup_server_name = tables.Column(
        verbose_name=_('Backup Server'),
        accessor='backup_server_display',
        order_by=('backup_server_name',),
    )
    backup_server_ip = tables.Column(
        verbose_name=_('Backup Server IP'),
        linkify=True,
    )
    target = tables.Column(
        verbose_name=_('Target'),
    )
    virtual_machines = columns.ManyToManyColumn(
        verbose_name=_('Virtual Machines'),
        linkify_item=True,
    )
    virtual_machine_count = tables.Column(
        verbose_name=_('VM Count'),
        empty_values=(),
        default=0,
    )

    # Advanced settings
    Algorithm = tables.Column(
        verbose_name=_('Algorithm'),
    )
    EnableDeduplication = columns.ChoiceFieldColumn(
        verbose_name=_('Deduplication'),
    )
    StorageEncryptionEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('Storage Encryption'),
    )
    RetainDaysToKeep = tables.Column(
        verbose_name=_('Retain Days'),
    )
    RetainCycles = tables.Column(
        verbose_name=_('Retain Cycles'),
    )
    EnableDeletedVmDataRetention = columns.ChoiceFieldColumn(
        verbose_name=_('Deleted VM Retention'),
    )
    RetainDaysToKeepDeletedVmData = tables.Column(
        verbose_name=_('Deleted VM Retain Days'),
    )

    # Synthetic full backup settings
    TransformFullToSynthetic = columns.ChoiceFieldColumn(
        verbose_name=_('Synthetic Full (Incremental)'),
    )
    TransformToSyntheticFull = columns.ChoiceFieldColumn(
        verbose_name=_('Synthetic Full (Reverse Incr.)'),
    )
    TransformToSyntheticKind = tables.Column(
        verbose_name=_('Synthetic Full Kind'),
    )
    TransformToSyntheticDays = tables.Column(
        verbose_name=_('Synthetic Full Days'),
    )
    SyntheticFullDayNumberInMonth = tables.Column(
        verbose_name=_('Synthetic Full Week'),
    )
    SyntheticFullDayOfWeek = tables.Column(
        verbose_name=_('Synthetic Full Weekday'),
    )
    TransformToSyntheticMonthly = tables.Column(
        verbose_name=_('Synthetic Full Months'),
    )

    # Active full backup settings
    EnableFullBackup = columns.ChoiceFieldColumn(
        verbose_name=_('Active Full Backup'),
    )
    FullBackupScheduleKind = tables.Column(
        verbose_name=_('Full Backup Kind'),
    )
    FullBackupDays = tables.Column(
        verbose_name=_('Full Backup Days'),
    )
    FullBackupDayNumberInMonth = tables.Column(
        verbose_name=_('Full Backup Week'),
    )
    FullBackupDayOfWeek = tables.Column(
        verbose_name=_('Full Backup Weekday'),
    )
    FullBackupMonths = tables.Column(
        verbose_name=_('Full Backup Months'),
    )

    # GFS settings
    EnableGFS = columns.ChoiceFieldColumn(
        verbose_name=_('GFS'),
    )
    WeeklyEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('GFS Weekly Schedule'),
    )
    WeeklyKeepBackupsFor = tables.Column(
        verbose_name=_('GFS Weekly Keep (weeks)'),
    )
    WeeklyKeepBackupsOnDayOfWeek = tables.Column(
        verbose_name=_('GFS Weekly Day'),
    )
    MonthlyEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('GFS Monthly Schedule'),
    )
    MonthlyKeepBackupsFor = tables.Column(
        verbose_name=_('GFS Monthly Keep (months)'),
    )
    MonthlyKeepBackupsWeekOfMonth = tables.Column(
        verbose_name=_('GFS Monthly Week'),
    )
    YearlyEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('GFS Yearly Schedule'),
    )
    YearlyKeepBackupsFor = tables.Column(
        verbose_name=_('GFS Yearly Keep (years)'),
    )
    YearlyKeepBackupsOnMonthOfYear = tables.Column(
        verbose_name=_('GFS Yearly Month'),
    )

    # Schedule options
    RunAutomatically = columns.ChoiceFieldColumn(
        verbose_name=_('Run Automatically'),
    )
    ScheduleDailyEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('Daily Enabled'),
    )
    ScheduleDailyTime = tables.TimeColumn(
        verbose_name=_('Daily Time'),
        format='H:i',
    )
    ScheduleDailyKind = tables.Column(
        verbose_name=_('Daily Kind'),
    )
    ScheduleDailyDays = tables.Column(
        verbose_name=_('Daily Days'),
    )
    ScheduleMonthlyEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('Monthly Enabled'),
    )
    ScheduleMonthlyTime = tables.TimeColumn(
        verbose_name=_('Monthly Time'),
        format='H:i',
    )
    ScheduleMonthlyDayOfWeek = tables.Column(
        verbose_name=_('Monthly Day of Week'),
    )
    ScheduleMonthlyDayNumberInMonth = tables.Column(
        verbose_name=_('Monthly Day number of Month'),
    )
    ScheduleMonthlyDayOfMonth = tables.Column(
        verbose_name=_('Monthly Day of Month'),
    )
    ScheduleMonthlyMonths = tables.Column(
        verbose_name=_('Monthly Months'),
    )
    SchedulePeriodicallyEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('Periodically Enabled'),
    )
    SchedulePeriodicallyEvery = tables.Column(
        verbose_name=_('Periodically Every'),
    )
    SchedulePeriodicallyUnit = tables.Column(
        verbose_name=_('Periodically Unit'),
    )
    SchedulePeriodicallyHourOffsetInMin = tables.Column(
        verbose_name=_('Hour Offset (min)'),
    )
    SchedulePeriodicallyMondaySchema = tables.Column(
        verbose_name=_('Monday Schema'),
    )
    SchedulePeriodicallyTuesdaySchema = tables.Column(
        verbose_name=_('Tuesday Schema'),
    )
    SchedulePeriodicallyWednesdaySchema = tables.Column(
        verbose_name=_('Wednesday Schema'),
    )
    SchedulePeriodicallyThursdaySchema = tables.Column(
        verbose_name=_('Thursday Schema'),
    )
    SchedulePeriodicallyFridaySchema = tables.Column(
        verbose_name=_('Friday Schema'),
    )
    SchedulePeriodicallySaturdaySchema = tables.Column(
        verbose_name=_('Saturday Schema'),
    )
    SchedulePeriodicallySundaySchema = tables.Column(
        verbose_name=_('Sunday Schema'),
    )
    AfterJobEnabled = columns.ChoiceFieldColumn(
        verbose_name=_('After Job Enabled'),
    )
    AfterJobName = tables.Column(
        verbose_name=_('After Job Name'),
    )

    comments = tables.Column(
        verbose_name=_('Comments'),
    )
    tags = columns.TagColumn(
        url_name='plugins:netbox_backupjobs:backupjob_list',
    )

    def render_virtual_machine_count(self, value, record):
        url = reverse('plugins:netbox_backupjobs:backupjob_virtual_machines', kwargs={'pk': record.pk})
        return format_html('<a href="{}">{}</a>', url, value or 0)

    def render_backup_server_name(self, value, record):
        if hasattr(value, 'get_absolute_url'):
            return format_html('<a href="{}">{}</a>', value.get_absolute_url(), value)
        return value or '—'

    def render_RetainDaysToKeepDeletedVmData(self, value, record):
        if record.EnableDeletedVmDataRetention == 'false':
            return format_html('<s>{}</s>', value) if value else '—'
        return value or '—'

    def _both_disabled(self, record):
        return record.TransformFullToSynthetic == 'false' and record.TransformToSyntheticFull == 'false'

    def render_TransformToSyntheticKind(self, value, record):
        text = record.get_TransformToSyntheticKind_display()
        if self._both_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_TransformToSyntheticDays(self, value, record):
        text = record.get_TransformToSyntheticDays_display()
        if self._both_disabled(record) or record.TransformToSyntheticKind == 'monthly':
            return format_html('<s>{}</s>', text)
        return text

    def render_SyntheticFullDayNumberInMonth(self, value, record):
        text = record.get_SyntheticFullDayNumberInMonth_display()
        if self._both_disabled(record) or record.TransformToSyntheticKind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_SyntheticFullDayOfWeek(self, value, record):
        text = record.get_SyntheticFullDayOfWeek_display()
        if self._both_disabled(record) or record.TransformToSyntheticKind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_TransformToSyntheticMonthly(self, value, record):
        text = record.get_TransformToSyntheticMonthly_display()
        if self._both_disabled(record) or record.TransformToSyntheticKind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def _full_backup_disabled(self, record):
        return record.EnableFullBackup == 'false'

    def render_FullBackupScheduleKind(self, value, record):
        text = record.get_FullBackupScheduleKind_display()
        if self._full_backup_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_FullBackupDays(self, value, record):
        text = record.get_FullBackupDays_display()
        if self._full_backup_disabled(record) or record.FullBackupScheduleKind == 'monthly':
            return format_html('<s>{}</s>', text)
        return text

    def render_FullBackupDayNumberInMonth(self, value, record):
        text = record.get_FullBackupDayNumberInMonth_display()
        if self._full_backup_disabled(record) or record.FullBackupScheduleKind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_FullBackupDayOfWeek(self, value, record):
        text = record.get_FullBackupDayOfWeek_display()
        if self._full_backup_disabled(record) or record.FullBackupScheduleKind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_FullBackupMonths(self, value, record):
        text = record.get_FullBackupMonths_display()
        if self._full_backup_disabled(record) or record.FullBackupScheduleKind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def _gfs_disabled(self, record):
        return record.EnableGFS == 'false'

    def render_WeeklyKeepBackupsFor(self, value, record):
        text = str(value) if value is not None else '—'
        if self._gfs_disabled(record) or record.WeeklyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_WeeklyKeepBackupsOnDayOfWeek(self, value, record):
        text = record.get_WeeklyKeepBackupsOnDayOfWeek_display()
        if self._gfs_disabled(record) or record.WeeklyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_MonthlyKeepBackupsFor(self, value, record):
        text = str(value) if value is not None else '—'
        if self._gfs_disabled(record) or record.MonthlyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_MonthlyKeepBackupsWeekOfMonth(self, value, record):
        text = record.get_MonthlyKeepBackupsWeekOfMonth_display()
        if self._gfs_disabled(record) or record.MonthlyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_YearlyKeepBackupsFor(self, value, record):
        text = str(value) if value is not None else '—'
        if self._gfs_disabled(record) or record.YearlyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_YearlyKeepBackupsOnMonthOfYear(self, value, record):
        text = record.get_YearlyKeepBackupsOnMonthOfYear_display()
        if self._gfs_disabled(record) or record.YearlyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def _run_automatically_disabled(self, record):
        return record.RunAutomatically == 'false'

    def render_ScheduleDailyTime(self, value, record):
        if self._run_automatically_disabled(record) or record.ScheduleDailyEnabled == 'false':
            return format_html('<s>{}</s>', value) if value else '—'
        return value or '—'

    def render_ScheduleDailyKind(self, value, record):
        text = record.get_ScheduleDailyKind_display()
        if self._run_automatically_disabled(record) or record.ScheduleDailyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_ScheduleDailyDays(self, value, record):
        text = record.get_ScheduleDailyDays_display()
        if (
            self._run_automatically_disabled(record)
            or record.ScheduleDailyEnabled == 'false'
            or record.ScheduleDailyKind != 'selected days'
        ):
            return format_html('<s>{}</s>', text)
        return text

    def render_ScheduleMonthlyTime(self, value, record):
        if self._run_automatically_disabled(record) or record.ScheduleMonthlyEnabled == 'false':
            return format_html('<s>{}</s>', value) if value else '—'
        return value or '—'

    def render_ScheduleMonthlyDayNumberInMonth(self, value, record):
        text = record.get_ScheduleMonthlyDayNumberInMonth_display()
        if self._run_automatically_disabled(record) or record.ScheduleMonthlyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_ScheduleMonthlyDayOfWeek(self, value, record):
        text = record.get_ScheduleMonthlyDayOfWeek_display()
        if (
            self._run_automatically_disabled(record)
            or record.ScheduleMonthlyEnabled == 'false'
            or record.ScheduleMonthlyDayNumberInMonth == 'this day'
        ):
            return format_html('<s>{}</s>', text)
        return text

    def render_ScheduleMonthlyDayOfMonth(self, value, record):
        text = record.get_ScheduleMonthlyDayOfMonth_display()
        if (
            self._run_automatically_disabled(record)
            or record.ScheduleMonthlyEnabled == 'false'
            or record.ScheduleMonthlyDayNumberInMonth != 'this day'
        ):
            return format_html('<s>{}</s>', text)
        return text

    def render_ScheduleMonthlyMonths(self, value, record):
        text = record.get_ScheduleMonthlyMonths_display()
        if self._run_automatically_disabled(record) or record.ScheduleMonthlyEnabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def _periodically_disabled(self, record):
        return self._run_automatically_disabled(record) or record.SchedulePeriodicallyEnabled == 'false'

    def render_SchedulePeriodicallyEvery(self, value, record):
        text = str(value) if value is not None else '—'
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallyUnit(self, value, record):
        text = record.get_SchedulePeriodicallyUnit_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallyHourOffsetInMin(self, value, record):
        text = str(value) if value is not None else '—'
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallyMondaySchema(self, value, record):
        text = record.get_SchedulePeriodicallyMondaySchema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallyTuesdaySchema(self, value, record):
        text = record.get_SchedulePeriodicallyTuesdaySchema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallyWednesdaySchema(self, value, record):
        text = record.get_SchedulePeriodicallyWednesdaySchema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallyThursdaySchema(self, value, record):
        text = record.get_SchedulePeriodicallyThursdaySchema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallyFridaySchema(self, value, record):
        text = record.get_SchedulePeriodicallyFridaySchema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallySaturdaySchema(self, value, record):
        text = record.get_SchedulePeriodicallySaturdaySchema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_SchedulePeriodicallySundaySchema(self, value, record):
        text = record.get_SchedulePeriodicallySundaySchema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_AfterJobName(self, value, record):
        if not value:
            return '—'
        if record.AfterJobEnabled == 'false':
            return format_html('<s>{}</s>', value)
        return format_html('<a href="{}">{}</a>', value.get_absolute_url(), value)

    class Meta(NetBoxTable.Meta):
        model = BackupJob
        fields = (
            'pk', 'id', 'name', 'status', 'jobtype', 'platform', 'job_creation_time', 'LastBackupEndTime', 'LastBackupResult', 'description', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'virtual_machine_count',
            'Algorithm', 'EnableDeduplication', 'StorageEncryptionEnabled',
            'RetainDaysToKeep', 'RetainCycles',
            'EnableDeletedVmDataRetention', 'RetainDaysToKeepDeletedVmData',
            'TransformFullToSynthetic', 'TransformToSyntheticFull',
            'TransformToSyntheticKind', 'TransformToSyntheticDays',
            'SyntheticFullDayNumberInMonth', 'SyntheticFullDayOfWeek',
            'TransformToSyntheticMonthly',
            'EnableFullBackup', 'FullBackupScheduleKind',
            'FullBackupDays', 'FullBackupDayNumberInMonth', 'FullBackupDayOfWeek',
            'FullBackupMonths',
            'EnableGFS',
            'WeeklyEnabled', 'WeeklyKeepBackupsFor', 'WeeklyKeepBackupsOnDayOfWeek',
            'MonthlyEnabled', 'MonthlyKeepBackupsFor', 'MonthlyKeepBackupsWeekOfMonth',
            'YearlyEnabled', 'YearlyKeepBackupsFor', 'YearlyKeepBackupsOnMonthOfYear',
            'RunAutomatically',
            'ScheduleDailyEnabled', 'ScheduleDailyTime', 'ScheduleDailyKind', 'ScheduleDailyDays',
            'ScheduleMonthlyEnabled', 'ScheduleMonthlyTime', 'ScheduleMonthlyDayOfWeek',
            'ScheduleMonthlyDayNumberInMonth', 'ScheduleMonthlyDayOfMonth', 'ScheduleMonthlyMonths',
            'SchedulePeriodicallyEnabled', 'SchedulePeriodicallyEvery', 'SchedulePeriodicallyUnit',
            'SchedulePeriodicallyHourOffsetInMin',
            'SchedulePeriodicallyMondaySchema', 'SchedulePeriodicallyTuesdaySchema',
            'SchedulePeriodicallyWednesdaySchema', 'SchedulePeriodicallyThursdaySchema',
            'SchedulePeriodicallyFridaySchema', 'SchedulePeriodicallySaturdaySchema',
            'SchedulePeriodicallySundaySchema',
            'AfterJobEnabled', 'AfterJobName',
            'comments', 'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = (
            'pk', 'name', 'status', 'jobtype', 'platform', 'LastBackupResult', 'description', 'virtual_machines', 'virtual_machine_count',
        )


# ========================
# virtualization model table columns
# ========================

### Add Backupjob column to Virtual Machine tables.
backupjob_column = columns.ManyToManyColumn(
    verbose_name=_('Backup Jobs'),
    linkify_item=True,
)

register_table_column(backupjob_column, 'backup_jobs', VirtualMachineTable)