from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_items(request):
    search_query = request.GET.get('search', '').strip()  # Ensure it's a string and not None

    print(f"Search Query Received: {search_query}")  # Debugging output

    # Retrieve items from the database with filtering
    if search_query:
        items = Item.objects.filter(name__icontains=search_query)
        print(f"Filtered Items: {items}")  # Debugging output
    else:
        items = Item.objects.all()

    # If no items exist in the database, return static sample data
    if not items.exists():
        static_data = [
            {"id": 1, "name": "Laptop", "description": "High-performance laptop", "price": 1200.99},
            {"id": 2, "name": "Smartphone", "description": "Latest model smartphone", "price": 799.49},
            {"id": 3, "name": "Headphones", "description": "Noise-canceling headphones", "price": 199.99},
        ]
        return Response(static_data)

    # Serialize and return database items if they exist
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
