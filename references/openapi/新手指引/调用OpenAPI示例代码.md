---
title: "调用OpenAPI示例代码"
entityId: "676001635843466240"
category: "新手指引"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/676001635843466240?productLineId=29&lang=zh-CN"
createdAt: "2025-02-08 09:49:09"
updatedAt: "2025-07-14 18:00:55"
views: 7485
---

# 调用OpenAPI示例代码

## 1 前言

文档列举了Java、JavaScript、python等常用语言http调用API的示例 ，代码仅供参考，具体实现逻辑可根据实际业务需求自行调整。

## 2 调用示例

### 2.1 Java

#### 2.1.1 概述

Java常见的http调用方式有Java自带的HttpURLConnection、OkHttp、Apache的httpclient等， 以下使用Apache的httpclient工具进行http调用参考示例。

#### 2.1.2 环境要求

Java 8、maven

#### 2.1.3 示例代码

1. 添加依赖

```
<dependencies>
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.13</version>
    </dependency>
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpmime</artifactId>
        <version>4.5.13</version>
    </dependency>
</dependencies>
```

2. 编写公共方法

```
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.HttpEntityEnclosingRequestBase;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.client.methods.HttpUriRequest;
import org.apache.http.entity.ContentType;
import org.apache.http.entity.StringEntity;
import org.apache.http.entity.mime.MultipartEntityBuilder;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import java.io.File;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

public class HttpClientUtils {

    /**
     * 发送 HTTP 请求的公共方法
     *
     * @param url            请求的 URL
     * @param method         请求方法，如 "GET", "POST"
     * @param contentType    请求内容类型，如 "application/json", "application/xml", "multipart/form-data"
     * @param body           请求体 json、xml...
     * @param headers        自定义请求头
     * @param connectTimeout 连接超时时间（毫秒）
     * @param socketTimeout  套接字超时时间（毫秒）
     * @param requestTimeout 请求超时时间（毫秒）
     * @return 响应结果字符串
     * @throws IOException 网络请求异常
     */
    public static String sendRequest(String url, String method, String contentType, String body, Map<String, String> headers, int connectTimeout, int socketTimeout, int requestTimeout) throws IOException {
        RequestConfig config = getRequestConfig(connectTimeout, socketTimeout, requestTimeout);
        HttpClient httpClient = HttpClients.custom()
                .setDefaultRequestConfig(config)
                .build();
        HttpUriRequest request;
        // 根据请求方法创建对应的请求对象
        switch (method.toUpperCase()) {
            case "GET":
                request = new HttpGet(url);
                break;
            case "POST":
                HttpPost httpPost = new HttpPost(url);
                setRequestBody(httpPost, contentType, body);
                request = httpPost;
                break;
            default:
                throw new IllegalArgumentException("Unsupported HTTP method: " + method);
        }

        // 设置请求头
        if (headers != null) {
            for (Map.Entry<String, String> entry : headers.entrySet()) {
                request.setHeader(entry.getKey(), entry.getValue());
            }
        }

        // 发送请求
        HttpResponse response = httpClient.execute(request);
        HttpEntity entity = response.getEntity();
        return entity != null ? EntityUtils.toString(entity, StandardCharsets.UTF_8) : null;
    }

    /**
     * 获取请求配置 设置请求超时配置 毫秒
     *
     * @param connectTimeout
     * @param socketTimeout
     * @param requestTimeout
     * @return
     */
    private static RequestConfig getRequestConfig(int connectTimeout, int socketTimeout, int requestTimeout) {
        return RequestConfig.custom()
                .setConnectTimeout(connectTimeout)
                .setSocketTimeout(socketTimeout)
                .setConnectionRequestTimeout(requestTimeout)
                .build();
    }

    /**
     * 设置请求体
     * @param request  请求对象
     * @param contentType 请求体类型
     * @param body 请求体
     */
    private static void setRequestBody(HttpEntityEnclosingRequestBase request, String contentType, String body) {
        if ("application/json".equals(contentType)) {
            request.setEntity(new StringEntity(body, ContentType.APPLICATION_JSON));
        } else if ("application/xml".equals(contentType)) {
            request.setEntity(new StringEntity(body, ContentType.APPLICATION_XML));
        }
        //... 其他报文格式添加
    }

    /**
     * 发送带文件上传的请求
     *
     * @param url            请求url
     * @param textParams     text类型参数
     * @param filesMap       文件类型参数
     * @param headers        请求头
     * @param connectTimeout 连接超时时间（毫秒）
     * @param socketTimeout  套接字超时时间（毫秒）
     * @param requestTimeout 请求超时时间（毫秒）
     * @return 响应结果字符串
     * @throws IOException 网络请求异常
     */
    public static String sendRequest(String url, Map<String, String> textParams, Map<String, List<File>> filesMap, Map<String, String> headers,int connectTimeout, int socketTimeout, int requestTimeout) throws IOException {

        RequestConfig config = getRequestConfig(connectTimeout, socketTimeout, requestTimeout);
        HttpClient httpClient = HttpClients.custom()
                .setDefaultRequestConfig(config)
                .build();
        HttpUriRequest request;
        HttpPost httpPost = new HttpPost(url);
        MultipartEntityBuilder builder = MultipartEntityBuilder.create();
        // 添加文件
        if (filesMap != null && !filesMap.isEmpty()) {
            for (Map.Entry<String, List<File>> entry : filesMap.entrySet()) {
                List<File> files = entry.getValue();
                String key = entry.getKey();
                for (File file : files) {
                    if (file != null && file.exists()) {
                        builder.addBinaryBody(key, file, ContentType.APPLICATION_OCTET_STREAM, file.getName());
                    }
                }
            }
        }
        // 添加文本参数
        if (textParams != null && !textParams.isEmpty()) {
            for (Map.Entry<String, String> entry : textParams.entrySet()) {
                builder.addTextBody(entry.getKey(), entry.getValue());
            }
        }
        httpPost.setEntity(builder.build());
        request = httpPost;
        // 设置请求头
        if (headers != null) {
            for (Map.Entry<String, String> entry : headers.entrySet()) {
                request.setHeader(entry.getKey(), entry.getValue());
            }
        }
        // 发送请求
        HttpResponse response = httpClient.execute(request);
        HttpEntity entity = response.getEntity();
        return entity != null ? EntityUtils.toString(entity, StandardCharsets.UTF_8) : null;
    }

}
```

3. 测试

```
//get请求
private static void getExample() {
        try {
            String url = "https://xxxxx?billno=unittest-00000025&pageSize=10&pageNo=1";
            String method = "GET";
            String contentType = "application/json";
            String body = "";
            Map<String, String> headers = new HashMap<>();
            headers.put("accesstoken", "your token");

            // 设置超时时间（毫秒）
            int connectTimeout = 5000;
            int socketTimeout = 5000;
            int requestTimeout = 5000;

            String response = HttpClientUtils.sendRequest(url, method, contentType, body, headers, connectTimeout, socketTimeout, requestTimeout);
            System.out.println("Response: " + response);
        } catch (IOException e) {
            //异常处理，切勿直接忽略异常
        }
    }

//post请求
private static void postExample() {
        try {
            String url = "https://xxx";
            String method = "POST";
            String contentType = "application/json";
            String body = "{\n" +
                    "\t\"data\":{\n" +
                    "\t\t\"billno\":\"unittest-00000025\"\n" +
                    "\t},\n" +
                    "\t\"pageSize\":10,\n" +
                    "\t\"pageNo\":1\n" +
                    "}";
            Map<String, String> headers = new HashMap<>();
            headers.put("accesstoken", "your token");
            // 设置超时时间（毫秒）
            int connectTimeout = 5000;
            int socketTimeout = 5000;
            int requestTimeout = 5000;

            String response = HttpClientUtils.sendRequest(url, method, contentType, body, headers, connectTimeout, socketTimeout, requestTimeout);
            System.out.println("Response: " + response);
        } catch (IOException e) {
             //异常处理，切勿直接忽略异常
        }
    }

//传输文件
private static void fileExample() {
        try {
            String url = "https://feature.kingdee.com:1026/deviai/kapi/v2/kdtest/open/openapi/test2/fileHandle";
            Map<String, String> headers = new HashMap<>();
            headers.put("accesstoken", "your token");
            Map<String, List<File>> fileMap = new HashMap<>();
            File file = new File("C:\\Users\\HP\\Desktop\\test.txt");
            fileMap.put("fileList", Arrays.asList(file));
            Map<String, String> textParams  = new HashMap<>();
            textParams.put("str","this is a test");

            // 设置超时时间（毫秒）
            int connectTimeout = 5000;
            int socketTimeout = 5000;
            int requestTimeout = 5000;

            String response = HttpClientUtils.sendRequest(url,textParams,fileMap, headers, connectTimeout, socketTimeout, requestTimeout);
            System.out.println("Response: " + response);
        } catch (IOException e) {
            //异常处理，切勿直接忽略异常
        }
    }
```

### 2.2 JavaScript

#### 2.2.1 概述

JavaScript常见http调用方式有 Fetch API、axios 、jQuery 等等。 以下是使用 axios 进行 HTTP 请求的示例，包括 GET、POST、文件处理等常见操作。

#### 2.2.2 环境要求

```
# 在Node.js 环境下
npm install axios
# 或者
yarn add axios
```

#### 2.2.3 示例代码

```
//get请求
var axios = require('axios');

var config = {
   method: 'get',
   url: 'https://xxx?billno=unittest-00000025&pageSize=10&pageNo=1',
   headers: {
      'accesstoken': 'your token'
   }
};
axios(config)
.then(function (response) {
   console.log(JSON.stringify(response.data));
})
.catch(function (error) {
   console.log(error);
});

//post请求
var axios = require('axios');
var data = JSON.stringify({
   "data": {
      "billno": "unittest-00000025"
   },
   "pageSize": 10,
   "pageNo": 1
});
var config = {
   method: 'post',
   url: 'https://xxxx',
   headers: {
      'accesstoken': 'your token',
      'Content-Type': 'application/json'
   },
   data : data
};

axios(config)
.then(function (response) {
   console.log(JSON.stringify(response.data));
})
.catch(function (error) {
   console.log(error);
});

//传输文件
var axios = require('axios');
var FormData = require('form-data');
var fs = require('fs');
var data = new FormData();
data.append('fileList', fs.createReadStream('C:\Users\HP\Desktop\test.txt'));
var config = {
   method: 'post',
   url: 'https://xxxxx',
   headers: {
      'accesstoken': 'your token',
      ...data.getHeaders()
   },
   data : data
};

axios(config)
.then(function (response) {
   console.log(JSON.stringify(response.data));
})
.catch(function (error) {
   console.log(error);
});
```

### 2.3PHP

#### 2.3.1 概述

PHP 常见HTTP调用方法有内置的file_get_contents、cURL等。下面以cURL库为例。

#### 2.3.2 环境要求

建议PHP 7.x 以上 ，并根据需求配置网络、SSL/TLS

#### 2.3.3 示例代码

1. get请求

```
<?php
// 目标 URL
$url = 'https://xxx';

// 准备请求头，包含认证信息
$headers = [
    'accesstoken: your token',
    'Content-Type: application/json'
];

// 初始化 cURL 会话
$ch = curl_init($url);

// 设置 cURL 选项
// 将响应结果作为字符串返回，而不是直接输出
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// 设置请求头
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

// 执行 cURL 请求并获取响应
$response = curl_exec($ch);

// 检查请求过程中是否出现错误
if (curl_errno($ch)) {
    echo 'cURL 请求错误: '. curl_error($ch);
} else {
    // 解析 JSON 格式的响应数据
    $data = json_decode($response, true);
    print_r($data);
}

// 关闭 cURL 会话，释放资源
curl_close($ch);
?>
```

2. post请求

```
<?php
// 目标 URL，需替换为实际的接口地址
$url = 'https://xxx';

// 报文数据
$data = [
    "data" => [
        "billno" => "unittest-00000025"
    ],
    "pageSize" => 10,
    "pageNo" => 1
];

// 设置请求头，包含 token 和内容类型
$headers = [
    'accesstoken: your token',
    'Content-Type: application/json'
];

// 将数据编码为 JSON 格式
$jsonData = json_encode($data);

// 初始化 cURL 会话
$ch = curl_init($url);

// 设置 cURL 选项
// 设置请求方法为 POST
curl_setopt($ch, CURLOPT_POST, true);
// 设置 POST 请求的主体数据
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
// 设置请求头
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
// 将响应结果作为字符串返回
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// 执行 cURL 请求并获取响应
$response = curl_exec($ch);

// 检查请求过程中是否出现错误
if (curl_errno($ch)) {
    echo 'cURL 请求错误: '. curl_error($ch);
} else {
    // 解析 JSON 格式的响应数据
    $data = json_decode($response, true);
    print_r($data);
}

// 关闭 cURL 会话，释放资源
curl_close($ch);
?>
```

### 2.4Go

#### 2.4.1 概述

在 Go 语言中进行 HTTP 调用可以使用标准库中的 net/http 包。

#### 2.4.2 环境要求

Go 环境，并根据需求配置网络、SSL/TLS

#### 2.4.3 示例代码

1. get请求

```
package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// 目标 URL
    url := "https://xxx"

	// 发送 GET 请求
	resp, err := http.Get(url)
	if err != nil {
		fmt.Printf("HTTP GET 请求失败: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// 检查响应状态码
	if resp.StatusCode != http.StatusOK {
		fmt.Printf("请求失败，状态码: %d\n", resp.StatusCode)
		return
	}

	// 读取响应体
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("读取响应体失败: %v\n", err)
		return
	}

	// 解析 JSON 响应
	var data []map[string]interface{}
	err = json.Unmarshal(body, &data)
	if err != nil {
		fmt.Printf("JSON 解析失败: %v\n", err)
		return
	}

	// 打印解析后的数据
	fmt.Println(data)
}
```

2. post请求

```
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	// 目标 URL
	url := "https://xxx"

	// 构建请求数据
	data := map[string]interface{}{
		"data": map[string]string{
			"billno": "unittest-00000025",
		},
		"pageSize": 10,
		"pageNo":   1,
	}

	// 将数据编码为 JSON
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Printf("JSON 编码失败: %v\n", err)
		return
	}

	// 创建 POST 请求
	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Printf("创建请求失败: %v\n", err)
		return
	}

	// 设置请求头
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("accesstoken", "your token")

	// 发送请求
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("HTTP POST 请求失败: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// 检查响应状态码
	if resp.StatusCode != http.StatusOK {
		fmt.Printf("请求失败，状态码: %d\n", resp.StatusCode)
		return
	}

	// 读取响应体
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("读取响应体失败: %v\n", err)
		return
	}

	// 解析 JSON 响应
	var responseData map[string]interface{}
	err = json.Unmarshal(body, &responseData)
	if err != nil {
		fmt.Printf("JSON 解析失败: %v\n", err)
		return
	}

	// 打印解析后的数据
	fmt.Println(responseData)
}
```

## 3 更多

更多编程语言的实例调用可根据postman、apifox等工具中提供的生成代码功能作为参考。

![](https://vip.kingdee.com/download/0109e512895d1639477fb320c6b592d056cc.png)
