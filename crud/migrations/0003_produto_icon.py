# Generated by Django 4.1.2 on 2022-10-23 03:27

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_produto_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='icon',
            field=stdimage.models.StdImageField(force_min_size=False, null=True, upload_to='icon', variations={'thumb': (124, 124)}, verbose_name='Imagem'),
        ),
    ]
