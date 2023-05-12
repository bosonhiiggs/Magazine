from django.contrib.auth.models import User
from django.core.management import BaseCommand

from myauth.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create admins profile')
        user = User.objects.get(username='admin')
        profile = Profile.objects.get_or_create(
            user=user,
            bio='',
            agreement_accepted=False,
            avatar=''
        )

        self.stdout.write(
            self.style.SUCCESS('Successfully added profile to admin!')
        )
