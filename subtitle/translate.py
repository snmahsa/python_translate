import os
from googletrans import Translator
from path import get_srt_file, Saveـpath
import random

def translate(origin_lang, dest_lang, src_file, dest_path):
    """
    origin_lang : The language of the file to be translated
    dest_lang : What language should this be translated into?
    src_file : Select the file to be translated
    dest_path : Path to save the translated file
    """
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    name = 'translated' + str(random.randint(1, 100))

    translator = Translator()

    # sub_lines is a list of line's file
    with open(src_file) as f:
        sub_lines = f.readlines()

    if not sub_lines:
        print("The file is empty or there are no lines in it")
    else:
        with open(os.path.join(dest_path, name), 'w', encoding="utf-8") as f:
            for line in sub_lines:
                if line and len(line) > 0:
                    if line[0] in nums:
                        f.write(line)
                    elif line == '/n':
                        f.write('/n')
                    else:
                        try:
                            line_dest = translator.translate(line, src=origin_lang, dest=dest_lang)
                            f.write(line_dest.text)
                        except Exception as e:
                            print(f"An error occurred during translation: {str(e)}")


