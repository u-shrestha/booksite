# Generated by Django 3.1.2 on 2021-01-29 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tntapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product')),
                ('category', models.CharField(max_length=50)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.RemoveField(
            model_name='image',
            name='album',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.RemoveField(
            model_name='package',
            name='category',
        ),
        migrations.RemoveField(
            model_name='package',
            name='feature',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.DeleteModel(
            name='Subscribe',
        ),
        migrations.DeleteModel(
            name='Testimonial',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Package',
        ),
        migrations.DeleteModel(
            name='PackageCategory',
        ),
        migrations.DeleteModel(
            name='PackageFeature',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(blank=True, to='tntapp.Product'),
        ),
    ]
