# 小微企业优惠底稿-tccit_small_summary

## 小微企业优惠底稿-主表 t_tccit_small_summary

- **表名称：** 小微企业优惠底稿-主表
- **表名：** t_tccit_small_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsmalldeductamount | 小型微利企业优惠减免税额 | numeric | 23 | 10 | √ | 0.0000000000 | 小型微利企业优惠减免税额 |
| 3 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 5 | fsmalltype | 小型微利企业资质判断 | varchar | 50 |  | √ | ' ' | 小型微利企业资质判断,枚举: |
| 6 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_small_summary |  | fid |
| 2 | idx_tccit_small_summary |  | forgid,fskssqq,fskssqz |

---

## 单据体-子表 t_tccit_small_sum_entry

- **表名称：** 单据体-子表
- **表名：** t_tccit_small_sum_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemtype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | ftaxyearamount | 年度应纳税所得额（元） | numeric | 23 | 10 | √ | 0.0000000000 | 年度应纳税所得额（元） |
| 4 | ftotalamount | 资产总额（万元） | numeric | 23 | 10 | √ | 0.0000000000 | 资产总额（万元） |
| 5 | fpeople | 从业人数 | numeric | 23 | 10 | √ | 0.0000000000 | 从业人数 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_small_sum_entry |  | fentryid |
| 2 | idx_tccit_small_sum_entry_fk |  | fid |
