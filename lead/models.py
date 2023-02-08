from django.db import models
from  django.contrib.auth.models import User

from team.models import Team

class Lead(models.Model):
    low = 'low'
    medium = 'medium'
    high = 'high'
    choises_priority = (
        (low,'Low'),
        (medium,'Medium'),
        (high,'High'),
    )

    new = 'new'
    contacted = 'contacted'
    won = 'won'
    lost = 'lost'

    choices_status = (
        (new,'New'),
        (contacted, 'Contacted'),
        (won, 'Won'),
        (lost, 'Lost'),
    )

    team = models.ForeignKey(Team, related_name='leads',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=choises_priority, default=medium)
    status = models.CharField(max_length=10, choices=choices_status, default=new)
    converted_to_client = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name