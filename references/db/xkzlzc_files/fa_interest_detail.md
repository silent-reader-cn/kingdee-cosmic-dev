# 计息明细表-fa_interest_detail

## 计息明细表-主表 t_fa_interest_detail

- **表名称：** 计息明细表-主表
- **表名：** t_fa_interest_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fleasecontractid | 租赁合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 10 | fdailyrate | 实际日利率(%) | numeric | 23 | 10 |  | null | 实际日利率(%) |
| 11 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_interest_detail |  | fid |
| 2 | idx_fa_interest_detail |  | fleasecontractid |

---

## 计息明细分录-子表 t_fa_interest_detail_e

- **表名称：** 计息明细分录-子表
- **表名：** t_fa_interest_detail_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbeginbalance | 期初余额 | numeric | 19 | 4 | √ | 0.0000 | 期初余额 |
| 3 | fleaseliabint | 租赁负债-利息 | numeric | 19 | 4 | √ | 0.0000 | 租赁负债-利息 |
| 4 | frealdailyrate | 实际日利率(%) | numeric | 23 | 10 | √ | 0 | 实际日利率(%) |
| 5 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | 'A' | 来源类型,枚举: A :新增 B :冲销 |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fendbalance | 期末余额 | numeric | 19 | 4 | √ | 0.0000 | 期末余额 |
| 9 | fleaseliabpay | 租赁负债-支付 | numeric | 19 | 4 | √ | 0.0000 | 租赁负债-支付 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_interest_detail_entry |  | fid |
| 2 | pk_t_fa_interest_detail_e |  | fentryid |
