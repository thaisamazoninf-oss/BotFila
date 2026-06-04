import time
import re
from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()
    
    page.goto("https://chat.sonax.net.br/app/omnichannel/chat")
    
    page.wait_for_selector("body > app-root > app-login > div > div.left-side > div > div:nth-child(2) > input")
    
    #usuário
    page.fill("body > app-root > app-login > div > div.left-side > div > div:nth-child(2) > input", "atendente02@amazoninf.com.br")
    #senha
    page.fill("div.left-side-form-input:nth-child(3) > input:nth-child(2)", "Amazon@2025")
    #Clique botão entrar
    page.click("button.roboto")
    time.sleep(2)
    #page.click("#botao-fechar")
    
    #Aguardar aparece a aba Conversando
    page.wait_for_selector("body > app-root > app-layout > ng-sidebar-container > div > div > app-chat-home > app-content > main > div > div > div > div.chats-nav.ng-star-inserted > div.chat_item_header.types-bot > span:nth-child(2)")
    
    #Selecionar aba de atendimento: BOT/Fila/Conversando
    page.click("body > app-root > app-layout > ng-sidebar-container > div > div > app-chat-home > app-content > main > div > div > div > div.chats-nav.ng-star-inserted > div.chat_item_header.types-bot > span:nth-child(3)")
    print("clique aba de atendimento")
    
    #Aguardar aparece a aba Conversando
    page.wait_for_selector("body > app-root > app-layout > ng-sidebar-container > div > div > app-chat-home > app-content > main > div > div > div > div.chats-nav.ng-star-inserted > app-protocol-list > div > app-protocol-item > div")
    
    #Clique na aba fila
    page.click("body > app-root > app-layout > ng-sidebar-container > div > div > app-chat-home > app-content > main > div > div > div > div.chats-nav.ng-star-inserted > app-protocol-list > div > app-protocol-item > div")
    print("clique no  ticket")
    
    page.wait_for_selector(".protocol.gupshup",timeout=5000)

    #pega apenas o que não estou 
    cards = page.locator(".protocol.gupshup")
    total_cards = cards.count()
    
    print (f"total_mensagens de atendimentos:{total_cards}")
    
    for i in range(total_cards):
        cards = page.locator(".protocol.gupshup")
        card = cards.nth(i)
        
        print(f"\nAbrindo atendimento {i + 1}")
        
        card.click()
        
        try:
            page.wait_for_selector(".message_user", timeout=5000)
        except TimeoutError:
            print("Nenhuma mensagem do usuário encontrada")
            continue
        
        #------------- Variaveis por atendimento ----------#
        tipo_usuario = None
        tipo_assunto = None
        oab = None
        email = None
        ja_imprimiu = False #Flag de controle
        matricula = None
        cpf = None
    
        email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        oab_pattern = r"\b\d{5,6}(?:\/[A-Z]{2})?\b"
        cpf_pattern = r"\b\d{3}\.?\d{3}\.?\d{3}\-?\d{2}\b"
        telefone_pattern = r"\b(?:+55\s?)?(?:(?\d{2})?\s?)?(?:9\d{4}|\d{4})-?\d{4}\b"
        matricula_pattern = r"\b\d{5,6}(?:[\/\-][A-Z]{2})?\b"
        

        mensagens = page.locator('.message_user')
        total_mensagens = mensagens.count()

        for j in range(total_mensagens):
            msg = mensagens.nth(j).text_content()
            
            if not texto:
                continue
            
            texto = msg.text_content()
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
            
        #ultimo_total = total_mensagens
        time.sleep(5)
                        
    print("Atendimento concluido.")
