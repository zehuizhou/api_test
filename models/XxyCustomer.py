from peewee import *

database = MySQLDatabase('xxy_customer', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class ActivityCustomerRequirement(BaseModel):
    company_id = BigIntegerField()
    customer_requirement_id = BigIntegerField(index=True)
    customer_requirement_name = CharField()
    customer_visit_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'activity_customer_requirement'

class ActivityObjection(BaseModel):
    company_id = BigIntegerField()
    customer_visit_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    objection_id = BigIntegerField()
    objection_name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'activity_objection'

class Allocation(BaseModel):
    company_id = BigIntegerField(index=True)
    content = CharField(null=True)
    create_user_avatar = CharField(null=True)
    create_user_id = BigIntegerField(index=True)
    create_user_name = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    new_user_id = BigIntegerField()
    new_user_name = CharField(null=True)
    number = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'allocation'

class AllocationCustomer(BaseModel):
    allocation_id = BigIntegerField()
    color_value = CharField()
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField()
    customer_name = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    level_id = BigIntegerField()
    level_name = CharField()
    old_user_id = BigIntegerField()
    old_user_name = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'allocation_customer'

class City(BaseModel):
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    province_id = BigIntegerField(index=True)
    sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'city'

class Color(BaseModel):
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    value = CharField()

    class Meta:
        table_name = 'color'

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

class Customer(BaseModel):
    address = CharField()
    city_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    company_id = BigIntegerField()
    customer_industry_annual_value_id = BigIntegerField()
    customer_industry_id = BigIntegerField()
    customer_industry_scale_id = BigIntegerField()
    customer_industry_type_id = BigIntegerField()
    customer_level_id = BigIntegerField()
    customer_source_id = BigIntegerField()
    customer_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    district_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_level = DateTimeField()
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    latitude = DecimalField(null=True)
    longitude = DecimalField(null=True)
    major_business = CharField(null=True)
    name = CharField()
    profitability = CharField(null=True)
    province_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    remark = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer'
        indexes = (
            (('name', 'company_id'), False),
        )

class CustomerCommunicate(BaseModel):
    company_id = BigIntegerField()
    content = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    visit_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'customer_communicate'

class CustomerContact(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_contact_type_id = BigIntegerField()
    customer_id = BigIntegerField()
    customer_opportunity_id = BigIntegerField(null=True)
    department = CharField(null=True)
    description = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    mobile = CharField(null=True)
    name = CharField()
    position = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    telephone = CharField(null=True)
    user_id = BigIntegerField()
    wechat = CharField(null=True)

    class Meta:
        table_name = 'customer_contact'

class CustomerContactType(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_contact_type'

class CustomerInReport(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer_in_report'

class CustomerIndustry(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_industry'

class CustomerIndustryAnnualValue(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_industry_annual_value'

class CustomerIndustryScale(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_industry_scale'

class CustomerIndustryType(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_industry_type'

class CustomerLevel(BaseModel):
    classify_type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    color_id = BigIntegerField(index=True)
    color_value = CharField()
    company_id = BigIntegerField(index=True)
    feature = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    interval_from = IntegerField(null=True)
    interval_to = IntegerField(null=True)
    is_effective = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    is_focused = IntegerField(null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    strategy = CharField(null=True)

    class Meta:
        table_name = 'customer_level'

class CustomerLevelConversion(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField(index=True)
    customer_level_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    update_by = BigIntegerField()

    class Meta:
        table_name = 'customer_level_conversion'

class CustomerManager(BaseModel):
    ca = CharField(null=True)
    cln = CharField(null=True)
    clname = CharField(null=True)
    cname = CharField(null=True)
    color = CharField(null=True)
    color_name = CharField(null=True)
    color_value = BigIntegerField(null=True)
    company_id = BigIntegerField(null=True)
    company_name = CharField(null=True)
    company_type_name = CharField(null=True)
    customer_name = CharField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    name = CharField(null=True)
    remark = CharField(null=True)
    reserve_name = CharField(null=True)
    status = IntegerField(null=True)
    type = CharField(null=True)

    class Meta:
        table_name = 'customer_manager'

class CustomerMoveReason(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    reason = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_move_reason'

class CustomerOpportunity(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField()
    deadline = DateTimeField(null=True)
    employee_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField(null=True)
    opportunity_status = IntegerField(constraints=[SQL("DEFAULT 2")], null=True)
    opportunity_type = IntegerField(constraints=[SQL("DEFAULT 2")], null=True)
    remark = CharField(null=True)
    source = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer_opportunity'
        indexes = (
            (('customer_id', 'name'), True),
        )

class CustomerOutReport(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField(index=True)
    customer_move_reason_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_last = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    remark = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    turn_type = IntegerField()
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer_out_report'

class CustomerProduct(BaseModel):
    amount = DecimalField()
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_product'

class CustomerReceive(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField(index=True)
    customer_sign_order_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_plan_receive = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_reality_receive = DateTimeField(null=True)
    id = BigAutoField()
    modify_user_id = BigIntegerField()
    plan_receive_amount = DecimalField()
    plan_user_id = BigIntegerField(index=True)
    reality_receive_amount = DecimalField(null=True)
    reality_user_id = BigIntegerField(index=True, null=True)
    receive_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_receive'

class CustomerRequirement(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_requirement'

class CustomerSalesStatistics(BaseModel):
    company_id = BigIntegerField()
    customer_total = IntegerField()
    customer_total_untracing = IntegerField()
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer_sales_statistics'
        indexes = (
            (('user_id', 'company_id'), True),
        )
        primary_key = CompositeKey('company_id', 'user_id')

class CustomerSeaInfo(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    move_hours = IntegerField()
    private_sea_no_visit_expire_hours = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_sea_info'

class CustomerSignOrder(BaseModel):
    cancel_reason = CharField(null=True)
    cancel_user_id = BigIntegerField(null=True)
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_sign_order = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    product_id = BigIntegerField(index=True)
    sign_amount = DecimalField()
    sign_type = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'customer_sign_order'

class CustomerSource(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'customer_source'

class CustomerTarget(BaseModel):
    company_id = BigIntegerField()
    content = CharField(null=True)
    date = DateTimeField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    mgr_id = BigIntegerField(null=True)
    param1 = BigIntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    type = IntegerField()
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer_target'

class CustomerUser(BaseModel):
    company_id = BigIntegerField()
    customer_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_own = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    manipulate_id = BigIntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer_user'

class CustomerUserCapacity(BaseModel):
    capacity = IntegerField()
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField()

    class Meta:
        table_name = 'customer_user_capacity'

class CustomerVisit(BaseModel):
    accompany_visit = CharField(null=True)
    company_id = BigIntegerField()
    content = CharField(null=True)
    customer_contact_id = BigIntegerField(null=True)
    customer_id = BigIntegerField(null=True)
    customer_level_id = BigIntegerField(null=True)
    customer_opportunity_id = BigIntegerField(null=True)
    customer_requirement_remark = CharField(null=True)
    gmt_contact = DateTimeField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_visit = DateTimeField(null=True)
    id = BigAutoField()
    objection_remark = CharField(null=True)
    policy = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    user_id = BigIntegerField()
    visit_remark = CharField(null=True)
    visit_result = CharField(null=True)
    visit_type_id = BigIntegerField()

    class Meta:
        table_name = 'customer_visit'

class District(BaseModel):
    city_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'district'

class HibernateSequence(BaseModel):
    next_val = BigIntegerField(null=True)

    class Meta:
        table_name = 'hibernate_sequence'
        primary_key = False

class LeaveUserCustomerTransfer(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id_leave = BigIntegerField()
    user_id_manager = BigIntegerField(index=True)

    class Meta:
        table_name = 'leave_user_customer_transfer'

class LevelConversion(BaseModel):
    company_id = BigIntegerField(null=True)
    customer_id = BigIntegerField(null=True)
    customer_level_id = BigIntegerField(null=True)
    gmt_create = DateTimeField(null=True)
    gmt_modified = DateTimeField(null=True)
    id = BigAutoField()
    status = IntegerField(null=True)
    update_by = BigIntegerField(null=True)

    class Meta:
        table_name = 'level_conversion'

class Objection(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'objection'

class Province(BaseModel):
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    remark = CharField(null=True)
    sort = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'province'

class ReportCustomer(BaseModel):
    color_value = CharField()
    company_id = BigIntegerField(index=True)
    customer_level_id = BigIntegerField()
    customer_level_name = CharField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    increased_customer = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    stock_customer = IntegerField()
    total_customer = IntegerField()
    user_id = BigIntegerField()

    class Meta:
        table_name = 'report_customer'

class ReportSignOrder(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    increased_sign_amount = DecimalField()
    increased_sign_order = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    total_sign_amount = DecimalField()
    total_sign_order = BigIntegerField()
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'report_sign_order'

class VisitType(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_default = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'visit_type'

