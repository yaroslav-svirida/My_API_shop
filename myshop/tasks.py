import logging

from myAPIshop import app
from myshop.models import Product, ProductInBasket


@app.task
def group_by_color():
    products = Product.objects.all()
    for product in products:
        if 'ATN0001' in product.article:
            product.colors_name_id = 1
            product.save()
            logging.error(f" 'ATN0001' {product.name}")

        elif 'ATN0002' in product.article:
            product.colors_name_id = 2
            product.save()
            logging.error(f" 'ATN0002' {product.name}")
        elif 'ATN0003' in product.article:
            product.colors_name_id = 3
            product.save()
            logging.error(f" 'ATN0003' {product.name}")
        elif 'ATN0004' in product.article:
            product.colors_name_id = 4
            product.save()
            logging.error(f" 'ATN0004' {product.name}")
        elif 'ATN0005' in product.article:
            product.colors_name_id = 5
            product.save()
            logging.error(f" 'ATN0005' {product.name}")
        elif 'ATN0006' in product.article:
            product.colors_name_id = 6
            product.save()
            logging.error(f" 'ATN0006' {product.name}")
        elif 'ATN0007' in product.article:
            product.colors_name_id = 7
            product.save()
            logging.error(f" 'ATN0007' {product.name}")
        elif 'ATN0007' in product.article:
            product.colors_name_id = 7
            product.save()
            logging.error(f" 'ATN0007' {product.name}")
        elif 'ATN0008' in product.article:
            product.colors_name_id = 8
            product.save()
            logging.error(f" 'ATN0008' {product.name}")
        elif 'ATN0009' in product.article:
            product.colors_name_id = 9
            product.save()
            logging.error(f" 'ATN0009' {product.name}")

        elif 'ATN001' in product.article:
            product.colors_name_id = 10
            product.save()
            logging.error(f" 'ATN001' {product.name}")


@app.task
def clear_basket():
    products = ProductInBasket.objects.all()
    products.delete()

