# Generated by Django 5.1.2 on 2024-11-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prog', '0010_respostausuario_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionario',
            name='prazo_disponibilidade',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questao',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='questoes/'),
        ),
    ]
