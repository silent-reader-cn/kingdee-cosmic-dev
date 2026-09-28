# 每日折旧日志-fa_dailydepre_log

## 折旧分录-子表 t_fa_dailydepre_log_entry

- **表名称：** 折旧分录-子表
- **表名：** t_fa_dailydepre_log_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepreresult | 折旧结果 | varchar | 100 |  |  | ' ' | 折旧结果 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ffincardid | 财务卡片ID | int8 | 64 |  | √ | 0 | [财务卡片基础资料 fa_card_fin_base](../fa_files/fa_card_fin_base.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_daideplogent_fid |  | fid |
| 2 | t_fa_dailydepre_log_entry_pkey |  | fentryid |

---

## 每日折旧日志-主表 t_fa_dailydepre_log

- **表名称：** 每日折旧日志-主表
- **表名：** t_fa_dailydepre_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbegindate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fresult | 日志记录 | text | 0 |  |  | null | 日志记录 |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fresult_tag | 日志记录_详情 | varchar | 60 |  | √ | ' ' | 日志记录_详情 |
| 9 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbilltypefield | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 13 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depre_log_fenddate |  | fenddate |
| 2 | t_fa_dailydepre_log_pkey |  | fid |
| 3 | idx_fa_dalydeprelog_fbillno |  | fbillno |
