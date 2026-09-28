# test01_rate_25-test01_rate_25

## test01_rate_25-主表 t_test01_rate_25

- **表名称：** test01_rate_25-主表
- **表名：** t_test01_rate_25

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fexratetable | 汇率表 | int8 | 64 |  |  | null | 汇率表 bd_exratetable |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftocurr | 目标币 | int8 | 64 |  |  | null | 币种 bd_currency |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fquotation | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 12 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 13 | ffromcurr | 原币 | int8 | 64 |  |  | null | 币种 bd_currency |
| 14 | fexrate | 汇率 | numeric | 23 | 10 |  | null | 汇率 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |
| 17 | fbilltypefield | 单据类型 | int8 | 64 |  |  | null | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_test01_rate_25 |  | fid |

---

## 单据体-子表 t_test01_rate_25_entry

- **表名称：** 单据体-子表
- **表名：** t_test01_rate_25_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftocurr1 | 目标币 | int8 | 64 |  |  | null | 币种 bd_currency |
| 3 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | ffromcurr1 | 原币 | int8 | 64 |  |  | null | 币种 bd_currency |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fexratetable1 | 汇率表 | int8 | 64 |  |  | null | 汇率表 bd_exratetable |
| 7 | fquotation1 | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 8 | fexratedate1 | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 11 | fexrate1 | 汇率 | numeric | 23 | 10 |  | null | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_test01_rate_25_entry |  | fentryid |
| 2 | idx_test01_rate_25_entry_fk |  | fid |
