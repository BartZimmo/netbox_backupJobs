# netbox_backupJobs
This is a netbox plugin for keeping track of backup jobs

This plugin was developed to document backup jobs from Veeam Backup & Replication 13. The focus is on capturing the most important information about a backup job, such as retention and GFS (Grandfather-Father-Son) settings.

## Requirements

- NetBox >= 4.6.0

## Features

- **Backup job tracking** — name, job type, platform (VMware, Hyper-V, ...), status, target, description and the original job creation time from the backup system.
- **Virtual machine association** — link a backup job to one or more NetBox virtual machines. The linked VMs (and their count) are shown on the backup job, and a "Backup Jobs" column/tab is added to the virtual machine views so you can see which jobs a VM belongs to.
- **Advanced job settings** — algorithm (incremental / reverse incremental), deduplication, storage encryption, and deleted VM data retention.
- **Synthetic full backup settings** — schedule (daily/monthly), days of week, week of month and months.
- **Active full backup settings** — schedule (daily/monthly), days of week, week of month and months.
- **GFS (Grandfather-Father-Son) retention** — independent weekly, monthly and yearly retention schedules, each with their own retention period and scheduling day/week/month.
- **Filtering** — filter backup jobs by any of the above, plus convenience filters such as "Has virtual machines" and "Has powered off virtual machines".
- **Global search** — backup jobs are indexed by name and by the names of their linked virtual machines, so searching for a VM also surfaces the backup job it belongs to.
