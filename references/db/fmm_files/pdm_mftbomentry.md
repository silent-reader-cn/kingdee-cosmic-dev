# BOM子项分录-pdm_mftbomentry

## BOM子项分录-主表 t_pdm_mftbomentry

- **表名称：** BOM子项分录-主表
- **表名：** t_pdm_mftbomentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 表头ID | int8 | 64 |  | √ | 0 | 表头ID |
| 2 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 3 | fissuemode | fissuemode | varchar | 30 |  | √ | ' ' |  |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | freppriority | freppriority | int8 | 64 |  | √ | 0 |  |
| 6 | fscraprate | fscraprate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fecnverion | fecnverion | varchar | 50 |  | √ | ' ' |  |
| 8 | foperatemrp | foperatemrp | varchar | 30 |  | √ | ' ' |  |
| 9 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 10 | fchilddenominator | fchilddenominator | numeric | 23 | 10 | √ | 0 |  |
| 11 | fplmbomentryid | fplmbomentryid | int8 | 64 |  | √ | 0 |  |
| 12 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 13 | fentryecnid | fentryecnid | varchar | 100 |  | √ | ' ' |  |
| 14 | fentrymatid | fentrymatid | int8 | 64 |  | √ | 0 |  |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 16 | fvaliddate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 17 | fisjumplevel | fisjumplevel | bpchar | 1 |  | √ | '0' |  |
| 18 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 19 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fentrychildtype | fentrychildtype | varchar | 30 |  | √ | ' ' |  |
| 21 | fqtydenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分母 |
| 22 | fecnvaliddate | fecnvaliddate | timestamp | 0 |  |  | null |  |
| 23 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 25 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 26 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 27 | fsupplymode | fsupplymode | varchar | 30 |  | √ | ' ' |  |
| 28 | fismodifiable | fismodifiable | bpchar | 1 |  | √ | '0' |  |
| 29 | foutorgid | foutorgid | int8 | 64 |  | √ | 0 |  |
| 30 | ftimeunit | ftimeunit | varchar | 30 |  | √ | ' ' |  |
| 31 | fisoptional | fisoptional | bpchar | 1 |  | √ | '0' |  |
| 32 | fisreplaceshow | fisreplaceshow | bpchar | 1 |  | √ | '0' |  |
| 33 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 34 | fsupplyorgid | fsupplyorgid | int8 | 64 |  | √ | 0 |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fentryecn | ECN版本 | int8 | 64 |  | √ | 0 | ECN版本 pdm_ecnversion |
| 37 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 38 | fsupplytype | fsupplytype | varchar | 30 |  | √ | ' ' |  |
| 39 | fiskey | fiskey | bpchar | 1 |  | √ | '0' |  |
| 40 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 41 | freplacemode | freplacemode | varchar | 5 |  | √ | ' ' |  |
| 42 | fchildnumerator | fchildnumerator | numeric | 23 | 10 | √ | 0 |  |
| 43 | foperationnumber | foperationnumber | varchar | 50 |  | √ | ' ' |  |
| 44 | fleadtime | fleadtime | int8 | 64 |  | √ | 0 |  |
| 45 | fmaterialattr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |
| 46 | foutlocationid | foutlocationid | int8 | 64 |  | √ | 0 |  |
| 47 | fentryconfigcode | fentryconfigcode | int8 | 64 |  | √ | 0 |  |
| 48 | fisreplaceplanmm | fisreplaceplanmm | bpchar | 1 |  | √ | '0' |  |
| 49 | fchildunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 50 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 51 | fqtynumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分子 |
| 52 | fecnno | fecnno | varchar | 50 |  | √ | ' ' |  |
| 53 | fisbackflush | fisbackflush | varchar | 30 |  | √ | ' ' |  |
| 54 | fisreplaceable | fisreplaceable | bpchar | 1 |  | √ | '0' |  |
| 55 | fprovidetype | fprovidetype | int8 | 64 |  | √ | 0 |  |
| 56 | ffixscrap | ffixscrap | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 57 | ftype | ftype | varchar | 30 |  | √ | ' ' |  |
| 58 | flocationid | flocationid | int8 | 64 |  | √ | 0 |  |
| 59 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 60 | fisstockalloc | fisstockalloc | bpchar | 1 |  | √ | '0' |  |
| 61 | freplaceplanstrategy | freplaceplanstrategy | varchar | 10 |  | √ | ' ' |  |
| 62 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 63 | fprovideorgid | fprovideorgid | int8 | 64 |  | √ | 0 |  |
| 64 | fisselectable | fisselectable | bpchar | 1 |  | √ | '0' |  |
| 65 | fauxpropertyid | fauxpropertyid | int8 | 64 |  | √ | 0 |  |
| 66 | fisbackflushnew | fisbackflushnew | varchar | 30 |  | √ | ' ' |  |
| 67 | freplaceplanid | freplaceplanid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_mftbomentry_fid |  | fid |
| 2 | idx_pdm_mftbomentry_m1 |  | fmaterialid |
| 3 | t_pdm_mftbomentry_pkey |  | fentryid |
| 4 | idx_pdm_mftbomentry_c2 |  | fid,finvaliddate |
| 5 | idx_pdm_mftbomentry_c1 |  | fid,fvaliddate,finvaliddate |
| 6 | idx_pdm_mftbomentry_c3 |  | fid,finvaliddate,fissuemode |
