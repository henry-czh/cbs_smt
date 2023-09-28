import sys
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)

class DataObject(QObject):
    dataChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._data = ""

    @pyqtSlot(str)
    def setData(self, data):
        self._data = data
        self.dataChanged.emit(data)

    @pyqtSlot(result=str)
    def getData(self):
        return self._data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("数据交互示例")

        self.web_view = QWebEngineView(self)
        self.setCentralWidget(self.web_view)

        self.data_obj = DataObject()

        # 将数据对象添加到Web通道
        self.web_channel = QWebChannel()
        self.web_channel.registerObject("dataObj", self.data_obj)
        self.web_view.page().setWebChannel(self.web_channel)

        # 加载包含JavaScript的HTML文件
        self.web_view.setHtml("""
            <html>
            <head>
                <script type="text/javascript" src="qrc:///qtwebchannel/qwebchannel.js"></script>
            </head>
            <body>
                <h1>Data from JavaScript:</h1>
                <p id="dataDisplay"></p>
                <button onclick="setDataToPython()">Set Data to Python</button>
                <button onclick="getDataFromPython()">Get Data from Python</button>
                <script type="text/javascript">
                    var dataDisplay = document.getElementById("dataDisplay");
                    new QWebChannel(qt.webChannelTransport, function(channel) {
                        var dataObj = channel.objects.dataObj;

                        // 设置数据到Python
                        window.setDataToPython = function() {
                            var newData = "11111111Data from JavaScript";
                            dataObj.setData(newData);
                        };

                        // 从Python获取数据
                        window.getDataFromPython = function() {
                            var data = dataObj.getData();
                            dataDisplay.innerHTML = data;
                        };
                    });
                </script>
            </body>
            </html>
        """)

if __name__ == '__main__':
    window = MainWindow()
    window.setGeometry(100, 100, 800, 600)
    window.show()

    sys.exit(app.exec_())

