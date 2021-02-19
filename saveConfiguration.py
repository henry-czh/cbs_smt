#!/usr/bin/env python
from PyQt5.QtWidgets import *

def saveMacroConfiguration(tableWidget):
    #++++++++++++++++++++++++++++++++++++++++
    # collect macro configuration
    #++++++++++++++++++++++++++++++++++++++++
    textOut = ''
    row_count = tableWidget.rowCount()
    for i in range(row_count):
        if type(tableWidget.item(i,0))==QTableWidgetItem:
            macro = tableWidget.item(i,0).text()
            value = ''
            if type(tableWidget.cellWidget(i,1))==QComboBox:
                value = tableWidget.cellWidget(i,1).currentText()
            #if macro and value:
            textOut = textOut+'%s = %s\n' % (macro,value)
    return textOut


def saveUnitConfiguration(treeWidget):
    #++++++++++++++++++++++++++++++++++++++++
    # collect design configuration
    #++++++++++++++++++++++++++++++++++++++++
    textOut='''
config cfg;
    design chip_tb;
    default worklib;
'''
    tree_col_count = treeWidget.columnCount()
    it = QTreeWidgetItemIterator(treeWidget)
    while it.value():
        item = it.value()
        #print (item.toolTip(0))
        if not item.isHidden():
            if item.toolTip(0):
                hdl_path = item.toolTip(0)
                cell_name = treeWidget.itemWidget(item,1).currentText().split(':')[1]
                textOut = textOut + '    instance %s use worklib.%s;\n' % (hdl_path,cell_name)
        it.__iadd__(1)
    textOut = textOut + 'endconfig\n'

    return textOut

def saveConfigFile(tableWidget,treeWidget):
    #++++++++++++++++++++++++++++++
    # save macro value
    #++++++++++++++++++++++++++++++
    textOut = saveMacroConfiguration(tableWidget)

    #++++++++++++++++++++++++++++++
    # save unit value
    #++++++++++++++++++++++++++++++
    it = QTreeWidgetItemIterator(treeWidget)
    while it.value():
        item = it.value()
        #print (item.toolTip(0))
        if not item.isHidden():
            if item.toolTip(0):
                item_name = item.text(2)
                item_value = treeWidget.itemWidget(item,1).currentText().split(':')[0]
                textOut = textOut + '%s = %s\n' % (item_name,item_value)
        it.__iadd__(1)

    return textOut