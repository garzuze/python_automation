# Lucas Garzuze Cordeiro - 29/02/2024
import os
import pdfplumber

all_text = ''
for subdir, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(subdir, file) # forma o nome completo do path, juntando o arquivo com a pasta
            try: 
                with pdfplumber.open(full_path) as pdf_object:
                    for page in pdf_object.pages:
                        single_page_txt = page.extract_text()
                        all_text = f'{all_text}\n{single_page_txt}' 
                    with open(file.replace('.pdf', '.txt'), 'w', encoding='utf-8', newline='') as txt_file:
                        txt_file.write(all_text)
                    pdf_object.close()
                        
            except Exception as e:
                print(e)