from django.db import models


# Create your models here.
class NationalPokedex(models.Model):
    class Meta:
        db_table = "national_pokedex"

    number = models.PositiveSmallIntegerField(
        verbose_name="Pokedex number", primary_key=True
    )
    name = models.CharField(
        verbose_name="Pokemon Name", max_length=12, unique=True
    )
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class TypeMaster(models.Model):
    class Meta:
        db_table = "type_mst"

    type = models.CharField(
        verbose_name="Type", max_length=5, primary_key=True
    )
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class AbilityMaster(models.Model):
    class Meta:
        db_table = "ability_mst"

    ability = models.CharField(
        verbose_name="Ability", max_length=8, primary_key=True
    )
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class FormMaster(models.Model):
    class Meta:
        db_table = "forms_mst"

    forms = models.CharField(
        verbose_name="forms", max_length=10, primary_key=True
    )
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class RegionMaster(models.Model):
    class Meta:
        db_table = "region_mst"

    region = models.CharField(
        verbose_name="Region", max_length=4, primary_key=True
    )
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class PokemonStatus(models.Model):
    class Meta:
        db_table = "pokemon_status"

    number = models.ForeignKey(
        NationalPokedex,
        verbose_name="National Pokedex Number",
        on_delete=models.PROTECT,
    )
    forms = models.ForeignKey(
        FormMaster,
        verbose_name="Forms",
        null=True,
        default=None,
        on_delete=models.PROTECT,
    )
    regional_variant = models.ForeignKey(
        RegionMaster,
        verbose_name="Regional variant",
        null=True,
        default=None,
        on_delete=models.PROTECT,
    )
    mega_evolution = models.BooleanField(
        verbose_name="Mega Evolution", default=False
    )
    primal_reversion = models.BooleanField(
        verbose_name="Primal Reversion", default=False
    )
    hp = models.PositiveSmallIntegerField(verbose_name="Hit Point")
    attack = models.PositiveSmallIntegerField(
        verbose_name="Attack",
    )
    defense = models.PositiveSmallIntegerField(verbose_name="Defense")
    special_attack = models.PositiveSmallIntegerField(
        verbose_name="Special Attack"
    )
    special_defense = models.PositiveSmallIntegerField(
        verbose_name="Special Defense"
    )
    speed = models.PositiveSmallIntegerField(verbose_name="Speed")
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
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
