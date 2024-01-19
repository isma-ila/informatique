from tkinter import *


class LiveController:

    def __init__(self, liveModel, liveView):
        self.model = liveModel
        self.view = liveView
        self.get_canvas = self.view.get_canvas()

        self.view.play()
        #
        self.view.mainloop()

