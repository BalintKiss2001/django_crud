from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializer import TaskSerializer
import datetime


@api_view(['GET'])
def get_tasks(request):
    test_data = {
        'title': 'Project Meeting',
        'description' : 'Project meeting with Team 1 at the second floor office',
        'creation_date' : datetime.datetime.now().isoformat(),
        'due_date' : (datetime.datetime.now() + datetime.timedelta(days=3)).isoformat(), 
        'status' : "pending"
    }
    serializer = TaskSerializer(data = test_data)
    tasks = Task.objects.all()

     #Filtering
    status_filter = request.query_params.get('status')
    due_date = request.query_params.get('due_date')

    if status_filter:
        tasks = tasks.filter(status=status_filter)
    if due_date:
        tasks = tasks.filter(due_date__date=due_date)

    #Sorting
    sort_by = request.query_params.get('sort_by')
    order = request.query_params.get('order')  # 'asc' || 'desc'

    if sort_by in ['creation_date', 'due_date']:
        if order == 'desc':
            sort_by = f'-{sort_by}'
        tasks = tasks.order_by(sort_by)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    