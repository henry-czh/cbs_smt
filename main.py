# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
import os
import copy
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
#from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#导入designer工具生成的login模块
#from cbs_v1 import Ui_MainWindow
from uvs import Ui_smt
import genDesignTree
import readConfiguration
import saveConfiguration
import icon

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QComboBox, QSpinBox
from PyQt5.QtSvg import QSvgWidget

class QComboBox_czh(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox_czh,self).__init__(parent)

    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()

class QSpinBox(QSpinBox):
    def __init__(self, parent=None):
        super(QSpinBox,self).__init__(parent)

    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()

class MyMainForm(QMainWindow, Ui_smt):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        #system setting
        self.cfg_file = os.getenv('MAIN_CFG_FILE')
        self.usr_cfg_file = os.getenv('USR_CFG_FILE')
        self.saveDir = os.getenv('CFG_SAVE_DIR')
        self.svgfile = os.getenv('SVG_FILE')
        #self.saveDir = os.path.abspath(os.path.join(os.getcwd(), "../config"))

        #self.svgwin.setWindowTitle('Basic Configuration')
        #icon_cfg = QIcon()
        #icon_cfg.addPixmap(QPixmap(":/ico/process.ico"), QIcon.Normal, QIcon.Off)
        #self.svgwin.setWindowIcon(icon_cfg)
        #self.macrowin.setWindowTitle('Increment Compile')
        #icon_incr = QIcon(":/ico/equalizer.ico")
        #self.macrowin.setWindowIcon(icon_incr)

        # 创建一个 QSvgWidget 并加载 SVG 图像
        svg_widget = QSvgWidget(self.scrollArea_svg)
        #svg_widget.setGeometry(0, 0, self.svgtab.width(), self.svgtab.height())
        # 创建一个垂直布局
        layout = QVBoxLayout(self.scrollArea_svg)
        # 将 QSvgWidget 添加到布局
        layout.addWidget(svg_widget)
        # 设置布局管理器，使 QSvgWidget 充满整个父窗口
        self.scrollArea_svg.setLayout(layout)

        svg_widget.load(self.svgfile)  # 替换为你的 SVG 图像文件路径

        # 创建一个 文件浏览窗口
        self.dir_model = QFileSystemModel()
        self.dir_model.setReadOnly(True)
        #self.current_path = QDir.currentPath()
        self.current_path = os.getenv('CBS_HOME')
        self.dir_model.setRootPath(self.current_path)
        self.treeView_filebrowser.setModel(self.dir_model)
        self.treeView_filebrowser.setRootIndex(self.dir_model.index(self.current_path))

        #set statusbar information
        self.statusbar.showMessage('Any questions, please contact chaozhanghu@foxmail.com  @Qsmtool 21.05-0001')
        self.statusbar.show()

       # #create right menu
       # self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
       # self.treeView.customContextMenuRequested.connect(self.creat_rightmenu)
       # self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
       # self.treeWidget.customContextMenuRequested.connect(self.creat_tree_rightmenu)

       # #tooltip
       # QToolTip.setFont(QFont('SansSerif',12))
       # self.treeView.setToolTip('单击右键可调出菜单')

       # #mdi multi window shou
       # self.mdiArea.addSubWindow(self.subwindow_3)
       # self.subwindow_3.show()
       # self.mdiArea.addSubWindow(self.subwindow_2)
       # self.subwindow_2.show()
       # self.mdiArea.addSubWindow(self.subwindow)
       # #self.subwindow.show()
       # self.subwindow.showMaximized()

       # #********************************************************
       # # connect buttons and function 
       # #********************************************************
       # # button "Apply"
       # self.pushButton.clicked.connect(self.applyConfig)
       # # button "Save"
       # self.pushButton_3.clicked.connect(self.saveConfigFile)
       # # button "Compare"
       # self.pushButton_5.clicked.connect(self.compareConfigFile)
       # # button "open"

       # self.pushButton_6.clicked.connect(self.loadConfigFile)
       # # tool button "reload"
       # self.actionreload.triggered.connect(self.reloadConfigFile)
       # # tool button "open"
       # self.actionopen.triggered.connect(self.loadConfigFile)

       # # action "Exit"
       # self.actionExit.triggered.connect(self.exitGui)

       # #read configuration file
       # self.cfg_dict,self.mode_dict = readConfiguration.readConfiguration(self.cfg_file,self.usr_cfg_file)
       # self.cfg_output_dict = readConfiguration.genOutPutCfg(self.cfg_file,self.usr_cfg_file)
       # self.cfg_dict = dict(sorted(self.cfg_dict.items(),key=lambda x:x[0]))
       # self.cfg_output_dict = dict(sorted(self.cfg_output_dict.items(),key=lambda x:x[0]))
       # # 默认配置值检查
       # self.check_default_cfg()

       # #gen dict from cfg file
       # self.designTree_dict=readConfiguration.genDesignTree(self.cfg_file,self.usr_cfg_file)
       # 
       # #default mode select
       # if len(self.mode_dict) >0:
       #     self.current_mode = list(self.mode_dict.keys())[0]
       #     self.current_mode_dict = self.mode_dict[self.current_mode]
       # else:
       #     self.current_mode_dict = {}

       # #****************************************************
       # # add tree item
       # #****************************************************
       # self.treeWidget.setColumnCount(3)
       # self.treeWidget.setHeaderLabels(['instance','module','item'])
       # self.treeWidget.setColumnWidth(0,300)
       # self.treeWidget.setColumnWidth(1,200)

       # self.build_design_tree(self.treeWidget,self.designTree_dict,self.cfg_output_dict,self.cfg_dict,0,self.current_mode_dict)
       # self.treeWidget.sortItems(0,Qt.AscendingOrder)

       # #****************************************************
       # # add mode select
       # #****************************************************
       # self.comboBox.addItems(self.mode_dict.keys())
       # #编程和用户方式都会触发的是currentIndexChanged；只有用户操作才会触发的是activated()
       # self.comboBox.activated.connect(self.mode_select)


       # #消除child節點
       # it = QTreeWidgetItemIterator(self.treeWidget)
       # while it.value():
       #     item = it.value()
       #     if not item.isHidden():
       #         if item.toolTip(0):
       #             item_value = self.treeWidget.itemWidget(item,1).currentText().split(':')[0]
       #             self.hidden_child(item,item_value,0)
       #     it.__iadd__(1)

       # #********************************************************
       # # add table item
       # #********************************************************
       # self.tableWidget.setColumnCount(2)
       # self.tableWidget.setShowGrid(False)
       # self.tableWidget.setColumnWidth(0,300)
       # self.tableWidget.setColumnWidth(1,200)
       # self.tableWidget.setHorizontalHeaderLabels(['macro','value'])
       # self.build_macro_table(self.cfg_dict,self.cfg_output_dict,self.current_mode_dict)

    def mode_select(self):
        current_mode = self.comboBox.currentText()
        self.treeWidget.clear()
        self.build_design_tree(self.treeWidget,self.designTree_dict,self.cfg_output_dict,self.cfg_dict,0,self.mode_dict[current_mode])
        self.treeWidget.sortItems(0,Qt.AscendingOrder)

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.build_macro_table(self.cfg_dict,self.cfg_output_dict,self.mode_dict[current_mode])
        self.tableWidget.sortItems(0,Qt.AscendingOrder)

        # 默认配置值检查
        # 模式选择过程不涉及默认值检查
        #self.check_default_cfg()

        #打印結果
        self.textBrowser.setTextColor(QColor('black'))
        text_out = '[CBS Console]$ Mode change to : %s Successfully ' % (current_mode)
        self.textBrowser.append(text_out)

        #消除child節點
        it = QTreeWidgetItemIterator(self.treeWidget)
        while it.value():
            item = it.value()
            if not item.isHidden():
                if item.toolTip(0):
                    item_value = self.treeWidget.itemWidget(item,1).currentText().split(':')[0]
                    self.hidden_child(item,item_value,0)
            it.__iadd__(1)


    def check_default_cfg(self):
        self.default_check,self.default_check_info = readConfiguration.checkDefaultSet(self,self.cfg_dict,self.cfg_output_dict)
        if self.default_check:
            self.textBrowser.setTextColor(QColor('red'))
            self.text_out = '[CBS Console]$ 错误！错误！错误！\n 默认配置不满足依赖关系！\n%s' % (self.default_check_info)
            self.textBrowser.append(self.text_out)
            QMessageBox.critical(self,'Fatal','默认配置错误，请联系相关管理员，修改原始配置文件后Reload！' )

    def build_design_tree(self,item,dt_dict,cfg_output_dict,cfg_dict,level,mode_dict):
        #print (dt_dict.keys())
        for i in dt_dict.keys():
            level = level+1
            sub_item = QTreeWidgetItem(item)
            sub_item.setText(0,i)
            if level<3:
                self.treeWidget.expandItem(sub_item)
            else:
                self.treeWidget.collapseItem(sub_item)
            #if 'modules' in dt_dict[i] and dt_dict[i]['item_name'] in cfg_output_dict:
            if 'modules' in dt_dict[i]:
                sub_item.setText(2,dt_dict[i]['item_name'])
                combbox = QComboBox_czh()
                combbox.addItems(dt_dict[i]['modules'])
                if dt_dict[i]['item_name'] in cfg_output_dict:
                    combbox.setCurrentText(cfg_dict[dt_dict[i]['item_name']]['module'][cfg_output_dict[dt_dict[i]['item_name']]])
                else:
                    combbox.setCurrentText(dt_dict[i]['default'])
                #如果配置项在mode控制下，则为const值，不能任意选择
                if dt_dict[i]['item_name'] in mode_dict:
                    combbox.setCurrentText(cfg_dict[dt_dict[i]['item_name']]['module'][mode_dict[dt_dict[i]['item_name']]])
                    self.cfg_output_dict[dt_dict[i]['item_name']] = mode_dict[dt_dict[i]['item_name']]
                    list_num = combbox.count()
                    #关闭所有选项为不可选状态
                    for num in range(list_num):
                        icon_lock = QIcon(":/ico/lock.ico")
                        sub_item.setIcon(1,icon_lock)
                        combbox.setItemData(num,QVariant(0),Qt.UserRole-1)
                self.treeWidget.setItemWidget(sub_item,1,combbox)
                #编程和用户方式都会触发的是currentIndexChanged；只有用户操作才会触发的是activated()
                combbox.activated.connect(self.update_design_tree)
                #combbox.currentIndexChanged.connect(self.update_design_tree)
            if 'hdl_path' in dt_dict[i]:
                sub_item.setToolTip(0,dt_dict[i]['hdl_path'])
                sub_item.setToolTip(1,dt_dict[i]['help'])
            if type(dt_dict[i]['sub_tree']) is list:
                continue
            else:
                self.build_design_tree(sub_item,dt_dict[i]['sub_tree'],cfg_output_dict,cfg_dict,level,mode_dict)

        return item

    def build_macro_table(self,cfg_dict,cfg_out_dict,mode_dict):
        for item in cfg_dict.keys():
            if not 'instance' in cfg_dict[item]:
                current_row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(current_row+1)
                combbox = QComboBox_czh()
                combbox.addItems(cfg_dict[item]['options'])
                combbox.setCurrentText(cfg_out_dict[item])
                ##默认不显示任何选项
                #combbox.setCurrentIndex(-1)

                #mode控制下的const设置
                if item in mode_dict:
                    combbox.setCurrentText(mode_dict[item])
                    self.cfg_output_dict[item] = mode_dict[item]
                    #获取下拉菜单个数
                    list_num = combbox.count()
                    #关闭所有选项为不可选状态
                    for i in range(list_num):
                        combbox.setItemData(i,QVariant(0),Qt.UserRole-1)
                        #恢复下拉菜单可选
                        #combbox.setItemData(i,QVariant(0),Qt.UserRole-0)

                combbox.activated.connect(self.update_macro_table)
                #combbox.currentIndexChanged.connect(self.update_macro_table)
                keyItem = QTableWidgetItem(item)
                keyItem.setToolTip(cfg_dict[item]['help'])
                keyItem.setFlags((Qt.ItemIsEnabled))
                if item in mode_dict:
                    icon_lock = QIcon(":/ico/lock.ico")
                    keyItem.setIcon(icon_lock)
                self.tableWidget.setItem(current_row,0,keyItem)
                self.tableWidget.setCellWidget(current_row,1,combbox)
                #self.tableWidget.removeCellWidget(current_row,1)
                #print (self.tableWidget.cellWidget(0,1).currentText())

    def update_macro_table(self):
        #将当前配置读入缓存
        cfg_temp_dict=copy.deepcopy(self.cfg_output_dict)
        #更新当前配置
        table_item = self.tableWidget.currentRow()
        item_name = self.tableWidget.item(table_item,0).text()
        item_value = self.tableWidget.cellWidget(table_item,1).currentText()
    
        #check本次修改是否成功，处理修改引发的后续关联性修改
        check_status = self.check_update(item_name,item_value,cfg_temp_dict)
        #check_status=1 代表有冲突，check失败
        if check_status:
            #恢复修改前的显示值
            old_value = self.cfg_output_dict[item_name]
            self.tableWidget.cellWidget(table_item,1).setCurrentText(old_value)

    def update_design_tree(self):
        #将当前配置读入缓存
        cfg_temp_dict = copy.deepcopy(self.cfg_output_dict)
        #更新当前配置
        item = self.treeWidget.currentItem()
        module_selected = self.treeWidget.itemWidget(item,1).currentText()
        item_name = item.text(2)
        item_value = module_selected.split(':')[0]

        #check本次修改是否成功，处理修改引发的后续关联性修改
        check_status = self.check_update(item_name,item_value,cfg_temp_dict)
        #check_status=1 代表有冲突，check失败
        if check_status:
            # 恢复修改前的显示值
            old_value = self.cfg_dict[item_name]['module'][self.cfg_output_dict[item_name]]
            self.treeWidget.itemWidget(item,1).setCurrentText(old_value)
            # 更新当前选择
            module_selected = self.treeWidget.itemWidget(item,1).currentText()
            item_name = item.text(2)
            item_value = module_selected.split(':')[0]
            # 有冲突则修改失败，child检查失效
            self.hidden_child(item,item_value,0)
        else:
            self.hidden_child(item,item_value,1)

    def check_update(self,item_name,item_value,cfg_temp_dict):
        #有依赖关系则打印提醒，有静默修改则发出警告
        quiet_change,has_depend,depend_info,depend_dict,cfg_temp_dict = readConfiguration.checkDependence(self,[item_name],item_name,item_value,self.cfg_dict,cfg_temp_dict,0,0,' ',{})
        #若无冲突，可正常更新配置；否则，取消本次修改，给出错误提示；可能发生在两个地方，1是当前修改项，2是静默修改项，均需要做check；
        conflict,conflict_info = readConfiguration.checkConflict(self,item_name,item_value,self.cfg_dict,cfg_temp_dict,depend_dict,0,' ')
        #print (conflict)

        if conflict:
            result = "Failed"
        else:
            result = 'Successfully'
        self.textBrowser.setTextColor(QColor('black'))
        text_out = '[CBS Console]$ 本次修改项 %s，目标配置 %s，结果： %s ' % (item_name,item_value,result)
        self.textBrowser.append(text_out)

        if conflict==0:
            # 没有冲突，更新输出cfg_output_dict
            cfg_temp_dict[item_name] = item_value
            self.cfg_output_dict = copy.deepcopy(cfg_temp_dict)

        if conflict==0 and has_depend and quiet_change==0:
            self.textBrowser.setTextColor(QColor('black'))
            text_out = ' info> 存在依赖关系，且目前均已满足,依赖关系如下: '
            self.textBrowser.append(text_out)
            self.textBrowser.setTextColor(QColor('green'))
            self.textBrowser.append(depend_info)
            QMessageBox.information(self,'信息','该配置存在依赖关系，但没有静默修改，详情见右下角Consel输出信息！')
        if conflict==0 and has_depend and quiet_change:
            #修改配置项显示信息
            for key in depend_dict:
                refresh_unit_item = self.treeWidget.findItems(key,Qt.MatchContains | Qt.MatchRecursive,2)
                refresh_macro_item=self.tableWidget.findItems(key,Qt.MatchContains | Qt.MatchRecursive)
                if len(refresh_unit_item) == 1:
                    is_valid = -1
                    new_text = self.cfg_dict[key]['module'][depend_dict[key]]
                    #findText返回的是index，0不能作为判断条件
                    is_valid = self.treeWidget.itemWidget(refresh_unit_item[0],1).findText(new_text,Qt.MatchExactly|Qt.MatchCaseSensitive)
                    if is_valid != -1:
                        self.treeWidget.itemWidget(refresh_unit_item[0],1).setCurrentText(new_text)
                        self.hidden_child(refresh_unit_item[0],depend_dict[key],1)
                    else:
                        QMessageBox.critical(self,'错误','配置项 %s 的options 格式错误！' % (key))
                elif len(refresh_macro_item) == 1:
                    self.tableWidget.cellWidget(self.tableWidget.row(refresh_macro_item[0]),1).setCurrentText(depend_dict[key])
                else:
                    QMessageBox.critical(self,'错误','配置项名称重复或不存在！')
            #打印提醒信息
            self.textBrowser.setTextColor(QColor('black'))
            text_out = ' warning> 存在依赖关系，通过静默修改后均已满足,修改后的依赖项配置为: '
            self.textBrowser.append(text_out)
            self.textBrowser.setTextColor(QColor('orange'))
            self.textBrowser.append(depend_info)
            QMessageBox.warning(self,'警告','该修改引发静默修改，详情见右下角Consel输出信息,Be Carefully！')
        #处理冲突情况
        if conflict!=0:
            #输出打印信息到控制台
            self.textBrowser.setTextColor(QColor('black'))
            text_out = ' error> Conflict 情况如下: '
            self.textBrowser.append(text_out)
            self.textBrowser.setTextColor(QColor('red'))
            #self.textBrowser.setText(text_out)
            self.textBrowser.append(conflict_info)
            #发出错误警告信息
            QMessageBox.critical(self,'错误','该配置存在被依赖关系，不能设置为当前值，请根据右下角Consel提示信息解除依赖！')
        return conflict

    def hidden_childen(self,item,info):
        item.setHidden(True)
        child_info = ''
        #从cfg_out_dict中删除不必要的层次关系设置项
        if item.toolTip(0):
            del_item = item.text(2)
            child_info = info + ' warning> 关闭设计节点 %s \n' % (item.toolTip(0))
            if del_item in self.cfg_output_dict:
                del self.cfg_output_dict[del_item] 
        #迭代查找child节点
        child_count = item.childCount()
        if child_count>0:
            for i in range(child_count):
                child_info = self.hidden_childen(item.child(i),child_info)
        return child_info

    def show_childen(self,item,info):
        item.setHidden(False)
        add_item = item.text(2)
        child_info = ''
        if add_item:
            #往cfg_out_dict中添加新出现的层次关系设置
            add_value = self.treeWidget.itemWidget(item,1).currentText()
            self.cfg_output_dict[add_item]= add_value.split(':')[0]
            #增加打印信息
            if item.toolTip(0):
                child_info = info + ' warning> 打开子节点：%s --> %s \n' % (item.toolTip(0),add_value.split(':')[0])
        #迭代查找child节点
        child_count = item.childCount()
        if child_count>0:
            for i in range(child_count):
                child_info = self.show_childen(item.child(i),child_info)
        return child_info

    def add_parent(self,item):
        #子节点设置hidden false后父节点自动显示
        #if item.isHidden():
        if item:
            item.setHidden(False)
            if item.toolTip(0):
                self.cfg_output_dict[item.text(2)] = 'D'
                design_tag = self.cfg_dict[item.text(2)]['module']['D']
                self.treeWidget.itemWidget(item,1).setCurrentText(design_tag)
                # 打印直接操作子节点
                child_info = ' warning> 打开设计节点 %s --> D ' % (item.toolTip(0))
                self.textBrowser.setTextColor(QColor('black'))
                self.textBrowser.append(child_info)
            self.add_parent(item.parent())

    def hidden_child(self,item,item_value,not_quiet):
        if item.isHidden():
            item.setHidden(False)
            self.cfg_output_dict[item.text(2)] = item_value.split(':')[0]
            # 打印直接操作子节点
            child_info = ' warning> 新增设计节点 %s --> %s' % (item.toolTip(0),item_value.split(':')[0])
            self.textBrowser.setTextColor(QColor('black'))
            self.textBrowser.append(child_info)
            # 检查父节点，释放被hidden父节点
            self.add_parent(item.parent())
        else:
            #根据树形结构决定子节点是否需要隐藏
            child_count = item.childCount()
            if item_value != 'D':
                child_info = ''
                for i in range(child_count):
                    if not item.child(i).isHidden():
                        #item.child(i).setHidden(True)
                        #迭代处理所有子节点，并返回处理打印信息
                        child_info = self.hidden_childen(item.child(i),child_info)
                        if not_quiet:
                            self.textBrowser.setTextColor(QColor('black'))
                            self.textBrowser.append(child_info)
            else:
                child_info = ' warning> 新增设计节点 %s --> D ' % (item.toolTip(0))
                if not_quiet:
                    self.textBrowser.append(child_info)
                for i in range(child_count):
                    item.child(i).setHidden(False)
                    child_info = self.show_childen(item.child(i),'')
                    if not_quiet:
                        self.textBrowser.append(child_info)

    def applyConfig(self,index):
        textOut_design = saveConfiguration.saveUnitConfiguration(self.treeWidget)
        textOut_macro = saveConfiguration.saveMacroConfiguration(self.tableWidget)
        self.textEdit.setPlainText(textOut_macro+textOut_design)

    def saveConfigFile(self):
        # get the input text
        text,ok = QInputDialog.getText(self,'保存文件','文件名')
        # 判断文件是否已经存在
        if os.path.exists(self.saveDir+'/Makefile.'+text):
            reply = QMessageBox.warning(self,'警告','该文件已存在，确认覆盖保存吗？',QMessageBox.Yes|QMessageBox.Yes,QMessageBox.No)
            if reply == QMessageBox.No:
                text,ok = QInputDialog.getText(self,'保存文件','文件名')
        if ok and text:
            outFile=open(self.saveDir+'/Makefile.%s' % (text),'w')
            # 从gui界面保存配置，所见即所得，被关闭的子节点及叶节点将不出现在配置文件中
            #textOut_cfg = saveConfiguration.saveConfigFileFromGui(self.tableWidget,self.treeWidget)
            # 从主配置字典中保存配置，则被关闭的子节点及叶节点都会被保存入配置文件中
            textOut_cfg = saveConfiguration.saveConfigFile(self.cfg_output_dict)
            outFile.write(textOut_cfg)
            outFile.close()

    def compareConfigFile(self):
        # get the input text
        exist_cfg=QFileDialog.getOpenFileName(self,'open file',self.saveDir)[0]
        if exist_cfg:
            #save current setting first
            outFile=open(QDir.homePath()+'/.current_setting.cbs','w')
            current_cfg = saveConfiguration.saveConfigFile(self.cfg_output_dict)
            outFile.write(current_cfg)
            outFile.close()
            os.system('gvim -d %s %s' % (QDir.homePath()+'/.current_setting.cbs',exist_cfg))
            #os.system('rm .current_setting')
    def exitGui(self):
        if os.path.exists(QDir.homePath()+'/.current_setting.cbs'):
            os.system('rm %s' % (QDir.homePath()+'/.current_setting.cbs'))
        self.close()

    def reloadConfigFile(self):
        self.cfg_dict = readConfiguration.readConfiguration(self.cfg_file,self.usr_cfg_file)
        self.cfg_dict = dict(sorted(self.cfg_dict.items(),key=lambda x:x[0]))
        self.cfg_output_dict = readConfiguration.genOutPutCfg(self.cfg_file,self.usr_cfg_file)
        self.designTree_dict=readConfiguration.genDesignTree(self.cfg_file,self.usr_cfg_file)
        self.cfg_output_dict = dict(sorted(self.cfg_output_dict.items(),key=lambda x:x[0]))
        # 默认配置值检查
        self.check_default_cfg()
        #重建tree結構
        self.treeWidget.clear()
        self.designTree_dict=readConfiguration.genDesignTree(self.cfg_file,self.usr_cfg_file)
        self.build_design_tree(self.treeWidget,self.designTree_dict,self.cfg_output_dict,self.cfg_dict,0,self.current_mode_dict)
        self.treeWidget.sortItems(0,Qt.AscendingOrder)
        #重建table表格
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.build_macro_table(self.cfg_dict,self.cfg_output_dict)

        #打印結果
        self.textBrowser.setTextColor(QColor('black'))
        text_out = '[CBS Console]$ ReLoad Successfully '
        self.textBrowser.append(text_out)

        #消除child節點
        it = QTreeWidgetItemIterator(self.treeWidget)
        while it.value():
            item = it.value()
            if not item.isHidden():
                if item.toolTip(0):
                    item_value = self.treeWidget.itemWidget(item,1).currentText().split(':')[0]
                    self.hidden_child(item,item_value,0)
            it.__iadd__(1)

    def compare_dismatch_cfg(self,load_cfg_dict):
        after_deal_dict = {}
        new_item = '新增配置项设定以下默认值：\n'
        has_delete_item = '以下配置项在新的配置下被删除：\n'
        for cfg_item in self.cfg_output_dict:
            if cfg_item in load_cfg_dict:
                after_deal_dict[cfg_item] = load_cfg_dict[cfg_item]
                del load_cfg_dict[cfg_item]
            else:
                after_deal_dict[cfg_item] = self.cfg_dict[cfg_item]['default']
                new_item = new_item + ' -> '+cfg_item+': '+after_deal_dict[cfg_item]+'\n'
                
        if len(load_cfg_dict):
            for item in load_cfg_dict:
                has_delete_item = has_delete_item + ' -> '+item+': '+load_cfg_dict[item]+'\n'
        if new_item:
            self.textBrowser.setTextColor(QColor('orange'))
            self.textBrowser.append(new_item)
        if has_delete_item:
            self.textBrowser.setTextColor(QColor('orange'))
            self.textBrowser.append(has_delete_item)
        return after_deal_dict

    def loadConfigFile(self):
        # get the input text
        exist_cfg=QFileDialog.getOpenFileName(self,'open file',self.saveDir)[0]
        if exist_cfg:
            load_cfg_dict = readConfiguration.loadExistCfg(exist_cfg)
            # 加载配置可能与当前主配置不一致，处理原则：
            # 1. 多的删除;
            # 2. 少的补充默认值;
            # 3. 给出提示信息;
            self.cfg_output_dict = self.compare_dismatch_cfg(load_cfg_dict)

            self.designTree_dict=readConfiguration.genDesignTree(self.cfg_file,self.usr_cfg_file)
            self.cfg_output_dict = dict(sorted(self.cfg_output_dict.items(),key=lambda x:x[0]))
            # 默认配置值检查
            self.check_default_cfg()
            #重建tree結構
            self.treeWidget.clear()
            self.designTree_dict=readConfiguration.genDesignTree(self.cfg_file,self.usr_cfg_file)
            self.build_design_tree(self.treeWidget,self.designTree_dict,self.cfg_output_dict,self.cfg_dict,0,self.current_mode_dict)
            self.treeWidget.sortItems(0,Qt.AscendingOrder)
            #重建table表格
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            self.build_macro_table(self.cfg_dict,self.cfg_output_dict,self.current_mode_dict)

            #打印結果
            self.textBrowser.setTextColor(QColor('black'))
            text_out = '[CBS Console]$ Load %s Successfully ' % (exist_cfg)
            self.textBrowser.append(text_out)

            #消除child節點
            it = QTreeWidgetItemIterator(self.treeWidget)
            while it.value():
                item = it.value()
                if not item.isHidden():
                    if item.toolTip(0):
                        item_value = self.treeWidget.itemWidget(item,1).currentText().split(':')[0]
                        self.hidden_child(item,item_value,0)
                it.__iadd__(1)


    def creat_rightmenu(self):
        self.treeView_menu=QMenu(self)

        self.actionA = QAction(u'Open With Gvim',self)
        self.actionA.triggered.connect(self.open_with_gvim)

        self.treeView_menu.addAction(self.actionA)
        self.treeView_menu.popup(QCursor.pos())

    def creat_tree_rightmenu(self):
        self.treeView_menu=QMenu(self)

        self.actionA = QAction(u'展开',self)
        self.actionA.triggered.connect(self.expend_child)
        self.treeView_menu.addAction(self.actionA)

        self.actionA = QAction(u'折叠',self)
        self.actionA.triggered.connect(self.collapse_child)
        self.treeView_menu.addAction(self.actionA)

        self.actionA = QAction(u'全部展开',self)
        self.actionA.triggered.connect(self.expend_all)
        self.treeView_menu.addAction(self.actionA)

        self.actionA = QAction(u'全部折叠',self)
        self.actionA.triggered.connect(self.collapse_all)
        self.treeView_menu.addAction(self.actionA)

        self.treeView_menu.popup(QCursor.pos())

    def expend_all(self):
        self.treeWidget.expandAll()

    def collapse_all(self):
        self.treeWidget.collapseAll()

    def expend_child(self):
        item = self.treeWidget.currentItem()
        self.expend_item(item)

    def collapse_child(self):
        item = self.treeWidget.currentItem()
        self.collapse_item(item)

    def expend_item(self,item):
        self.treeWidget.expandItem(item)
        child_count = item.childCount()
        if child_count>0:
            for i in range(child_count):
                self.expend_item(item.child(i))

    def collapse_item(self,item):
        self.treeWidget.collapseItem(item)
        child_count = item.childCount()
        if child_count>0:
            for i in range(child_count):
                self.collapse_item(item.child(i))

    def open_with_gvim(self):
        file_name = self.dir_model.filePath(self.treeView.currentIndex())
        os.system('gvim %s' % (file_name))

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
