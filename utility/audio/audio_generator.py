import edge_tts

async def generate_audio(text,outputFilename):
    communicate = edge_tts.Communicate("人是为活着本身而活着，而不是为了活着之外的任何事物所活着。","zh-CN-YunjianNeural")
    await communicate.save(outputFilename)





