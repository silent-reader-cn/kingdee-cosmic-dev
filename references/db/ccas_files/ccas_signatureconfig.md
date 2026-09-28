# 签章配置-ccas_signatureconfig

## 签章配置-主表 t_ccas_signatureconfig

- **表名称：** 签章配置-主表
- **表名：** t_ccas_signatureconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | femail | 邮件 | varchar | 1 |  | √ | '0' | 邮件 |
| 4 | flastenablees | 最近启动的电子签章 | varchar | 50 |  | √ | ' ' | 最近启动的电子签章 |
| 5 | fshortmessage | 短信 | varchar | 1 |  | √ | '0' | 短信 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | inx_ccas_signatureconfig_sta |  | fstatus |
| 2 | pk_ccas_signatureconfig |  | fid |

---

## 签章配置-多语言表 t_ccas_signatureconfig_l

- **表名称：** 签章配置-多语言表
- **表名：** t_ccas_signatureconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 10 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccas_signatureconfig_l |  | fpkid |
| 2 | udx_ccas_signatureconfig_l |  | fid,flocaleid |

---

## 单据体-子表 t_ccas_signature_entry

- **表名称：** 单据体-子表
- **表名：** t_ccas_signature_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpagingseal | 骑缝章 | varchar | 1000 |  | √ | ' ' | 骑缝章 |
| 3 | fusestatus | 使用状态 | varchar | 1 |  | √ | 'B' | 使用状态,枚举: A :可用 B :禁用 |
| 4 | fsigningsequence | 签署顺序 | varchar | 1000 |  | √ | '0' | 签署顺序 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbusinesstype | 单据类型（废弃） | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 7 | fkeyword | 关键词定位 | varchar | 1000 |  | √ | ' ' | 关键词定位 |
| 8 | fentrynumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 9 | frulefielddataid | 选择单据数据id | varchar | 50 |  | √ | ' ' | 选择单据数据id |
| 10 | frulefieldname | 规则识别字段 | varchar | 50 |  | √ | ' ' | 规则识别字段 |
| 11 | frulefield | 规则识别字段标识 | varchar | 50 |  | √ | ' ' | 规则识别字段标识 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbilltype | 业务对象 | varchar | 50 |  | √ | '1' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | frulefielddataname | 识别标准 | varchar | 50 |  | √ | ' ' | 识别标准 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_signature_entryno |  | fid,fentrynumber |
| 2 | pk_ccas_signature_entry |  | fentryid |
