# 退回重新投标-src_retender

## 退回重新投标-主表 t_src_retender

- **表名称：** 退回重新投标-主表
- **表名：** t_src_retender

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 寻源项目F7 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fistender | 允许供应商修改标书 | bpchar | 1 |  | √ | '1' | 允许供应商修改标书 |
| 6 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 8 | fisreturnbid | 开标和评标后允许退回重新投标 | bpchar | 1 |  | √ | '0' | 开标和评标后允许退回重新投标 |
| 9 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |
| 10 | fbidchangeid | 寻源项目变更F7 | int8 | 64 |  | √ | 0 | 寻源项目变更F7 src_bidchangef7 |
| 11 | fchgsrcbillid | 变更源单ID | int8 | 64 |  | √ | 0 | 变更源单ID |
| 12 | fstopbiddate | 原投标截止时间 | timestamp | 0 |  |  | null | 原投标截止时间 |
| 13 | fcompbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fisquote | 允许供应商修改报价 | bpchar | 1 |  | √ | '0' | 允许供应商修改报价 |
| 15 | fnewstopbiddate | 新投标截止时间 | timestamp | 0 |  |  | null | 新投标截止时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_retender |  | fid |
| 2 | idx_src_retender_pid |  | fparentid |

---

## 报价单分录-子表 t_src_retenderentry

- **表名称：** 报价单分录-子表
- **表名：** t_src_retenderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftenderid | 投标单 | int8 | 64 |  | √ | 0 | 投标单F7 tnd_tenderbillf7 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_retenderentry_fid |  | fid |
| 2 | pk_src_retenderentry |  | fentryid |
