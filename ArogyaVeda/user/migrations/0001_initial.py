from django.db import migrations, models
class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('patient_id', models.IntegerField(blank=True, editable=False, null=True, unique=True)),
            ],
        ),
    ]
