from flaggart.filehandling import *
import pytest
from PIL import Image

########################################################################################################################################################################
# Unit Tests
########################################################################################################################################################################

#pngify

def test_pngify_basic():
    im1 = Image.open("tests/files/scot.png")
    im2 = pngify(open("tests/files/scot.svg", 'rb'))
    assert list(im1.getdata()) == list(im2.getdata())

#TODO include a test that'll fail due to the brazil flag issue