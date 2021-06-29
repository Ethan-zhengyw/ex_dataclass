# 使用ex_dataclass定义飞书消息请求参数类型

## 原始接口定义
[发送消息](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/reference/im-v1/message/create)

请求body的第一层包含三个key：
* receive_id
* content
* msg_type

其中，content是复杂的json格式字符串，它的详细定义又需要参考：[发送消息content说明](https://open.feishu.cn/document/uAjLw4CM/ukTMukTMukTM/im-v1/message/create_json)

接下来我们使用ex_dataclass来定义这个请求body的类型
