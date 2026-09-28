# 对账汇总-sim_split_count_check

## 对账汇总-主表 t_sim_count_check

- **表名称：** 对账汇总-主表
- **表名：** t_sim_count_check

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvoiceamountsum | 原始金额汇总 | numeric | 23 | 10 | √ | 0.0000000000 | 原始金额汇总 |
| 3 | ftotaltaxdiffer | 税额差值 | numeric | 23 | 10 | √ | 0.0000000000 | 税额差值 |
| 4 | ftotalamount | 发票价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 发票价税合计 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftotaltaxsum | 原始税额汇总 | numeric | 23 | 10 | √ | 0.0000000000 | 原始税额汇总 |
| 7 | fdatefield | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 8 | finvoiceconfirms | 已确认单据编号 | varchar | 255 |  | √ | ' ' | 已确认单据编号 |
| 9 | ftotaltax | 发票税额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票税额 |
| 10 | finvoiceconfirms_tag | 已确认单据编号_详情 | text | 0 |  |  | null | 已确认单据编号_详情 |
| 11 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额 |
| 12 | fissuestatus | 开票状态 | varchar | 50 |  | √ | ' ' | 开票状态,枚举: 0 :已开票 1 :开票中 2 :未开票 3 :开票失败 4 :已作废 5 :已红冲 |
| 13 | ftotalamountdiffer | 价税合计差值 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计差值 |
| 14 | fbuyername | 购方名称 | varchar | 50 |  | √ | ' ' | 购方名称 |
| 15 | finvoiceamountdiffer | 金额差值 | numeric | 23 | 10 | √ | 0.0000000000 | 金额差值 |
| 16 | ftotalamountsum | 原始价税汇总 | numeric | 23 | 10 | √ | 0.0000000000 | 原始价税汇总 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_count_check |  | fid |
| 2 | idx_sim_count_check |  | forgid |

---

## 单据体-子表 t_sim_count_check_items

- **表名称：** 单据体-子表
- **表名：** t_sim_count_check_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forigtotalamount | 原始价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 原始价税合计 |
| 3 | fconfirmstate | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: 0 :未确认 1 :部分确认 2 :已确认 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 6 | forigtotaltax | 原始税额 | numeric | 23 | 10 | √ | 0.0000000000 | 原始税额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbillno | 原始单据编号 | varchar | 50 |  | √ | ' ' | 原始单据编号 |
| 9 | foriginvoiceamount | 原始金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原始金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_count_check_items |  | fentryid |
| 2 | idx_sim_count_check_items_fk |  | fid |
