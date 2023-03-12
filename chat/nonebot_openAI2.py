import json,logging,requests,os
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot import on_message,on_command
def chat(question: str, file: str = "./chatdata/data.json")->str:
    API_KEY="YOUR_API_KEY"
    # 使用网络代理，如果不需要代理请注释掉下面一行并删除requests对PROXY的引用
    PROXY={"https":"http://127.0.0.1:7890"}
    headers = {
        "Host": "api.openai.com:443",
        "Authorization": "Bearer "+API_KEY,
        "Content-Type": "application/json"
    }
    with open(file, 'r') as f:
        data = json.load(f)
        logging.info(data)
    # data为聊天内容，格式为[{"role": "user", "content": "你好"},{"role": "assistant", "content": "你好"}]
    # post_data为openai的请求数据，格式为{"model": "gpt-3.5-turbo","messages":data}请求时需要转换为json格式
    data+=[{"role": "user", "content": question}]
    post_data = {
        "model": "gpt-3.5-turbo",
        "messages":data
    }
    ans=""
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions",headers=headers, data=json.dumps(post_data), proxies=PROXY)
        logging.info(response)
        ans=response.json()['choices'][0]['message']['content']
        ans=ans[2:]
        data+=[{"role": "user", "content": question},{"role": "assistant", "content": ans}]
        with open(file,'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except requests.exceptions.RequestException as e:
        ans="请求错误，错误信息为："+e
    finally:
        return ans
    
def newchat(file: str)->None:
    with open(file, 'w') as f:
        json.dump([], f)
    
async def atme_checker(event: MessageEvent) -> bool:
    if event.is_tome():
        return True
    return False

ai2 = on_message(priority=70, block=True, rule=atme_checker)
chatreset = on_command("reset",priority=65, block=True)

@ai2.handle()
async def _(event:MessageEvent):
    senderQQ=event.get_user_id()
    filepath="./chat_data/"+str(senderQQ)+".json"
    if not os.path.exists(filepath):
        newchat(filepath)
    reply=chat(event.raw_message,filepath)
    await ai2.finish(message=reply)

@chatreset.handle()
async def _(event:MessageEvent):
    senderQQ=event.get_user_id()
    filepath="./chat_data/"+str(senderQQ)+".json"
    newchat(filepath)
    await chatreset.finish(message="已重置聊天记忆")

if __name__ == '__main__':
    newchat("./chat_data/data.json")
    print(chat("你好", "./chat_data/data.json"))