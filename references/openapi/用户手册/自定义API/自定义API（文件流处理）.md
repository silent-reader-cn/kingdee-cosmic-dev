---
title: "自定义API（文件流处理）"
entityId: "644193911996299264"
category: "用户手册 / 自定义API"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/644193911996299264?productLineId=29&lang=zh-CN"
createdAt: "2024-11-12 15:16:37"
updatedAt: "2025-12-19 14:23:15"
views: 6114
---

# 自定义API（文件流处理）

## 变更记录

| 产品版本 | 更新内容 | 更新日期 |
| --- | --- | --- |
| V5.0.011 | 初始版本 | 2022年6月 |
| V7.0.6 | 自定义Java插件API支持单个参数接收多个文件 | 2025年2月 |

---

## 1业务场景

OpenAPI支持处理文件流，适用于以下业务场景：

- 对文件流进行处理；
- 对图像、证书、文档、附件等进行处理；
- 文件的上传及下载。

## 2解决方案

1. 使用自定义Java插件开发API接口，并在开放平台注册此自定义API。
2. 上传文件时请求消息格式应设置为：multipart/form-data。
3. 定义一个OpenApiFile类型的入参（可以定义多个)，插件中可以获取到上传的文件名/类型/文件流(byte[])
4. 其他参数（如业务单号、ID）按正常的参数定义即可。
5. 如果要返回文件流或下载文件请设置http头的AcceptType为：application/octet-stream，
6. 如果只返回文件处理结果信息可以设置http头ContentType为：application/json。
7. 性能考虑单次文件传输大小最多为30M，可通过MC参数修改默认文件流最大报文大小：OpenApi.FileItem.MaxSize，单位是字节b。

### 2.1代码示例

下面的示例插件代码演示：

1)如何上传文件；

2)如何处理文件并下载。

```
@ApiController(value = "dev", desc = "自定义API Demo样例2")
@ApiMapping(value = "/openapi/test2")
public class CustomDemoTestController {
    @ApiPostMapping(value = "/uploadFile", desc = "上传文件流")
    public CustomApiResult<String> uploadFile(@NotNull @ApiParam("订单号") String billNo, @ApiParam("文件流") OpenApiFile file1) {
        /*
            如何开发API支持文件流处理：
            ==============================
            1. 上传文件时请求消息格式应设置为：multipart/form-data。
            2. 定义一个OpenApiFile类型的入参（可以定义多个)，插件中可以获取到上传的文件名/类型/文件流(byte[])
            3. 其他参数（如业务单号、ID）按正常的参数定义即可。
            4. 如果要返回文件流或下载文件请设置http头的AcceptType为：application/octet-stream，
                   如果只返回文件处理结果信息可以设置http头ContentType为：application/json。
            注：由于性能考虑单次文件传输大小最多为30M。
         */

        if (StringUtil.isEmpty(billNo) || file1 == null || file1.getFileData() == null) {
            //手动设置http状态码406
            ServiceApiContext.getResponse().setHttpStatus(HttpStatus.NOT_ACCEPTABLE.getStatusCode());
            //返回失败错误码：errorCode：900101（业务自行约定）  & status=false
            return CustomApiResult.fail("900101", "订单号billNo及文件流file1不能为空。");
        }
        String msg = "您的订单号：" + billNo + "，上传的文件名是：" + file1.getFileName() + "，类型是：" + file1.getContentType()
                + "，文件长度为（Bytes）：" + file1.getFileData().length;
        return CustomApiResult.success(msg);
    }

    @ApiPostMapping(value = "/processFile", desc = "处理文件流")
    public CustomApiResult<OpenApiFile> processFile(@NotNull @ApiParam("订单号") String billNo, @ApiParam("文件流") OpenApiFile file1) {
        if (StringUtil.isEmpty(billNo) || file1 == null || file1.getFileData() == null) {
            //手动设置http状态码406
            ServiceApiContext.getResponse().setHttpStatus(HttpStatus.NOT_ACCEPTABLE.getStatusCode());
            //返回失败错误码：errorCode：900101（业务自行约定）  & status=false
            return CustomApiResult.fail("900101", "订单号billNo及文件流file1不能为空。");
        }

        if (!file1.getFileName().contains(".txt")) {
            //手动设置http状态码406
            ServiceApiContext.getResponse().setHttpStatus(HttpStatus.NOT_ACCEPTABLE.getStatusCode());
            //返回失败错误码：errorCode：900102（业务自行约定）  & status=false
            return CustomApiResult.fail("900102", "此演示案例只能处理文本文件，你可以编写用例处理图像/EXCEL等文件。");
        }

        try {
            //demo代码，请替换成实际业务逻辑。下面演示对输入的文档文件进行加工，在头部添加了加工信息。
            byte[] message = ("此文件已被OpenAPI插件处理，订单号：" + billNo + "，处理时间：" + (new Date()).toString() + " \n\r").getBytes(Charset.forName("UTF-8"));
            byte[] resultFileData = new byte[file1.getFileData().length + message.length];
            System.arraycopy(message, 0, resultFileData, 0, message.length);
            System.arraycopy(file1.getFileData(), 0, resultFileData, message.length, file1.getFileData().length);

            //返回的文件流处理参数：
            // 1. fileName:文件名；    2. fileType:如：application/vnd.ms-excel,text/plain
            // 3. downloadStream：true-下载文件；false-输出文件流；4. data：文件流
            OpenApiFile result = new OpenApiFile("New" + file1.getFileName(), MediaType.TEXT_PLAIN, true, resultFileData);
            return CustomApiResult.success(result);
        } catch (Exception ex) {
            //手动设置http状态码
            ServiceApiContext.getResponse().setHttpStatus(HttpStatus.BAD_REQUEST.getStatusCode());
            //返回失败错误码：errorCode：400  & status=false
            return CustomApiResult.fail("400", "处理时发生错误：" + ex.getMessage());
        }
    }
}
```

### 2.2 注册自定义API

菜单：开放服务云 - OpenAPI - API开发，新增 “自定义API”。

选择所属应用，填写API编码及名称，API分类。在“类名”处输入你的API插件类全路径名称，例如：kd.bos.openapi.service.custom.demo.CustomDemoTestController。

选择方法名。已将此JAVA代码发布为自定义API。此时可以直接使用Postman测试REST协议的API。

![](https://vip.kingdee.com/download/0109b35cb6e2be7f4d079e0477cda4954d67.png)

![](https://vip.kingdee.com/download/0109638f3af288d34cb08fb04ea9612776ce.png)

### 2.3 测试API

使用Postman测试。请求方式选择POST，请求消息格式应设置为：multipart/form-data，填写相应的参数，并选择一个文件。注：在选择文件时请选择类型File。

1） 测试上传

如果只返回文件处理结果信息可以设置http头ContentType为：application/json

注：由于性能考虑单次文件传输大小最多为30M。一个file参数只支持上传1个附件，用户可以定义多个file参数或多次调用实现上传多个附件。

![](https://vip.kingdee.com/download/0109c0ca6f0a1d7447f3b862ed7daa8a4119.png)

2） 测试下载

如果要返回文件流或下载文件请设置http头的Accept-Type为：application/octet-stream。

注：如果要测试文件下载，请点击Postman的“Send and download”，而不是“Send”按钮。

![](https://vip.kingdee.com/download/01098d38daef5d554d35b02d9322d9ca8925.png)

此Demo演示的文件在我的电脑中可以找到被下载的文件，示例代码是对一个文本文件做出了相应的处理，可以根据业务需要对图像或EXCEL等文件进行按需加工。

![](https://vip.kingdee.com/download/010931ba63c5c87e490287a8d1bb186bced8.png)

### 2.4 多文件处理

苍穹平台OpenAPI（7.0.6以上），支持单个参数传入多个文件，在方法参数中写成List<OpenApiFile>即可接收到多个文件，也可定义多个List<OpenApiFile>的参数，接口代码示例如下。

```
	@ApiPostMapping(value = "/fileHandle", desc = "多文件处理")
    public CustomApiResult<String> fileHandle(@ApiParam("billno") String billno
            , @ApiParam("file") OpenApiFile file
            , @ApiParam("file1") OpenApiFile file1
            , @ApiParam("fileList") List<OpenApiFile> fileList
            , @ApiParam("fileList1") List<OpenApiFile> fileList1) {
		return CustomApiResult.success("");
	}
```

![](https://vip.kingdee.com/download/0109c68528908d0f4a52aac858d57175b644.png)

## 3 注意事项

- OpenAPI只处理小文件，大文件的处理建议使用文件上传接口（uploadFile.do）。
- 性能考虑单次所有文件传输大小最多为50M，可通过MC租户级参数修改默认文件流最大报文大小：OpenApi.FileItem.MaxSize，单位为字节b。

## 4更多资讯

[金蝶AI苍穹开放平台OpenAPI调用流程](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=213309216805890816&productLineId=29)

[金蝶AI苍穹开放平台OpenAPI开发认证指南](https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?category=239331354741842688&id=218694224487485696&productLineId=29)
