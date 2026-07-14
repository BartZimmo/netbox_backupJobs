import django_tables2 as tables
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from netbox.tables import NetBoxTable, columns
from netbox_backupjobs.models import BackupCopyJob

__all__ = (
    'BackupCopyJobTable',
)


class BackupCopyJobTable(NetBoxTable):
    """
    Table for displaying BackupCopyJob objects in list views.
    """
    name = tables.Column(
        verbose_name=_('Name'),
        linkify=True,
    )
    status = columns.ChoiceFieldColumn(
        verbose_name=_('Status'),
    )
    mode = tables.Column(
        verbose_name=_('Copy Mode'),
    )
    data_transfer_mode = tables.Column(
        verbose_name=_('Data Transfer Mode'),
    )
    jobtype = tables.Column(
        verbose_name=_('Job Type'),
    )
    job_creation_time = tables.DateTimeColumn(
        verbose_name=_('Job Creation Time'),
        format='Y-m-d H:i',
    )
    last_backup_result = columns.ChoiceFieldColumn(
        verbose_name=_('Last Backup Result'),
    )
    description = tables.Column(
        verbose_name=_('Description'),
    )
    retain_days_to_keep = tables.Column(
        verbose_name=_('Retain Days to Keep'),
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
    backup_jobs = columns.ManyToManyColumn(
        verbose_name=_('Backup Jobs'),
        linkify_item=True,
        separator=mark_safe('<br>'),
    )

    # Advanced settings
    enable_deduplication = columns.ChoiceFieldColumn(
        verbose_name=_('Deduplication'),
    )
    storage_encryption_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('Storage Encryption'),
    )
    transaction_log_copy_enabled = columns.ChoiceFieldColumn(
        verbose_name=_('Transaction Log Copy'),
    )
    enable_deleted_vm_data_retention = columns.ChoiceFieldColumn(
        verbose_name=_('Deleted VM Retention'),
    )
    retain_days_to_keep_deleted_vm_data = tables.Column(
        verbose_name=_('Deleted VM Retain Days'),
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
    transfer_window = columns.ChoiceFieldColumn(
        verbose_name=_('Transfer Window'),
    )
    transfer_window_monday_schema = tables.Column(
        verbose_name=_('Monday Schema'),
    )
    transfer_window_tuesday_schema = tables.Column(
        verbose_name=_('Tuesday Schema'),
    )
    transfer_window_wednesday_schema = tables.Column(
        verbose_name=_('Wednesday Schema'),
    )
    transfer_window_thursday_schema = tables.Column(
        verbose_name=_('Thursday Schema'),
    )
    transfer_window_friday_schema = tables.Column(
        verbose_name=_('Friday Schema'),
    )
    transfer_window_saturday_schema = tables.Column(
        verbose_name=_('Saturday Schema'),
    )
    transfer_window_sunday_schema = tables.Column(
        verbose_name=_('Sunday Schema'),
    )

    # Schedule options (used when mode is periodic)
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

    def render_backup_server_name(self, value, record):
        if hasattr(value, 'get_absolute_url'):
            return format_html('<a href="{}">{}</a>', value.get_absolute_url(), value)
        return value or '—'

    def render_retain_days_to_keep_deleted_vm_data(self, value, record):
        if record.enable_deleted_vm_data_retention == 'false':
            return format_html('<s>{}</s>', value) if value else '—'
        return value or '—'

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

    def _transfer_window_not_by_schema(self, record):
        return record.transfer_window != 'by_schema'

    def render_transfer_window_monday_schema(self, value, record):
        text = record.get_transfer_window_monday_schema_display()
        if self._transfer_window_not_by_schema(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_transfer_window_tuesday_schema(self, value, record):
        text = record.get_transfer_window_tuesday_schema_display()
        if self._transfer_window_not_by_schema(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_transfer_window_wednesday_schema(self, value, record):
        text = record.get_transfer_window_wednesday_schema_display()
        if self._transfer_window_not_by_schema(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_transfer_window_thursday_schema(self, value, record):
        text = record.get_transfer_window_thursday_schema_display()
        if self._transfer_window_not_by_schema(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_transfer_window_friday_schema(self, value, record):
        text = record.get_transfer_window_friday_schema_display()
        if self._transfer_window_not_by_schema(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_transfer_window_saturday_schema(self, value, record):
        text = record.get_transfer_window_saturday_schema_display()
        if self._transfer_window_not_by_schema(record):
            return format_html('<s>{}</s>', text)
        return text

    def render_transfer_window_sunday_schema(self, value, record):
        text = record.get_transfer_window_sunday_schema_display()
        if self._transfer_window_not_by_schema(record):
            return format_html('<s>{}</s>', text)
        return text

    def _run_automatically_disabled(self, record):
        return record.mode != 'periodic' or record.run_automatically == 'false'

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
        model = BackupCopyJob
        fields = (
            'pk', 'id', 'name', 'status', 'mode', 'data_transfer_mode', 'jobtype', 'job_creation_time',
            'last_backup_result', 'description',
            'backup_server_name', 'backup_server_ip',
            'retain_days_to_keep', 'target', 'backup_jobs',
            'enable_deduplication', 'storage_encryption_enabled', 'transaction_log_copy_enabled',
            'enable_deleted_vm_data_retention', 'retain_days_to_keep_deleted_vm_data',
            'enable_gfs',
            'weekly_enabled', 'weekly_keep_backups_for', 'weekly_keep_backups_on_day_of_week',
            'monthly_enabled', 'monthly_keep_backups_for', 'monthly_keep_backups_week_of_month',
            'yearly_enabled', 'yearly_keep_backups_for', 'yearly_keep_backups_on_month_of_year',
            'transfer_window',
            'transfer_window_monday_schema', 'transfer_window_tuesday_schema', 'transfer_window_wednesday_schema',
            'transfer_window_thursday_schema', 'transfer_window_friday_schema', 'transfer_window_saturday_schema',
            'transfer_window_sunday_schema',
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
            'tags', 'created', 'last_updated', 'actions',
        )
        default_columns = (
            'pk', 'name', 'status', 'mode', 'jobtype', 'last_backup_result', 'description',
        )
