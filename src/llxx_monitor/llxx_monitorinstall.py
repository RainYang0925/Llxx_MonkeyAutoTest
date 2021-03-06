# --*coding:utf-8*--
'''
Created on 2016年10月29日

@author: fanxin, eachen

APP自己调用安装
'''
# pip install simplejson
import string

from llxx_monitor import llxx_monitorunit, llxx_result


class llxx_monitorinstall(llxx_monitorunit):  
    
    def onMonitor(self, message):
        isInstall = string.find(message, "start_activity") != -1 and string.find(message, "com.android.packageinstaller.PackageInstallerActivity") != -1
        if isInstall:
            params = {};
            self.hookApp(llxx_result(message, "apk_install", params))
            # print message
        
        ## 安装完成
        isInstallOk = string.find(message, "安装完成") != -1 and string.find(message, "打开")
        if isInstallOk:
            params = {};
            params["sucess"] = True
            self.hookApp(llxx_result(message, "apk_install_report", params))
            self._isinstallok = True
            self.remove()
            # print message
            
