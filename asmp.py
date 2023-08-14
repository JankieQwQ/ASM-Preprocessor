import sys
import re

def error(message, code=-1):
    print('[ERROR] ' + message)
    sys.exit(code)

def main(filename):
    text = []
    try:
        with open(filename, 'r') as f:
            text = f.readlines()
    except:
        error('Unable to open the target file')
    defines = {}
    includes = []
    for line in text:
        match_define = re.search(r'#define\s+(\w+)\s+(\w+)', line)
        if match_define:
            word1 = match_define.group(1)
            word2 = match_define.group(2)
            defines[word1] = word2
            continue
        match_include = re.search(r'#include\s*<(.+?)>', line)
        if match_include:
            include_file = match_include.group(1)
            includes.append(include_file)
    new_text = []
    for line in text:
        for word1, word2 in defines.items():
            line = line.replace(word1, word2)
        match_include = re.search(r'#include\s*<(.+?)>', line)
        if match_include:
            include_file = match_include.group(1)
            try:
                with open(include_file, 'r') as inc_file:
                    included_text = inc_file.read()
                    new_text.append(included_text)
            except:
                error(f'Unable to open the included file: {include_file}')
        else:
            new_text.append(line)
    try:
        with open(filename, 'w') as f:
            f.writelines(new_text)
    except:
        error('Unable to write the modified file')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        error('Usage: asmp [ASM File]')
