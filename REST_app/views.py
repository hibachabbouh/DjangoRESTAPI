

from pstats import Stats
import statistics
from rest_framework.response import Response
from rest_framework import status


from rest_framework.decorators import api_view
from REST_app.models import Item
from REST_app.serializers import ItemSerializer
@api_view(['GET'])
def getData(request):
   items=Item.objects.all()
   serializer=ItemSerializer(items,many=True)
   return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
   serializer=ItemSerializer(data=request.data)
   if serializer.is_valid():
      serializer.save()
   return Response(serializer.data)

@api_view(['GET'])
def getById(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response(status=statistics.HTTP_404_NOT_FOUND)
    
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteItem(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def updateItem(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ItemSerializer(item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




