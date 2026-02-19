import os
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_root(request, format=None):
    # build base url using environment variable to avoid certificate issues
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base = f"https://{codespace}-8000.app.github.dev"
    else:
        base = "http://localhost:8000"
    return Response({
        'activities': f"{base}/api/activities/",
        'teams': f"{base}/api/teams/",
    })


@api_view(['GET', 'POST'])
def activities_list(request, format=None):
    # placeholder view for activities endpoint
    return Response({'message': 'activities endpoint'})


@api_view(['GET', 'POST'])
def teams_list(request, format=None):
    # placeholder view for teams endpoint
    return Response({'message': 'teams endpoint'})
