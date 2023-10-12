# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uvs.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_smt(object):
    def setupUi(self, smt):
        smt.setObjectName("smt")
        smt.setWindowModality(QtCore.Qt.WindowModal)
        smt.resize(1245, 816)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        smt.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ico/uvs_white.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        smt.setWindowIcon(icon)
        smt.setWindowOpacity(10.0)
        smt.setTabShape(QtWidgets.QTabWidget.Rounded)
        smt.setDockNestingEnabled(True)
        self.centralwidget = QtWidgets.QWidget(smt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.broswer_tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.broswer_tabWidget.sizePolicy().hasHeightForWidth())
        self.broswer_tabWidget.setSizePolicy(sizePolicy)
        self.broswer_tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.broswer_tabWidget.setMaximumSize(QtCore.QSize(16777, 16777))
        self.broswer_tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.broswer_tabWidget.setFont(font)
        self.broswer_tabWidget.setMouseTracking(True)
        self.broswer_tabWidget.setTabletTracking(True)
        self.broswer_tabWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.broswer_tabWidget.setAutoFillBackground(True)
        self.broswer_tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.broswer_tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.broswer_tabWidget.setTabsClosable(False)
        self.broswer_tabWidget.setObjectName("broswer_tabWidget")
        self.FileBrowser = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FileBrowser.sizePolicy().hasHeightForWidth())
        self.FileBrowser.setSizePolicy(sizePolicy)
        self.FileBrowser.setBaseSize(QtCore.QSize(170, 100))
        self.FileBrowser.setAccessibleName("")
        self.FileBrowser.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.FileBrowser.setObjectName("FileBrowser")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.FileBrowser)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeView_filebrowser = QtWidgets.QTreeView(self.FileBrowser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_filebrowser.sizePolicy().hasHeightForWidth())
        self.treeView_filebrowser.setSizePolicy(sizePolicy)
        self.treeView_filebrowser.setMinimumSize(QtCore.QSize(170, 100))
        self.treeView_filebrowser.setMaximumSize(QtCore.QSize(167772, 167772))
        self.treeView_filebrowser.setBaseSize(QtCore.QSize(0, 0))
        self.treeView_filebrowser.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeView_filebrowser.setWordWrap(True)
        self.treeView_filebrowser.setObjectName("treeView_filebrowser")
        self.horizontalLayout_2.addWidget(self.treeView_filebrowser)
        self.broswer_tabWidget.addTab(self.FileBrowser, "")
        self.DesignHierarchy = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DesignHierarchy.sizePolicy().hasHeightForWidth())
        self.DesignHierarchy.setSizePolicy(sizePolicy)
        self.DesignHierarchy.setMinimumSize(QtCore.QSize(170, 100))
        self.DesignHierarchy.setBaseSize(QtCore.QSize(170, 100))
        self.DesignHierarchy.setObjectName("DesignHierarchy")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DesignHierarchy)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.DesignHierarchy)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.treeWidget.setFont(font)
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)
        self.broswer_tabWidget.addTab(self.DesignHierarchy, "")
        self.main_tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.main_tabWidget.sizePolicy().hasHeightForWidth())
        self.main_tabWidget.setSizePolicy(sizePolicy)
        self.main_tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.main_tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.main_tabWidget.setFont(font)
        self.main_tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.main_tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.main_tabWidget.setTabsClosable(False)
        self.main_tabWidget.setMovable(True)
        self.main_tabWidget.setObjectName("main_tabWidget")
        self.svgtab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.svgtab.sizePolicy().hasHeightForWidth())
        self.svgtab.setSizePolicy(sizePolicy)
        self.svgtab.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.svgtab.setFont(font)
        self.svgtab.setObjectName("svgtab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.svgtab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea_svg = QtWidgets.QScrollArea(self.svgtab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea_svg.sizePolicy().hasHeightForWidth())
        self.scrollArea_svg.setSizePolicy(sizePolicy)
        self.scrollArea_svg.setBaseSize(QtCore.QSize(1700, 800))
        self.scrollArea_svg.setWidgetResizable(True)
        self.scrollArea_svg.setObjectName("scrollArea_svg")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 894, 563))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea_svg.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea_svg)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ico/process.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.main_tabWidget.addTab(self.svgtab, icon1, "")
        self.macrotab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.macrotab.setFont(font)
        self.macrotab.setObjectName("macrotab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.macrotab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.run = QtWidgets.QPushButton(self.macrotab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ico/new_doc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run.setIcon(icon2)
        self.run.setCheckable(False)
        self.run.setChecked(False)
        self.run.setObjectName("run")
        self.horizontalLayout.addWidget(self.run)
        self.stopSimuate = QtWidgets.QPushButton(self.macrotab)
        self.stopSimuate.setObjectName("stopSimuate")
        self.horizontalLayout.addWidget(self.stopSimuate)
        self.progressBar = QtWidgets.QProgressBar(self.macrotab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_2 = QtWidgets.QFrame(self.macrotab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_13 = QtWidgets.QCheckBox(self.macrotab)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 1, 10, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.macrotab)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.macrotab)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 9, 1, 1)
        self.cleanCB = QtWidgets.QCheckBox(self.macrotab)
        self.cleanCB.setObjectName("cleanCB")
        self.gridLayout.addWidget(self.cleanCB, 1, 0, 1, 1)
        self.waveCB = QtWidgets.QCheckBox(self.macrotab)
        self.waveCB.setObjectName("waveCB")
        self.gridLayout.addWidget(self.waveCB, 4, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.macrotab)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.macrotab)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.macrotab)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.macrotab)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 5, 1, 1)
        self.pld_runCB = QtWidgets.QCheckBox(self.macrotab)
        self.pld_runCB.setObjectName("pld_runCB")
        self.gridLayout.addWidget(self.pld_runCB, 1, 7, 1, 1)
        self.compiler = QtWidgets.QCheckBox(self.macrotab)
        self.compiler.setObjectName("compiler")
        self.gridLayout.addWidget(self.compiler, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.macrotab)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 9, 1, 2)
        self.pldcompCB = QtWidgets.QCheckBox(self.macrotab)
        self.pldcompCB.setObjectName("pldcompCB")
        self.gridLayout.addWidget(self.pldcompCB, 1, 6, 1, 1)
        self.buildCB = QtWidgets.QCheckBox(self.macrotab)
        self.buildCB.setObjectName("buildCB")
        self.gridLayout.addWidget(self.buildCB, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.macrotab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 8, 1, 1)
        self.mlCB = QtWidgets.QCheckBox(self.macrotab)
        self.mlCB.setObjectName("mlCB")
        self.gridLayout.addWidget(self.mlCB, 2, 0, 1, 1)
        self.simu_runCB = QtWidgets.QCheckBox(self.macrotab)
        self.simu_runCB.setObjectName("simu_runCB")
        self.gridLayout.addWidget(self.simu_runCB, 1, 4, 1, 1)
        self.simu_elabCB = QtWidgets.QCheckBox(self.macrotab)
        self.simu_elabCB.setObjectName("simu_elabCB")
        self.gridLayout.addWidget(self.simu_elabCB, 2, 3, 1, 1)
        self.simu_simCB = QtWidgets.QCheckBox(self.macrotab)
        self.simu_simCB.setObjectName("simu_simCB")
        self.gridLayout.addWidget(self.simu_simCB, 2, 4, 1, 1)
        self.cloudCB = QtWidgets.QCheckBox(self.macrotab)
        self.cloudCB.setObjectName("cloudCB")
        self.gridLayout.addWidget(self.cloudCB, 2, 1, 1, 1)
        self.updateconfigsCB = QtWidgets.QCheckBox(self.macrotab)
        self.updateconfigsCB.setObjectName("updateconfigsCB")
        self.gridLayout.addWidget(self.updateconfigsCB, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line_3 = QtWidgets.QFrame(self.macrotab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveDiag = QtWidgets.QPushButton(self.macrotab)
        self.saveDiag.setObjectName("saveDiag")
        self.horizontalLayout_4.addWidget(self.saveDiag)
        self.reload = QtWidgets.QPushButton(self.macrotab)
        self.reload.setObjectName("reload")
        self.horizontalLayout_4.addWidget(self.reload)
        self.selectalltc = QtWidgets.QPushButton(self.macrotab)
        self.selectalltc.setObjectName("selectalltc")
        self.horizontalLayout_4.addWidget(self.selectalltc)
        self.lineEdit = QtWidgets.QLineEdit(self.macrotab)
        self.lineEdit.setTabletTracking(True)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.diag_table = QtWidgets.QTableWidget(self.macrotab)
        self.diag_table.setToolTip("")
        self.diag_table.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.diag_table.setDragEnabled(True)
        self.diag_table.setAlternatingRowColors(True)
        self.diag_table.setShowGrid(False)
        self.diag_table.setGridStyle(QtCore.Qt.DashLine)
        self.diag_table.setObjectName("diag_table")
        self.diag_table.setColumnCount(0)
        self.diag_table.setRowCount(0)
        self.diag_table.horizontalHeader().setCascadingSectionResizes(True)
        self.diag_table.horizontalHeader().setSortIndicatorShown(True)
        self.diag_table.horizontalHeader().setStretchLastSection(True)
        self.diag_table.verticalHeader().setCascadingSectionResizes(True)
        self.diag_table.verticalHeader().setSortIndicatorShown(True)
        self.diag_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.diag_table)
        self.main_tabWidget.addTab(self.macrotab, "")
        self.tooltab = QtWidgets.QWidget()
        self.tooltab.setObjectName("tooltab")
        self.tableWidget = QtWidgets.QTableWidget(self.tooltab)
        self.tableWidget.setGeometry(QtCore.QRect(350, 210, 256, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.main_tabWidget.addTab(self.tooltab, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget_2.setMaximumSize(QtCore.QSize(16777215, 160000))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setToolTipDuration(0)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Consel = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        self.Consel.setFont(font)
        self.Consel.setObjectName("Consel")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Consel)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget_2.addTab(self.Consel, "")
        self.pewview = QtWidgets.QWidget()
        self.pewview.setObjectName("pewview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pewview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.pewview)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.tabWidget_2.addTab(self.pewview, "")
        self.verticalLayout_4.addWidget(self.splitter_2)
        smt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(smt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1245, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")
        self.menuSimulator = QtWidgets.QMenu(self.menuMode)
        self.menuSimulator.setObjectName("menuSimulator")
        self.menuDebug = QtWidgets.QMenu(self.menuMode)
        self.menuDebug.setObjectName("menuDebug")
        self.menuEmulator = QtWidgets.QMenu(self.menuMode)
        self.menuEmulator.setObjectName("menuEmulator")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        smt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(smt)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        smt.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(smt)
        self.toolBar.setObjectName("toolBar")
        smt.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(smt)
        self.toolBar_2.setObjectName("toolBar_2")
        smt.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionsave = QtWidgets.QAction(smt)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/note_accept.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsave.setIcon(icon3)
        self.actionsave.setObjectName("actionsave")
        self.actionreload = QtWidgets.QAction(smt)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ico/refresh.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionreload.setIcon(icon4)
        self.actionreload.setObjectName("actionreload")
        self.actionopen = QtWidgets.QAction(smt)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ico/search_page.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionopen.setIcon(icon5)
        self.actionopen.setObjectName("actionopen")
        self.actionExit = QtWidgets.QAction(smt)
        self.actionExit.setObjectName("actionExit")
        self.actionFile_Bowser = QtWidgets.QAction(smt)
        self.actionFile_Bowser.setObjectName("actionFile_Bowser")
        self.actionConfiguration = QtWidgets.QAction(smt)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.actionXcelium = QtWidgets.QAction(smt)
        self.actionXcelium.setObjectName("actionXcelium")
        self.actionVCS = QtWidgets.QAction(smt)
        self.actionVCS.setObjectName("actionVCS")
        self.actionVerdi = QtWidgets.QAction(smt)
        self.actionVerdi.setObjectName("actionVerdi")
        self.actionVerdi_2 = QtWidgets.QAction(smt)
        self.actionVerdi_2.setObjectName("actionVerdi_2")
        self.actionFormal = QtWidgets.QAction(smt)
        self.actionFormal.setObjectName("actionFormal")
        self.actionPLD = QtWidgets.QAction(smt)
        self.actionPLD.setObjectName("actionPLD")
        self.actionZebu = QtWidgets.QAction(smt)
        self.actionZebu.setObjectName("actionZebu")
        self.actionX1 = QtWidgets.QAction(smt)
        self.actionX1.setObjectName("actionX1")
        self.actionAbout_SMT = QtWidgets.QAction(smt)
        self.actionAbout_SMT.setObjectName("actionAbout_SMT")
        self.menuFile.addAction(self.actionExit)
        self.menuWindow.addAction(self.actionFile_Bowser)
        self.menuWindow.addAction(self.actionConfiguration)
        self.menuSimulator.addAction(self.actionXcelium)
        self.menuSimulator.addAction(self.actionVCS)
        self.menuSimulator.addAction(self.actionVerdi)
        self.menuDebug.addAction(self.actionVerdi_2)
        self.menuEmulator.addAction(self.actionPLD)
        self.menuEmulator.addAction(self.actionZebu)
        self.menuEmulator.addAction(self.actionX1)
        self.menuMode.addSeparator()
        self.menuMode.addSeparator()
        self.menuMode.addSeparator()
        self.menuMode.addAction(self.menuSimulator.menuAction())
        self.menuMode.addAction(self.menuEmulator.menuAction())
        self.menuMode.addAction(self.actionFormal)
        self.menuMode.addAction(self.menuDebug.menuAction())
        self.menuHelp.addAction(self.actionAbout_SMT)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addAction(self.actionreload)
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addSeparator()
        self.toolBar_2.addSeparator()

        self.retranslateUi(smt)
        self.broswer_tabWidget.setCurrentIndex(0)
        self.main_tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(smt)

    def retranslateUi(self, smt):
        _translate = QtCore.QCoreApplication.translate
        smt.setWindowTitle(_translate("smt", "Simulate Manager Tool"))
        self.broswer_tabWidget.setWhatsThis(_translate("smt", "<html><head/><body><p><span style=\" font-weight:600;\">File Browser</span></p></body></html>"))
        self.broswer_tabWidget.setTabText(self.broswer_tabWidget.indexOf(self.FileBrowser), _translate("smt", "File Browser"))
        self.broswer_tabWidget.setTabText(self.broswer_tabWidget.indexOf(self.DesignHierarchy), _translate("smt", "Design Hierarchy"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.svgtab), _translate("smt", "配置管理"))
        self.run.setToolTip(_translate("smt", "执行选中testcase的指定任务，可多任务并行"))
        self.run.setText(_translate("smt", "运行"))
        self.stopSimuate.setToolTip(_translate("smt", "停止选中的testcase项的执行"))
        self.stopSimuate.setText(_translate("smt", "停止"))
        self.progressBar.setToolTip(_translate("smt", "任务进度"))
        self.checkBox_13.setText(_translate("smt", "CheckBox"))
        self.label_3.setText(_translate("smt", "PLD"))
        self.checkBox_4.setText(_translate("smt", "CheckBox"))
        self.cleanCB.setText(_translate("smt", "clean"))
        self.waveCB.setText(_translate("smt", "waveform"))
        self.label.setText(_translate("smt", "Common"))
        self.label_2.setText(_translate("smt", "Simu"))
        self.pld_runCB.setText(_translate("smt", "run"))
        self.compiler.setText(_translate("smt", "compiler"))
        self.label_4.setText(_translate("smt", "Zenu"))
        self.pldcompCB.setText(_translate("smt", "comp"))
        self.buildCB.setText(_translate("smt", "build"))
        self.mlCB.setText(_translate("smt", "multi-lib"))
        self.simu_runCB.setText(_translate("smt", "run"))
        self.simu_elabCB.setText(_translate("smt", "elab"))
        self.simu_simCB.setText(_translate("smt", "sim"))
        self.cloudCB.setText(_translate("smt", "cloud-platform"))
        self.updateconfigsCB.setText(_translate("smt", "update-configs"))
        self.saveDiag.setToolTip(_translate("smt", "保存修改后的diag内容到本地文件"))
        self.saveDiag.setText(_translate("smt", "保存"))
        self.reload.setToolTip(_translate("smt", "同步本地diag文件内容"))
        self.reload.setText(_translate("smt", "刷新"))
        self.selectalltc.setToolTip(_translate("smt", "选择全部testcase项"))
        self.selectalltc.setText(_translate("smt", "全选"))
        self.diag_table.setSortingEnabled(True)
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.macrotab), _translate("smt", "仿真管理"))
        self.main_tabWidget.setTabText(self.main_tabWidget.indexOf(self.tooltab), _translate("smt", "tooltab"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Consel), _translate("smt", "Consel"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.pewview), _translate("smt", "preview"))
        self.menuFile.setTitle(_translate("smt", "File"))
        self.menuWindow.setTitle(_translate("smt", "Window"))
        self.menuMode.setTitle(_translate("smt", "Mode"))
        self.menuSimulator.setTitle(_translate("smt", "Simulator"))
        self.menuDebug.setTitle(_translate("smt", "Debug"))
        self.menuEmulator.setTitle(_translate("smt", "Emulator"))
        self.menuHelp.setTitle(_translate("smt", "Help"))
        self.toolBar.setWindowTitle(_translate("smt", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("smt", "toolBar_2"))
        self.actionsave.setText(_translate("smt", "save"))
        self.actionsave.setToolTip(_translate("smt", "save config file"))
        self.actionreload.setText(_translate("smt", "Reload"))
        self.actionreload.setToolTip(_translate("smt", "重新加载配置文件"))
        self.actionopen.setText(_translate("smt", "open"))
        self.actionExit.setText(_translate("smt", "Exit"))
        self.actionFile_Bowser.setText(_translate("smt", "File Bowser"))
        self.actionConfiguration.setText(_translate("smt", "Basic Configuration"))
        self.actionXcelium.setText(_translate("smt", "Xcelium"))
        self.actionVCS.setText(_translate("smt", "VCS"))
        self.actionVerdi.setText(_translate("smt", "Galasim"))
        self.actionVerdi_2.setText(_translate("smt", "Verdi"))
        self.actionFormal.setText(_translate("smt", "Formal"))
        self.actionPLD.setText(_translate("smt", "PLD"))
        self.actionZebu.setText(_translate("smt", "Zebu"))
        self.actionX1.setText(_translate("smt", "X1"))
        self.actionAbout_SMT.setText(_translate("smt", "About SMT"))
from ui import icon_rc
