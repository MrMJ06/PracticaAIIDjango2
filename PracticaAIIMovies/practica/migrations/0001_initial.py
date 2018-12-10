# Generated by Django 2.0 on 2018-12-10 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('artista_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('pais', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Discografica',
            fields=[
                ('discografica_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('pais', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('estilo_id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tiempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.IntegerField()),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practica.Artista')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='tiempo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practica.Usuario'),
        ),
        migrations.AddField(
            model_name='artista',
            name='discografica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='practica.Discografica'),
        ),
        migrations.AddField(
            model_name='artista',
            name='estilos',
            field=models.ManyToManyField(blank=True, default=[], to='practica.Estilo'),
        ),
    ]
