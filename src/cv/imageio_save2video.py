import imageio
import os

invideopath = "sample_in.mp4"

#---------------------------------------------------------------------
outvideopath = "sample_out.mp4"
# You need to install the program FFMPEG and tell it where it is installed
os.environ['IMAGEIO_FFMPEG_EXE'] =  r"C:\Program Files\ffmpeg-2021-11-18-git-85a6b7f7b7-essentials_build\bin\ffmpeg.exe"


reader = imageio.get_reader(invideopath)
fps = reader.get_meta_data()['fps']

writer = imageio.get_writer(outvideopath, fps=fps)

for im in reader:
    # im is numpy array
    writer.append_data(im)
writer.close()

print("done")
