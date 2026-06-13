#while page.locator(".protocol.gupshup:not(.ativo)").count()> 0:
    while page.locator(".protocol.gupshup").count()> 0:
        try:
            email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
            oab_pattern = r"\b\d{5,6}(?:[\/\-][A-Z]{2})?\b"
            cpf_pattern = r"\b\d{3}\.?\d{3}\.?\d{3}\-?\d{2}\b"
            telefone_pattern = r"\b(?:+55\s?)?(?:(?\d{2})?\s?)?(?:9\d{4}|\d{4})-?\d{4}\b"
            matricula_pattern = r"\b\d{5,6}(?:[\/\-][A-Z]{2})?\b"
            
            
            #### Capturar dentro da Mensagem ######
            page.wait_for_selector(".message_user")
            
            #pega apenas o que não estou 
            cards = page.locator(".protocol.gupshup")
            total_cards = cards.count()
            
            print (f"total de atendimentos:{total_cards}")

            #Sempre pega o primeiro diponivel
            card = cards.first
            card.click()
                
                
            #------------- Variaveis por atendimento ----------#
            tipo_usuario = None
            tipo_assunto = None
            oab = None
            email = None
            ja_imprimiu = False #Flag de controle
            matricula = None
            cpf = None
            
            mensagens_usuario = page.locator('.message_user')
            total = mensagens_usuario.count()
            
            
        #if total > ultimo_total:
        #    print(f"Novas mensagens{total - ultimo_total}")
        
            for i in range(total):
                msg = mensagens_usuario.nth(i)
                texto = msg.text_content()
                
                if not texto:
                    continue
                
                texto_limpo = texto.strip()
                
                #print ("Mensagem lidas:",texto_limpo)
                
                #--------- Coletando Perfil ----------------#
                if "advogado" in texto_limpo.lower():
                    tipo_usuario = "Advogado"
                
                elif "servidor" in texto_limpo.lower():
                    tipo_usuario = "Servidor"
                
                elif "público em geral" in texto_limpo.lower():
                    tipo_usuario = "PGeral"
                
            
                #----------Se for Servidor -----------------#
                if tipo_usuario == "Servidor":
                    matricula_encontrada = re.findall(matricula_pattern, texto_limpo)
                    if matricula_encontrada:
                        matricula = matricula_encontrada.group()
                        
                if tipo_usuario == "Servidor" and not ja_imprimiu :
                    print("usuario: Sevidor")
                    #print("matricula:", matricula)
                    print("-"*20)
                    
                    ja_imprimiu = True
                    break #opcional para o loop. 

                #--------- Se For Advogado ----------------#
                
                if tipo_usuario == "Advogado":
                    oab_encontradas = re.findall(oab_pattern, texto_limpo)
                    email_encontrado = re.findall(email_pattern, texto_limpo)
                    
                    if oab_encontradas:
                        oab = oab_encontradas.group()
                        
                    if email_encontrado:
                        email = email_encontrado.group()
                
                if tipo_usuario == "Advogado" and not ja_imprimiu:
                    print("usuario: Advogado")
                    print(f"OAB:{oab}")
                    #print(f"Email:{email}")
                    print("-"*20)
                    
                    ja_imprimiu = True
                    break #opcional para o loop. 
                
                    #ultimo_total = total
                    time.sleep(5)
                    
        except Exception as e:
            print("Erro no monitoramento", e)
            time.sleep(3)