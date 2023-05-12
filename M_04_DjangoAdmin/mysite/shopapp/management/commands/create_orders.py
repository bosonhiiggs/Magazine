from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create order')
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_address='Ul Nevskogo d 8',
            promocode='1234SALE1234',
            user=user
        )

        self.stdout.write(self.style.SUCCESS('Order created'))