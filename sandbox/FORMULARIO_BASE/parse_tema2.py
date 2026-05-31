import os
import re
import glob

input_dir = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\TEMA_2'
output_file = r'C:\Users\jesus\REPOS\DIODOS-Y-TRANSISTORES\sandbox\FORMULARIO_BASE\Formulario-tema_2.md'

files = sorted(glob.glob(os.path.join(input_dir, 'tema_2-nota_*.md')))

combined_text = '# Formulario Tema 2\n\n'
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
                    m2 = re.match(r'^\*\s*(?:\*\*)?([A-Za-z0-9_{}()\\,\.\+\-\^]+)(?:\*\*)?:\s*(.*)', l_strip)
                    
                    if m1:
                        var_name = m1.group(1).strip()
                        var_desc = m1.group(2).strip()
                        variables[var_name] = var_desc
                    elif m2:
                        var_name = m2.group(1).strip()
                        var_desc = m2.group(2).strip()
                        # Exclude common sub-bullets that are not variables
                        if var_name.lower() not in ['valores', 'nota', 'condición', 'criterio', 'uso']:
                            variables[var_name] = var_desc
                i += 1
            continue
            
        # Ignore main title
        if line.startswith('# '):
            i += 1
            continue
            
        cleaned_lines.append(line)
        i += 1
        
    combined_text += '\n'.join(cleaned_lines) + '\n\n---\n\n'

# Cleanup extra dashes and newlines
combined_text = re.sub(r'\n{3,}', '\n\n', combined_text)

# Add the variable glossary
combined_text += '## Glosario de Variables\n\n'
for var in sorted(variables.keys()):
    combined_text += f'* **{var}**: {variables[var]}\n'

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(combined_text)
