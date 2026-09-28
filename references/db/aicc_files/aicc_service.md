# 模型服务-aicc_service

## 模型服务-主表 t_aicc_service

- **表名称：** 模型服务-主表
- **表名：** t_aicc_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpromptids | 提示词ids | varchar | 255 |  | √ | ' ' | 提示词ids |
| 3 | frequestsample | 请求参数示例 | varchar | 255 |  | √ | ' ' | 请求参数示例 |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [算法服务—类型 aicc_servicetype](../aicc_files/aicc_servicetype.md) |
| 5 | fpromptids_tag | 提示词ids_详情 | text | 0 |  |  | ' ' | 提示词ids_详情 |
| 6 | fresponsesample_tag | 返回结果参数示例_详情 | text | 0 |  |  | ' ' | 返回结果参数示例_详情 |
| 7 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: LLM :文本大模型 EMBEDDING :embedding向量模型 RERANK :rerank重排序模型 AUDIO :语音识别模型 DOC_PARSE :文档解析 |
| 8 | fchunktoken | embedding片段最大字符数 | int4 | 32 |  | √ | 0 | embedding片段最大字符数 |
| 9 | fprocessids | 任务流ids | varchar | 255 |  | √ | ' ' | 任务流ids |
| 10 | fqueuelength | 队列长度 | int4 | 32 |  | √ | 0 | 队列长度 |
| 11 | ftablestatus | 启用算法服务 | bpchar | 1 |  | √ | '0' | 启用算法服务 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fresponsesample | 返回结果参数示例 | varchar | 255 |  | √ | ' ' | 返回结果参数示例 |
| 15 | fprocessids_tag | 任务流ids_详情 | text | 0 |  |  | ' ' | 任务流ids_详情 |
| 16 | fagentids_tag | 智能体ids_详情 | text | 0 |  |  | ' ' | 智能体ids_详情 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fkddatapackage | 使用金蝶大模型流量包 | bpchar | 1 |  | √ | '0' | 使用金蝶大模型流量包 |
| 20 | fconfigmodel | model | varchar | 50 |  | √ | ' ' | model |
| 21 | fwaittime | 任务等待时间（单位s） | int4 | 32 |  | √ | 0 | 任务等待时间（单位s） |
| 22 | frequestsample_tag | 请求参数示例_详情 | text | 0 |  |  | ' ' | 请求参数示例_详情 |
| 23 | fllmtype | API出入参样式 | int8 | 64 |  | √ | 0 | [API出入参样式 aicc_llm](../aicc_files/aicc_llm.md) |
| 24 | fsupportstream | 文本逐字生成 | bpchar | 1 |  | √ | '0' | 文本逐字生成 |
| 25 | fversion | 服务版本号 | varchar | 50 |  | √ | ' ' | 服务版本号 |
| 26 | fname | 服务名称 | varchar | 200 |  | √ | ' ' | 服务名称 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fembeddingconfig | embedding名称 | int8 | 64 |  | √ | 0 | [embedding配置 aicc_embedding_config](../aicc_files/aicc_embedding_config.md) |
| 29 | fcreatetime | 上架时间 | timestamp | 0 |  |  | null | 上架时间 |
| 30 | fmodelowner | 模型提供方 | varchar | 50 |  | √ | ' ' | 模型提供方,枚举: KINGDEE :金蝶 DEEPSEEK :DeepSeek VOLCENGINE :火山引擎 BAIDU :百度智能云 ALICLOUD :阿里云 MOONSHOT :Moonshot AI TENCENT :腾讯云 ZHIPU :智谱 XUNFEI :讯飞 SILICONFLOW :硅基流动 BAICHUAN :百川 OPENAI :OpenAI OTHER :其他 |
| 31 | fagentids | 智能体ids | varchar | 255 |  | √ | ' ' | 智能体ids |
| 32 | fisvisible | 是否可见 | bpchar | 1 |  | √ | '1' | 是否可见 |
| 33 | fcustomtoken |  | int4 | 32 |  | √ | 0 |  |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fservicetag | 模型能力 | varchar | 200 |  | √ | ' ' | 模型能力,枚举: A :深度思考 B :Function Call C :联网搜索 D :图片理解 E :开启/关闭思考过程 |
| 36 | fnumber | 服务编码 | varchar | 30 |  | √ | ' ' | 服务编码 |
| 37 | fdesc | 模型服务说明 | varchar | 2000 |  |  | null | 模型服务说明 |
| 38 | fcontexttoken | 模型上下文长度 | varchar | 50 |  | √ | ' ' | 模型上下文长度,枚举: 4096 :4k 8192 :8k 16384 :16k 32768 :32k 65536 :64k 131072 :128k 262144 :256k -1 :自定义 0 :未设置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_service_fnumber |  | fnumber |
| 2 | pk_t_aicc_service |  | fid |

---

## 模型服务-多语言表 t_aicc_service_l

- **表名称：** 模型服务-多语言表
- **表名：** t_aicc_service_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 服务名称 | varchar | 200 |  | √ | ' ' | 服务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_aicc_service_l |  | fpkid |
| 2 | idx_aicc_service_l_fid |  | fid |

---

## 单据体1-子表 t_aicc_instance

- **表名称：** 单据体1-子表
- **表名：** t_aicc_instance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhost | fhost | varchar | 200 |  | √ | ' ' |  |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fauthurl | 认证URL地址 | varchar | 500 |  | √ | ' ' | 认证URL地址 |
| 5 | fmodifytime | 实例修改日期 | timestamp | 0 |  |  | null | 实例修改日期 |
| 6 | finstancedesc | 实例描述 | varchar | 255 |  | √ | ' ' | 实例描述 |
| 7 | fstatus | 实例状态 | varchar | 50 |  | √ | ' ' | 实例状态 |
| 8 | fmodelurl | 服务URL地址 | varchar | 500 |  | √ | ' ' | 服务URL地址 |
| 9 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 10 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 11 | fusersecetkey | 代理用户密钥 | varchar | 512 |  | √ | ' ' | 代理用户密钥 |
| 12 | fserviceid | 算法服务 | int8 | 64 |  | √ | 0 | [模型服务 aicc_service](../aicc_files/aicc_service.md) |
| 13 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 16 | fclientid | ClientID | varchar | 512 |  | √ | ' ' | ClientID |
| 17 | fsecretkey | SecretKey | varchar | 512 |  | √ | ' ' | SecretKey |
| 18 | fmaxparallel | 最大并发数 | int8 | 64 |  | √ | 0 | 最大并发数 |
| 19 | fcustomparam | 请求体body | varchar | 1024 |  | √ | ' ' | 请求体body |
| 20 | fcustomheader | 请求头header | varchar | 1024 |  | √ | ' ' | 请求头header |
| 21 | fprotocol | fprotocol | varchar | 50 |  | √ | ' ' |  |
| 22 | fport | fport | int8 | 64 |  | √ | 0 |  |
| 23 | fcontexturl | fcontexturl | varchar | 500 |  | √ | ' ' |  |
| 24 | fenable |  | varchar | 50 |  | √ | ' ' |  |
| 25 | fauthtype | 认证 | varchar | 50 |  | √ | ' ' | 认证,枚举: NONE :无须认证 API2SIGN :摘要认证 OAUTHTOKEN :APIKEY认证（原TOKEN认证） APIKEY :老版AZURE认证（原APIKEY认证） BAIDU :BAIDU AWS_SIGN_V4 :亚马逊v4签名认证 TENCENT_HUNYUAN :腾讯混元认证 XUNFEI_SPARK :讯飞星火 XMINDAI :XMINDAI TENCENT_HUNYUAN_PRO_V3 :腾讯混元V3认证 KINGDEE :KINGDEE DOUBAO :DOUBAO KD_DATA_PACKAGE :金蝶大模型流量包 |
| 26 | fnumber | fnumber | varchar | 50 |  | √ | ' ' |  |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fparalleltype | 并发策略控制 | varchar | 20 |  | √ | ' ' | 并发策略控制,枚举: QPS :QPS RPM :RPM |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aicc_instance_fserviceid |  | fserviceid |
| 2 | pk_t_aicc_instance |  | fentryid |
