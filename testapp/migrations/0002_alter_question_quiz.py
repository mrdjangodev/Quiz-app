# Generated by Django 4.0.5 on 2022-06-16 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_alter_quiz_image'),
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quizz.quiz'),
        ),
    ]
