from email.policy import default
from enum import unique
from tortoise import fields, Model
from pydantic import BaseModel
from datetime import datetime
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.IntField(pk=True, index=True)
    username = fields.CharField(max_length=200)
    email = fields.CharField(max_length=200, unique=True)
    password = fields.CharField(max_length=200)
    is_verified = fields.BooleanField(default=False)
    join_date = fields.DatetimeField(default=datetime.utcnow)


class Business(Model):
    id = fields.IntField(pk=True, index=True)
    business_name = fields.CharField(max_length=200)
    city = fields.CharField(max_length=100)
    region = fields.CharField(max_length=200)
    business_description = fields.TextField()
    logo = fields.CharField(max_length=200, default='default.jpg')
    owner = fields.ForeignKeyField("models.User", related_name='business')


class Product(Model):
    id = fields.IntField(pk=True, index=True)
    name = fields.CharField(max_length=200)
    category = fields.CharField(max_length=100)
    original_price = fields.DecimalField(max_digits=12, decimal_places=2)
    new_price = fields.DecimalField(max_digits=12, decimal_places=2)
    percentage_discount = fields.IntField()
    offer_expiration = fields.DateField(default=datetime.utcnow)
    product_image = fields.CharField(max_length=200, default='product.jpg')
    business = fields.ForeignKeyField(
        'models.Business', related_name='products')


user_pydantic = pydantic_model_creator(
    User, name='User', exclude=("is_verified", ))
user_pydanticIn = pydantic_model_creator(
    User, name='UserIn', exclude_readonly=True)
user_pydanticOut = pydantic_model_creator(
    User, name='UserOut', exclude=("password", ))


business_pydantic = pydantic_model_creator(Business, name='Business')
business_pydanticIn = pydantic_model_creator(
    Business, name='BusinessIn', exclude_readonly=True)

product_pydantic = pydantic_model_creator(Product, name='Product')
product_pydanticIn = pydantic_model_creator(
    Product, name='ProductIn', exclude=("percentage_discount", "id"))
