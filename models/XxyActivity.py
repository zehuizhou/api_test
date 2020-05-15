from peewee import *

database = MySQLDatabase('xxy_activity', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Activity(BaseModel):
    approval_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    behavior_id = BigIntegerField(index=True)
    behavior_type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    company_id = BigIntegerField(index=True)
    content = CharField()
    customer_id = BigIntegerField(index=True, null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    operation_id = BigIntegerField(index=True, null=True)
    operation_type = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'activity'

class ActivityBak(BaseModel):
    approval_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    behavior_id = BigIntegerField(index=True)
    behavior_type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    company_id = BigIntegerField(index=True)
    content = CharField()
    customer_id = BigIntegerField(index=True, null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    operation_id = BigIntegerField(index=True, null=True)
    operation_type = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'activity_bak'

class ActivityReply(BaseModel):
    activity_id = BigIntegerField()
    company_id = BigIntegerField()
    content = CharField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    reply_from = BigIntegerField()
    reply_to = BigIntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'activity_reply'

