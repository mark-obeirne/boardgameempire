def all_categories(request):
    """ Return all categories from Category model """
    from products.models import Category
    return {
        'all_categories': Category.objects.all().order_by('friendly_name')
    }


def all_mechanics(request):
    """ Return all categories from Category model """
    from products.models import Mechanic
    return {
        'all_mechanics': Mechanic.objects.all().order_by('friendly_name')
    }
