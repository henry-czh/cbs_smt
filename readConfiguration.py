#!/usr/bin/env python

import os
import sys
import re
from os import system

def readConfiguration():
    src_rf = open("test.cfg",'r')

    cfg_dict={}
    dpd_list=[]
    dpd_key_list=[]

    comment_pattern=re.compile(r'^[ ]*?[//|#|$]')
    dpd_pattern=re.compile(r'{.*?}')
    top_pattern=re.compile(r'^[ ]*?<tb_top=')
    item_pattern=re.compile(r'^[ ]*?<config_item=')
    inst_pattern=re.compile(r'^[ ]*?\[instance\]')
    mdul_pattern=re.compile(r'^[ ]*?\[module\]')
    opts_pattern=re.compile(r'^[ ]*?\[options\]')
    deft_pattern=re.compile(r'^[ ]*?\[default\]')
    help_pattern=re.compile(r'^[ ]*?\[help\]')
    dpdon_pattern=re.compile(r'^[ ]*?\[depends on\]')

    for line in src_rf.readlines():
        if re.match(comment_pattern,line):
            continue
        if re.match(top_pattern,line):
            top_top=re.sub('\<tb_top\=','',line).strip().strip('>')
        if re.match(item_pattern,line):
            cfg_key = re.sub('\<config_item\=','',line).strip().strip('>')
            cfg_dict[cfg_key]={}
        if re.match(inst_pattern,line) and re.sub('\[instance\]','',line).strip() != '':
            cfg_dict[cfg_key]['instance'] = re.sub('\[instance\]','',line).strip().split(' ')
            cbs_mode=1
        if re.match(opts_pattern,line) and re.sub('\[options\]','',line).strip() !=' ':
            options = re.sub('\[options\]','',line).strip().split(' ')
            cfg_dict[cfg_key]['options']=[]
            cfg_dict[cfg_key]['module']={}
            for op in options:
                if len(op.split(':'))>1:
                    cfg_dict[cfg_key]['module'][op.split(':')[0]] = op
                    #cfg_dict[cfg_key]['module'][op.split(':')[0]] = op.split(':')[1]
                cfg_dict[cfg_key]['options'].append(op.strip().split(':')[0])
            cfg_dict[cfg_key]['options'].append('*')
        if re.match(deft_pattern,line) and re.sub('\[default\]','',line).strip() != ' ':
            cfg_dict[cfg_key]['default'] = re.sub('\[default\]','',line).strip()
        if re.match(help_pattern,line) and re.sub('\[help\]','',line).strip() != ' ':
            cfg_dict[cfg_key]['help'] = re.sub('\[help\]','',line).strip()
        if re.match(dpdon_pattern,line):
            dpd_str = re.sub('','',line).strip()
            dpd_dict={}
            if dpd_str != '':
                dpd_list = re.findall(dpd_pattern,dpd_str)
                for item in dpd_list:
                    item = re.sub('.options','',item)
                    item = re.sub('=',':',item).split(':')
                    item_key = item[0].strip('{')
                    if item_key in dpd_dict.keys():
                        dpd_key_list = dpd_dict[item[0].strip('{')]
                        dpd_key_list.append({item[1]:item[2].strip('}')})
                    else:
                        dpd_key_list=[]
                        dpd_key_list.append({item[1]:item[2].strip('}')})
                    dpd_dict[item[0].strip('{')]=dpd_key_list
                cfg_dict[cfg_key]['depends on'] = dpd_dict
    src_rf.close()
    return cfg_dict

def create_dict(tdict,inst_list,module_list,hdl_path,help_info,item_name,default):
    if len(inst_list)==1:
        tdict[inst_list[0]] = dict()
        tdict[inst_list[0]]['modules']=module_list
        tdict[inst_list[0]]['hdl_path']=hdl_path
        tdict[inst_list[0]]['help']=help_info
        tdict[inst_list[0]]['item_name']=item_name
        tdict[inst_list[0]]['sub_tree']=[]
        default_opt = ''
        for item in module_list:
            if item.split(':')[0] == default:
                default_opt = item
        if default_opt=='':
            raise Exception('default opt not in options list!!!')
        else:
            tdict[inst_list[0]]['default']=default_opt
    else:
        if not inst_list[0] in tdict:
            tdict[inst_list[0]] = dict()
            tdict[inst_list[0]]['sub_tree'] = dict()
        else:
            if not type(tdict[inst_list[0]]['sub_tree']) is dict:
                tdict[inst_list[0]]['sub_tree']=dict()
        create_dict(tdict[inst_list[0]]['sub_tree'],inst_list[1:],module_list,hdl_path,help_info,item_name,default)
    return tdict

def genDesignTree():
    cfg_dict = readConfiguration()
    tree_dict = dict()

    for item in cfg_dict.keys():
        if 'instance' in cfg_dict[item]:
            #print (cfg_dict[item]['instance'])
            instance_list = cfg_dict[item]['instance'][0].strip().split('.')
            if len(instance_list)==0:
                raise Exception('%s has \"instance\",but its value is null!! check the config file' % (item))
            module_list = list(cfg_dict[item]['module'].values())
            hdl_path = cfg_dict[item]['instance'][0]
            help_info = cfg_dict[item]['help']
            default = cfg_dict[item]['default']
            tree_dict=create_dict(tree_dict,instance_list,module_list,hdl_path,help_info,item,default)
        else:
            continue
            print ('[%s] is a macro item' % (item))
    return tree_dict

#create temp config database
def genOutPutCfg(cfg_dict):
    cfg_temp_dict = dict()
    for item in cfg_dict:
        if 'default' in cfg_dict[item]:
            cfg_temp_dict[item] = cfg_dict[item]['default']
        else:
            cfg_temp_dict[item] = '*'
            reply = QMessageBox.warning(self,'警告','item : %s don\'t have default options,add it?' % (item),QMessageBox.Yes|QMessageBox.Yes,QMessageBox.No)
            if reply == QMessageBox.Yes:
                line_num = os.system('grep -n %s ./test.cfg' % (item))
                os.system('gvim ./test.cfg +%s' % (line_num))
                cfg_dict = readConfiguration.readConfiguration()
                cfg_temp_dict[item] = cfg_dict[item]['default']
    return cfg_temp_dict

def checkDependence(item_name,item_value,cfg_dict,cfg_temp_dict,status,has_depend,depend_info,depend_dict):
    if 'depends on' in cfg_dict[item_name] and item_value in cfg_dict[item_name]['depends on']:
        has_depend = 1
        depend_list = cfg_dict[item_name]['depends on'][item_value]
        for item in depend_list:
            #判断是否有因依赖关系发生的默认修改
            for k in item:
                if k in cfg_temp_dict:
                    if cfg_temp_dict[k] != item[k]:
                        status = 1
                else:
                        status = 1
                cfg_temp_dict[k] = item[k]
                depend_info = depend_info + item_name + ' = ' + item_value + ' --> ' + str(item) + '\n '
                depend_dict.update(item)
                s,d,info,dpd_dict,tmp_dict = checkDependence(k,item[k],cfg_dict,cfg_temp_dict,status,has_depend,depend_info,depend_dict)
                depend_info = info
    return status,has_depend,depend_info,depend_dict,cfg_temp_dict

def checkConflict(item_name,item_value,cfg_dict,cfg_temp_dict,depend_dict,conflict,conflict_info):
    for item in cfg_dict:
        #检查当前项的conflict情况
        temp_depend_dict = depend_dict
        temp_depend_dict.update({item_name:item_value})
        #检查静默修改部分的conflict情况
        for key,value in temp_depend_dict.items():
            if 'depends on' in cfg_dict[item] and item in cfg_temp_dict:
                if cfg_temp_dict[item] in cfg_dict[item]['depends on']:
                    depend_list = cfg_dict[item]['depends on'][cfg_temp_dict[item]]
                    for be_depend_dict in depend_list:
                        if key in be_depend_dict and be_depend_dict[key] != value:
                            conflict = 1
                            conflict_info = conflict_info + '%s = %s need %s = %s ,but you want to change %s to %s .\n ' % (item,cfg_temp_dict[item],key,be_depend_dict[key],key,value)
    return conflict,conflict_info

#def create_dpd_link(link_dict,cfg_dict,item_name):
#    link_dict[item_name]=dict()
#    link_dict[item_name][]
#def genDependLink():
#    cfg_dict = readConfiguration()
#    depend_link_dict = dict()
#
#    for item in cfg_dict.keys():
#        if 'depends on' in cfg_dict[item]:
#            depend_link_dict = create_dpd_link(depend_link_dict,cfg_dict,item)

if __name__=='__main__':
    #readConfiguration()
    genDesignTree()

            