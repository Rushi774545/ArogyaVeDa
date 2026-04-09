from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('Prediction_App', '0002_medicine'),
    ]
    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='frequency',
            new_name='duration_days',
        ),
    ]
