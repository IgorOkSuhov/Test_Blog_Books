from faker import Faker


from user.models import User

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'generate random data'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10_000):
            try:
                email = fake.email()
                User.objects.create(
                    email = email,
                    first_name = fake.first_name(),
                    last_name = fake.last_name(),
                )
            except IntegrityError:
                print(email)
    print(User.objects.count())


