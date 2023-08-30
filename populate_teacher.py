import os
import random
import django
from faker import Faker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
from first_app.models import Teacher

fakegen = Faker()


def populate(n=5):
    subjects = ['Physics', 'Biology', 'Mathematics', 'Foreign Language']
    # print(n)
    for entry in range(n):
        fake_name = fakegen.name()
        fake_subject = random.choices(subjects)[0] # One random from list
        print(f'{fake_name}, {fake_subject}')
        Teacher.objects.get_or_create(name=fake_name, subject=fake_subject)

populate(10)
print('Added Into Teacher model.')
