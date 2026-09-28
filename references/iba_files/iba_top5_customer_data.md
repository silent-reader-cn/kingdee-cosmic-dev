# 收入前五客户表-iba_top5_customer_data

## 结构明细-子表 t_customer_data_detail

- **表名称：** 结构明细-子表
- **表名：** t_customer_data_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomer_name | 客户名称 | varchar | 50 |  | √ | ' ' | 客户名称 |
| 3 | frate | 占年度销售额比例 | numeric | 30 | 10 | √ | 0 | 占年度销售额比例 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fitem_number | 排名 | varchar | 50 |  | √ | ' ' | 排名,枚举: customer_01 :第1名 customer_02 :第2名 customer_03 :第3名 customer_04 :第4名 customer_05 :第5名 total :前五客户合计 |
| 6 | famount | 销售额 | numeric | 30 | 10 | √ | 0 | 销售额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_customer_data_detail_fk |  | fid |
| 2 | pk_t_customer_data_detail |  | fentryid |

---

## 收入前五客户表-主表 t_iba_top5_customer_data

- **表名称：** 收入前五客户表-主表
- **表名：** t_iba_top5_customer_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotal_income | 营业总收入 | numeric | 30 | 10 | √ | 0 | 营业总收入 |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fipoorg | 编制组织 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 9 | fsourcetype | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: 1 :手工引入 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 12 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 13 | fcycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 14 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 15 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位,枚举: 1 :元 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iba_top5_customer_data |  | fid |
| 2 | idx_iba_top5_customer_data |  | fipoorg |
