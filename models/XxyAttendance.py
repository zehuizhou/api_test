from peewee import *

database = MySQLDatabase('xxy_attendance', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AttendanceGroup(BaseModel):
    company_id = BigIntegerField()
    employee_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'attendance_group'

class AttendanceGroupUser(BaseModel):
    attendance_group_id = BigIntegerField()
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    is_attendance = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'attendance_group_user'

class AttendancePosition(BaseModel):
    address = CharField(null=True)
    attendance_group_id = BigIntegerField(index=True)
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    latitude = DecimalField(null=True)
    longitude = DecimalField(null=True)
    name = CharField(null=True)
    offset = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'attendance_position'

class AttendanceRecord(BaseModel):
    attendance_group_id = BigIntegerField()
    attendance_group_name = CharField()
    attendance_shift_id = BigIntegerField()
    attendance_shift_time_id = BigIntegerField()
    clock_in_image = CharField(null=True)
    clock_status = IntegerField()
    clock_type = IntegerField()
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_valid = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    phone_name = CharField(null=True)
    position_type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    remark = CharField(null=True)
    standard_attendance_time = DateTimeField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)
    uuid = CharField()

    class Meta:
        table_name = 'attendance_record'

class AttendanceRecordPositionGps(BaseModel):
    attendance_record_id = BigIntegerField(index=True)
    clock_address = CharField()
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    latitude = DecimalField()
    longitude = DecimalField()
    offset = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'attendance_record_position_gps'

class AttendanceRecordPositionWifi(BaseModel):
    attendance_record_id = BigIntegerField(index=True)
    attendance_wifi_id = BigIntegerField()
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'attendance_record_position_wifi'

class AttendanceRestRecord(BaseModel):
    clock_address = CharField()
    clock_in_image = CharField(null=True)
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    latitude = DecimalField()
    longitude = DecimalField()
    position_type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    remark = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(index=True)
    uuid = CharField()

    class Meta:
        table_name = 'attendance_rest_record'

class AttendanceShift(BaseModel):
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'attendance_shift'

class AttendanceShiftTime(BaseModel):
    attendance_shift_id = BigIntegerField(index=True)
    company_id = BigIntegerField()
    earliest_on_duty = TimeField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    latest_off_duty = TimeField(null=True)
    off_duty = TimeField()
    on_duty = TimeField()
    start_clock_in = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    stop_clock_in = IntegerField()

    class Meta:
        table_name = 'attendance_shift_time'

class AttendanceWifi(BaseModel):
    address = CharField(null=True)
    attendance_group_id = BigIntegerField(index=True)
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'attendance_wifi'

class AttendanceWorkday(BaseModel):
    attendance_group_id = BigIntegerField(index=True)
    attendance_shift_id = BigIntegerField(index=True, null=True)
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    week_day = IntegerField()

    class Meta:
        table_name = 'attendance_workday'

class AttendanceWorkingTime(BaseModel):
    company_id = BigIntegerField()
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")])
    hours = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    id = BigAutoField()
    minutes = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    sum_minute = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    user_id = BigIntegerField(index=True)
    week_day = DateField()

    class Meta:
        table_name = 'attendance_working_time'

