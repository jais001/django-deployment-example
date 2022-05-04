import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UdemyProject.settings')

import django

django.setup()

from AppTwo.models import User
from faker import Faker

fake = Faker()


def populate(n=5):
    for entry in range(n):
        fake_name = fake.name().split()
        first_name = fake_name[0]
        last_name = fake_name[1]
        email = fake.email()

        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
        user.save()


if __name__ == '__main__':
    populate(20)
    print('complete')
