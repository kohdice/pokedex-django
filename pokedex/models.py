from django.db import models


# Create your models here.
class NationalPokedex(models.Model):
    class Meta:
        db_table = "national_pokedex"

    number = models.PositiveSmallIntegerField(
        verbose_name="National Pokedex number", primary_key=True
    )
    name = models.CharField(
        verbose_name="Pokemon Name", max_length=12, unique=True
    )
    created_by = models.CharField(
        verbose_name="Created by", max_length=255
    )
    created_at = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True
    )
    updated_by = models.CharField(
        verbose_name="Updated by", max_length=255
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated by", auto_now=True
    )


class TypeMaster(models.Model):
    class Meta:
        db_table = "type_mst"

    type = models.CharField(
        verbose_name="Type", max_length=5, primary_key=True
    )
    created_by = models.CharField(
        verbose_name="Created by", max_length=255
    )
    created_at = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True
    )
    updated_by = models.CharField(
        verbose_name="Updated by", max_length=255
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated by", auto_now=True
    )


class PokemonType(models.Model):
    class Meta:
        db_table = "pokemon_type"

    number = models.ForeignKey(
        NationalPokedex,
        verbose_name="National Pokemon Number",
        on_delete=models.PROTECT
    )
    type_1 = models.ForeignKey(
        TypeMaster,
        verbose_name="Type 1",
        related_name="type_1",
        on_delete=models.PROTECT,
    )
    type_2 = models.ForeignKey(
        TypeMaster,
        verbose_name="Type 2",
        related_name="type_2",
        null=True,
        default=False,
        on_delete=models.PROTECT,
    )
    created_by = models.CharField(
        verbose_name="Created by", max_length=255
    )
    created_at = models.DateTimeField(
        verbose_name="Created at", auto_now_add=True
    )
    updated_by = models.CharField(
        verbose_name="Updated by", max_length=255
    )
    updated_at = models.DateTimeField(
        verbose_name="Updated by", auto_now=True
    )
