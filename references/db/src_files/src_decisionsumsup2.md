# 中标金额汇总分录(MOV)-src_decisionsumsup2

## 中标金额汇总分录(MOV)-主表 t_src_decisionsumsup2

- **表名称：** 中标金额汇总分录(MOV)-主表
- **表名：** t_src_decisionsumsup2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | frank | frank | int8 | 64 |  | √ | 0 |  |
| 3 | fmaxamount | 标杆未税金额 | numeric | 23 | 10 | √ | 0 | 标杆未税金额 |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fresult | 是否中标 | varchar | 30 |  | √ | ' ' | 是否中标,枚举: 1 :中标 2 :未中标 3 :预中标 |
| 6 | famount | 中标未税金额 | numeric | 23 | 10 | √ | 0 | 中标未税金额 |
| 7 | fpackageid | 标段 | int8 | 64 |  | √ | 0 | [标段名称 src_packagef7](../src_files/src_packagef7.md) |
| 8 | fpreorderratio1 | 预定标含税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标含税占比(%) |
| 9 | fcategoryid | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 10 | floctaxamount | 报价含税金额 | numeric | 23 | 10 | √ | 0 | 报价含税金额 |
| 11 | fpreorderratio | 预定标未税占比(%) | numeric | 23 | 10 | √ | 0 | 预定标未税占比(%) |
| 12 | forderratio | 中标未税占比(%) | numeric | 23 | 10 | √ | 0 | 中标未税占比(%) |
| 13 | fbudgetamount | 预估含税采购金额 | numeric | 23 | 10 | √ | 0 | 预估含税采购金额 |
| 14 | fpreamount | 预定标未税金额 | numeric | 23 | 10 | √ | 0 | 预定标未税金额 |
| 15 | ftaxamountrate | 含税价差率(%) | numeric | 23 | 10 | √ | 0 | 含税价差率(%) |
| 16 | fpretaxamount | 预定标含税金额 | numeric | 23 | 10 | √ | 0 | 预定标含税金额 |
| 17 | fcontracttype | 签约属性 | bpchar | 1 |  | √ | ' ' | 签约属性,枚举: 1 :2方 2 :3方 3 :4方 |
| 18 | ftaxamount | 中标含税金额 | numeric | 23 | 10 | √ | 0 | 中标含税金额 |
| 19 | famountrate | 未税价差率(%) | numeric | 23 | 10 | √ | 0 | 未税价差率(%) |
| 20 | fphone | 手机号 | varchar | 50 |  | √ | ' ' | 手机号 |
| 21 | fmaxtaxamount | 标杆含税金额 | numeric | 23 | 10 | √ | 0 | 标杆含税金额 |
| 22 | fprojectid | 寻源项目 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 23 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 24 | femail | 邮箱 | varchar | 50 |  | √ | ' ' | 邮箱 |
| 25 | fbidcount | 中标标的数 | int4 | 32 |  | √ | 0 | 中标标的数 |
| 26 | fcontractamount | 签约中标未税金额 | numeric | 23 | 10 | √ | 0 | 签约中标未税金额 |
| 27 | fpackagename | fpackagename | varchar | 50 |  | √ | ' ' |  |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 29 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 bos_user :人员 src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 30 | flocamount | 报价未税金额 | numeric | 23 | 10 | √ | 0 | 报价未税金额 |
| 31 | ftaxamountdiff | 含税价差 | numeric | 23 | 10 | √ | 0 | 含税价差 |
| 32 | fcontracttaxamount | 签约中标含税金额 | numeric | 23 | 10 | √ | 0 | 签约中标含税金额 |
| 33 | famountdiff | 未税价差 | numeric | 23 | 10 | √ | 0 | 未税价差 |
| 34 | flinkman | 联系人 | varchar | 50 |  | √ | ' ' | 联系人 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | forderratio1 | 中标含税占比(%) | numeric | 23 | 10 | √ | 0 | 中标含税占比(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_decisionsumsup2_fpid |  | fparentid |
| 2 | pk_src_decisionsumsup2 |  | fentryid |
| 3 | idx_src_decisionsumsup2_fpag |  | fpackageid |
| 4 | idx_src_decisionsumsup2_fid |  | fid |
| 5 | idx_src_decisionsumsup2_fcid |  | fcategoryid |
| 6 | idx_src_decisionsumsup2_fsup |  | fsupplierid |
| 7 | idx_src_decisionsumsup2_fpro |  | fprojectid |
