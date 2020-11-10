from django.db.models.query import QuerySet
from django.db.models import Model


def get_all_objects_from_model(model: Model) -> QuerySet:
    all_objects = model.objects.all()
    return all_objects
