def _get_all_model_objects(model: 'Django model') -> 'django.db.models.query.QuerySet':
    all_objects = model.objects.all()
    return all_objects
