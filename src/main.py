import cv2
import yaml

from src.camera.wro_camera import WROCamera
from src.utils.wro_fps import WROFPS

with open("config/wro_settings.yaml", "r") as file:
    settings = yaml.safe_load(file)


camera = WROCamera(

    settings["camera"]["width"],
    settings["camera"]["height"]

)

fps_counter = WROFPS()


while True:

    frame = camera.get_frame()

    fps = fps_counter.update()

    cv2.putText(

        frame,

        f"FPS : {fps:.1f}",

        (20,40),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,255,0),

        2

    )

    cv2.imshow(

        settings["display"]["window_name"],

        frame

    )

    key = cv2.waitKey(1)

    if key == 27:

        break


camera.release()

cv2.destroyAllWindows()
