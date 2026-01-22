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
    st = item.lstrip().replace('<br>','\n')

    st=re.sub(r'`([^`]+)`', lambda m: f'\033[01;07;38;05;232;48;05;232m{m.group(1)}\033[0m', st)
    
    st=re.sub(r'\_\_([^`]+)\_\_', lambda m: f'\33[3;1;1m{m.group(1)}\033[0m', st)
    
    st=re.sub(r'\*\*([^`]+)\*\*', lambda m: f'\33[1;1;1m{m.group(1)}\033[0m', st)

    if item == '':
        finally_text+='\n'

    elif st.startswith('#'):
        finally_text+=f"\33[1;1;1m{st.split(" ", 1)[1]}\33[0m\n"
    
    elif st.startswith('- ') or st.startswith('* ') or st.startswith('+ '):
        finally_text+=f"{st.replace('-', '\33[34m◦\33[0m', 1).replace('*', '\33[34m◦\33[0m', 1).replace('+', '\33[34m◦\33[0m', 1)}\n"
    
    elif st.startswith('```'):
        if start_or_end_code == 0:
            finally_text+='\33[3;32;32m'+st.replace("```", '')+'\033[1;48;05;0m\n\n'
            start_or_end_code+=1
        else:    
            finally_text+=st.replace("```", '\33[0m')+'\n'
            start_or_end_code-=1
    
    else:
        finally_text+=st+'\n'
    
    #while bool(re.search(r'`[^`]`', bufer_st)) or bool(re.search(r'\_\_[^*]+\_\_', bufer_st)) or bool(re.search(r'\*\*[^*]+\*\*', bufer_st)):

print(finally_text)