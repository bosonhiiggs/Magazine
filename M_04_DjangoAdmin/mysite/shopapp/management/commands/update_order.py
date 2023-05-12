from django.core.management import BaseCommand

from shopapp.models import Order, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()
        if not order:
            self.stdout.write('No order yet')

        products = Product.objects.all()

        for product in products:
            order.product.add(product)

        order.save()

        self.stdout.write(self.style.SUCCESS(
            f'Successfuly added products {order.product.all()} to order {order}'
        ))