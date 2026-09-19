import os
import sys
import re

file=sys.argv[1]

with open(file, 'r') as f:
    text = f.read()

finally_text=''
start_or_end_code=0

string = text.split('\n')

for item in string:

    item = re.sub(r'`([^`]+)`', lambda m: f'\033[01;07;38;05;232;48;05;232m{m.group(1)}\033[0m', item)
    item = re.sub(r'\_\_([^`]+)\_\_', lambda m: f'\33[3;1;1m{m.group(1)}\033[0m', item)
    item = re.sub(r'\*\*([^`]+)\*\*', lambda m: f'\33[1;1;1m{m.group(1)}\033[0m', item)
    item = re.sub(r'\~\~([^`]+)\~\~', lambda m: f'\033[30;40;1;9m{m.group(1)}\033[0m', item)
    item = re.sub(r'\*([^`]+)\*', lambda m: f'\033[39;49;3m{m.group(1)}\033[0m', item)

    st = item.lstrip().replace('<br>','\n')

    if item == '':
        finally_text+="\n"

    elif st.startswith('#'):
        finally_text+=f"\33[1;1;1m{st.split(" ", 1)[1]}\33[0m\n"

    elif st.startswith('>'):
        temp = st
        num_s = 0

        for i in range(1, 15):
            if temp.startswith('>'):
                temp = temp.replace('>', "", 1)
                num_s += 1
            else:
                break

        finally_text += f"\033[45;3m{st.replace('>', '\033[30;49;1m| ', num_s)}\33[0m\n"
    
    elif st.startswith('- '):
        finally_text += f"{st.replace('-', '\33[34m◦\33[0m', 1)}\n"
    elif st.startswith('* '):
        finally_text += f"{st.replace('*', '\33[34m◦\33[0m', 1)}\n"
    elif st.startswith('+ '):
        finally_text += f"{st.replace('+', '\33[34m◦\33[0m', 1)}\n"

    elif st.startswith('```'):
        if start_or_end_code == 0:
            finally_text += '\33[3;32;32m'+st.replace("```", '')+'\033[1;48;05;0m\n\n'
            start_or_end_code += 1
        else:    
            finally_text += st.replace("```", '\33[0m')+'\n'
            start_or_end_code -= 1

    elif st.startswith('---') and st.endswith('---'):
        finally_text+=f"\033[0m{'_'*os.get_terminal_size()[0]}\33[0m\n"
    
    else:
        finally_text += item+'\n'

print(finally_text)
