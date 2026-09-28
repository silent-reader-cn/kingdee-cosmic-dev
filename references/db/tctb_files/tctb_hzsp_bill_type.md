# 汇总审批单据类型-tctb_hzsp_bill_type

## 数据子表字段映射-子表 t_tctb_hzsp_bill_fieldsub

- **表名称：** 数据子表字段映射-子表
- **表名：** t_tctb_hzsp_bill_fieldsub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhzspsubfieldname | 汇总审批业务单明细表字段名称 | varchar | 50 |  | √ | ' ' | 汇总审批业务单明细表字段名称 |
| 3 | fsubfieldname | 业务单子表字段名称 | varchar | 50 |  | √ | ' ' | 业务单子表字段名称 |
| 4 | hzspsubfieldnum | 汇总审批业务单明细表字段编码 | varchar | 50 |  | √ | ' ' | 汇总审批业务单明细表字段编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsubfieldnum | 业务单子表字段编码 | varchar | 50 |  | √ | ' ' | 业务单子表字段编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_hzsp_bill_fieldsub_fk |  | fid |
| 2 | pk_tctb_hzsp_bill_fieldsub |  | fentryid |

---

## 汇总审批单据类型-主表 t_tctb_hzsp_bill_type

- **表名称：** 汇总审批单据类型-主表
- **表名：** t_tctb_hzsp_bill_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 汇总审批单单据名称 | varchar | 50 |  | √ | ' ' | 汇总审批单单据名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillname | 业务单据实体名称 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbillstatusinterface | 同步汇总审批单单据状态实现接口 | varchar | 100 |  | √ | ' ' | 同步汇总审批单单据状态实现接口 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fhzspbillname | 汇总审批单单据实体名称 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | fbillorg | 业务组织字段 | varchar | 50 |  | √ | ' ' | 业务组织字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_hzsp_bill_type |  | fid |
| 2 | idx_tctb_hzsp_bill_fbillorg |  | fbillorg |

---

## 汇总审批单据类型-多语言表 t_tctb_hzsp_bill_type_l

- **表名称：** 汇总审批单据类型-多语言表
- **表名：** t_tctb_hzsp_bill_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 汇总审批单单据名称 | varchar | 50 |  | √ | ' ' | 汇总审批单单据名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_hzsp_bill_type_l_0 |  | fid,flocaleid |
| 2 | pk_tctb_hzsp_bill_type_l |  | fpkid |

---

## 数据主表字段映射-子表 t_tctb_hzsp_bill_field

- **表名称：** 数据主表字段映射-子表
- **表名：** t_tctb_hzsp_bill_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhzspfieldname | 汇总审批单子表字段名称 | varchar | 50 |  | √ | ' ' | 汇总审批单子表字段名称 |
| 3 | ffieldnum | 业务单主表字段编码 | varchar | 50 |  | √ | ' ' | 业务单主表字段编码 |
| 4 | ffieldname | 业务单主表字段名称 | varchar | 50 |  | √ | ' ' | 业务单主表字段名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fhzspfieldnum | 汇总审批单子表字段编码 | varchar | 50 |  | √ | ' ' | 汇总审批单子表字段编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_hzsp_bill_field |  | fentryid |
| 2 | idx_tctb_hzsp_bill_field_fk |  | fid |

---

## 金额字段映射-子表 t_tctb_hzsp_bill_amount

- **表名称：** 金额字段映射-子表
- **表名：** t_tctb_hzsp_bill_amount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhzspamountfieldname | 汇总审批单主表合计金额字段名称 | varchar | 50 |  | √ | ' ' | 汇总审批单主表合计金额字段名称 |
| 3 | famountfieldname | 业务单字段名称 | varchar | 50 |  | √ | ' ' | 业务单字段名称 |
| 4 | famountfieldnum | 业务单字段编码 | varchar | 50 |  | √ | ' ' | 业务单字段编码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fhzspamountfieldnum | 汇总审批单主表合计金额字段编码 | varchar | 50 |  | √ | ' ' | 汇总审批单主表合计金额字段编码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_hzsp_bill_amount_fk |  | fid |
| 2 | pk_tctb_hzsp_bill_amount |  | fentryid |
