from LiveController import LiveController
from LiveModel import LiveModel
from LiveView import LiveView

if __name__ == '__main__':
    model = LiveModel()
    view = LiveView(model)
    controller = LiveController(model, view)