# Generated by Django 5.1.2 on 2024-11-16 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prog', '0003_questao_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('questoes', models.ManyToManyField(to='prog.questao')),
            ],
        ),
    ]