# -*- coding: utf-8 -*-

from faker import Faker
from random import sample
import string

# 本地化
fake = Faker(locale='zh_CN')

# 如需添加扩展新数据，需要继承重新 BaseProvider
from faker.providers import BaseProvider


# 创建自己的自定义扩展类
class My_Provider(BaseProvider):

    def my_method(self):
        return 'my_method'


# 将扩展类加入实例
fake.add_provider(My_Provider)

'''
示例调用自定义方法
print(fake.my_method())
'''

# 如需固定生成内容，打开seed
'''
seed = 1000
fake.seed(seed)
'''

'''地址'''
fake_country = fake.country()  # 国家
fake_city = fake.city()  # 城市
fake_city_suffix = fake.city_suffix()  # 行政单位后缀
fake_address = fake.address()  # 全称地址 邮编
fake_street_address = fake.street_address()  # 街道地址名称
fake_street_name = fake.street_name()  # 街道名称
fake_postcode = fake.postcode()  # 邮编
fake_latitude = fake.latitude()  # 纬度
fake_longitude = fake.longitude()  # 经度

'''人物'''
fake_name = fake.name()  # 姓名
fake_last_name = fake.last_name()  # 姓
fake_first_name = fake.first_name()  # 名
fake_name_male = fake.name_male()  # 男姓名
fake_last_name_male = fake.last_name_male()  # 男姓
fake_first_name_male = fake.first_name_male()  # 男名
fake_name_female = fake.name_female()  # 女姓名

'''条码'''
fake_ean8 = fake.ean8()  # 8位数字条码
fake_ean13 = fake.ean13()  # 13位数字条码
fake_ean = fake.ean()  # 随机数字条码

'''颜色'''
fake_hex_color = fake.hex_color()  # 16进制表示的颜色
fake_rgb_css_color = fake.rgb_css_color()  # css用的rgb色
fake_rgb_color = fake.rgb_color()  # 表示rgb色的字符串
fake_color_name = fake.color_name()  # 颜色名字
fake_safe_hex_color = fake.safe_hex_color()  # 安全16进制色
fake_safe_color_name = fake.safe_color_name()  # 安全颜色名字

'''公司'''
fake_company = fake.company()  # 公司名
fake_company_suffix = fake.company_suffix()  # 公司名后缀

'''银行卡'''
fake_credit_card_number = fake.credit_card_number(card_type=None)  # 信用卡号
fake_credit_card_provider = fake.credit_card_provider(card_type=None)  # 卡的提供者、开卡行
fake_credit_card_security_code = fake.credit_card_security_code(card_type=None)  # 卡的安全密码
fake_credit_card_expire = fake.credit_card_expire()  # 卡的有效期
fake_credit_card_full = fake.credit_card_full(card_type=None)  # 完整卡信息

'''货币'''
fake_currency_code = fake.currency_code()  # 货币代码

'''时间日期'''
fake_date_time = fake.date_time(tzinfo=None)  # 随机日期时间
fake_iso8601 = fake.iso8601(tzinfo=None)  # 以iso8601标准输出的日期
fake_date_time_this_month = fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)  # 本月的某个日期
fake_date_time_this_year = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)  # 本年的某个日期
fake_date_time_this_decade = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)  # 本年代内的一个日期
fake_date_time_this_century = fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)  # 本世纪一个日期
fake_date_time_between = fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)  # 两个时间间的一个随机时间
fake_timezone = fake.timezone()  # 时区
fake_time = fake.time(pattern="%H:%M:%S")  # 时间（可自定义格式）
fake_am_pm = fake.am_pm()  # 随机上午下午
fake_month = fake.month()  # 随机月份
fake_month_name = fake.month_name()  # 随机月份名字
fake_year = fake.year()  # 随机年
fake_day_of_week = fake.day_of_week()  # 随机星期几
fake_day_of_month = fake.day_of_month()  # 随机月中某一天
fake_time_delta = fake.time_delta()  # 随机时间延迟
fake_date_object = fake.date_object()  # 随机日期对象
fake_time_object = fake.time_object()  # 随机时间对象
fake_unix_time = fake.unix_time()  # 随机unix时间（时间戳）
fake_date = fake.date(pattern="%Y-%m-%d %H:%M:%S")  # 随机日期（可自定义格式）
fake_date_time_ad = fake.date_time_ad(tzinfo=None)  # 公元后随机日期

'''文件'''
fake_sfile_name = fake.file_name(category="image", extension="png")  # 文件名（指定文件类型和后缀名）
fake_file_name = fake.file_name()  # 随机生成各类型文件
fake_file_extension = fake.file_extension(category=None)  # 文件后缀
fake_mime_type = fake.mime_type(category=None)  # mime-type

'''互联网'''
fake_ipv4 = fake.ipv4(network=False)  # ipv4地址
fake_ipv6 = fake.ipv6(network=False)  # ipv6地址
fake_uri_path = fake.uri_path(deep=None)  # uri路径
fake_uri_extension = fake.uri_extension()  # uri扩展名
fake_uri = fake.uri()  # uri
fake_url = fake.url()  # url
fake_image_url = fake.image_url(width=None, height=None)  # 图片url
fake_domain_word = fake.domain_word()  # 域名主体
fake_domain_name = fake.domain_name()  # 域名
fake_tld = fake.tld()  # 域名后缀
fake_user_name = fake.user_name()  # 用户名
fake_user_agent = fake.user_agent()  # UA
fake_mac_address = fake.mac_address()  # MAC地址
fake_safe_email = fake.safe_email()  # 安全邮箱
fake_free_email = fake.free_email()  # 免费邮箱
fake_company_email = fake.company_email()  # 公司邮箱
fake_email = fake.email()  # 邮箱
fake_linux_platform_token = fake.linux_platform_token()  # linux 平台信息
fake_linux_processor = fake.linux_processor()  # linux 平台信息
fake_windows_platform_token = fake.windows_platform_token()  # windows 平台信息
fake_mac_platform_token = fake.mac_platform_token()  # 邮箱 # mac平台信息
fake_internet_explorer = fake.internet_explorer()  # IE浏览器
fake_opera = fake.opera()  # opera浏览器
fake_firefox = fake.firefox()  # firefox浏览器
fake_safari = fake.safari()  # safari浏览器
fake_chrome = fake.chrome()  # chrome浏览器

'''工作'''
fake_job = fake.job()  # 工作职位

'''乱数假文'''
fake_text = fake.text(max_nb_chars=200)  # 随机生成一篇文章
fake_word = fake.word()  # 随机单词
fake_words = fake.words(nb=3)  # 随机生成几个词
fake_sentence = fake.sentence(nb_words=6, variable_nb_words=True)  # 随机生成一个句子
fake_sentences = fake.sentences(nb=3)  # 随机生成几个句子
fake_paragraph = fake.paragraph(nb_sentences=3, variable_nb_sentences=True)  # 随机生成一段文字(字符串)
fake_paragraphs = fake.paragraphs(nb=3)  # 随机生成成几段文字(列表)

'''杂项'''
fake_binary = fake.binary(length=10)  # 随机二进制字符串(可指定长度)
fake_language_code = fake.language_code()  # 随机语言代码
fake_md5 = fake.md5(raw_output=False)  # 随机md5，16进制字符串
fake_sha1 = fake.sha1(raw_output=False)  # 随机sha1，16进制字符串
fake_sha256 = fake.sha256(raw_output=False)  # 随机sha256，16进制字符串
fake_boolean = fake.boolean(chance_of_getting_true=50)  # 随机真假值(得到True的几率是50%)
fake_null_boolean = fake.null_boolean()  # 随机真假值和null
fake_password = fake.password(length=10, special_chars=True, digits=True, upper_case=True,
                              lower_case=True)  # 随机密码（可指定密码策略）
fake_locale = fake.locale()  # 随机本地代码
fake_uuid4 = fake.uuid4()  # 随机uuid

'''电话号码'''
fake_phone_number = fake.phone_number()  # 电话
fake_phonenumber_prefix = fake.phonenumber_prefix()  # 运营商号段，手机号码前三位

'''python数据'''
fake_pyint = fake.pyint()  # 随机int
fake_pyfloat = fake.pyfloat(left_digits=None, right_digits=None, positive=False)  # 浮点数
fake_pydecimal = fake.pydecimal(left_digits=None, right_digits=None, positive=False)  # 随机高精度数
fake_pystr = fake.pystr(min_chars=None, max_chars=20)  # 随机字符串（可指定长度）
fake_pybool = fake.pybool()  # 随机bool值
fake_pyiterable = fake.pyiterable(nb_elements=10, variable_nb_elements=True)  # 随机iterable
fake_pylist = fake.pylist(nb_elements=10, variable_nb_elements=True)  # 随机生成一个list
fake_pydict = fake.pydict(nb_elements=10, variable_nb_elements=True)  # 随机字典
fake_pyset = fake.pyset(nb_elements=10, variable_nb_elements=True)  # 随机set
fake_pytuple = fake.pytuple(nb_elements=10, variable_nb_elements=True)  # 随机tuple
fake_pystruct = fake.pystruct()  # 随机生成3个有10个元素的python数据结构

'''人物描述'''
fake_profile = fake.profile(fields=None, sex=None)  # 人物描述信息：姓名、性别、地址、公司等
fake_simple_profile = fake.simple_profile(sex="m")  # 人物精简信息
fake_ssn = fake.ssn(18)  # 身份证号


# 随机生成任意长度的字符串
def random_str(length: int = 6):
    return ''.join(sample(string.ascii_letters, length))


if __name__ == '__main__':
    while True:
        print(fake.company())
