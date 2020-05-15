from peewee import *

database = MySQLDatabase('xxy_report', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Report(BaseModel):
    company_id = BigIntegerField()
    content = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    template_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'report'

class ReportActivity(BaseModel):
    activity_id = BigIntegerField(unique=True)
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    report_id = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'report_activity'

class ReportCopy(BaseModel):
    company_id = BigIntegerField()
    copy_to_dept_code = CharField(null=True)
    copy_to_user_id = BigIntegerField(null=True)
    copy_to_user_name = CharField(null=True)
    copy_type = IntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    report_id = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    template_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'report_copy'

class ReportNotCopy(BaseModel):
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    not_copy_to_user_id = BigIntegerField(null=True)
    not_copy_to_user_name = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'report_not_copy'

class ReportRead(BaseModel):
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    is_read = IntegerField()
    report_id = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'report_read'
        indexes = (
            (('company_id', 'user_id', 'report_id'), False),
        )

class ReportSchedule(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    report_id = BigIntegerField()
    schedule_id = BigIntegerField(index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'report_schedule'

class Template(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'template'

class TemplateField(BaseModel):
    company_id = BigIntegerField(index=True)
    function = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    is_null = IntegerField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    template_id = BigIntegerField(index=True)
    type = IntegerField()

    class Meta:
        table_name = 'template_field'

class TemplateUser(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    template_id = BigIntegerField(index=True)
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'template_user'

class Terminal(BaseModel):
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    name = CharField(null=True)
    status = IntegerField(null=True)
    terminal_id = BigIntegerField(null=True)
    workshop_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'terminal'

class TerminalGroup(BaseModel):
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    group_id = BigIntegerField(null=True)
    id = BigAutoField()
    status = IntegerField(null=True)
    terminal_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'terminal_group'

class TerminalStatus(BaseModel):
    alarm_status = IntegerField(null=True)
    company_id = BigIntegerField(null=True)
    count = IntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    is_count_cross_zero = CharField(null=True)
    running_status = IntegerField(null=True)
    standby_status = IntegerField(null=True)
    status = IntegerField(null=True)
    terminal_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'terminal_status'

class Workshop(BaseModel):
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    name = CharField(null=True)
    status = IntegerField(null=True)

    class Meta:
        table_name = 'workshop'

