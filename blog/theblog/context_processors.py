from .models import Category

def category_list_processor(request):
    cat_list = Category.objects.all()
    return {'cat_list': cat_list}