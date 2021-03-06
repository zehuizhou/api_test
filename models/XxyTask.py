from peewee import *

database = MySQLDatabase('xxy_task', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AttendanceStat(BaseModel):
    all_customers = IntegerField(null=True)
    attendence_already = IntegerField(null=True)
    attendence_late = IntegerField(null=True)
    attendence_missed = IntegerField(null=True)
    attendence_out = IntegerField(null=True)
    checkin_missed = IntegerField(null=True)
    checkin_persons = IntegerField(null=True)
    checkin_times = IntegerField(null=True)
    company_id = BigIntegerField(null=True)
    date = CharField(null=True)
    department_code = CharField(null=True)
    department_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    log_miss = IntegerField(null=True)
    log_ok = IntegerField(null=True)
    new_customers = IntegerField(null=True)
    sign_order_money = DecimalField(null=True)
    sign_order_month_money = DecimalField(null=True)
    sign_order_month_mount = IntegerField(null=True)
    sign_order_mount = IntegerField(null=True)
    status = IntegerField(null=True)
    user_id = BigIntegerField(null=True)
    visit_actual = IntegerField(null=True)
    visit_no_plan = IntegerField(null=True)
    visit_plan = IntegerField(null=True)

    class Meta:
        table_name = 'attendance_stat'

class CheckinStat(BaseModel):
    checkin_missed = IntegerField(null=True)
    checkin_persons = IntegerField(null=True)
    checkin_times = IntegerField(null=True)
    company_id = BigIntegerField(null=True)
    date = CharField(null=True)
    department_code = CharField(null=True)
    department_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    status = IntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'checkin_stat'

class LogStat(BaseModel):
    company_id = BigIntegerField(null=True)
    date = CharField(null=True)
    department_code = CharField(null=True)
    department_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    log_miss = IntegerField(null=True)
    log_ok = IntegerField(null=True)
    status = IntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'log_stat'

class SaleStat(BaseModel):
    all_customers = IntegerField(null=True)
    company_id = BigIntegerField(null=True)
    date = CharField(null=True)
    department_code = CharField(null=True)
    department_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    new_customers = IntegerField(null=True)
    sign_order_money = DecimalField(null=True)
    sign_order_month_money = DecimalField(null=True)
    sign_order_month_mount = IntegerField(null=True)
    sign_order_mount = IntegerField(null=True)
    status = IntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'sale_stat'

class Task(BaseModel):
    company_id = BigIntegerField(index=True)
    deadline = DateField()
    description = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    task_status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    title = CharField()
    type = IntegerField()
    type_id = BigIntegerField(index=True, null=True)
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'task'

class TaskReply(BaseModel):
    company_id = BigIntegerField()
    content = CharField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    reply_from = BigIntegerField()
    reply_to = BigIntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    task_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'task_reply'

class TaskUser(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_cadre = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_top = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    task_from = BigIntegerField(index=True)
    task_id = BigIntegerField(index=True)
    task_to = BigIntegerField(index=True)

    class Meta:
        table_name = 'task_user'

class VisitStat(BaseModel):
    company_id = BigIntegerField(null=True)
    date = CharField(null=True)
    department_code = CharField(null=True)
    department_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    status = IntegerField(null=True)
    user_id = BigIntegerField(null=True)
    visit_actual = IntegerField(null=True)
    visit_no_plan = IntegerField(null=True)
    visit_plan = IntegerField(null=True)

    class Meta:
        table_name = 'visit_stat'

