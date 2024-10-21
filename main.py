import cv2 as cv
import sys

from cv2.mat_wrapper import Mat

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def main(title: str):
    img: Mat = cv.imread(cv.samples.findFile("starry_night.jpg"))
    if img is None:
        sys.exit("Could not read the image.")
    cv.imshow(f"Display window using {title}", img)
    k = cv.waitKey(0)
    # treat the s key as a signal to save the image as a .png
    if k == ord("s"):
        cv.imwrite("starry_night.png", img)
        print("Wrote image as .png")
    else:
        print('Did not write the image as .png')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    msg = f'Python version {get_python_version()}'
    print(msg)
    main(msg)

