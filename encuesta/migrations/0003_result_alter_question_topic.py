# Generated by Django 4.2.4 on 2023-10-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0002_topic_question_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ManyToManyField(blank=True, related_name='topic', to='encuesta.topic'),
        ),
    ]
