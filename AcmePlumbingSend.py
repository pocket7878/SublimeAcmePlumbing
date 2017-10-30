import sublime, sublime_plugin
import os
from .Mouse import MouseCommand

class AcmePlumbingSend(MouseCommand):
    """ Sends the current selected text to the plumbing """
    def run(self, edit):
        file_name = self.view.file_name()
        sel = self.selection_at_cursor()
        message = {
            "selection_start": sel.a,
            "selection_end": sel.b,
            "data": self.view.substr(sel),
            "cwd": os.path.dirname(file_name) if file_name else None,
            "src": self.view.id(),
        }
        self.view.sel().clear()
        self.view.run_command("acme_plumbing", message)
