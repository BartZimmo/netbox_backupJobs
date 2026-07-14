import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from utilities.tables import register_table_column
from virtualization.tables import VirtualMachineTable
from netbox_backupjobs.models import BackupJob

__all__ = (
    'BackupJobTable',
    'VirtualMachineBackupJobsTable',
    'BackupCopyJobBackupJobsTable',
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
    last_backup_end_time = tables.DateTimeColumn(
        verbose_name=_('Last Backup End Time'),
        format='Y-m-d H:i',
    )
    last_backup_result = columns.ChoiceFieldColumn(
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
        separator=mark_safe('<br>'),
    )
    virtual_machine_count = tables.Column(
        verbose_name=_('VM Count'),
        empty_values=(),
        default=0,
    )
    copy_jobs = columns.ManyToManyColumn(
        verbose_name=_('Backup Copy Jobs'),
        linkify_item=True,
        separator=mark_safe('<br>'),
    )

    # Advanced settings
    algorithm = tables.Column(
        verbose_name=_('Algorithm'),
    )
    enable_deduplication = columns.ChoiceFieldColumn(
        verbose_name=_('Deduplication'),
    )
    storage_encryption_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('Storage Encryption'),
    )
    retain_days_to_keep = tables.Column(
        verbose_name=_('Retain Days'),
    )
    retain_cycles = tables.Column(
        verbose_name=_('Retain Cycles'),
    )
    enable_deleted_vm_data_retention = columns.ChoiceFieldColumn(
        verbose_name=_('Deleted VM Retention'),
    )
    retain_days_to_keep_deleted_vm_data = tables.Column(
        verbose_name=_('Deleted VM Retain Days'),
    )

    # Synthetic full backup settings
    transform_full_to_synthetic = columns.ChoiceFieldColumn(
        verbose_name=_('Synthetic Full (Incremental)'),
    )
    transform_to_synthetic_full = columns.ChoiceFieldColumn(
        verbose_name=_('Synthetic Full (Reverse Incr.)'),
    )
    transform_to_synthetic_kind = tables.Column(
        verbose_name=_('Synthetic Full Kind'),
    )
    transform_to_synthetic_days = tables.Column(
        verbose_name=_('Synthetic Full Days'),
    )
    synthetic_full_day_number_in_month = tables.Column(
        verbose_name=_('Synthetic Full Week'),
    )
    synthetic_full_day_of_week = tables.Column(
        verbose_name=_('Synthetic Full Weekday'),
    )
    transform_to_synthetic_monthly = tables.Column(
        verbose_name=_('Synthetic Full Months'),
    )

    # Active full backup settings
    enable_full_backup = columns.ChoiceFieldColumn(
        verbose_name=_('Active Full Backup'),
    )
    full_backup_schedule_kind = tables.Column(
        verbose_name=_('Full Backup Kind'),
    )
    full_backup_days = tables.Column(
        verbose_name=_('Full Backup Days'),
    )
    full_backup_day_number_in_month = tables.Column(
        verbose_name=_('Full Backup Week'),
    )
    full_backup_day_of_week = tables.Column(
        verbose_name=_('Full Backup Weekday'),
    )
    full_backup_months = tables.Column(
        verbose_name=_('Full Backup Months'),
    )

    # GFS settings
    enable_gfs = columns.ChoiceFieldColumn(
        verbose_name=_('GFS'),
    )
    weekly_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('GFS Weekly Schedule'),
    )
    weekly_keep_backups_for = tables.Column(
        verbose_name=_('GFS Weekly Keep (weeks)'),
    )
    weekly_keep_backups_on_day_of_week = tables.Column(
        verbose_name=_('GFS Weekly Day'),
    )
    monthly_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('GFS Monthly Schedule'),
    )
    monthly_keep_backups_for = tables.Column(
        verbose_name=_('GFS Monthly Keep (months)'),
    )
    monthly_keep_backups_week_of_month = tables.Column(
        verbose_name=_('GFS Monthly Week'),
    )
    yearly_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('GFS Yearly Schedule'),
    )
    yearly_keep_backups_for = tables.Column(
        verbose_name=_('GFS Yearly Keep (years)'),
    )
    yearly_keep_backups_on_month_of_year = tables.Column(
        verbose_name=_('GFS Yearly Month'),
    )

    # Schedule options
    run_automatically = columns.ChoiceFieldColumn(
        verbose_name=_('Run Automatically'),
    )
    schedule_daily_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('Daily Enabled'),
    )
    schedule_daily_time = tables.TimeColumn(
        verbose_name=_('Daily Time'),
        format='H:i',
    )
    schedule_daily_kind = tables.Column(
        verbose_name=_('Daily Kind'),
    )
    schedule_daily_days = tables.Column(
        verbose_name=_('Daily Days'),
    )
    schedule_monthly_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('Monthly Enabled'),
    )
    schedule_monthly_time = tables.TimeColumn(
        verbose_name=_('Monthly Time'),
        format='H:i',
    )
    schedule_monthly_day_of_week = tables.Column(
        verbose_name=_('Monthly Day of Week'),
    )
    schedule_monthly_day_number_in_month = tables.Column(
        verbose_name=_('Monthly Day number of Month'),
    )
    schedule_monthly_day_of_month = tables.Column(
        verbose_name=_('Monthly Day of Month'),
    )
    schedule_monthly_months = tables.Column(
        verbose_name=_('Monthly Months'),
    )
    schedule_periodically_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('Periodically Enabled'),
    )
    schedule_periodically_every = tables.Column(
        verbose_name=_('Periodically Every'),
    )
    schedule_periodically_unit = tables.Column(
        verbose_name=_('Periodically Unit'),
    )
    schedule_periodically_hour_offset_in_min = tables.Column(
        verbose_name=_('Hour Offset (min)'),
    )
    schedule_periodically_monday_schema = tables.Column(
        verbose_name=_('Monday Schema'),
    )
    schedule_periodically_tuesday_schema = tables.Column(
        verbose_name=_('Tuesday Schema'),
    )
    schedule_periodically_wednesday_schema = tables.Column(
        verbose_name=_('Wednesday Schema'),
    )
    schedule_periodically_thursday_schema = tables.Column(
        verbose_name=_('Thursday Schema'),
    )
    schedule_periodically_friday_schema = tables.Column(
        verbose_name=_('Friday Schema'),
    )
    schedule_periodically_saturday_schema = tables.Column(
        verbose_name=_('Saturday Schema'),
    )
    schedule_periodically_sunday_schema = tables.Column(
        verbose_name=_('Sunday Schema'),
    )
    after_job_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('After Job Enabled'),
    )
    after_job_name = tables.Column(
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

    def render_retain_days_to_keep_deleted_vm_data(self, value, record):
        if record.enable_deleted_vm_data_retention == 'false':
            return format_html('<s>{}</s>', value) if value else '—'
        return value or '—'

    def _both_disabled(self, record):
        return record.transform_full_to_synthetic == 'false' and record.transform_to_synthetic_full == 'false'

    def render_transform_to_synthetic_kind(self, value, record):
        text = record.get_transform_to_synthetic_kind_display()
        if self._both_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_transform_to_synthetic_days(self, value, record):
        text = record.get_transform_to_synthetic_days_display()
        if self._both_disabled(record) or record.transform_to_synthetic_kind == 'monthly':
            return format_html('<s>{}</s>', text)
        return text

    def render_synthetic_full_day_number_in_month(self, value, record):
        text = record.get_synthetic_full_day_number_in_month_display()
        if self._both_disabled(record) or record.transform_to_synthetic_kind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_synthetic_full_day_of_week(self, value, record):
        text = record.get_synthetic_full_day_of_week_display()
        if self._both_disabled(record) or record.transform_to_synthetic_kind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_transform_to_synthetic_monthly(self, value, record):
        text = record.get_transform_to_synthetic_monthly_display()
        if self._both_disabled(record) or record.transform_to_synthetic_kind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def _full_backup_disabled(self, record):
        return record.enable_full_backup == 'false'

    def render_full_backup_schedule_kind(self, value, record):
        text = record.get_full_backup_schedule_kind_display()
        if self._full_backup_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_full_backup_days(self, value, record):
        text = record.get_full_backup_days_display()
        if self._full_backup_disabled(record) or record.full_backup_schedule_kind == 'monthly':
            return format_html('<s>{}</s>', text)
        return text

    def render_full_backup_day_number_in_month(self, value, record):
        text = record.get_full_backup_day_number_in_month_display()
        if self._full_backup_disabled(record) or record.full_backup_schedule_kind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_full_backup_day_of_week(self, value, record):
        text = record.get_full_backup_day_of_week_display()
        if self._full_backup_disabled(record) or record.full_backup_schedule_kind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def render_full_backup_months(self, value, record):
        text = record.get_full_backup_months_display()
        if self._full_backup_disabled(record) or record.full_backup_schedule_kind == 'daily':
            return format_html('<s>{}</s>', text)
        return text

    def _gfs_disabled(self, record):
        return record.enable_gfs == 'false'

    def render_weekly_keep_backups_for(self, value, record):
        text = str(value) if value is not None else '—'
        if self._gfs_disabled(record) or record.weekly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_weekly_keep_backups_on_day_of_week(self, value, record):
        text = record.get_weekly_keep_backups_on_day_of_week_display()
        if self._gfs_disabled(record) or record.weekly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_monthly_keep_backups_for(self, value, record):
        text = str(value) if value is not None else '—'
        if self._gfs_disabled(record) or record.monthly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_monthly_keep_backups_week_of_month(self, value, record):
        text = record.get_monthly_keep_backups_week_of_month_display()
        if self._gfs_disabled(record) or record.monthly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_yearly_keep_backups_for(self, value, record):
        text = str(value) if value is not None else '—'
        if self._gfs_disabled(record) or record.yearly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_yearly_keep_backups_on_month_of_year(self, value, record):
        text = record.get_yearly_keep_backups_on_month_of_year_display()
        if self._gfs_disabled(record) or record.yearly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def _run_automatically_disabled(self, record):
        return record.run_automatically == 'false'

    def render_schedule_daily_time(self, value, record):
        if self._run_automatically_disabled(record) or record.schedule_daily_enabled == 'false':
            return format_html('<s>{}</s>', value) if value else '—'
        return value or '—'

    def render_schedule_daily_kind(self, value, record):
        text = record.get_schedule_daily_kind_display()
        if self._run_automatically_disabled(record) or record.schedule_daily_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_daily_days(self, value, record):
        text = record.get_schedule_daily_days_display()
        if (
            self._run_automatically_disabled(record)
            or record.schedule_daily_enabled == 'false'
            or record.schedule_daily_kind != 'selected days'
        ):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_monthly_time(self, value, record):
        if self._run_automatically_disabled(record) or record.schedule_monthly_enabled == 'false':
            return format_html('<s>{}</s>', value) if value else '—'
        return value or '—'

    def render_schedule_monthly_day_number_in_month(self, value, record):
        text = record.get_schedule_monthly_day_number_in_month_display()
        if self._run_automatically_disabled(record) or record.schedule_monthly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_monthly_day_of_week(self, value, record):
        text = record.get_schedule_monthly_day_of_week_display()
        if (
            self._run_automatically_disabled(record)
            or record.schedule_monthly_enabled == 'false'
            or record.schedule_monthly_day_number_in_month == 'this day'
        ):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_monthly_day_of_month(self, value, record):
        text = record.get_schedule_monthly_day_of_month_display()
        if (
            self._run_automatically_disabled(record)
            or record.schedule_monthly_enabled == 'false'
            or record.schedule_monthly_day_number_in_month != 'this day'
        ):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_monthly_months(self, value, record):
        text = record.get_schedule_monthly_months_display()
        if self._run_automatically_disabled(record) or record.schedule_monthly_enabled == 'false':
            return format_html('<s>{}</s>', text)
        return text

    def _periodically_disabled(self, record):
        return self._run_automatically_disabled(record) or record.schedule_periodically_enabled == 'false'

    def render_schedule_periodically_every(self, value, record):
        text = str(value) if value is not None else '—'
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_unit(self, value, record):
        text = record.get_schedule_periodically_unit_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_hour_offset_in_min(self, value, record):
        text = str(value) if value is not None else '—'
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_monday_schema(self, value, record):
        text = record.get_schedule_periodically_monday_schema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_tuesday_schema(self, value, record):
        text = record.get_schedule_periodically_tuesday_schema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_wednesday_schema(self, value, record):
        text = record.get_schedule_periodically_wednesday_schema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_thursday_schema(self, value, record):
        text = record.get_schedule_periodically_thursday_schema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_friday_schema(self, value, record):
        text = record.get_schedule_periodically_friday_schema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_saturday_schema(self, value, record):
        text = record.get_schedule_periodically_saturday_schema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_schedule_periodically_sunday_schema(self, value, record):
        text = record.get_schedule_periodically_sunday_schema_display()
        if self._periodically_disabled(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_after_job_name(self, value, record):
        if not value:
            return '—'
        if record.after_job_enabled == 'false':
            return format_html('<s>{}</s>', value)
        return format_html('<a href="{}">{}</a>', value.get_absolute_url(), value)

    class Meta(NetBoxTable.Meta):
        model = BackupJob
        fields = (
            'pk', 'id', 'name', 'status', 'jobtype', 'platform', 'job_creation_time', 'last_backup_end_time', 'last_backup_result', 'description', 'backup_server_name', 'backup_server_ip', 'target', 'virtual_machines', 'virtual_machine_count',
            'copy_jobs',
            'algorithm', 'enable_deduplication', 'storage_encryption_enabled',
            'retain_days_to_keep', 'retain_cycles',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            'transform_full_to_synthetic', 'transform_to_synthetic_full',
            'transform_to_synthetic_kind', 'transform_to_synthetic_days',
            'synthetic_full_day_number_in_month', 'synthetic_full_day_of_week',
            'transform_to_synthetic_monthly',
            'enable_full_backup', 'full_backup_schedule_kind',
            'full_backup_days', 'full_backup_day_number_in_month', 'full_backup_day_of_week',
            'full_backup_months',
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            'run_automatically',
            'schedule_daily_enabled', 'schedule_daily_time', 'schedule_daily_kind', 'schedule_daily_days',
            'schedule_monthly_enabled', 'schedule_monthly_time', 'schedule_monthly_day_of_week',
            'schedule_monthly_day_number_in_month', 'schedule_monthly_day_of_month', 'schedule_monthly_months',
            'schedule_periodically_enabled', 'schedule_periodically_every', 'schedule_periodically_unit',
            'schedule_periodically_hour_offset_in_min',
            'schedule_periodically_monday_schema', 'schedule_periodically_tuesday_schema',
            'schedule_periodically_wednesday_schema', 'schedule_periodically_thursday_schema',
            'schedule_periodically_friday_schema', 'schedule_periodically_saturday_schema',
            'schedule_periodically_sunday_schema',
            'after_job_enabled', 'after_job_name',
            'comments', 'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = (
            'pk', 'name', 'status', 'jobtype', 'platform', 'last_backup_result', 'description', 'virtual_machines', 'virtual_machine_count',
        )


class VirtualMachineBackupJobsTable(BackupJobTable):
    """
    Used on the VirtualMachine 'Backup Jobs' tab. A separate subclass so that column
    visibility/ordering preferences there are independent from the main BackupJob list view,
    since NetBox keys those preferences by table class name.
    """
    class Meta(BackupJobTable.Meta):
        pass


class BackupCopyJobBackupJobsTable(BackupJobTable):
    """
    Used on the BackupCopyJob 'Backup Jobs' tab. A separate subclass so that column
    visibility/ordering preferences there are independent from the main BackupJob list view,
    since NetBox keys those preferences by table class name.
    """
    class Meta(BackupJobTable.Meta):
        pass


# ========================
# virtualization model table columns
# ========================

### Add Backupjob column to Virtual Machine tables.
backupjob_column = columns.ManyToManyColumn(
    verbose_name=_('Backup Jobs'),
    linkify_item=True,
    separator=mark_safe('<br>'),
)

register_table_column(backupjob_column, 'backup_jobs', VirtualMachineTable)