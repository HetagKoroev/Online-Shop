from typing import List
from ..models import ConcreteProduct


def _get_all_model_objects() -> List[tuple]:
    all_objects = ConcreteProduct.objects.all()
    name_price_description = [(obj.name, obj.price, obj.description) for obj in all_objects]
    return name_price_description
