from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Person
from home.serializers import PeopleSerializer


@api_view(['GET','POST'])

def index(request):
    if request.method == 'GET':
        json_response={
            "name":"Praveen",
            "courses":"Python",
            'method':'GET'
        }
    else :
        data = request.data
        print(data)
        json_response={
            "name":"Praveen",
            "courses":"Python",
            'method':'POST'
        }
    return Response(json_response)

@api_view(['GET','POST'])
def person(request):
    if request.method == 'GET':
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many =True)
        return Response(serializer.data)
    
    else:
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    


