from peewee import *

database = MySQLDatabase('xxy_checkin', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Checkin(BaseModel):
    address = CharField()
    checkin_latitude = DecimalField()
    checkin_longitude = DecimalField()
    company_id = BigIntegerField()
    company_latitude = DecimalField(null=True)
    company_longitude = DecimalField(null=True)
    company_name = CharField()
    customer_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    imei = CharField(null=True)
    phone_name = CharField(null=True)
    remarks = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'checkin'

class CheckinImage(BaseModel):
    avatar = CharField()
    checkin_id = BigIntegerField()
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'checkin_image'

