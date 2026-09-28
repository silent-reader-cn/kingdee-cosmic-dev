# 税率统计单据-sim_taxrate_bill

## 税率统计单据-主表 t_sim_taxrate_bill

- **表名称：** 税率统计单据-主表
- **表名：** t_sim_taxrate_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissuedevice | 开票设备 | varchar | 50 |  | √ | ' ' | 开票设备 |
| 3 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 028 :电子专票 026 :电子普票 |
| 4 | fsalername | 销方名称 | varchar | 50 |  | √ | ' ' | 销方名称 |
| 5 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 6 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 7 | fsalertaxno | 销方税号 | varchar | 50 |  | √ | ' ' | 销方税号 |
| 8 | finvoicenature | 发票性质 | varchar | 30 |  | √ | ' ' | 发票性质,枚举: 0 :蓝票 1 :红票 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_taxrate_bill |  | fid |
| 2 | idx_sim_taxrate_bill |  | fdate |

---

## 单据体-子表 t_sim_taxrate_bill_item

- **表名称：** 单据体-子表
- **表名：** t_sim_taxrate_bill_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftenpercent | 10% | numeric | 23 | 10 | √ | 0.0000000000 | 10% |
| 3 | fthreepercent | 3% | numeric | 23 | 10 | √ | 0.0000000000 | 3% |
| 4 | fcountdimension | 统计维度 | varchar | 30 |  | √ | ' ' | 统计维度,枚举: amount :金额 tax :税额 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fthirteenpercent | 13% | numeric | 23 | 10 | √ | 0.0000000000 | 13% |
| 7 | fsixpercent | 6% | numeric | 23 | 10 | √ | 0.0000000000 | 6% |
| 8 | fzeropercent | 0% | numeric | 23 | 10 | √ | 0.0000000000 | 0% |
| 9 | ftotal | 合计 | numeric | 23 | 10 | √ | 0.0000000000 | 合计 |
| 10 | fonepercent | 1% | numeric | 23 | 10 | √ | 0.0000000000 | 1% |
| 11 | fotherpercent | 其他 | numeric | 23 | 10 | √ | 0.0000000000 | 其他 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffivepercent | 5% | numeric | 23 | 10 | √ | 0.0000000000 | 5% |
| 14 | fninepercent | 9% | numeric | 23 | 10 | √ | 0.0000000000 | 9% |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sim_taxrate_bill_item |  | fentryid |
| 2 | idx_sim_taxrate_bill_item_fk |  | fid |
