import csv
from datetime import datetime
from django.core.management import BaseCommand
from commanders.models import Commander


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Name of the CSV file with commanders'
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                if (row['birth'] != 'null'):
                    birth = datetime.strptime(row['birth'], '%Y-%m-%d').date()
                else:
                    birth = None
                if (row['death'] != 'null'):
                    death = datetime.strptime(row['death'], '%Y-%m-%d').date()
                else:
                    death = None
                procedence = row['procedence']

                self.stdout.write(self.style.NOTICE(name))

                Commander.objects.create(
                    name=name,
                    birth=birth,
                    death=death,
                    procedence=procedence,
                )

        self.stdout.write(self.style.SUCCESS('COMMANDERS SUCCESFULLY IMPORTED'))
