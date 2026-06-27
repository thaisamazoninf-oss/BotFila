import asyncio
import edge_tts
import pygame

async def falar(texto):
    communicate = edge_tts.Communicate(
        texto,
        voice="pt-BR-FranciscaNeural"
    )
    
    await communicate.save("voz.mp3")
    
    pygame.mixer.init()
    pygame.mixer.music.load("voz.mp3")
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)
        
asyncio.run(falar("Novo atendimento. Cliente João Silva"))