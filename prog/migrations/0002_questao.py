# Generated by Django 5.1.2 on 2024-11-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
                ('alternativa_a', models.CharField(max_length=255)),
                ('alternativa_b', models.CharField(max_length=255)),
                ('alternativa_c', models.CharField(max_length=255)),
                ('alternativa_d', models.CharField(max_length=255)),
                ('resposta_correta', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
            ],
        ),
    ]