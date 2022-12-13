import openai,asyncio
# 请在这里填入你的openai的organization和api_key
openai.organization = "org-qwertyuiasdfghj"
openai.api_key = "sk-qwertyuiopasdfghjklzxcvbnm1234567890"
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot import on_message
# 此函数用于获取回答
def get_answer(question:str)->str:
	respose=openai.Completion.create(
	    model="text-davinci-003",
	    prompt=question,
	    max_tokens=1024,
	    temperature=0
	)
	ans=respose.choices[0].text
	ans=ans[2:]
	if ans.startswith("\n"):
		ans=ans[1:]
	return ans
# 检测是否和机器人相关，在群里@机器人和私聊机器人都可触发，但是@全体成员不触发
async def atme_checker(event: MessageEvent) -> bool:
    if event.is_tome():
        return True
    return False

ai = on_message(priority=70, block=True, rule=atme_checker)
@ai.handle()
async def _(event:MessageEvent):
    loop=asyncio.get_event_loop()
    print(event.raw_message)
    reply=await loop.run_in_executor(None,get_answer,event.raw_message)
    await ai.finish(message=reply)