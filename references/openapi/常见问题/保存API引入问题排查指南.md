---
title: "保存API引入问题排查指南"
entityId: "594477647900699392"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/594477647900699392?productLineId=29&lang=zh-CN"
createdAt: "2024-06-28 10:41:56"
updatedAt: "2025-04-30 14:08:22"
views: 3206
---

# 保存API引入问题排查指南

## 1 前言

本文档适用解决以下问题：

- 保存操作API会触发什么事件？
- 保存操作API，若API传了某个字段的值，但实际单据里为空或者其他值。
- 如何在代码里区分API的保存引入还是表单页面的保存引入？

## 2 保存操作API触发事件

#### 保存操作API属于数据引入，类似在页面上直接点保存按钮，引入时会触发以下事件：

**2.1 保存按钮的操作插件或者配置的校验规则**

![](https://vip.kingdee.com/download/01095b33d898713e420ea787b9077ca9180d.png)

**2.2 单据表单或者单据体分录的业务规则**

![](https://vip.kingdee.com/download/010931051ab7953a427ca2a3238e22632c19.png)

**2.3 表单插件里的initImportData、beforeImportData、afterImportData方法；**

![](https://vip.kingdee.com/download/0109b9cf7ae5036e4c03b62daa0e2452b012.png)

**2.4 API是否绑定了扩展插件**

![](https://vip.kingdee.com/download/0109604772e86fc74a69929270753f5b6bb5.png)

**2.5 若在V2版本的保存操作API中，配置了参数firePropChanged为true，那么在更新数据时，会触发表单插件的值更新propertyChanged事件。**

![](https://vip.kingdee.com/download/010979427862400449e0af62bb05d8c5a543.png)

## 3 字段引入后，单据里字段却为空或者其他值时

#### 首先有一个确定的前提，开放平台OpenAPI不会对原入参进行任何干预，已知保存操作API会触发的事件，那么建议按以下方法排查。

- 保存按钮的操作插件或者配置的校验规则 —— 查看是否跟引入的字段有关处理逻辑，或直接先禁用掉。
- 单据表单或者单据体分录的业务规则 —— 查看是否跟引入的字段有关处理逻辑，或直接先禁用掉。
- 表单插件里的initImportData、beforeImportData、afterImportData方法 —— 查看是否跟引入的字段有关处理逻辑或可先配置保存参数is_importinit为false，此时不会触发这三个引入方法（适用版本BOS V6.0.1），再进行调用API。
- 触发表单插件的值更新propertyChanged事件 —— 查看是否配置了保存参数firePropChanged为true。
- API绑定了扩展插件 —— 查看是否跟引入的字段有关处理逻辑，或直接先禁用掉。
- 若在API引入时会触发的插件里对某个字段进行了赋值，表单页面可以正常触发赋值，但API引入时不生效，**此时建议本地调试下，是否在赋值前方法就已经返回了。**
- 查看表单该字段是否有对应的**数据库字段。**
- 通过字段的**字段标识**查看传的字段是否正确，避免**同名**的字段引入。
- 查看API配置页面的请求参数是否配置了需要引入的字段，若无配置，即使传了也不生效。
- 设计器查看该字段功能控制-允许导入开关是否打开。
- 若该表单已经被扩展，那么扩展后的表单按上述方法都排查一遍。
