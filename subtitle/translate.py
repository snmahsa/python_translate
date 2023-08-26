import os
from googletrans import Translator
from path import get_srt_file, Saveـpath
import random

def translate(origin_lang, dest_lang ,src_file, dest_path, name):
    """
    origin_lang : The language of the file to be translated
    dest_lang : What language should this be translated into?
    src_file : Select the file to be translated
    dest_path : Path to save the translated file
    name : The name of the new file
    """
    nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    if len(name) == 0:
        name = 'translated'.random.randint(1, 100)

    translator = Translator()

    with open(src_file) as f:
        sub_lines = f.readlines()

    with open(os.path.join(dest_path, name), 'w', encoding="utf-8") as f:
        for line_en in sub_lines:
            #print(line_en)
            if line_en[0] in nums:
                f.write(line_en)

            elif line_en=='/n':
                f.write('/n')
            else:
                if line_en:
                    line_fa = translator.translate(line_en, src='en', dest='fa')
                    f.write(line_fa.text)
    