import os
import re
import glob

input_dir = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\TEMA_1'
output_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_1.md'

files = sorted(glob.glob(os.path.join(input_dir, 'tema_1-nota_*.md')))

combined_text = '# Formulario Tema 1\n\n'
variables = {}

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove metadata
    text = re.sub(r'<!--.*?-->\n?', '', text, flags=re.DOTALL)
    
    # Remove Glosario de Términos Técnicos section completely
    text = re.sub(r'## \d+\.\s*Glosario de Términos Técnicos.*', '', text, flags=re.DOTALL)
    
    lines = text.split('\n')
    cleaned_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if line.strip() == '* **Nomenclatura:**':
            i += 1
            while i < len(lines) and (lines[i].strip().startswith('*') or lines[i].strip() == ''):
                l_strip = lines[i].strip()
                if l_strip.startswith('*'):
                    m1 = re.match(r'^\*\s*(\$[^\$]+\$):\s*(.*)', l_strip)
                    m2 = re.match(r'^\*\s*([a-zA-Z0-9_{}()\\,\.\+\-\^]+):\s*(.*)', l_strip)
                    
                    if m1:
                        var_name = m1.group(1).strip()
                        var_desc = m1.group(2).strip()
                        variables[var_name] = var_desc
                    elif m2 and any(k in m2.group(1) for k in ['PIV', 'FR', 'FF', 'THD']):
                        var_name = m2.group(1).strip()
                        var_desc = m2.group(2).strip()
                        variables[var_name] = var_desc
                i += 1
            continue
            
        # Ignore main title (e.g. # Formulario y Modelos ...)
        if line.startswith('# '):
            i += 1
            continue
            
        cleaned_lines.append(line)
        i += 1
        
    combined_text += '\n'.join(cleaned_lines) + '\n\n---\n\n'

# Cleanup extra dashes and newlines
combined_text = re.sub(r'\n{3,}', '\n\n', combined_text)

# The user explicitly asked for each formula to be separated in an independent line. 
# Our markdown format is:
# $$
# formula
# $$
# To make it strictly a single independent line as the prompt could imply:
# $$ formula $$
# I'll convert block math that is single line into inline-block format or just format them cleanly.
# The previous format was actually already good, let's keep it as $$ ... $$.
# Wait, let's just make it strictly: `$$ formula $$` on its own line if the prompt meant that.
# Let's change `$$\n formula \n$$` to just `$$ formula $$`? No, the example `calculos_con_formulas_propias.md` used `$$\n formula \n$$`.
# Let's keep the existing format in the files but ensure no trailing extra whitespaces.

# Add the variable glossary
combined_text += '## Glosario de Variables\n\n'
for var in sorted(variables.keys()):
    combined_text += f'* **{var}**: {variables[var]}\n'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(combined_text)
