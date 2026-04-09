from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('Prediction_App', '0006_predictionhistory_medicine'),
    ]
    operations = [
        migrations.RenameModel(
            old_name='PredictionHistory',
            new_name='PredictionSummary',
        ),
    ]
