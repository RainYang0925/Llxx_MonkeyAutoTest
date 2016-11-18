# --*coding:utf-8*--
'''
Created on 2016年11月28日

@author: fanxin, eachen
测试云滴租车
'''

from llxx_app import llxx_app
from cloueduser_startmain import StartMain
from cloueduser_monitor_location import MonitorLocationDialog
from cloueduser_test_login import TestLoginGroup
from cloueduser_monitor_startactivity import MonitorStartActivity
from cloueduser_monitor_click import MonitorClick

app = llxx_app("com.cloudd.user")
app.setReportPath("test_report.html")

# # 监听意外弹出框
app.addMonitorUnit(MonitorLocationDialog())
app.addMonitorUnit(MonitorStartActivity())
app.addMonitorUnit(MonitorClick())

# # 测试用例
app.addTestUnit(StartMain())
app.addTestGroup(TestLoginGroup())
app.start()