from django.db import migrations, models
class Migration(migrations.Migration):
    dependencies = [
        ('user', '0001_initial'),
    ]
    operations = [
        migrations.AddField(
            model_name='patient',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
    ]
