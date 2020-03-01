# Generated by Django 3.0.3 on 2020-02-28 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Карточка для сравнения',
                'verbose_name_plural': 'Карточки для сравнения',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('question', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Comparison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('left', 'Левый'), ('right', 'Правый')], max_length=20, verbose_name='Выбор')),
                ('left_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='left_comparisons', to='core.Card')),
                ('right_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='right_comparisons', to='core.Card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Poll'),
        ),
    ]
