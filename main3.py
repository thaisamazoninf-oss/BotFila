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
    page.wait_for_selector("body > app-root > app-layout-omnichannel > div > div > div > div > div > div > div > app-chat-home > div > div.sidebar-body.chat-main-sidebar > div.chats-nav > div.chat_item_header.types-bot > span:nth-child(2)")
    
    #Selecionar aba de atendimento: BOT/Fila/Conversando
    page.locator('body > app-root > app-layout-omnichannel > div > div > div > div > div > div > div > app-chat-home > div > div.sidebar-body.chat-main-sidebar > div.chats-nav > div.chat_item_header.types-bot > span:nth-child(2)').click()
    print("clique aba de atendimento")
    
    atendimento_em_andamento = False
    ultimo_total = None
    
    while True:
        try:
            #contator de números de atendimento na fila
            total = int(
                page.locator('xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/div[1]/span[2]/div/span')
                .text_content()
                .strip()
            )
            
            if total != ultimo_total:
                if total == 0:
                    print("Nenhum atendimento na fila")
                elif total == 1:
                    print("Há 1 atendimento na fila")
                else:
                    print(f"Há {total} atendimento na fila")
                
                ultimo_total = total
            
            #Iniciar atendimento
            #if total > 0 and not atendimento_em_andamento:
            #    atendimento_em_andamento = True
                
            #    print ("Abrindo atendimento")
                
            #    page.locator(
            #        ""
            #    ).first.click()
                
            #    print("Atendimento iniciado")
                
            #    atendimento_em_andamento = False
        
        except Exception as e:
            print(f"Erro ao monitorar fila:{e}")
        
        page.wait_for_timeout(1000)
    
    
page.wait_for_selector(".protocol.gupshup",timeout=5000)
    
    
print("Atendimento concluido.")
