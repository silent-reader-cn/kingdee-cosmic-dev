# 规则设置-ccas_signconfigrule

## 规则设置-主表 t_ccas_signrule

- **表名称：** 规则设置-主表
- **表名：** t_ccas_signrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | frulefielddataid | 选择单据数据id | varchar | 50 |  | √ | ' ' | 选择单据数据id |
| 4 | frulefieldname | 规则识别字段 | varchar | 50 |  | √ | ' ' | 规则识别字段 |
| 5 | frulefieldtype | 规则识别字段类型 | varchar | 50 |  | √ | ' ' | 规则识别字段类型,枚举: BasedataField :基础资料 BillType :单据类型 |
| 6 | frulefield | 规则识别字段标识 | varchar | 50 |  | √ | ' ' | 规则识别字段标识 |
| 7 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fbusinesstype | 单据类型（废弃） | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 9 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 10 | frulefielddataformid | 选择数据对应实体 | varchar | 50 |  | √ | ' ' | 选择数据对应实体 |
| 11 | fbusiness | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | frulefielddataname | 选择单据数据名称 | varchar | 50 |  | √ | ' ' | 选择单据数据名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccas_signrule_business |  | fbusiness,frulefield |
| 2 | pk_ccas_signrule |  | fid |
| 3 | udx_ccas_signrule_number |  | fnumber |

---

## 规则设置-多语言表 t_ccas_signrule_l

- **表名称：** 规则设置-多语言表
- **表名：** t_ccas_signrule_l

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
| 1 | pk_ccas_signrule_l |  | fpkid |
| 2 | udx_ccas_signrule_l |  | fid,flocaleid |

---

## 参与方-子表 t_ccas_signruleentry

- **表名称：** 参与方-子表
- **表名：** t_ccas_signruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeywordflag | 关键词定位 | varchar | 1 |  | √ | '0' | 关键词定位 |
| 3 | fpagingsealflag | 设置骑缝章 | varchar | 1 |  | √ | '0' | 设置骑缝章 |
| 4 | fsigningsequence | 签署顺序 | int4 | 32 |  | √ | 0 | 签署顺序 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparticipantcontacts | 参与方联系人 | varchar | 100 |  | √ | '1' | 参与方联系人 |
| 7 | fpagingsealposition | 骑缝章位置 | numeric | 23 | 10 | √ | 0 | 骑缝章位置 |
| 8 | fmanagersignflag | 企业经办人签名 | varchar | 1 |  | √ | '0' | 企业经办人签名 |
| 9 | fkeyword | 关键词 | varchar | 50 |  | √ | ' ' | 关键词 |
| 10 | fparticipantphone | 参与方手机号 | varchar | 100 |  | √ | '1' | 参与方手机号 |
| 11 | fparticipantid | 参与方标识 | varchar | 50 |  | √ | '1' | 参与方标识 |
| 12 | fparticipantname | 参与方名称 | varchar | 100 |  | √ | '1' | 参与方名称 |
| 13 | fparticipantemail | 参与方邮箱 | varchar | 100 |  | √ | '1' | 参与方邮箱 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | udx_ccas_signruleentry_partic |  | fid,fparticipantid |
| 2 | pk_ccas_signruleentry |  | fentryid |
