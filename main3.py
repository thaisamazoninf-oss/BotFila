import time
from selectors import Selectors
from playwright.sync_api import sync_playwright, TimeoutError

usuario = "atendente02@amazoninf.com.br"
senha = "Amazon@2025"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False
    )
    page = browser.new_page()
    
    #Acessar o site
    page.goto(Selectors.Login.SITE)
    
    #Aguardar aparecer o campo usuario
    page.wait_for_selector(Selectors.Login.AGUARDAR_USUARIO)
    
    #Adiciona o usuário
    page.fill(Selectors.Login.USUARIO,usuario)
    
    #Adiciona a senha
    page.fill(Selectors.Login.SENHA, senha)
    
    #Clique botão entrar
    page.click(Selectors.Login.ENTRAR)
    time.sleep(2)
    
    #Clique no botão Fechar (caso exista)
    #page.click("#botao-fechar")
    
    #Aguardar aparece a BOT/Fila/Conversando
    page.wait_for_selector(Selectors.Fila.ABA_FILA)
    
    #Selecionar aba de atendimento: BOT/Fila/Conversando
    page.locator(Selectors.Fila.ABA_FILA).click()
    print("clique aba desejada")
    
    #page.locator(Selectors.Card.CARD).click()
    #print ("Clique no card")
    
    #perfil = page.locator(Selectors.Card.CARD_PERFIL).text.content()
    #print("Perfil do usuário:", perfil)
    
    atendimento_em_andamento = False
    ultimo_total = None
    ultimo_total2 = None
    
    while True:
        try:
            #contador de números de atendimento na fila
            total = int(
                page.locator(Selectors.Fila.CONTADOR_FILA)
                .text_content()
                .strip()
            )
            
            #contador de números de atendimento do bot
            total2 = int(
                page.locator(Selectors.Fila.CONTADOR_BOT)
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
                
            if total2 != ultimo_total2:
                if total2 == 0:
                    print("Nenhum atendimento no bot")
                elif total2 == 1:
                    print("Há 1 atendimento no bot")
                else:
                    print(f"Há {total2} atendimento no bot")
                
                ultimo_total2 = total2
        
        except Exception as e:
            print(f"Erro ao monitorar fila:{e}")
        
        page.wait_for_timeout(1000)
    
    
page.wait_for_selector(".protocol.gupshup",timeout=5000)
    
    
print("Atendimento concluido.")
