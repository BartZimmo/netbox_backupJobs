from django.urls import include, path

from utilities.urls import get_model_urls
from netbox.views.generic import ObjectChangeLogView
from . import views

app_name = 'netbox_backupjobs'
urlpatterns = [

    # BackupJobs
    path('backupjobs/', include(get_model_urls('netbox_backupjobs', 'backupjob', detail=False))),
    path('backupjobs/<int:pk>/', include(get_model_urls('netbox_backupjobs', 'backupjob'))),

    # BackupCopyJobs
    path('backupcopyjobs/', include(get_model_urls('netbox_backupjobs', 'backupcopyjob', detail=False))),
    path('backupcopyjobs/<int:pk>/', include(get_model_urls('netbox_backupjobs', 'backupcopyjob'))),

]
