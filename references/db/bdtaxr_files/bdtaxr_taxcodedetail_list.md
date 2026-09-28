# 税码结果明细弹窗列表-bdtaxr_taxcodedetail_list

## 税码结果明细弹窗列表-主表 t_bdtaxr_taxcode_detail

- **表名称：** 税码结果明细弹窗列表-主表
- **表名：** t_bdtaxr_taxcode_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintervalstartdate | 区间开始日期 | timestamp | 0 |  |  | null | 区间开始日期 |
| 3 | fintervalenddate | 区间结束日期 | timestamp | 0 |  |  | null | 区间结束日期 |
| 4 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 5 | ftaxbaseamount | 对应税基 | numeric | 23 | 10 | √ | 0 | 对应税基 |
| 6 | ftaxcodetype | 税码结果类型 | int8 | 64 |  | √ | 0 | [税码明细结果类型 bastax_code_detailstype](../bastax_files/bastax_code_detailstype.md) |
| 7 | fresultsource | fresultsource | varchar | 36 |  | √ | ' ' |  |
| 8 | fdays | 交集期间天数 | int8 | 64 |  | √ | 0 | 交集期间天数 |
| 9 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | fsumintervalamount | 各区间税额合计 | numeric | 23 | 10 | √ | 0 | 各区间税额合计 |
| 11 | ftaxratetype | 税率类型 | int8 | 64 |  | √ | 0 | [税率类型 bd_taxratetype](../basedata_files/bd_taxratetype.md) |
| 12 | ftotaldays | 总天数 | int8 | 64 |  | √ | 0 | 总天数 |
| 13 | fresultnumber | 结果编码 | varchar | 120 |  | √ | ' ' | 结果编码 |
| 14 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 15 | fresultname | 结果名称 | varchar | 200 |  | √ | ' ' | 结果名称 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fproportion | 总天数占比 | numeric | 23 | 10 | √ | 0 | 总天数占比 |
| 18 | fresultid | fresultid | varchar | 200 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_taxcode_detail_fk |  | fid |
| 2 | pk_bdtaxr_taxcode_detail |  | fentryid |

---

## 单据体-子表 t_bdtaxr_taxcode_sdetail

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_taxcode_sdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fintervalamount | 适用税基 | numeric | 23 | 10 | √ | 0 | 适用税基 |
| 2 | fintervaltaxrate | 适用税率 | numeric | 23 | 10 | √ | 0 | 适用税率 |
| 3 | fintervaltaxamount | 各区间税额 | numeric | 23 | 10 | √ | 0 | 各区间税额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | finterval | 区间 | varchar | 200 |  | √ | ' ' | 区间 |
| 8 | fintervaljson | fintervaljson | varchar | 255 |  | √ | ' ' |  |
| 9 | fintervaljson_tag | fintervaljson_tag | text | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_taxcode_sdetail |  | fdetailid |
| 2 | idx_bdtaxr_taxcode_sdetail_fk |  | fentryid |
