import sys
import subprocess
from PyQt5.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    finished = pyqtSignal(str)  # 任务完成信号

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # 等待子进程完成
        self.process.wait()  # 等待外部进程执行完成
        self.finished.emit(commands[i])  # 发射任务完成信号

class MutiWorkThread():
    def __init__(self, table, consol, progressBar):
        super().__init__()
        self.table = table
        self.consol = consol
        self.progressBar = progressBar
        self.finishedTasks = 0

        self.progressBar.setValue(0)

    def run(self):
        # 定义要执行的命令列表，每个元素是一个命令字符串
        commands = self.collectCMDs()

        # 存储子进程的 Popen 对象
        self.threads = []

        # 启动子进程并存储 Popen 对象
        for command in commands:
            thread = WorkerThread(command)
            thread.finished.connect(self.taskFinished)
            self.threads.append(thread)
            thread.start()

        self.checkProcessStatus()

    def taskFinished(self, testcaseStr):
        self.consol.consel(testcaseStr, 'black')
        self.finishedTasks = self.finishedTasks + 1
        progress_value = (self.finishedTasks / self.threads ) * 100
        self.progressBar.setValue(progress_value)

    def checkProcessStatus(self):
        # 监控每个子进程的状态
        for i, thread in enumerate(self.threads):
            return_code = thread.process.poll()  # 获取子进程的返回码

            if return_code is None:
                self.consol.consel(f"子进程 {commands[i]}: 仍在运行", 'black')
            elif return_code == 0:
                self.consol.consel(f"子进程 {commands[i]}: 执行成功", 'green')
            else:
                self.consol.consel(f"子进程 {commands[i]}: 执行失败 (返回码 {return_code}", 'black')
    
    def collectCMDs(self):
        selected_items = self.collectItems()

        cmds = []
        for item in selected_items:
            cmds.append(self.collectOpts(item))
        
        return cmds

    def collectItems(self):
        # 遍历表格的行
        selected_items = []
        for row in range(self.table.rowCount()):
            status_item = self.table.item(row, 0)
            item = self.table.item(row, 1)
            if item.checkState() == Qt.Checked:
                selected_items.append(self.table.item(row, 2).text())
                # 创建QPixmap对象并设置图像
                pixmap = QPixmap("./ico/loading.png")
                status_item.setIcon(QIcon(pixmap))

        return selected_items

    #********************************************************
    # 运行仿真：1. 收集参数；2. 运行单个用例;
    #********************************************************
    def collectOpts(self, testcase):
        # 1. 收集参数
        cmd = 'make test=' + testcase + ' '
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
        if self.mlCB.isChecked():
            cmd = cmd + 'ml=1 '
        
        self.consol.consel(cmd, 'black')
        return cmd