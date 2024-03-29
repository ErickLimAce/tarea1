# Generated by Django 4.1.7 on 2023-03-30 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("calculadora", "0002_usuarios_partidas_jugador"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="partidas_jugador",
            name="id_usuario",
        ),
        migrations.AlterField(
            model_name="partidas_jugador",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name="Usuarios",
        ),
        migrations.AddField(
            model_name="partidas_jugador",
            name="usuario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="calculadora.usuario",
            ),
            preserve_default=False,
        ),
    ]
