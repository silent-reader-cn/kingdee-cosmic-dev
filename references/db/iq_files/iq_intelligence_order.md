# 智测测评单-iq_intelligence_order

## 智测测评单-主表 t_iq_intelligence_order

- **表名称：** 智测测评单-主表
- **表名：** t_iq_intelligence_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmarket_plate_type | 上市板块 | varchar | 50 |  | √ | ' ' | 上市板块,枚举: HZB :上交所主板 KCB :科创板 SZB :深交所主板 CYB :创业板 BJS :北交所 |
| 3 | fipoorgname | IPO主体名称(固化) | varchar | 50 |  | √ | ' ' | IPO主体名称(固化) |
| 4 | fhadbuildnum | 已生成报告次数 | int4 | 32 |  | √ | 0 | 已生成报告次数 |
| 5 | fipo_org | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 6 | fperiodstartyear | 三年财务数据开始年份 | int8 | 64 |  | √ | 2020 | 三年财务数据开始年份 |
| 7 | findustrytype | 行业类型(固化) | int8 | 64 |  | √ | 0 | [证监会行业 csrc_industry_info](../ipobase_files/csrc_industry_info.md) |
| 8 | freportcurperiod | 报告当年期 | int8 | 64 |  | √ | 12 | 报告当年期 |
| 9 | fcompany_type | 企业类型 | varchar | 50 |  | √ | ' ' | 企业类型,枚举: YBQY :一般企业 BJQCY :表决权差异 HCQYW :红筹企业（境外未上市） HCQYY :红筹企业（境外已上市） |
| 10 | fupdatetime | 测评更新时间 | timestamp | 0 |  |  | null | 测评更新时间 |
| 11 | fop_user | 测评人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fnicestandardnum | 最佳标准号 | int8 | 64 |  | √ | 0 | 最佳标准号 |
| 13 | freportcycle | 周期 | varchar | 50 |  | √ | '4' | 周期,枚举: 4 :月报 5 :季报 6 :半年报 7 :年报 |
| 14 | fop_time | 测评创建时间 | timestamp | 0 |  |  | null | 测评创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_org_evaluate |  | fipo_org,fmarket_plate_type,fcompany_type |
| 2 | pk_iq_intelligence_order |  | fid |

---

## 标准结果-子表 t_iq_intelligence_o_std

- **表名称：** 标准结果-子表
- **表名：** t_iq_intelligence_o_std

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhardquotapassnum | 硬指标通过数 | int8 | 64 |  | √ | 0 | 硬指标通过数 |
| 3 | fhardquotatotalnum | 硬指标总数 | int8 | 64 |  | √ | 0 | 硬指标总数 |
| 4 | fstandardnum | 标准号 | int8 | 64 |  | √ | 0 | 标准号 |
| 5 | fpass | 是否通过 | int8 | 64 |  | √ | 0 | 是否通过 |
| 6 | fquotapassnum | 指标通过数 | int8 | 64 |  | √ | 0 | 指标通过数 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsatisfyratio | 满足度 | numeric | 23 | 10 |  | null | 满足度 |
| 10 | fquotatotalnum | 指标总数 | int8 | 64 |  | √ | 0 | 指标总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iq_intelligence_o_std |  | fentryid |
| 2 | index_order_standardnum |  | fstandardnum |
