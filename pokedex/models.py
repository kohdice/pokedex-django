from django.db import models


# Create your models here.
class NationalPokedex(models.Model):
    class Meta:
        db_table = "national_pokedex"

    number = models.PositiveSmallIntegerField(
        verbose_name="Pokedex number",
        primary_key=True
    )
    name = models.CharField(
        verbose_name="Pokemon Name",
        max_length=12,
        unique=True,
        null=False
    )


class PokemonType(models.Model):
    class Meta:
        db_table = "pokemon_type"

    type = models.CharField(
        verbose_name="Type",
        max_length=5,
        primary_key=True
    )


class PokemonAbility(models.Model):
    class Meta:
        db_table = "pokemon_ability"

    ability = models.CharField(
        verbose_name="Ability",
        max_length=8,
        primary_key=True
    )


class PokemonForms(models.Model):
    class Meta:
        db_table = "pokemon_forms"

    forms = models.CharField(
        verbose_name="forms",
        max_length=10,
        primary_key=True
    )


class Region(models.Model):
    class Meta:
        db_table = "region"

    region = models.CharField(
        verbose_name="Region",
        max_length=4,
        primary_key=True
    )


class PokemonStatus(models.Model):
    class Meta:
        db_table = "pokemon_status"

    national_pokedex_number = models.ForeignKey(
        NationalPokedex,
        verbose_name="National Pokedex Number",
        related_name="national_pokedex_number",
        null=False,
        on_delete=models.PROTECT
    )
    pokemon_name = models.ForeignKey(
        NationalPokedex,
        verbose_name="Pokemon Name",
        related_name="pokemon_name",
        null=False,
        on_delete=models.PROTECT
    )
    type_1 = models.ForeignKey(
        PokemonType,
        verbose_name="Type_1",
        related_name="type_1",
        null=False,
        on_delete=models.PROTECT
    )
    type_2 = models.ForeignKey(
        PokemonType,
        verbose_name="Type_2",
        related_name="type_2",
        default=None,
        on_delete=models.PROTECT
    )
    ability_1 = models.ForeignKey(
        PokemonAbility,
        verbose_name="Ability_1",
        related_name="ability_1",
        null=False,
        on_delete=models.PROTECT
    )
    ability_2 = models.ForeignKey(
        PokemonAbility,
        verbose_name="Ability_2",
        related_name="ability_2",
        default=None,
        on_delete=models.PROTECT
    )
    hidden_ability = models.ForeignKey(
        PokemonAbility,
        verbose_name="Hidden_Ability",
        related_name="hidden_ability",
        default=None,
        on_delete=models.PROTECT
    )
    hp = models.PositiveSmallIntegerField(
        verbose_name="Hit Point",
        null=False
    )
    attack = models.PositiveSmallIntegerField(
        verbose_name="Attack",
        null=False
    )
    defense = models.PositiveSmallIntegerField(
        verbose_name="Defense",
        null=False
    )
    special_attack = models.PositiveSmallIntegerField(
        verbose_name="Special Attack",
        null=False
    )
    special_defense = models.PositiveSmallIntegerField(
        verbose_name="Special Defense",
        null=False
    )
    speed = models.PositiveSmallIntegerField(
        verbose_name="Speed",
        null=False
    )
    forms = models.ForeignKey(
        PokemonForms,
        verbose_name="Forms",
        default=False,
        on_delete=models.PROTECT
    )
    regional_variant = models.ForeignKey(
        Region,
        verbose_name="Regional variant",
        default=None,
        on_delete=models.PROTECT
    )
    mega_evolution = models.BooleanField(
        verbose_name="Mega Evolution",
        default=False
    )
    primal_reversion = models.BooleanField(
        verbose_name="Primal Reversion",
        default=False
    )
