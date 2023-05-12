from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Orders


class Command(BaseCommand):
    """
    Create Orders
    """
    def handle(self, *args, **options):
        self.stdout.write('Create order')
        user = User.objects.get(username='admin')
        order = Orders.objects.get_or_create(
            delivery_address='ul Nikitinskay, d 17',
            promocode='1234SALE',
            user=user,
        )
        self.stdout.write(f'Created order {order}')
