# 模型服务模版-aicc_service_template

## 模型服务模版-主表 t_aicc_service_template

- **表名称：** 模型服务模版-主表
- **表名：** t_aicc_service_template

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodel | model | varchar | 50 |  | √ | ' ' | model |
| 3 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: llm :文本大模型 rerank :rerank重排序模型 embedding :embedding向量模型 |
| 4 | fauthurl | 认证地址 | varchar | 500 |  | √ | ' ' | 认证地址 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fembmaxlen | embedding最大字符数 | int8 | 64 |  | √ | 0 | embedding最大字符数 |
| 7 | fsupplier | 服务提供商 | varchar | 50 |  | √ | ' ' | 服务提供商,枚举: DEEPSEEK :DeepSeek TENCENT :腾讯云 VOLCENGINE :火山引擎 BAIDU :百度智能云 MOONSHOT :Moonshot AI SILICONFLOW :硅基流动 ALICLOUD :阿里云 PRIVATEDEPLOY :私有化部署 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodelseqno | 排序号 | int4 | 32 |  | √ | 0 | 排序号 |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fembeddingconfig | embedding配置 | int8 | 64 |  | √ | 0 | [embedding配置 aicc_embedding_config](../aicc_files/aicc_embedding_config.md) |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fclientid | ClientID | varchar | 255 |  | √ | ' ' | ClientID |
| 16 | fcontext | 模型上下文长度 | varchar | 50 |  | √ | ' ' | 模型上下文长度,枚举: lte4k :小于等于4k 8k :8k 16k :16k 32k :32k 64k :64k 128k :128k 256k :256k 0 :自定义 |
| 17 | fmodeldesc | 模型描述 | varchar | 255 |  | √ | ' ' | 模型描述 |
| 18 | fmodeldesc_tag | 模型描述_详情 | text | 0 |  |  | null | 模型描述_详情 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fbasellm | 基础大模型 | int8 | 64 |  | √ | 0 | [API出入参样式 aicc_llm](../aicc_files/aicc_llm.md) |
| 21 | fmodelname | 模型名称 | varchar | 255 |  | √ | ' ' | 模型名称 |
| 22 | furl | 服务URL地址 | varchar | 2000 |  | √ | ' ' | 服务URL地址 |
| 23 | fauthtype | 认证方式 | varchar | 50 |  | √ | ' ' | 认证方式,枚举: NONE :无须认证 API2SIGN :摘要认证 OAUTHTOKEN :TOKEN认证 APIKEY :APIKEY BAIDU :BAIDU AWS_SIGN_V4 :亚马逊v4签名认证 TENCENT_HUNYUAN :腾讯混元认证 XUNFEI_SPARK :讯飞星火 XMINDAI :XMINDAI TENCENT_HUNYUAN_PRO_V3 :腾讯混元V3认证 KINGDEE :KINGDEE |
| 24 | fcustomcontext | 自定义上下文长度（单位KB） | int8 | 64 |  | √ | 0 | 自定义上下文长度（单位KB） |
| 25 | fabilitytag | 模型能力 | varchar | 50 |  | √ | ' ' | 模型能力,枚举: functioncall :Function call think :深度思考 search :联网搜索 picpreceive :图片理解 |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_service_template_billno |  | fbillno |
| 2 | pk_t_aicc_service_template |  | fid |
