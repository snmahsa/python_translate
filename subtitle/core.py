import os
from path import get_srt_file, Saveـpath
from translate import translate

def run():
    src_file = get_srt_file()
    dest_path = Saveـpath()
    if src_file is not None and dest_path is not None:
        translate(origin_lang, dest_lang, src_file, dest_path)
    else:
        print('It is necessary to select the translatable file and the path to save the translation')    

