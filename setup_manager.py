
OPTIONS={'resources':'''folder.pbm,
floppy_disc.pbm,
lock_icon.pbm,
folder_small.pbm,
arrow_right.pbm,
arrow_left.pbm,
arrow_left_short.pbm,
arrow_right_short.pbm,
exit_icon.pbm, add_icon.pbm,
minus_icon.pbm, arrow_right_down.pbm,
arrow_left_tiny.pbm,
arrow_right_tiny.pbm,
hamburger_icon.pbm,
page_icon.pbm'''}

from setuptools import setup

setup(
app=["ProducerProjectCreator.py"],
version="0.7.0",
options={'py2app' : OPTIONS},
setup_requires=['py2app'],
)