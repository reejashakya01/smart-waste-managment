from datetime import datetime

from apps.collector.models import CollectionAssignment


def create_collector_assignment(collection):
    collection_assignment = CollectionAssignment.objects.create(
        collection_request=collection,
        requested_at=datetime.now()
    )

    return collection_assignment