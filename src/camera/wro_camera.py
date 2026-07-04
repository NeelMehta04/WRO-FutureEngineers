"""
wro_camera.py

Camera interface for the Raspberry Pi Camera Module 3 Wide.
"""

from picamera2 import Picamera2
from libcamera import controls

import cv2


class WROCamera:

    def __init__(self,
                 width=640,
                 height=480):

        self.picam2 = Picamera2()

        configuration = self.picam2.create_preview_configuration(

            main={
                "size": (width, height)
            }

        )

        self.picam2.configure(configuration)

        self.picam2.set_controls(
            {
                "AfMode": controls.AfModeEnum.Continuous
            }
        )

        self.picam2.start()

    def get_frame(self):

        frame = self.picam2.capture_array()

        frame = cv2.cvtColor(
            frame,
            cv2.COLOR_RGB2BGR
        )

        return frame

    def release(self):

        self.picam2.stop()
