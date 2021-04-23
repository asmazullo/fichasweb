# Generated by Django 3.2 on 2021-04-19 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bloco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloco_ordem', models.IntegerField(default=1000)),
                ('bloco_nome', models.CharField(max_length=200)),
                ('bloco_pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalidade_nome', models.CharField(max_length=200)),
                ('modalidade_pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_ordem', models.IntegerField(default=1000)),
                ('nivel_nome', models.CharField(max_length=200)),
                ('nivel_pub_date', models.DateField(auto_now_add=True)),
                ('modalidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.modalidade')),
            ],
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimento_dificuldade', models.CharField(choices=[('A', 'Muito Fácil: A'), ('B', 'Fácil: B'), ('C', 'Moderado: C'), ('D', 'Difícil: D'), ('E', 'Muito Difícil: E')], default='A', max_length=1)),
                ('movimento_pub_date', models.DateField(auto_now_add=True)),
                ('movimento_ativo', models.BooleanField(default=True)),
                ('movimento_nome', models.CharField(max_length=200)),
                ('movimento_explicacao', models.TextField(default='')),
                ('bloco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.bloco')),
            ],
        ),
        migrations.AddField(
            model_name='bloco',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.nivel'),
        ),
    ]