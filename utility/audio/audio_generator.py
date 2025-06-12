import edge_tts

async def generate_audio(text,outputFilename):
    communicate = edge_tts.Communicate(text,"zh-CN-YunjianNeural")
    await communicate.save(outputFilename)





