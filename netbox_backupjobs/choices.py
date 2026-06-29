from utilities.choices import ChoiceSet
from django.utils.translation import gettext_lazy as _


#
# BackupJob
#

class BackupJobStatusChoices(ChoiceSet):
    key = 'BackupJob.status'

    STATUS_ENABLED = 'enabled'
    STATUS_DISABLED = 'disabled'
    

    CHOICES = [
        (STATUS_ENABLED, _('Enabled'), 'green'),
        (STATUS_DISABLED, _('Disabled'), 'blue'),        
    ]