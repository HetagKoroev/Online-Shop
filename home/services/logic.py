from typing import List


def get_all_model_objects(model: 'Django model') -> List[tuple]:
    all_objects = model.objects.all()
    return all_objects
