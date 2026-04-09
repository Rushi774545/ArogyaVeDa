from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('Prediction_App', '0003_rename_frequency_medicine_duration_days'),
    ]
    operations = [
        migrations.CreateModel(
            name='PredictionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('predicted_disease', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
