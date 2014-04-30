from PySide.QtGui import QDialog
import ui.start_dlg_ui

class StartDialog(QDialog):
    """
    Shows starting dialog.
    """
    def __init__(self,parent=None):
        super(StartDialog, self).__init__(parent)
        self.ui = ui.start_dlg_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.setModal(True)
        self.ui.progressBar.setRange(0, 100)
        self.show()
        self.ui.progressBar.setValue(1)

    def version(self, version):
        self.ui.labelVersion.setText("V."+str(version))
        
    def progress(self,  value):
        self.ui.progressBar.setValue(value)
        
    #@TODO: put another text message to inform what it is doing...
