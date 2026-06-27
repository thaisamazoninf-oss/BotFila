import time
import pyttsx3
from selectors import Selectors
from playwright.sync_api import sync_playwright, TimeoutError

usuario = "atendente02@amazoninf.com.br"
senha = "Amazon@2025"

engine = pyttsx3.init()

def iniciar_automacao():

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
        page.locator(Selectors.Fila.ABA_CONVERSANDO).click()
        print("clique aba desejada")
        
        #page.locator(Selectors.Card.CARD).click()
        #print ("Clique no card")
        
        #Aguardar o card perfil aparecer. 
        page.wait_for_selector(Selectors.Card.CARD_TESTE) 
        
        #Ler o perfil no CARD.
        perfil = page.locator(Selectors.Card.CARD_TESTE).first.inner_text()
        print("Perfil do usuário:", perfil)
        
        atendimento_em_andamento = False
        ultimo_totalFila = None
        ultimo_totalBot = None
        ultimo_totalConversa = None
        
        while True:
            try:
                #contador de números de atendimento na fila
                totalFila = int(
                    page.locator(Selectors.Fila.CONTADOR_FILA)
                    .text_content()
                    .strip()
                )
                
                #contador de números de atendimento do bot
                totalBot = int(
                    page.locator(Selectors.Fila.CONTADOR_BOT)
                    .text_content()
                    .strip()
                )
                
                #contato conversando
                totalConversa = int(
                    page.locator(Selectors.Fila.CONTADOR_CONVERSANDO)
                    .text_content()
                    .strip()
                )
                
                # Total de usuarios na aba Bot
                if totalBot != ultimo_totalBot:
                    if totalBot == 0:
                        print("Nenhum atendimento no bot")
                        engine.say("Nenhum atendimento no  bot")
                        engine.runAndWait()
                        
                    elif totalBot == 1:
                        print("Há 1 atendimento no bot")
                    else:
                        print(f"Há {totalBot} atendimento no bot")
                    
                    ultimo_totalBot = totalBot
                    
                # Total de usuarios na aba Fila
                if totalFila != ultimo_totalFila:
                    if totalFila == 0:
                        print("Nenhum atendimento na fila")
                    elif totalFila == 1:
                        print("Há 1 atendimento na fila")
                    else:
                        print(f"Há {totalFila} atendimento na fila")
                    
                    ultimo_totalFila = totalFila
                    
                # Total de usuarios na aba Conversando
                if totalConversa != ultimo_totalConversa:
                    if totalConversa == 0:
                        print("No momento, analista sem atendimento")
                    elif totalConversa == 1:
                        print("Analista com 1 atendimento")
                    else:
                        print(f"O analista está com {totalConversa} atendimento")
                    
                    ultimo_totalConversa = totalConversa

            
            except Exception as e:
                print(f"Erro ao monitorar fila:{e}")
            
            page.wait_for_timeout(1000)
        
        
    page.wait_for_selector(".protocol.gupshup",timeout=5000)
        
        
    print("Atendimento concluido.")
