# Generated by Django 5.1.4 on 2024-12-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartaPresentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('calificacion', models.DecimalField(decimal_places=1, max_digits=3)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('horario', models.CharField(max_length=100)),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]