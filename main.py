# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
import os
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
#from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#导入designer工具生成的login模块
from cbs_v1 import Ui_MainWindow
import genDesignTree
import readConfiguration
import saveConfiguration
#from xml2tree import genDesignTree


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        #self.gridLayout_config = QtWidgets.QGridLayout(self.subwindow)
        self.subwindow.setWindowTitle('Basic Configuration')
        icon_cfg = QIcon()
        icon_cfg.addPixmap(QPixmap(".\\ico/process.ico"), QIcon.Normal, QIcon.Off)
        self.subwindow.setWindowIcon(icon_cfg)
        self.subwindow_2.setWindowTitle('Increment Compile')
        icon_incr = QIcon("./ico/equalizer.ico")
        #icon_incr.addPixmap(QPixmap(".\\ico/equalizer.ico"), QIcon.Normal, QIcon.Off)
        self.subwindow_2.setWindowIcon(icon_incr)

        self.dir_model = QFileSystemModel()
        self.dir_model.setRootPath(QDir.currentPath())
        self.treeView.setModel(self.dir_model)

        #create right menu
        self.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.creat_rightmenu)

        #tooltip
        QToolTip.setFont(QFont('SansSerif',12))
        self.treeView.setToolTip('单击右键可调出菜单')

        #mdi multi window shou
        self.mdiArea.addSubWindow(self.subwindow_2)
        self.subwindow_2.show()
        self.mdiArea.addSubWindow(self.subwindow)
        self.subwindow.show()

        #********************************************************
        # connect buttons and function 
        #********************************************************
        # button "Apply"
        self.pushButton.clicked.connect(self.applyConfig)
        # button "Save"
        self.pushButton_3.clicked.connect(self.saveConfigFile)

        #read configuration file
        self.cfg_dict = readConfiguration.readConfiguration()
        #print (cfg_dict)
        self.cfg_output_dict = readConfiguration.genOutPutCfg(self.cfg_dict)
    
        #****************************************************
        # add tree item
        #****************************************************
        #gen dict from cfg file
        self.designTree_dict=readConfiguration.genDesignTree()

        self.treeWidget.setColumnCount(3)
        self.treeWidget.setHeaderLabels(['instance','module','item'])
        self.treeWidget.setColumnWidth(0,200)
        self.treeWidget.setColumnWidth(1,150)

        self.build_design_tree(self.treeWidget,self.designTree_dict,self.cfg_output_dict,self.cfg_dict)

        #********************************************************
        # add table item
        #********************************************************
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setColumnWidth(0,200)
        self.tableWidget.setHorizontalHeaderLabels(['macro','value'])
        self.build_macro_table(self.cfg_dict)

    def build_design_tree(self,item,dt_dict,cfg_output_dict,cfg_dict):
        for i in dt_dict.keys():
            sub_item = QTreeWidgetItem(item)
            sub_item.setText(0,i)
            if 'modules' in dt_dict[i]:
                sub_item.setText(2,dt_dict[i]['item_name'])
                combbox = QComboBox()
                combbox.addItems(dt_dict[i]['modules'])
                combbox.setCurrentText(dt_dict[i]['default'])
                self.treeWidget.setItemWidget(sub_item,1,combbox)
                #编程和用户方式都会触发的是currentIndexChanged；只有用户操作才会触发的是activated()
                combbox.activated.connect(self.update_node_expand)
            if 'hdl_path' in dt_dict[i]:
                sub_item.setToolTip(0,dt_dict[i]['hdl_path'])
                sub_item.setToolTip(1,dt_dict[i]['help'])
            if type(dt_dict[i]['sub_tree']) is list:
                continue
            else:
                self.build_design_tree(sub_item,dt_dict[i]['sub_tree'],cfg_output_dict,cfg_dict)
        return item

    def build_macro_table(self,cfg_dict):
        for item in cfg_dict.keys():
            if not 'instance' in cfg_dict[item]:
                current_row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(current_row+1)
                combbox = QComboBox()
                combbox.addItems(cfg_dict[item]['options'])
                combbox.setCurrentText(cfg_dict[item]['default'])
                ##默认不显示任何选项
                #combbox.setCurrentIndex(-1)
                ##获取下拉菜单个数
                #list_num = combbox.count()
                ##关闭所有选项为不可选状态
                #for i in range(list_num):
                #    #恢复下拉菜单可选
                #    #combbox.setItemData(i,QVariant(0),Qt.UserRole-0)
                #    combbox.setItemData(i,QVariant(0),Qt.UserRole-1)
                #combbox.currentIndexChanged.connect(self.update_node_expand)
                keyItem = QTableWidgetItem(item)
                keyItem.setToolTip(cfg_dict[item]['help'])
                #keyItem.setFlags((Qt.ItemIsEnabled))
                self.tableWidget.setItem(current_row,0,keyItem)
                self.tableWidget.setCellWidget(current_row,1,combbox)
                #self.tableWidget.removeCellWidget(current_row,1)
                #print (self.tableWidget.cellWidget(0,1).currentText())
    
    def update_node_expand(self):
        #将当前配置读入缓存
        cfg_temp_dict = self.cfg_output_dict
        #更新当前配置
        item = self.treeWidget.currentItem()
        module_selected = self.treeWidget.itemWidget(item,1).currentText()
        item_name = item.text(2)
        item_value = module_selected.split(':')[0]

        #有依赖关系则打印提醒，有静默修改则发出警告
        status,has_depend,depend_info,depend_dict,cfg_temp_dict = readConfiguration.checkDependence(item_name,item_value,self.cfg_dict,cfg_temp_dict,0,0,' ',{})
        #若无冲突，可正常更新配置；否则，取消本次修改，给出错误提示；可能发生在两个地方，1是当前修改项，2是静默修改项，均需要做check；
        conflict,conflict_info = readConfiguration.checkConflict(item_name,item_value,self.cfg_dict,cfg_temp_dict,depend_dict,0,' ')

        if conflict:
            result = "Failed"
        else:
            result = 'Successfully'
        self.textBrowser.setTextColor(QColor('black'))
        text_out = '[CBS Console]$ 本次修改项 %s，目标配置 %s，结果： %s ' % (item_name,item_value,result)
        self.textBrowser.append(text_out)

        if conflict==0 and has_depend and status==0:
            self.textBrowser.setTextColor(QColor('black'))
            text_out = ' info> 存在依赖关系，且目前均已满足,依赖关系如下: '
            self.textBrowser.append(text_out)
            self.textBrowser.setTextColor(QColor('green'))
            self.textBrowser.append(depend_info)
            QMessageBox.information(self,'信息','该配置存在依赖关系，但没有静默修改，详情见右下角Consel输出信息！')
        if conflict==0 and has_depend and status:
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
                        #print (new_text)
                        self.treeWidget.itemWidget(refresh_unit_item[0],1).setCurrentText(new_text)
                        self.hidden_child(refresh_unit_item[0],depend_dict[key])
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
        if conflict==0:
            cfg_temp_dict[item_name] = item_value
            self.cfg_output_dict = cfg_temp_dict
        else:
            #恢复修改前的显示值
            old_value = self.cfg_dict[item_name]['module'][self.cfg_output_dict[item_name]]
            self.treeWidget.itemWidget(item,1).setCurrentText(old_value)
            #输出打印信息到控制台
            self.textBrowser.setTextColor(QColor('black'))
            text_out = ' error> Conflict 情况如下: '
            self.textBrowser.append(text_out)
            self.textBrowser.setTextColor(QColor('red'))
            #self.textBrowser.setText(text_out)
            self.textBrowser.append(conflict_info)
            #发出错误警告信息
            QMessageBox.critical(self,'错误','该配置存在被依赖关系，不能设置为当前值，请根据右下角Consel提示信息解除依赖！')
            #更新当前选择
            module_selected = self.treeWidget.itemWidget(item,1).currentText()
            item_name = item.text(2)
            item_value = module_selected.split(':')[0]

        self.hidden_child(item,item_value)

    def hidden_child(self,item,item_value):
        #根据树形结构决定子节点是否需要隐藏
        child_count = item.childCount()
        if item_value != 'D':
            for i in range(child_count):
                if not item.child(i).isHidden():
                    item.child(i).setHidden(True)
                    child_info = ' warning> 关闭设计节点 %s\n ' % (item.child(i).toolTip(0))
                    self.textBrowser.append(child_info)
                    #从cfg_out_dict中删除不必要的层次关系设置项
                    del_item = item.child(i).text(2)
                    if del_item in self.cfg_output_dict:
                        del self.cfg_output_dict[del_item] 
        else:
            child_info = ' warning> 新增设计节点 %s\n ' % (item.toolTip(0))
            for i in range(child_count):
                item.child(i).setHidden(False)
                #往cfg_out_dict中添加新出现的层次关系设置
                add_item = item.child(i).text(2)
                add_value = self.treeWidget.itemWidget(item.child(i),1).currentText()
                self.cfg_output_dict[add_item]= add_value.split(':')[0]
                #增加打印信息
                child_info = child_info + '   子节点：%s --> %s \n ' % (item.child(i).toolTip(0),add_value.split(':')[0])
            self.textBrowser.append(child_info)

    def applyConfig(self,index):
        textOut_design = saveConfiguration.saveUnitConfiguration(self.treeWidget)
        textOut_macro = saveConfiguration.saveMacroConfiguration(self.tableWidget)
        self.textEdit.setPlainText(textOut_macro+textOut_design)
        print (self.cfg_output_dict)

    def saveConfigFile(self):
        # get the input text
        text,ok = QInputDialog.getText(self,'保存文件','文件名')
        # 判断文件是否已经存在
        if os.path.exists('./Makefile.'+text):
            reply = QMessageBox.warning(self,'警告','该文件已存在，确认覆盖保存吗？',QMessageBox.Yes|QMessageBox.Yes,QMessageBox.No)
            if reply == QMessageBox.No:
                text,ok = QInputDialog.getText(self,'保存文件','文件名')
        if ok and text:
            outFile=open('./Makefile.%s' % (text),'w')
            textOut_cfg = saveConfiguration.saveConfigFile(self.tableWidget,self.treeWidget)
            outFile.write(textOut_cfg)
            outFile.close()

    def update_src_file(self):
        print ('%s' % (self.combox1.currentText()))

    def creat_rightmenu(self):
        self.treeView_menu=QMenu(self)

        self.actionA = QAction(u'delete',self)

        self.treeView_menu.addAction(self.actionA)
        self.treeView_menu.popup(QCursor.pos())

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
