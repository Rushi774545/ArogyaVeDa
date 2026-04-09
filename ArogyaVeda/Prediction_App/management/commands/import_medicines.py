import csv
import os
from django.core.management.base import BaseCommand
from Prediction_App.models import Medicine
class Command(BaseCommand):
    help = 'Import medicines from CSV'
    def handle(self, *args, **kwargs):
        csv_path = 'medicine_table.csv'
        if not os.path.exists(csv_path):
            from django.conf import settings
            csv_path = os.path.join(settings.BASE_DIR, 'medicine_table.csv')
        if not os.path.exists(csv_path):
            self.stdout.write(self.style.ERROR(f'File not found: {csv_path}'))
            return
        with open(csv_path, 'r') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                Medicine.objects.update_or_create(
                    medicine_name=row['medicine_name'],
                    disease_name=row['disease_name'],
                    defaults={
                        'dosage': row['dosage'],
                        'duration_days': row['duration_days'],
                        'description': row['description']
                    }
                )
                count += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {count} medicines'))
