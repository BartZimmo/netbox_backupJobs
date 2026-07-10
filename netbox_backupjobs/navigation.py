from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton, get_plugin_config

### BackupJobs ###

backupjobs_items = (
    PluginMenuItem(
        link='plugins:netbox_backupjobs:backupjob_list',
        link_text='Veeam BackupJobs',
        permissions=["netbox_backupjobs.view_backupjob"],
        buttons= [
            PluginMenuButton(
                link='plugins:netbox_backupjobs:backupjob_add',
                title='Add Veeam BackupJob',
                icon_class='mdi mdi-plus-thick',
                permissions=["netbox_backupjobs.add_backupjob"],
            ),
            PluginMenuButton(
                link='plugins:netbox_backupjobs:backupjob_bulk_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=["netbox_backupjobs.add_backupjob"],
            ),
        ],
    ),
)



### BackupCopyJobs ###

backupcopyjobs_items = (
    PluginMenuItem(
        link='plugins:netbox_backupjobs:backupcopyjob_list',
        link_text='Veeam BackupCopyJobs',
        permissions=["netbox_backupjobs.view_backupcopyjob"],
        buttons= [
            PluginMenuButton(
                link='plugins:netbox_backupjobs:backupcopyjob_add',
                title='Add Veeam BackupCopyJob',
                icon_class='mdi mdi-plus-thick',
                permissions=["netbox_backupjobs.add_backupcopyjob"],
            ),
            PluginMenuButton(
                link='plugins:netbox_backupjobs:backupcopyjob_bulk_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=["netbox_backupjobs.add_backupcopyjob"],
            ),
        ],
    ),
)

### -> Add new Menu Items above this line if needed.

### Menu ###


if get_plugin_config('netbox_backupjobs', 'top_level_menu'):
    menu = PluginMenu(
        label=f'BackupJobs',
        groups=(
            ('BackupJobs', backupjobs_items),
            ('BackupCopyJobs', backupcopyjobs_items),
        ),
        icon_class = 'mdi mdi-clipboard-text-multiple-outline'
    )
else:
    menu_items = backupjobs_items + backupcopyjobs_items