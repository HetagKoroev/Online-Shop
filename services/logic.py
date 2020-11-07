def get_all_objects_from_model(model: 'Django model') -> 'django.db.models.query.QuerySet':
    all_objects = model.objects.all()
    return all_objects
