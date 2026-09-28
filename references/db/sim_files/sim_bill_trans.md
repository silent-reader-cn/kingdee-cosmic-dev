# 转换单据明细(旧)-sim_bill_trans

## 单据体-子表 t_sim_bill_trans_item

- **表名称：** 单据体-子表
- **表名：** t_sim_bill_trans_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 3 | ftax | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbillno | 原单据编号 | varchar | 50 |  | √ | ' ' | 原单据编号 |
| 8 | fgoodsitemsid | 原明细行id | int8 | 64 |  | √ | 0 | 原明细行id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_bill_trans_item_fk |  | fid |
| 2 | pk_sim_bill_trans_item |  | fentryid |

---

## 转换单据明细(旧)-主表 t_sim_bill_trans

- **表名称：** 转换单据明细(旧)-主表
- **表名：** t_sim_bill_trans

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfirmbillno | 已确认单据编号 | varchar | 100 |  | √ | ' ' | 已确认单据编号 |
| 3 | fchangestate | 有效状态 | varchar | 10 |  | √ | ' ' | 有效状态,枚举: 0 :有效 1 :撤回（有开票信息） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_bill_trans |  | fconfirmbillno |
| 2 | pk_sim_bill_trans |  | fid |
