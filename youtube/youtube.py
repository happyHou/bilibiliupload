# -*- coding:utf-8 -*-
from bilibiliupload import *
import os
import time
import glob

video_dir = '/Users/happyhou/onedrive/OneDrive - vlity.ac.id/11'
b = Bilibili()

login_status = b.login('username', 'pass')
print("Login:", login_status)


def upload(video_file, title, cover):
    videoPart = VideoPart(video_file, title, title)
    tags = {u"婆媳关系", u"搞笑", u"惊奇", u"沙雕", u"感人", u"亲情", u"电影剪辑", u"喜剧"}
    b.upload(parts=videoPart, title=title, tid=21, tag=tags, desc=title,
             source='', cover=b.cover_up(cover))


def log(str):
    print("logE>>>> ", str)


file_total_count = len(glob.glob1(video_dir, "*.mp4"))
current = 1
files = os.listdir(video_dir)
for file in files:
    pattern = file.split(".", 1)
    if pattern[1] == "mp4":
        log("begin" + pattern[0])
        print(current, "/", file_total_count)
        current = current + 1
        upload(os.path.join(video_dir, file), pattern[0],
               os.path.join(video_dir, pattern[0] + ".jpg"))
        log("remove")
        os.remove(os.path.join(video_dir, file))
        os.remove(os.path.join(video_dir, pattern[0] + ".jpg"))
        log("sleep 1 minutes")
        time.sleep(60)

