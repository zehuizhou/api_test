from peewee import *

database = MySQLDatabase('xxy_schedule', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class NoFollowStat(BaseModel):
    changed_date_ids = CharField(null=True)
    changed_date_number = IntegerField(constraints=[SQL("DEFAULT 0")])
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_stat = DateTimeField(null=True)
    id = BigAutoField()
    need_follow_up_ids = CharField(null=True)
    need_follow_up_number = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'no_follow_stat'

class Schedule(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_activity_id = BigIntegerField(null=True)
    customer_id = BigIntegerField(index=True)
    customer_visit_id = BigIntegerField(index=True, null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_visit = DateTimeField()
    id = BigAutoField()
    schedule_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)
    visit_policy = CharField(null=True)

    class Meta:
        table_name = 'schedule'

class ScheduleCheckin(BaseModel):
    checkin_id = BigIntegerField(index=True)
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    schedule_id = BigIntegerField(index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'schedule_checkin'

class ScheduleCustomerVisit(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_visit_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    schedule_id = BigIntegerField(index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'schedule_customer_visit'

