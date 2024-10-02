from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Location(Model):
    id = fields.IntField(primary_key=True)
    address = fields.CharField(max_length=512, null=True)
    latitude = fields.FloatField()
    longitude = fields.FloatField()
    location_type = fields.CharField(max_length=64, null=True)


class Blacklist(Model):
    id = fields.IntField(primary_key=True)
    location = fields.ForeignKeyField(
        "models.Location", related_name="blacklisted_location"
    )
    user = fields.ForeignKeyField(
        "models.User", related_name="user_blacklisted_location"
    )


Location_Pydantic = pydantic_model_creator(Location)
Blacklist_Pydantic = pydantic_model_creator(Blacklist)