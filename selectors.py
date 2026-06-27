class Selectors:
    
    class Login:
        #link do site
        SITE = 'https://chat.sonax.net.br/app/omnichannel/chat'
        
        #Selector - AGUARDAR APARECER CAMPO USUÁRIO NA TELA
        AGUARDAR_USUARIO = "body > app-root > app-login > div > div.left-side > div > div:nth-child(2) > input"
        
        #Selector - Campo  usuario
        USUARIO = "body > app-root > app-login > div > div.left-side > div > div:nth-child(2) > input"
        
        #Selector - Campo senha
        SENHA = "div.left-side-form-input:nth-child(3) > input:nth-child(2)"
        
        #Selector - Botão entrar
        ENTRAR = "button.roboto"

        
    class Fila:
        #Selector - Fila
        ABA_FILA = "body > app-root > app-layout-omnichannel > div > div > div > div > div > div > div > app-chat-home > div > div.sidebar-body.chat-main-sidebar > div.chats-nav > div.chat_item_header.types-bot > span:nth-child(2)"
        
        CONTADOR_FILA = "xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/div[1]/span[2]/div/span"
        
        ABA_BOT = "xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/div[1]/span[1]"
        
        CONTADOR_BOT = "xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/div[1]/span[1]/div/span"
        
        ABA_CONVERSANDO = "xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/div[1]/span[3]"
        
        CONTADOR_CONVERSANDO = "xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/div[1]/span[3]/div/span"
        
        
    
    class Card:
        CARD = "xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/app-protocol-list/div/app-protocol-item/div"
        
        CARD_PERFIL = "xpath=/html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[3]/div/app-protocol-view/div/app-protocol-view-messages/div[2]/div[1]/div/div/div[22]/div/div/div[1]/span/markdown/p"
        
        CARD_TESTE = "xpath=//html/body/app-root/app-layout-omnichannel/div/div/div/div/div/div/div/app-chat-home/div/div[1]/div[2]/div[1]/span[3]/span"