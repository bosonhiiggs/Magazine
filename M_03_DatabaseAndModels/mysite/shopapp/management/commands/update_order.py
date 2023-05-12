from shopapp.models import Orders, Product
from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Orders.objects.first()
        if not order:
            self.stdout.write('no order found')
            return

        products = Product.objects.all()

        for product in products:
            order.products.add(product)

        order.save()
        self.stdout.write(self.style.SUCCESS(f'Successfuly added products {order.products.all()} to order {order}'))