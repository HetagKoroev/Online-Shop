from typing import List


def get_all_model_objects(model: 'Django model') -> List[tuple]:
    all_objects = model.objects.all()
    name_price_description = [obj for obj in all_objects]
    return name_price_description
