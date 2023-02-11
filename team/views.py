from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from team.models import Team


def edit_team(request, pk):
    team = get_object_or_404(Team, created_by=request.user, pk=pk)
    return render(request, 'team/edit_team.html', {
        'team': team
    })
