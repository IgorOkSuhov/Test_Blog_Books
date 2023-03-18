from faker import Faker

from user.models import Book

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'generate random books'

    def handle(self, *args, **options):
        fake = Faker()
        for _ in range(10_000):
            try:
                title = fake.last_name()
                Book.objects.create(
                    title = title,
                )
            except IntegrityError:
                print(title)
    print(Book.objects.count())
