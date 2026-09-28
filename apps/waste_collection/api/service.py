from apps.waste_collection.models import CollectionActivity

def create_collection_activity_log(collection, message):
    activity = CollectionActivity.objects.create(
        collection = collection,
        name = message
    )
    return activity
