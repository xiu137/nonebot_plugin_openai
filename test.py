import openai
# 请在这里填入你的openai的organization和api_key
openai.organization = "org-qwertyuiasdfghj"
openai.api_key = "sk-qwertyuiopasdfghjklzxcvbnm1234567890"

def get_answer(question:str)->str:
	respose=openai.Completion.create(
	    model="text-davinci-003",
	    prompt=question,
	    max_tokens=1024,
	    temperature=0
	)
	return respose.choices[0].text

if __name__=="__main__":
    print(get_answer("怎么用python输出hello world"))