# 项目年采信息f7-src_demandf7one

## 项目年采信息f7-主表 t_src_yearinfo

- **表名称：** 项目年采信息f7-主表
- **表名：** t_src_yearinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 主单据id | int8 | 64 |  | √ | 0 | 主单据id |
| 2 | fintegerfield | fintegerfield | int8 | 64 |  | √ | 0 |  |
| 3 | funit1unit1 | funit1unit1 | int8 | 64 |  | √ | 0 |  |
| 4 | fsuppliername11 | fsuppliername11 | varchar | 50 |  | √ | ' ' |  |
| 5 | fserviceattributes1 | fserviceattributes1 | varchar | 50 |  | √ | ' ' |  |
| 6 | ftaxamount1 | ftaxamount1 | numeric | 23 | 10 | √ | 0 |  |
| 7 | freqorg11 | freqorg11 | int8 | 64 |  | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fsupplierno11 | fsupplierno11 | int8 | 64 |  | √ | 0 |  |
| 10 | freqsource1 | freqsource1 | varchar | 30 |  | √ | ' ' |  |
| 11 | flinenumber11 | flinenumber11 | varchar | 50 |  | √ | ' ' |  |
| 12 | fspecialreasonyear | fspecialreasonyear | varchar | 50 |  | √ | ' ' |  |
| 13 | fcategory3 | 品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 14 | fentrystatus1 | fentrystatus1 | varchar | 30 |  | √ | ' ' |  |
| 15 | freqdescribeyear1 | freqdescribeyear1 | varchar | 500 |  |  | ' ' |  |
| 16 | fprojectno11 | fprojectno11 | varchar | 50 |  | √ | ' ' |  |
| 17 | fprojectname11 | fprojectname11 | varchar | 50 |  | √ | ' ' |  |
| 18 | fld | fld | varchar | 50 |  | √ | ' ' |  |
| 19 | fcostattribution1 | fcostattribution1 | int8 | 64 |  | √ | 0 |  |
| 20 | fcategory3code | 品类编码 | varchar | 50 |  | √ | ' ' | 品类编码 |
| 21 | fserviceattributes | fserviceattributes | varchar | 30 |  | √ | ' ' |  |
| 22 | fcategorysmall1 | fcategorysmall1 | int8 | 64 |  | √ | 0 |  |
| 23 | fisdecision1 | fisdecision1 | varchar | 30 |  | √ | '0' |  |
| 24 | fcategorymid1 | fcategorymid1 | int8 | 64 |  | √ | 0 |  |
| 25 | fdemandnumber | fdemandnumber | int8 | 64 |  | √ | 0 |  |
| 26 | fqty2 | fqty2 | int8 | 64 |  | √ | 0 |  |
| 27 | fspecialreason11 | fspecialreason11 | varchar | 300 |  |  | ' ' |  |
| 28 | fyearswitch1 | fyearswitch1 | bpchar | 1 |  | √ | ' ' |  |
| 29 | ftype | ftype | varchar | 30 |  | √ | ' ' |  |
| 30 | funit1 | funit1 | int8 | 64 |  | √ | 0 |  |
| 31 | freqqty1 | freqqty1 | numeric | 23 | 10 | √ | 0 |  |
| 32 | fcategorybig1 | fcategorybig1 | int8 | 64 |  | √ | 0 |  |
| 33 | ftype1 | ftype1 | int8 | 64 |  | √ | 0 |  |
| 34 | fcategory3name | 品类名称 | varchar | 50 |  | √ | ' ' | 品类名称 |
| 35 | fbiginsmallld | fbiginsmallld | int8 | 64 |  | √ | 0 |  |
| 36 | fcheckboxfield | fcheckboxfield | bpchar | 1 |  | √ | ' ' |  |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fapplyno11 | fapplyno11 | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_yearinfo__fid |  | fid |
| 2 | pk_src_yearinfo |  | fentryid |
| 3 | idx_src_yearinfo_applyno |  | fapplyno11 |
