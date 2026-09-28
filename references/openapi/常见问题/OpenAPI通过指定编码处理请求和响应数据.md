---
title: "OpenAPI通过指定编码处理请求和响应数据"
entityId: "478934973433530368"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/478934973433530368?productLineId=29&lang=zh-CN"
createdAt: "2023-08-14 14:36:36"
updatedAt: "2023-08-14 14:58:00"
views: 1235
---

# OpenAPI通过指定编码处理请求和响应数据

## 1业务场景

- 对于一些特定环境不支持UTF-8编码方式
- 一些环境使用的不是UTF-8编码格式，而且不能随意修改编码方式

针对以上场景，调用API会出现乱码情况（API默认编码格式是UTF-8）

## 2解决方案

- API可以通过请求头 **Accept-Charset** 设置使用那种编码方式处理请求和响应数据

## 3 关键操作

请求头通过 **Accept-Charset**设置要使用的编码格式，多个编码方式用英文逗号分隔。API请求会按照顺序找到支持的编码方式，如果第一个支持就用第一个编码方式，如果第一个不支持就检查第二个编码方式是否支持，以此类推找到支持的编码方式为止，如果都不支持则抛出异常

![](https://vip.kingdee.com/download/0109d950b77988d54103858461671e61e2c8.png)

## 4 注意事项

- 不配置Accept-Charset默认按照UTF-8方式处理出入参
- 配置了就按照顺序找到可用的编码方式处理
- 如果配置的都不支持则抛出异常
