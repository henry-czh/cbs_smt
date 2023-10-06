#!/bin/env python
#_*_ coding:UTF-8 _*_

'''
 File         : updateSavedConfig.py
 Author       : chaozhanghu0053 (chaozhanghu@phytium.com.cn)
 Date         : 2022/06/08
 Version      : 1.0
 Description  :
 
 copyright Copyright (c) 2021-2022, Phytium Technology Co.,Ltd. All rights reserved.
'''

import os
import sys
import parseConfig
import readConfiguration
#import cProfile

def updateConfig(fileContent,cfg_dict,tdict):
    load_dict = readConfiguration.loadExistCfg(fileContent)

    check_status,load_dict,check_info = readConfiguration.compareDismatchCfg(cfg_dict,load_dict,tdict)

    print check_info

    text_out = '#// Generated automatic by CMT,don\'t change!'
    for item in sorted(load_dict):
        text_out +=  '\n' + item + ' = ' + load_dict[item] + '\n'

    return text_out,check_status

def updateSavedConfigs():
    curdir = os.getenv("CURDIR")
    curdir = os.path.join(curdir,'config')

    base_cfg_file = os.getenv("BASE_CFG_FILE")
    usr_cfg_file  = os.getenv("USER_CFG_FILE")

    config_dict = parseConfig.parseConfig(base_cfg_file,usr_cfg_file)
    cfg_dict    = config_dict['cfg']

    tdict = readConfiguration.genDesignTree(cfg_dict)

    updateSuccess = True
    
    for path,directory,filelist in os.walk(curdir):
        for filename in filelist:
            if filename in ['usr.cfg','update.cfg','Makefile.default']:
                continue

            if filename[0]=='.':
                continue

            print "[%s] 开始更新 ... " % (filename)

            fileContext = open(os.path.join(path,filename),'r')
            update      = open(os.path.join(path,'update.cfg'),'w')

            updatedContext,check_status = updateConfig(fileContext,cfg_dict,tdict)

            updateSuccess = not check_status
            
            update.write(updatedContext)
            update.close()

            os.rename(os.path.join(path,'update.cfg'),os.path.join(path,filename))

            print "[%s] 更新完成！" % (filename)

    if updateSuccess:
        print "\n所有配置文件Update Successfully!\n"

if __name__=="__main__":
    #cProfile.run("updateSavedConfigs()")
    updateSavedConfigs()
