from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('Prediction_App', '0004_predictionhistory'),
    ]
    operations = [
        migrations.AddField(
            model_name='predictionrecord',
            name='probabilities_json',
            field=models.TextField(blank=True, null=True),
        ),
    ]
