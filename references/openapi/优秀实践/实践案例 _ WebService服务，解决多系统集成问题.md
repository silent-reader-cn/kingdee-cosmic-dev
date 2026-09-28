---
title: "实践案例 | WebService服务，解决多系统集成问题"
entityId: "376311639396233728"
category: "优秀实践"
productLineId: 29
source: "https://vip.kingdee.com/knowledge/specialDetail/226337046514476288?productLineId=29&lang=zh-CN"
knowledgeUrl: "https://vip.kingdee.com/knowledge/376311639396233728?productLineId=29&lang=zh-CN"
createdAt: "2022-11-04 10:08:06"
updatedAt: "2026-07-30 11:36:53"
views: 113783
---

# 实践案例 | WebService服务，解决多系统集成问题

# 小编推荐

由于历史发展原因，企业内部往往不止存在一套信息管理系统。在某些大型企业中，系统甚至会高达**几十套**。集团总部想要及时掌握各子公司的经营情况，但这往往需要投入大量的人力物力进行系统集成才能实现。

但是现在，通过苍穹**OpenApi2.0的WebService服务**，即可轻松实现企业内部系统的集成，**极大限度地降低开发成本**。一线案例，亲测有效。欲知详情，请往下看~

**撰稿人：金蝶伙伴**—杨超**。**

---

# 1业务背景

## 1.1 业务场景及痛点

2022年初，拥有烟草行业复杂业务集成项目WebService经验的我们，遇到了医药零售行业的系统集成WebService需求。与烟草行业不同，该医药客户原系统在对接外围系统时基本使用**Basic认证方式**的WebService处理数据。

由于Basic认证方式安全度很低，存在风险，因此需要引入苍穹发布的WebService替换原有的Basic认证的WebService，由后续服务流程或者数据集成方案处理业务数据，将数据保存到对应业务单据。

之前该客户使用WebService对接了该企业异构系统（**17个数据中心**），庞大的数据量对WebService是一个严峻的考验，且该企业原系统的WebService较为复杂，客户需要熟悉完整的WebService接口，并开发出对应的解析模块才可处理数据。

这需要客户对业务和功能的熟悉度很高，特别是其中的一些开发方式，客户在做功能性调整时，需要小心谨慎地处理功能代码，所以在开发和运维的过程中考虑的东西较多，导致时间成本较高。

## 1.2 客户诉求及期望

该医药零售客户希望苍穹实现的WebService能满足以下需求点：

1、保留原系统原生WebService的格式，仅变动地址，做到**无感切换Web Service**。

2、能承载大数据量的处理，单接口单日最高数据承载量达到**百万级别**。

3、将原始Basic认证方式取消，改为**access_token**认证方式，安全度更高。

4、**低代码化编辑**和**快速发布苍穹WebService**，降低运维成本。

5、拥有完整的日志监控，支持**历史调用数据回溯**，查找问题更加方便。

# 2解决方案

苍穹研发的WebService低代码开发功能，极大满足了客户痛点和诉求，主要优点如下：

1、通过简单的配置就可以实现WebService的发布，支持**原生WSDL文件**导入解析**自动生成**WebService，可以**保留原始结构**并大大减少了开发难度和开发周期，降低功能实现的代码量。

2、支持字段的**新增、修改**操作，并可以在导入的基础上**再次修改WebService结构**。

3、支持**SOAP1.1**和**SOAP1.2**协议。

4、支持多种方式调用接口，功能实现上更加灵活；

5、拥有完整的WebService测试模块；

6、拥有**完整的日志监控**，支持历史调用数据回溯，定位问题更加方便。

该客户通过苍穹发布的WebService服务，结合服务流程和集成方案来处理异构系统的数据，轻松集成了企业内部遗留系统。整体方案分为3步：

**步骤一：将WebService发布到开放平台。**

在【集成管理】中配置WebService，将WebService发布到开放平台，低代码方式实现；

**步骤二：WebService内部配置调用服务流程或者数据集成方案。**

由服务流程或数据集成方案来实现数据的加工和单据的生成，同时将**接收数据**和**处理数据**分开，客户无需再去使用WebClient解析WebService实现后续功能。中间环节也**仅需关注WebService是否接收到数据**，**是否将数据传输给服务流程或数据集成方案**，全程通过低代码方式实现；

**步骤三：服务流程或数据集成方案实现数据加工。**

服务流程或数据集成方案将接收从WebService传输的数据，加工后将数据存入到对应单据。

## 2.1 关键步骤配置及效果展示

下面，小编将展示**三个关键步骤**的配置方法及其效果。

**步骤一：导入WSDL文件反向生成WebService**

首先，通过【集成管理】→【自定义API】，进入菜单后，选择【导入API】下拉菜单，“根据WSDL文件导入”，选择WSDL文件进行上传，WSDL编辑器**自动载入**WebService定义。

![](https://vip.kingdee.com/download/0109a88598a610024cb682ce69108278f74b.png)

进入“自定义API”菜单
![](https://vip.kingdee.com/download/0109cc64b95274064dc8b93a73dca6ea221a.png)

选择“根据WSDL文件导入”

![](https://vip.kingdee.com/download/0109dc898121412f4d0ea65139236bee5fa1.png)

WSDL上传并自动载入WebService定义

然后，选择**操作名称**，即可进入WebService详细设计页面，客户仅需调整对应参数。

![](https://vip.kingdee.com/download/01094177804d92454d3797726fa80c9d98b3.png)

选择操作名称

![](https://vip.kingdee.com/download/010942fb007ee88d4d4e83ac9dc8409042b2.png)

WebService详细设计页面调整参数

**步骤二：平台标准功能测试WebService**

保存并启用即可发布WebService，在【开放平台】可根据需求设定报文格式的测试接口，同时设置**报文可编辑**。

具体测试操作：进入【开放平台】，选择【API管理】进入列表，选择对应的接口编码，进入详情页面，点击“API测试”即可进入测试窗口进行测试，可以切换报文的格式。
![](https://vip.kingdee.com/download/010971b122124a244ba480ab1f86ed796b91.png)

【开放平台】应用

![](https://vip.kingdee.com/download/01091ab77859cd2c4762bd5d0a33a211bfd6.png)

【API管理】列表

![](https://vip.kingdee.com/download/0109994ad86077be4a18abe61c21e229a067.png)

【API测试】示例

![](https://vip.kingdee.com/download/0109b3a6a34f56754e9b99f67536f73dd91b.png)

接口测试窗口

![](https://vip.kingdee.com/download/01090927217814c84342ad64d430d27cf4c9.png)

切换报文格式

以**SOAP1.1**为例，选择SOAP1.1后，对应的请求报文和响应报文均会以**XML形式**展现，如下图所示：

![](https://vip.kingdee.com/download/0109f884a881a0424e0bb019afe3c5d3abf2.png)

XML的形式展现

**步骤三：SoapUI工具测试WebService**

获取Web Service完整地址，如图地址为：

[http://yxtuat.yxtmart.cn/ierp/kapi/v2/iscb/route/script_tt2erp_ActiveMRP_OUT?wsdl](https://vip.kingdee.com/tolink?target=http%3A%2F%2Fyxtuat.yxtmart.cn%2Fierp%2Fkapi%2Fv2%2Fiscb%2Froute%2Fscript_tt2erp_ActiveMRP_OUT%3Fwsdl)（注：标准产品自带测试功能，一般情况下不需要通过测试工具也能完成测试）

将地址引入到**SoapUI**中执行，详细的信息会展示在响应报文栏里，并带有请求状态码。

![](https://vip.kingdee.com/download/010920d2f100eb384818b3006a252fd6460e.png)

地址获取示例

![](https://vip.kingdee.com/download/010934883e07a7c648cc89a12a7c7a9c0ba7.png)

将地址引入到SoapUI中执行

![](https://vip.kingdee.com/download/0109fef4631aca8c40b8a6d14c0e6918acef.png)

生成两种协议测试

![](https://vip.kingdee.com/download/0109c7a457dcc91b4635963334f74283216e.png)

补充对应的参数即可测试

![](https://vip.kingdee.com/download/0109bd2868cc32f6412da36fa08cc936b972.png)

响应报文信息

# 3竞品比较

IPaaS产品也有类似于WebService的功能发布，但此功能发布WebService的方式较为复杂，**未脱离对原生WebService的定义方式**，用户使用此产品定义WebService还是需要熟悉**完整的WSDL代码**，并修改代码，且过程中新增了一些个性化配置，导致发布的WebService增加了IPaaS的**代码前缀**，使用WebService需要解析更多的代码。

苍穹WebService与IPaaS发布WebService功能优劣对比详情如下图所示：

![](https://vip.kingdee.com/download/0109c0049fe610dd444097ff924f699769e5.png)

竞品比较详情

# 4方案的可推广价值

本方案主要提供了WebService的低代码化发布的功能，在同项目内与WebService类似的需求也能受益于此方案。此WebService方案一经推出就受客户和开发人员一致好评，**极大简化了开发步骤**，并**大幅提高开发效率**，具体体现在以下三个方面：

1、**WebService功能接口在项目实践中占比非常高。**

2、WebService**发布简单**，**可动态调配**，只需要做简单的**导入或者新增参数配置**即可快速发布WebService，效率是传统开发的**十倍之多**。

3、WebService有**完整的日志监控**，可以快速**定位问题**。

# 5注意事项

如果没有初始的WSDL文件，就需要从页面配置WebService，依然是低代码化的配置方式实现WebService发布。

---

**#往期推荐#**

# [OpenAPI2.0—轻松构建WebService服务](https://vip.kingdee.com/knowledge/specialDetail/282527627108140288?category=283972955728903680&id=333244538238596608&productLineId=29)

# [“语言不通”？看WebService如何集成](https://vip.kingdee.com/knowledge/specialDetail/282527627108140288?category=283974674537326080&id=292615873255085312&productLineId=29)

# [不一样的书签功能，解锁WebOffice新技能](https://vip.kingdee.com/knowledge/specialDetail/282527627108140288?category=283959429534711296&id=324570928674285056&productLineId=29)

# [WebOffice小科普，轻松助力在线Office办公](https://vip.kingdee.com/knowledge/specialDetail/282527627108140288?category=283959429534711296&id=323512124964209408&productLineId=29)
更多精彩内容，”码“上了解↓

![](https://vip.kingdee.com/download/01096ed2095472e14a17914b1fb957677f71.png)
