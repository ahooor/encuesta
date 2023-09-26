# Generated by Django 4.2.4 on 2023-09-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ManyToManyField(blank=True, to='encuesta.topic'),
        ),
    ]
