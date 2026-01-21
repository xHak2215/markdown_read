import os
import sys

file=sys.argv[1]

with open(file, 'r') as f:
    text = f.read()

finally_text=''
start_or_end_code=0

string = text.split('\n')

for item in string:
    st=item.lstrip()
    if item == '':
        finally_text+='\n'

    elif st.startswith('#'):
        finally_text+=f"\33[1;1;1m{st.split(" ", 1)[1]}\33[0m\n"

    elif st.startswith('**') and st.endswith('**'):
        finally_text+=f"\33[1;1;1m{st.split("**")[1]}\33[0m\n"
    
    elif st.startswith('-') or st.startswith('*') or st.startswith('+'):
        finally_text+=f"{st.replace('-', '\33[34m◦\33[0m', 1).replace('*', '\33[34m◦\33[0m', 1).replace('+', '\33[34m◦\33[0m', 1)}\n"
    
    elif st.startswith('__'):
        finally_text+=f"\33[3;1;1m{st.split("__")[1]}\33[0m\n"
    
    elif st.startswith('```'):
        if start_or_end_code == 0:
            finally_text+='\33[3;32;32m'+st.replace("```", '')+'\33[0;0;32m\n\n'
            start_or_end_code+=1
        else:    
            finally_text+=st.replace("```", '\33[0m')+'\n'
            start_or_end_code-=1

    else:
        finally_text+=item+'\n'



print(finally_text)