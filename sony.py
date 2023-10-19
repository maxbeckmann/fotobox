from libsonyapi.camera import Camera, ConnectionError
from libsonyapi.actions import Actions
from PIL import Image
import requests
import threading


class CameraHandler:

    def __init__(self):
        try:
            self._camera = Camera()
        except ConnectionError as ex:
            self._camera = None  # todo: show error on display
            raise ex

    def get_camera(self):
        return self._camera

    def get_one_picture(self):
        try:
            res = self._camera.do(Actions.actTakePicture)
            if res.get('result') is not None:
                photo_path = res['result'][0][0]
                photo_name = photo_path.split('/')[-1]
                im = Image.open(requests.get(photo_path, stream=True).raw)
                im.save('img/' + photo_name)  # todo: directory must be before start and liveview directory
                return im
            return None
        except ConnectionError:
            return None

if __name__ == "__main__":
    c = CameraHandler()
    c.get_one_picture()