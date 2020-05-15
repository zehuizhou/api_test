import pytest
import os
from datetime import datetime
from py.xml import html
import configparser

"""命令行传参：--env"""


def pytest_addoption(parser):
    """
    从cmd传入env参数
    :param parser:
    :return:
    """
    parser.addoption(
        "--env", action="store", default="dev", help="test environment:test or dev"
    )


@pytest.fixture(scope="module", autouse=True)
def write_cmdopt(request):
    """根据cmd传入的env参数，修改配置文件"""
    cmd_env = request.config.getoption("--env")
    conf = configparser.ConfigParser()
    ini_path = os.path.dirname(os.path.abspath(__file__)) + "/config/conf.ini"
    conf.read(ini_path)
    conf.set("cmd", "env", cmd_env)
    conf.write(open(ini_path, "r+", encoding="utf-8"))


"""
增加测试报告Description列
"""


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     getattr(report, 'extra', [])
#     report.nodeid = report.nodeid.encode('utf-8').decode('unicode_escape')
