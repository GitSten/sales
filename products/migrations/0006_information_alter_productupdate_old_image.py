# Generated by Django 5.0.6 on 2024-07-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_productupdate_old_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='productupdate',
            name='old_image',
            field=models.ImageField(blank=True, default=1, upload_to='product_updates/'),
            preserve_default=False,
        ),
    ]
