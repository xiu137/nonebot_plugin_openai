# openAI插件及测试代码

在官网账号获取openAI的API并修改代码中openai.api_key的值，理论上openai.organization好像不需要，反正我顺手写上了

将文件至于src/plugin目录下即可，触发条件为私聊或者群中@机器人，我个人是通过增加权重数值以避免和其他插件冲突

这个是[另一位大佬写的插件](https://github.com/Special-Week/nonebot_plugin_openai),我自己写的时候只添加了很少的功能，如果有其他需求可以去这里找找灵感。

![使用案例](./simple.png)

## openai的聊天API调用

新增聊天的代码部分，基于原来的=openai包中的chatcompletion方法。考虑到某些问题，所以使用requests请求openai的api，而不是使用openai包中的方法。

在使用前在nonebot的工作目录下创建chat_data文件夹，用于存放聊天记录。并填写openai的api_key。触发条件和之前相同

openAI和openAI2是两个独立的插件，实际仅需添加一个即可