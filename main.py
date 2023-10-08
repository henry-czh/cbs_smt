# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#��������������������
import sys
import os
import copy
import subprocess
import signal
import time

#PyQt5��������������������PyQt5.QtWidgets������
#from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from xml.etree import ElementTree as ET

#����designer����������login����
from ui.uvs import Ui_smt
from backend_scripts import genDesignTree
from backend_scripts import extractDiag
from custom_pyqt import webChannel
from custom_pyqt.custom_widget import *
from ico import icon

from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import QComboBox, QSpinBox
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtSvg import QSvgRenderer, QGraphicsSvgItem
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngine import QtWebEngine


class MyMainForm(QMainWindow, Ui_smt):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 设置窗口关闭策略为允许通过关闭按钮关闭
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.setWindowFlags(self.windowFlags() | Qt.WindowCloseButtonHint)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # System Setting
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.cfg_file = os.getenv('BASE_CONFIG_FILE')
        self.usr_cfg_file = os.getenv('USER_CONFIG_FILE')
        self.saveDir = os.getenv('CONFIG_SAVE_DIR')
        self.svgfile = os.getenv('SVG_FILE')
        self.html_file = os.getenv('HTML_FILE')
        self.diag_file = os.getenv('DIAG_FILE')
        #self.saveDir = os.path.abspath(os.path.join(os.getcwd(), "../config"))

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Create Console Window
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.textBrowser = ColoredTextBrowser(self.Consel)
        font = QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 启动后台CGI服务
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 要执行的外部命令
        #cgi_path = os.path.abspath(os.path.join(os.getcwd(), "verif_config"))
        #command = "cd %s; python2 -m CGIHTTPServer 8008  > ~/.uvs/cgihttp.out" % (cgi_path)

        # 使用subprocess.Popen()创建非阻塞子进程
        #self.process = subprocess.Popen(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setsid)

        # 获取命令的标准输出和标准错误
        #stdout_data, stderr_data = process.communicate()
        #self.textBrowser.consel(process.stdout, 'black')
        #self.textBrowser.consel(process.stderr, 'black')

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 创建一个web界面
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        #self.main_tabWidget.addTab(self.web_view, "HTML")
        # 创建 QWebEngineView 组件
        self.web_view = QWebEngineView()
        self.main_tabWidget.setTabText(0, "仿真配置")
        self.scrollArea_svg.setWidget(self.web_view)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 增加web与qt程序之间的数据通道
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.data_obj = webChannel.DataObject(self.textBrowser)

        # 将数据对象添加到Web通道
        self.web_channel = QWebChannel()
        self.web_channel.registerObject("dataObj", self.data_obj)
        self.web_view.page().setWebChannel(self.web_channel)


        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 加载web界面
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        #self.web_view.loadFinished.connect(self.loadFinished)
        #self.web_view.loadProgress.connect(self.loadProgress)
        self.web_view.setUrl(QUrl.fromLocalFile(self.html_file))
        #self.web_view.setUrl(QUrl("http://127.0.0.1:8008/qtconfig.html"))

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 打开外部网页, 用以集成内网各平台环境
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 创建 QWebEngineView 组件
        self.baidu_view = QWebEngineView()
        self.main_tabWidget.addTab(self.baidu_view, "搜索引擎")
        self.baidu_view.setUrl(QUrl("http://www.baidu.com"));

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # 创建一个文件浏览器
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.dir_model = QFileSystemModel()
        self.dir_model.setReadOnly(True)
        #self.current_path = QDir.currentPath()
        self.current_path = os.getenv('CBS_HOME')
        self.dir_model.setRootPath(self.current_path)
        self.treeView_filebrowser.setModel(self.dir_model)
        self.treeView_filebrowser.setRootIndex(self.dir_model.index(self.current_path))
        self.treeView_filebrowser.setColumnWidth(0, 300)

        # create right menu
        self.treeView_filebrowser.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeView_filebrowser.customContextMenuRequested.connect(self.creat_rightmenu)
        # double click
        self.treeView_filebrowser.doubleClicked.connect(self.creat_rightmenu)
        
        # tooltip
        QToolTip.setFont(QFont('SansSerif',10))
        self.treeView_filebrowser.setToolTip('双击或单击右键可调出菜单')

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Create Diag Table
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.diag_info = extractDiag.extractDiag(self.diag_file)
        self.textBrowser.consel("打开diag文件成功!", 'green')

        # 设置初始行数和列数
        line_nums = len(self.diag_info)
        self.diag_table.setRowCount(line_nums)
        self.diag_table.setColumnCount(10)

        # 设置选择模式为整行选择
        self.diag_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 隐藏行序号
        self.diag_table.verticalHeader().setVisible(False)

        # 设置表头标签
        table_header = [" ", " ",
                        "testcase*", 
                        "path*", 
                        "config*",
                        "comp_argvs",
                        "run_argvs",
                        "run_boards",
                        "scp",
                        "argv"]
        self.diag_table.setHorizontalHeaderLabels(table_header)

        self.table_data = []  # 存储表格数据的列表
        for row, rowData in enumerate(self.diag_info):
            self.table_data.append(rowData)
            for col, cellData in enumerate(rowData):
                item = QTableWidgetItem(str(cellData))
                self.diag_table.setItem(row, col+2, item)

            # 在每行的最后一列添加一个勾选框
            checkbox = QCheckBox()
            self.diag_table.setCellWidget(row, 1, checkbox)

        # 连接文本框的文本更改事件到过滤函数
        self.lineEdit.textChanged.connect(self.filterTable)
        # 设置占位符文本
        self.lineEdit.setPlaceholderText("Filter..")

        # 调整列宽以适应内容
        self.diag_table.resizeColumnsToContents()

        # 为表格添加右键菜单
        self.diag_table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.diag_table.customContextMenuRequested.connect(self.diagTableContextMenu)

        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Set statusbar information
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.statusbar.showMessage('如有疑问, 请联系 chaozhanghu@phytium.com.cn  @Qsmtool 23.09-0001')
        self.statusbar.show()

       # #********************************************************
       # # connect buttons and function 
       # #********************************************************
        self.run.clicked.connect(self.runSimulate)
       # # button "Apply"
       # self.pushButton.clicked.connect(self.applyConfig)
       # # button "Save"
       # self.pushButton_3.clicked.connect(self.saveConfigFile)
       # # button "Compare"
       # self.pushButton_5.clicked.connect(self.compareConfigFile)
       # # button "open"

       # self.pushButton_6.clicked.connect(self.loadConfigFile)
       # # tool button "reload"
        #self.actionopen.triggered.connect(self.loadConfigFile)

        # action "Exit"
        self.actionExit.triggered.connect(self.exitGui)

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

    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #   xxxxxxxxxx      Functions       xxxxxxxxxxxx
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def runSimulate(self):
        cmd = ' '
        if self.cleanCB.isChecked():
            cmd = cmd + 'clean '
        if self.updateconfigsCB.isChecked():
            cmd = cmd + 'updateconfigs '
        if self.buildCB.isChecked():
            cmd = cmd + 'build '
        if self.compiler.isChecked():
            cmd = cmd + 'compiler '
        if self.simu_runCB.isChecked():
            cmd = cmd + 'run '
        if self.simu_elabCB.isChecked():
            cmd = cmd + 'elab '
        if self.simu_simCB.isChecked():
            cmd = cmd + 'sim '
        if self.pldcompCB.isChecked():
            cmd = cmd + 'comp '
        if self.pld_runCB.isChecked():
            cmd = cmd + 'run '

        cmd = 'make' + cmd
        self.textBrowser.consel(cmd, 'black')
    #********************************************************
    # 自定义关闭串口前的动作
    #********************************************************
    def closeEvent(self, event):
        # 在关闭窗口前执行自定义动作
        confirm = self.confirmation_dialog()
        if confirm:
            if os.path.exists(QDir.homePath()+'/.current_setting.cbs'):
                os.system('rm %s' % (QDir.homePath()+'/.current_setting.cbs'))
            #self.process.terminate()
            #self.process.wait()
            #os.killpg(self.process.pid,signal.SIGTERM) 
            event.accept()  # 允许关闭窗口
        else:
            event.ignore()  # 取消关闭窗口

    def confirmation_dialog(self):
        # 创建一个确认对话框
        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("确认关闭窗口")
        confirm_dialog.setText("是否确定关闭窗口?")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        # 显示对话框并等待用户的选择
        user_choice = confirm_dialog.exec_()

        # 根据用户的选择返回True或False
        if user_choice == QMessageBox.Yes:
            return True
        else:
            return False

    def filterTable(self):
        filter_text = self.lineEdit.text().strip()
        for row, rowData in enumerate(self.table_data):
            show_row = any(filter_text in str(cellData).lower() for cellData in rowData)
            self.diag_table.setRowHidden(row, not show_row)

    def diagTableContextMenu(self, pos):
        # 创建右键菜单
        context_menu    = QMenu(self)
        action_edit     = QAction("编辑", self)
        action_delete   = QAction("删除", self)
        action_add      = QAction("新增", self)

        # 连接菜单项的槽函数
        action_edit.triggered.connect(self.editTableItem)
        action_delete.triggered.connect(self.deleteTableItem)
        action_add.triggered.connect(self.addTableItem)

        # 将菜单项添加到右键菜单
        #context_menu.addAction(action_edit)
        context_menu.addAction(action_delete)
        context_menu.addAction(action_add)

        # 显示右键菜单
        context_menu.exec_(self.diag_table.mapToGlobal(pos))

    def editTableItem(self):
        # 编辑选定的表格项
        selected_items = self.diag_table.selectedItems()
        if selected_items:
            item = selected_items[0]
            item.setText("编辑后的内容")

    def deleteTableItem(self):
        # 删除选定的行
        selected_rows = set()
        for item in self.diag_table.selectedItems():
            selected_rows.add(item.row())

        for row in selected_rows:
            self.diag_table.removeRow(row)

    def addTableItem(self):
        # 新增一行并复制当前选中的行
        selected_rows = set()
        for item in self.diag_table.selectedItems():
            selected_rows.add(item.row())

        new_row = self.diag_table.rowCount()
        self.diag_table.insertRow(new_row)

        # 在每行的最后一列添加一个勾选框
        checkbox = QCheckBox()
        self.diag_table.setCellWidget(new_row, 1, checkbox)

        if not selected_rows:
            return

        for row in selected_rows:
            for col in range(self.diag_table.columnCount()):
                if col in [0,1]:
                    continue
                source_item = self.diag_table.item(row, col)
                if source_item:
                    if col == 2:
                        new_item = QTableWidgetItem(source_item.text()+'_new')
                    else:
                        new_item = QTableWidgetItem(source_item.text())
                    self.diag_table.setItem(new_row, col, new_item)
        
        # 调整列宽以适应内容
        self.diag_table.resizeColumnsToContents()

    def exitGui(self):
        self.close()

    def loadFinished(self, ok):
        if not ok:
            print("页面加载失败")

    def loadProgress(self, progress):
        print("加载进度:", progress)

    def Click_Svg(self, event):
        # 这是鼠标点击事件的处理函数
        # event 是一个鼠标事件对象，你可以在这里实现自定义的交互逻辑
        pos = self.view.mapToScene(event.pos())  # 将窗口坐标映射到场景坐标
        #items = self.scene.items(pos)
        items = self.scene.itemAt(pos, self.view.transform())
        #for item in items:
        if isinstance(items, QGraphicsSvgItem):
            self.textBrowser.consel(items.elementId(), 'black')
                # 找到了 SVG 图像项
                # 获取元素的属性并显示
                #self.textBrowser.consel("Clicked on an SVG item at position (%d, %d)" %(pos.x(), pos.y()), 'black')
                #element_index = item.renderer().elementAt(pos.toPoint())
                #self.textBrowser.consel(element_index, 'black')
                #element_attributes = item.renderer().elementAttributes(item.renderer().elementAt(pos.toPoint()))
                #for attr_name, attr_value in element_attributes.items():
                #    #print(f"{attr_name}: {attr_value}")
                #    self.textBrowser.consel("(%s, %s)" %(attr_name, attr_value), 'black')
                # 如果点击了 SVG 图像，检查是否有超链接
                #if self.hasHyperlink(item, pos):
                #    # 执行超链接相关的操作
                #    self.textBrowser.consel("Clicked on SVG item with hyperlink",'green')
                #else:
                #    self.textBrowser.consel("no", 'red')

    def hasHyperlink(self, svg_item, pos):
        # 检查 QGraphicsSvgItem 是否包含超链接
        # 解析 SVG 图像以查找 <a> 元素并获取其超链接目标
        svg_tree = ET.parse(self.svgfile)
        root = svg_tree.getroot()
        for elem in root.iter():
            if not svg_item.contains(svg_item.mapFromScene(pos)):
                continue
            if not elem.tag.endswith('}a'):
                continue
            xlink_href = elem.get('{http://www.w3.org/1999/xlink}href')
            self.textBrowser.consel(xlink_href, 'black')
            #if xlink_href and svg_item.contains(svg_item.mapFromScene(svg_item.sceneBoundingRect().topLeft())):
            if xlink_href:
                return True
            else:
                return False
        return False

    def open_with_gvim(self):
        index = self.treeView_filebrowser.currentIndex()
        if index.isValid() and not self.dir_model.isDir(index):
            file_name = self.dir_model.filePath(index)
            self.textBrowser.consel("打开文件 %s" % (file_name), 'black')
            os.system('gvim --remote-tab-silent %s' % (file_name))

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

    def creat_rightmenu(self):
        self.treeView_menu=QMenu(self)

        self.actionA = QAction(u'Open With Gvim',self)
        self.actionA.triggered.connect(self.open_with_gvim)

        self.treeView_menu.addAction(self.actionA)
        self.treeView_menu.popup(QCursor.pos())

if __name__ == "__main__":
    #QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    
    ## 设置Qt::AA_UseOpenGLES属性
    #QCoreApplication.setAttribute(Qt.AA_UseOpenGLES)

    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
