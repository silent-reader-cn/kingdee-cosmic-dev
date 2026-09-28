# 生产改制日志-pom_restructlog

## 生产改制日志-主表 t_pom_restructlog

- **表名称：** 生产改制日志-主表
- **表名：** t_pom_restructlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbfbaseqty | 改制前基本数量 | numeric | 23 | 10 | √ | 0 | 改制前基本数量 |
| 3 | fexecbatchid | 执行批次id | int8 | 64 |  | √ | 0 | 执行批次id |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 6 | forderid | 工单f7 | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 7 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | forderentryid | 工单分录f7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 9 | fbfqty | 改制前数量 | numeric | 23 | 10 | √ | 0 | 改制前数量 |
| 10 | fafbaseqty | 改制后基本数量 | numeric | 23 | 10 | √ | 0 | 改制后基本数量 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | frestructtype | 改制类型 | varchar | 5 |  | √ | ' ' | 改制类型,枚举: A :在产改制 B :库存改制 |
| 13 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fafqty | 改制后数量 | numeric | 23 | 10 | √ | 0 | 改制后数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_restructlog_fid |  | forderentryid |
| 2 | pk_pom_restructlog |  | fid |

---

## 执行明细-子表 t_pom_restructlogentry

- **表名称：** 执行明细-子表
- **表名：** t_pom_restructlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frestructstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :校验失败 1 :改制后工单创建成功 2 :改制后工单创建失败 3 :改制前工单变更成功 4 :改制前生产工单变更失败 5 :自动挪料成功 6 :自动挪料部分成功 7 :自动挪料失败 8 :自动退料成功 9 :自动退料部分成功 10 :自动退料失败 |
| 3 | ftorderid | 改制后工单f7 | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 4 | fafentryseq | 改制后分录行 | int4 | 32 |  | √ | 0 | 改制后分录行 |
| 5 | ftmaterialid | 改制后物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 6 | fresreasonid | 改制原因 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftorderentryid | 改制后工单分录f7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_restructlogentry_fid |  | fid |
| 2 | pk_pom_restructlogentry |  | fentryid |

---

## 执行明细-分表 t_pom_restructlogentry_d

- **表名称：** 执行明细-分表
- **表名：** t_pom_restructlogentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fdesc_tag | 描述_详情 | text | 0 |  |  | null | 描述_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_restructlogentryd_fid |  | fid |
| 2 | pk_pom_restructlogentry_d |  | fentryid |
