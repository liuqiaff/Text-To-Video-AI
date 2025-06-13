import os
from openai import OpenAI
import json

if len(os.environ.get("GROQ_API_KEY")) > 30:
    from groq import Groq
    model = "llama3-70b-8192"
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
        )
else:
    OPENAI_API_KEY = os.getenv('OPENAI_KEY')
    model = "gpt-4o"
    client = OpenAI(api_key=OPENAI_API_KEY)

def generate_script(topic):
    prompt = (
        """你是一个经验丰富的内容创作者，专门为 YouTube Shorts 制作趣味知识类短视频脚本。
    你的视频时长不超过 50 秒（约 140 字），内容要简短、有趣、有创意。
    
    当用户请求某类“冷知识”时，你需要用**中文**生成短视频脚本。

    例如用户请求：
    奇怪的冷知识
    你可以输出如下内容：

    你不知道的奇怪冷知识：
    - 香蕉是浆果，但草莓不是。
    - 一朵云可以重达上百万磅。
    - 有一种水母在生物学上是永生的。
    - 蜂蜜永远不会变质，考古学家在古埃及墓中发现的蜂蜜仍然可以食用。
    - 历史上最短的战争只持续了38分钟。
    - 章鱼有三颗心，血液是蓝色的。

    你现在的任务是根据用户输入的“知识类型”，输出最佳的脚本。

    请保持内容新颖、有趣、简短，并用**中文**输出。

    严格使用如下格式输出，**只返回一个合法的 JSON 对象**，key 为 `script`：

    # Output
    {"script": "这里是脚本内容..."}
    """
    )

    response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": topic}
            ]
        )
    content = response.choices[0].message.content
    print("zzz"+content)
    try:
        script = json.loads(content)["script"]
    except Exception as e:
        json_start_index = content.find('{')
        json_end_index = content.rfind('}')
        print(content)
        content = content[json_start_index:json_end_index+1]
        script = json.loads(content)["script"]
    return script
