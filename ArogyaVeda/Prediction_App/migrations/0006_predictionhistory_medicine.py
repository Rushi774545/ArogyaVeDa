from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('Prediction_App', '0005_predictionrecord_probabilities_json'),
    ]
    operations = [
        migrations.AddField(
            model_name='predictionhistory',
            name='medicine',
            field=models.TextField(blank=True, null=True),
        ),
    ]
