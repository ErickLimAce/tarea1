# Generated by Django 4.1.7 on 2023-03-31 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("calculadora", "0003_usuario_remove_partidas_jugador_id_usuario_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Partida_Jugadores",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("minutos_jugados", models.IntegerField()),
                ("puntaje", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="usuarios",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name="Partidas_Jugador",
        ),
        migrations.DeleteModel(
            name="Usuario",
        ),
        migrations.AddField(
            model_name="partida_jugadores",
            name="id_usuario",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="calculadora.usuarios"
            ),
        ),
    ]