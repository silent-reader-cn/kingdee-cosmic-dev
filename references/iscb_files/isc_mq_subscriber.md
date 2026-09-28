# 消息订阅主题-isc_mq_subscriber

## 消息订阅主题-主表 t_iscb_mq_subscriber

- **表名称：** 消息订阅主题-主表
- **表名：** t_iscb_mq_subscriber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcharset | 字符集 | varchar | 100 |  | √ | ' ' | 字符集 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmq_server | 消息队列服务器 | int8 | 64 |  | √ | 0 | 消息队列服务器 isc_mq_server |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | fparse_script | 消息解析脚本 | varchar | 510 |  | √ | ' ' | 消息解析脚本 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmsg_digest | 消息摘要模板 | varchar | 150 |  |  | ' ' | 消息摘要模板 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcustom_config | 自定义参数配置 | varchar | 1000 |  |  | ' ' | 自定义参数配置 |
| 17 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 18 | fparse_script_tag | 消息解析脚本_详情 | text | 0 |  |  | null | 消息解析脚本_详情 |
| 19 | fmulti_line | 是否多值 | bpchar | 1 |  | √ | '1' | 是否多值 |
| 20 | fsub_ip_perttern | 订阅者IP | varchar | 500 |  | √ | ' ' | 订阅者IP |
| 21 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 300 |  | √ | ' ' | 编码 |
| 23 | fdata_structure | 数据结构 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_mq_sub |  | fnumber |
| 2 | t_iscb_mq_subscriber_pkey |  | fid |

---

## 消息订阅主题-多语言表 t_iscb_mq_subscriber_l

- **表名称：** 消息订阅主题-多语言表
- **表名：** t_iscb_mq_subscriber_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_mq_sub_l |  | fid,fname |
| 2 | t_iscb_mq_subscriber_l_pkey |  | fpkid |
