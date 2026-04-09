from django.db import migrations
class Migration(migrations.Migration):
    dependencies = [
        ('Prediction_App', '0007_rename_predictionhistory_predictionsummary'),
    ]
    operations = [
        migrations.RenameModel(
            old_name='PredictionRecord',
            new_name='PredictionHistory',
        ),
        migrations.RenameModel(
            old_name='PredictionSummary',
            new_name='PredictionResult',
        ),
    ]
