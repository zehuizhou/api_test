from peewee import *

database = MySQLDatabase('xxy_message', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AppConfig(BaseModel):
    access_key_id = CharField(null=True)
    access_key_secret = CharField(null=True)
    app_code = BigIntegerField(null=True)
    app_key_android = CharField(null=True)
    app_key_ios = CharField(null=True)
    app_name = CharField(null=True)
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    region_id = CharField(null=True)
    status = IntegerField(null=True)

    class Meta:
        table_name = 'app_config'

class Comments(BaseModel):
    comment = CharField(null=True)
    comment_type = IntegerField()
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    source_user_avatar = CharField(null=True)
    source_user_id = BigIntegerField()
    source_user_name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    target_object_id = BigIntegerField()
    target_object_type = IntegerField()
    target_user_id = BigIntegerField(index=True, null=True)
    target_user_name = CharField(null=True)
    target_user_read_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'comments'

class Message(BaseModel):
    company_id = BigIntegerField(null=True)
    content = CharField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    title = CharField()
    type = IntegerField()
    user_id = BigIntegerField()

    class Meta:
        table_name = 'message'

class PushRecord(BaseModel):
    app_code = BigIntegerField(null=True)
    app_name = CharField(null=True)
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_pushed = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_read = IntegerField(constraints=[SQL("DEFAULT 1")])
    message_id = BigIntegerField()
    message_type = IntegerField()
    read_stat = BigIntegerField(null=True)
    source_id = BigIntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    target_type = BigIntegerField(null=True)
    target_user_id = BigIntegerField()
    target_value = BigIntegerField(null=True)

    class Meta:
        table_name = 'push_record'

class PushScopeConfig(BaseModel):
    company_id = BigIntegerField(null=True)
    depart_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    message_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    target_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    target_type_class = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    target_user_ids = CharField(null=True)

    class Meta:
        table_name = 'push_scope_config'

class PushScopeConfigDept(BaseModel):
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    msg_type = CharField(null=True)
    src_dept_id = BigIntegerField(null=True)
    status = IntegerField(null=True)
    up_levels = IntegerField(null=True)

    class Meta:
        table_name = 'push_scope_config_dept'

