# 研发费用明细表-iba_rdexpense

## 研发费用明细表-主表 t_iba_rdexpense

- **表名称：** 研发费用明细表-主表
- **表名：** t_iba_rdexpense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fipoorg | 编制组织 | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | freportdate | 报告期 | timestamp | 0 |  |  | null | 报告期 |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 8 | fsourcetype | 来源方式 | varchar | 50 |  | √ | ' ' | 来源方式,枚举: 1 :手工引入 |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 11 | fperiod | 期 | int4 | 32 |  | √ | 0 | 期 |
| 12 | fcycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位,枚举: 1 :人民币/元 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_rdexpense |  | fid |
| 2 | idx_pk_iba_rdexpense |  | fnumber |

---

## 单据体-子表 t_rdexpense_detail

- **表名称：** 单据体-子表
- **表名：** t_rdexpense_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue | 研发费用 | numeric | 23 | 10 |  | null | 研发费用 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fquota | 指标 | int8 | 64 |  | √ | 0 | 指标库 ipo_quota_info |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdexpense_detail_fk |  | fquota |
| 2 | pk_rdexpense_detail |  | fentryid |
