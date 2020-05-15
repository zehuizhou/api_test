from peewee import *

database = MySQLDatabase('xxy_research', **{'charset': 'utf8', 'use_unicode': True, 'host': '10.10.201.223', 'user': 'ms_user', 'password': 'ms_passwd'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Answer(BaseModel):
    answer = CharField(null=True)
    company_id = BigIntegerField(index=True)
    exam_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    option_ids = CharField(null=True)
    scores = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    subject_id = BigIntegerField(index=True)
    type = IntegerField(null=True)

    class Meta:
        table_name = 'answer'

class Batch(BaseModel):
    company_id = BigIntegerField(index=True)
    customer_id = BigIntegerField(null=True)
    customer_name = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_submit = IntegerField(constraints=[SQL("DEFAULT 0")])
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_id = BigIntegerField(null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'batch'

class Classify(BaseModel):
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'classify'

class Diff(BaseModel):
    company_id = BigIntegerField(index=True)
    exam_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    last_answer = CharField(null=True)
    local_answer = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    subject_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'diff'

class Exam(BaseModel):
    batch_id = BigIntegerField(index=True)
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    is_submit = IntegerField(constraints=[SQL("DEFAULT 0")])
    paper_id = BigIntegerField(index=True)
    score = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    user_name = CharField(null=True)

    class Meta:
        table_name = 'exam'

class Option(BaseModel):
    company_id = BigIntegerField(index=True)
    content = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    score = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    subject_id = BigIntegerField(index=True)

    class Meta:
        table_name = 'option'

class Paper(BaseModel):
    commit_by = BigIntegerField(null=True)
    commit_name = CharField(null=True)
    company_id = BigIntegerField(index=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    name = CharField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)

    class Meta:
        table_name = 'paper'

class Subject(BaseModel):
    classify_id = BigIntegerField(index=True)
    company_id = BigIntegerField(index=True)
    content = CharField(null=True)
    gmt_create = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    gmt_modified = DateTimeField(constraints=[SQL("DEFAULT current_timestamp()")], null=True)
    id = BigAutoField()
    number = CharField(null=True)
    paper_id = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    type = IntegerField()

    class Meta:
        table_name = 'subject'

