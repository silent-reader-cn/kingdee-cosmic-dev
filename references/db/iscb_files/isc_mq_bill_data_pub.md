# 单据消息发布-isc_mq_bill_data_pub

## 单据消息发布-多语言表 t_iscb_mq_bill_data_pub_l

- **表名称：** 单据消息发布-多语言表
- **表名：** t_iscb_mq_bill_data_pub_l

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
| 1 | t_iscb_mq_bill_data_pub_l_pkey |  | fpkid |
| 2 | idx_iscb_mq_bd_pub_l |  | fid |

---

## 发布字段-子表 t_iscb_mq_bill_data_pub_f

- **表名称：** 发布字段-子表
- **表名：** t_iscb_mq_bill_data_pub_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdata_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 3 | ffield | 字段名 | varchar | 300 |  | √ | ' ' | 字段名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdescription | 字段描述 | varchar | 100 |  | √ | ' ' | 字段描述 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_mq_bd_pub_f |  | fid,fentryid |
| 2 | t_iscb_mq_bill_data_pub_f_pkey |  | fentryid |

---

## 单据消息发布-主表 t_iscb_mq_bill_data_pub

- **表名称：** 单据消息发布-主表
- **表名：** t_iscb_mq_bill_data_pub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fmeta_data | 集成对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 4 | fformat_script_tag | 数据发布前处理脚本_详情 | text | 0 |  |  | null | 数据发布前处理脚本_详情 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fformat_script | 数据发布前处理脚本 | varchar | 510 |  | √ | ' ' | 数据发布前处理脚本 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fmessage_queue | 消息发布主题 | int8 | 64 |  | √ | 0 | 消息发布主题 isc_mq_publisher |
| 16 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | fevents | 单据事件 | varchar | 1000 |  | √ | ' ' | 单据事件,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_mq_bill_data_pub_pkey |  | fid |
| 2 | idx_iscb_mq_bd_pub |  | fmeta_data,fmessage_queue |
