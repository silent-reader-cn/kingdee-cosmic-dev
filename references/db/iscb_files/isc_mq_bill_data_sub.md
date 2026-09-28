# 单据消息订阅-isc_mq_bill_data_sub

## 单据消息订阅-主表 t_iscb_mq_bill_data_sub

- **表名称：** 单据消息订阅-主表
- **表名：** t_iscb_mq_bill_data_sub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmeta_data | 集成对象 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fprehandle_script | 消息预处理脚本 | varchar | 510 |  | √ | ' ' | 消息预处理脚本 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 9 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fprehandle_script_tag | 消息预处理脚本_详情 | text | 0 |  |  | null | 消息预处理脚本_详情 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fmessage_queue | 消息订阅主题 | int8 | 64 |  | √ | 0 | [消息订阅主题 isc_mq_subscriber](../iscb_files/isc_mq_subscriber.md) |
| 16 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_mq_bill_data_sub_pkey |  | fid |
| 2 | idx_num_bill_data_sub |  | fnumber |

---

## 赋值字段-子表 t_iscb_mq_bill_data_sub_f

- **表名称：** 赋值字段-子表
- **表名：** t_iscb_mq_bill_data_sub_f

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdata_type | 数据类型 | varchar | 100 |  | √ | ' ' | 数据类型 |
| 3 | ffield | 字段名 | varchar | 300 |  | √ | ' ' | 字段名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdefault_value | 默认值 | varchar | 100 |  | √ | ' ' | 默认值 |
| 6 | fdescription | 字段描述 | varchar | 100 |  | √ | ' ' | 字段描述 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fcandidate_key | 是否候选键 | bpchar | 1 |  | √ | ' ' | 是否候选键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_mq_bill_data_sub_f_pkey |  | fentryid |
| 2 | idx_bill_data_sub_f_fk |  | fid |

---

## 单据消息订阅-多语言表 t_iscb_mq_bill_data_sub_l

- **表名称：** 单据消息订阅-多语言表
- **表名：** t_iscb_mq_bill_data_sub_l

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
| 1 | t_iscb_mq_bill_data_sub_l_pkey |  | fpkid |
| 2 | idx_bill_data_sub_l_0 |  | fid,flocaleid |

---

## 操作选择-子表 t_iscb_mq_bill_data_sub_o

- **表名称：** 操作选择-子表
- **表名：** t_iscb_mq_bill_data_sub_o

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcondition | 选择条件 | varchar | 1000 |  | √ | ' ' | 选择条件 |
| 5 | foperation | 操作 | varchar | 30 |  | √ | ' ' | 操作,枚举: |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_mq_bill_data_sub_o_pkey |  | fentryid |
| 2 | idx_bill_data_sub_o_fk |  | fid |
