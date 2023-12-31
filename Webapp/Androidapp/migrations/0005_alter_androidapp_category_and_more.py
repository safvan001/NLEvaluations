# Generated by Django 4.2.1 on 2023-08-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Androidapp', '0004_androidapp_category_androidapp_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='androidapp',
            name='category',
            field=models.CharField(choices=[('Entertainment', 'Entertainment'), ('Utility', 'Utility'), ('Others', 'Others')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='androidapp',
            name='subcategory',
            field=models.CharField(choices=[('Social Media', 'Social Media'), ('Media Player', 'Media Player'), ('Gamming', 'Gamming')], default='1', max_length=50),
        ),
    ]
