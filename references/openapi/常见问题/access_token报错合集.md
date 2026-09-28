---
title: "access_token报错合集"
entityId: "473850934762799616"
category: "常见问题"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/473850934762799616?productLineId=29&lang=zh-CN"
createdAt: "2023-07-31 13:54:27"
updatedAt: "2024-11-19 18:29:58"
views: 11620
---

# access_token报错合集

### 1. 获取appToken时，报错提示：<title>404 Not Found</title>

**原因：****请求地址错误**，检查url末尾是否有空格、换行，或者请求地址多了ierp/等

![](https://vip.kingdee.com/download/0109512d8b50ec8e48ae9c09798e476ff024.png)

### 2. 获取appToken时，报错提示：第三方应用ID或应用密钥不正确。

**原因：第三方应用ID或密钥不正确，或这个第三方应用被禁用了**，重新传入正确的appId/appSecret或启用第三方应用即可。

![](https://vip.kingdee.com/download/01094630cc2b706446eebaa21a2fc10dee16.png)

### 3. 获取accessToken时，报错提示："非法操作。","errorCode": "login.loginBizException",

**原因：****请求方式**错误****，login.do接口的请求方式必须为“POST”，否则执行失败。

![](https://vip.kingdee.com/download/01093c9936e8cb96421ab91640a1f0822990.png)

### 4. 请求头参数使用access_token，调用失败，提示“未经授权的访问”，但使用accesstoken，却可以调用成功

- **原因**：nginx代理默认会忽略请求头中带下划线的参数，所以需要修改nigix配置。
- 操作步骤：进入nginx文件夹下面的conf文件夹，在conf里面找到nginx.conf， 然后在http里面添加属性underscores_in_headers，该参数默认为off，会将带下划线的请求头参数标记为无效。将underscores_in_headers 赋值为on。然后进入sbin目录下，重启nginx就可以了。（Linux重启密令：./nginx -s reload 。）

### 5. 保存第三方应用时，系统提示“AccessToken加密认证密钥”不符合密码复杂性及长度要求？

- **原因：**第三方应用设置了密码强度校验，必须包含大小写、数字和特殊符号，长度介于16~50个字符（下划线“_”不算特殊字符）。

### 6. 调用API报错，提示：“未经授权的访问。”？

- **原因****1**：accessToken已失效，建议重新获取accessToken。
- **原****因2**：第三方应用已被禁用，需要去开放平台启用第三方应用。

![](https://vip.kingdee.com/download/01090e2f0c805ca341f7ae6ac20714be7655.png)

### 7. 调用API报错，提示：“当前第三方应用不在启用时间范围内”？

- **原因**：第三方应用当前不可用，需要修改第三方应用的启用时间或停止时间。

![](https://vip-admin.kingdee.com/download/01097bcbe88799fc46bab3ca92c729687ec3.png)

### 8. 调用API报错，提示：“该第三方应用-ISRM没有此接口访问权限”？

- **原因**：新增的第三方应用，默认没有API访问权限，需要手工配置“API授权清单”。

![](https://vip-admin.kingdee.com/download/0109f4f805d081c247c98e42d5007a733d8a.png)
