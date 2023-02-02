from groups.models import Group
from django.http import JsonResponse, Http404
from groups.serializers import GroupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def groups(request):
    if request.method == 'GET':
        data = Group.objects.all()
        serializer = GroupSerializer(data, many=True)
        return Response({'groups': serializer.data})
    elif request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'group': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST', 'DELETE'])
def group(request, id):
    try:
        data = Group.objects.get(pk=id)
    except Group.DoesNotExist:
        raise Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupSerializer(data)
        return Response({'group': serializer.data})

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        serializer = GroupSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'group': serializer.data})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
