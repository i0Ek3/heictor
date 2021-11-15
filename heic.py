import os
import pyheif

from PIL import Image
from loguru import logger


BLUE = '\033[34m'
CYAN = '\033[36m'


def read_and_save(filename, itype):
    heif_file = pyheif.read(filename + "HEIC")
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    filename += itype
    image.save(filename, itype)


def check(filename, bits):
    types = ["JPEG", "PNG", "HEIC", "jpeg", "png", "heic"]
    ext = filename[len(filename)-bits:]

    if len(ext) != bits:
        logger.error(BLUE + "Wrong bits!")
        os._exit()
    elif ext not in types:
        logger.error(BLUE + "Please input the correct filename: {}".format(ext))
        os._exit()
    else:
        pass



def main():

    heic = input(CYAN + "Please input the heic filename[example.HEIC]: \n")
    name = heic[:-4]
    check(heic, len(heic)-len(name))

    itype = input(CYAN + "Please specific the type you want to save[JPEG, PNG]: \n")
    check(itype, len(itype))
    read_and_save(name, itype)


if __name__ == '__main__':
    main()
