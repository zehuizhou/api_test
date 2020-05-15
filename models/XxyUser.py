from peewee import *
database = MySQLDatabase('xxy_user', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Approve(BaseModel):
    apply_id = BigIntegerField()
    apply_name = CharField()
    apply_position = CharField(null=True)
    approve_status = IntegerField()
    company_id = BigIntegerField(null=True)
    content = CharField()
    flow_no = IntegerField()
    flow_total = IntegerField()
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    model_id = BigIntegerField()
    model_name = CharField()
    remark = CharField(null=True)
    status = IntegerField(null=True)

    class Meta:
        table_name = 'approve'

class ApproveAppendix(BaseModel):
    approve_id = BigIntegerField()
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(null=True)
    url = CharField()

    class Meta:
        table_name = 'approve_appendix'

class ApproveCopy(BaseModel):
    approve_id = BigIntegerField(null=True)
    approve_status = IntegerField(null=True)
    company_id = BigIntegerField(null=True)
    copy_id = BigIntegerField(null=True)
    copy_name = CharField(null=True)
    copy_role = CharField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    model_id = BigIntegerField(null=True)
    status = IntegerField(null=True)

    class Meta:
        table_name = 'approve_copy'

class ApproveFlow(BaseModel):
    approve_id = BigIntegerField()
    approve_status = IntegerField(null=True)
    approver_id = BigIntegerField()
    approver_name = CharField()
    approver_position = CharField(null=True)
    comment_id = BigIntegerField(null=True)
    company_id = BigIntegerField(null=True)
    flow_no = IntegerField()
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    model_id = BigIntegerField()
    model_name = CharField()
    status = IntegerField(null=True)

    class Meta:
        table_name = 'approve_flow'

class ApproveImage(BaseModel):
    approve_id = BigIntegerField()
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(null=True)
    url = CharField()

    class Meta:
        table_name = 'approve_image'

class ApproveModel(BaseModel):
    company_id = BigIntegerField(null=True)
    format = CharField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    model_id = BigIntegerField(null=True)
    model_name = CharField(null=True)
    status = IntegerField(null=True)

    class Meta:
        table_name = 'approve_model'

class ApproveModelUser(BaseModel):
    company_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    model_id = BigIntegerField(null=True)
    model_name = CharField(null=True)
    status = IntegerField(null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'approve_model_user'

class Company(BaseModel):
    address = CharField()
    contact = CharField()
    credit_code = CharField(unique=True)
    email = CharField(null=True)
    enter_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    legal_person = CharField()
    licence = CharField()
    logo = CharField(null=True)
    mobile = CharField()
    name = CharField()
    remark = CharField(null=True)
    short_name = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'company'

class CompanyDepartment(BaseModel):
    code = CharField()
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    level = IntegerField()
    name = CharField()
    parent_id = BigIntegerField()
    roles = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'company_department'

class CompanyDepartmentUser(BaseModel):
    code = CharField()
    company_department_id = BigIntegerField(index=True)
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    is_supervisor = IntegerField(constraints=[SQL("DEFAULT 0")])
    position = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'company_department_user'

class CompanyUser(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    is_current = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    is_login = BigIntegerField(constraints=[SQL("DEFAULT 1")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'company_user'

class Module(BaseModel):
    code = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    package_name = CharField()
    remark = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'module'

class SaleStatistics(BaseModel):
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    status = IntegerField(null=True)

    class Meta:
        table_name = 'sale_statistics'

class User(BaseModel):
    avatar = CharField(null=True)
    birthday = DateField(null=True)
    company_id = BigIntegerField(null=True)
    gender = IntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_login = IntegerField(null=True)
    login_fail_times = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    mobile = CharField(unique=True)
    name = CharField()
    password = CharField()
    personal_signature = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'user'

class UserLoginLog(BaseModel):
    device = CharField(null=True)
    device_type = IntegerField(constraints=[SQL("DEFAULT 2")], null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    imei = CharField(null=True)
    ip = CharField()
    os = CharField(null=True)
    status = IntegerField()
    user_id = BigIntegerField()
    version = CharField(null=True)

    class Meta:
        table_name = 'user_login_log'

class UserModule(BaseModel):
    company_id = BigIntegerField(index=True, null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    module_id = BigIntegerField(index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'user_module'

class UserSalt(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    salt = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(unique=True)

    class Meta:
        table_name = 'user_salt'

class XxyAppVersion(BaseModel):
    client_os = IntegerField()
    description = CharField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_release = DateTimeField()
    id = BigAutoField()
    is_force_update = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    url = CharField(null=True)
    version = CharField()

    class Meta:
        table_name = 'xxy_app_version'

models_map = {

}