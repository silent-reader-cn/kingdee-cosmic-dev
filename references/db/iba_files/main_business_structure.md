# 主营结构表-main_business_structure

## 主营结构表-主表 t_iba_mbusiness_structure

- **表名称：** 主营结构表-主表
- **表名：** t_iba_mbusiness_structure

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
| 9 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fperiod | 期 | int4 | 32 |  | √ | 1 | 期 |
| 12 | fcycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位,枚举: 1 :元 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_mbusiness_structure |  | fid |
| 2 | idx_iba_mbusiness_structure |  | fipoorg |

---

## 结构明细-子表 t_iba_structure_detail

- **表名称：** 结构明细-子表
- **表名：** t_iba_structure_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgrossmargin | 毛利率 | numeric | 23 | 10 |  | null | 毛利率 |
| 3 | fincomecomposition | 收入构成 | numeric | 23 | 10 |  | null | 收入构成 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcostcomposition | 成本构成 | numeric | 23 | 10 |  | null | 成本构成 |
| 6 | fincomeratio | 收入占比 | numeric | 23 | 10 |  | null | 收入占比 |
| 7 | fgpratio | 毛利占比 | numeric | 23 | 10 |  | null | 毛利占比 |
| 8 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: 0 :按产品 1 :按行业 2 :按地区 |
| 9 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 10 | fgpcomposition | 毛利构成 | numeric | 23 | 10 |  | null | 毛利构成 |
| 11 | fcostratio | 成本占比 | numeric | 23 | 10 |  | null | 成本占比 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fproductname | 产品名称 | varchar | 50 |  | √ | ' ' | 产品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iba_structure_detail_fk |  | fid |
| 2 | pk_iba_structure_detail |  | fentryid |
