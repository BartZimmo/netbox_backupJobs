from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton, get_plugin_config

### BackupJobs ###

backupjobs_items = (
    PluginMenuItem(
        link='plugins:netbox_backupjobs:backupjob_list',
        link_text='BackupJobs',
        permissions=["netbox_backupjobs.view_backupjob"],
        buttons= [
            PluginMenuButton(
                link='plugins:netbox_backupjobs:backupjob_add',
                title='Add BackupJob',
                icon_class='mdi mdi-plus-thick',
                permissions=["netbox_backupjobs.add_backupjob"],
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
        ),
        icon_class = 'mdi mdi-clipboard-text-multiple-outline'
    )
else:
    menu_items = backupjobs_items