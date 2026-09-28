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
| 18 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 19 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 20 | fentrychildtype | fentrychildtype | varchar | 30 |  | √ | ' ' |  |
| 21 | fqtydenominator | 基本单位用量：分母 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分母 |
| 22 | fecnvaliddate | fecnvaliddate | timestamp | 0 |  |  | null |  |
| 23 | funitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fversionid | 版本号 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fwarehouseid | fwarehouseid | int8 | 64 |  | √ | 0 |  |
| 26 | frepacetype | frepacetype | varchar | 50 |  | √ | ' ' |  |
| 27 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 28 | fsupplymode | fsupplymode | varchar | 30 |  | √ | ' ' |  |
| 29 | fismodifiable | fismodifiable | bpchar | 1 |  | √ | '0' |  |
| 30 | foutorgid | foutorgid | int8 | 64 |  | √ | 0 |  |
| 31 | ftimeunit | ftimeunit | varchar | 30 |  | √ | ' ' |  |
| 32 | fisoptional | fisoptional | bpchar | 1 |  | √ | '0' |  |
| 33 | fentrymasterid | fentrymasterid | int8 | 64 |  | √ | 0 |  |
| 34 | fisreplaceshow | fisreplaceshow | bpchar | 1 |  | √ | '0' |  |
| 35 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 36 | fsupplyorgid | fsupplyorgid | int8 | 64 |  | √ | 0 |  |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fentryecn | ECN版本 | int8 | 64 |  | √ | 0 | [ECN版本 pdm_ecnversion](../fmm_files/pdm_ecnversion.md) |
| 39 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 40 | fsupplytype | fsupplytype | varchar | 30 |  | √ | ' ' |  |
| 41 | fiskey | fiskey | bpchar | 1 |  | √ | '0' |  |
| 42 | fmaterialid | 子项编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 43 | freplacemode | freplacemode | varchar | 5 |  | √ | ' ' |  |
| 44 | fchildnumerator | fchildnumerator | numeric | 23 | 10 | √ | 0 |  |
| 45 | foperationnumber | foperationnumber | varchar | 50 |  | √ | ' ' |  |
| 46 | fleadtime | fleadtime | int8 | 64 |  | √ | 0 |  |
| 47 | fmaterialattr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 |
| 48 | foutlocationid | foutlocationid | int8 | 64 |  | √ | 0 |  |
| 49 | fentryconfigcode | fentryconfigcode | int8 | 64 |  | √ | 0 |  |
| 50 | fisreplaceplanmm | fisreplaceplanmm | bpchar | 1 |  | √ | '0' |  |
| 51 | fchildunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 52 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 53 | fqtynumerator | 基本单位用量：分子 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位用量：分子 |
| 54 | fecnno | fecnno | varchar | 50 |  | √ | ' ' |  |
| 55 | fisbackflush | fisbackflush | varchar | 30 |  | √ | ' ' |  |
| 56 | fisreplaceable | fisreplaceable | bpchar | 1 |  | √ | '0' |  |
| 57 | fprovidetype | fprovidetype | int8 | 64 |  | √ | 0 |  |
| 58 | ffixscrap | ffixscrap | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 59 | ftype | ftype | varchar | 30 |  | √ | ' ' |  |
| 60 | flocationid | flocationid | int8 | 64 |  | √ | 0 |  |
| 61 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 62 | fisstockalloc | fisstockalloc | bpchar | 1 |  | √ | '0' |  |
| 63 | freplaceplanstrategy | freplaceplanstrategy | varchar | 10 |  | √ | ' ' |  |
| 64 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 65 | fprovideorgid | fprovideorgid | int8 | 64 |  | √ | 0 |  |
| 66 | fisselectable | fisselectable | bpchar | 1 |  | √ | '0' |  |
| 67 | fauxpropertyid | fauxpropertyid | int8 | 64 |  | √ | 0 |  |
| 68 | fisbackflushnew | fisbackflushnew | varchar | 30 |  | √ | ' ' |  |
| 69 | freplaceplanid | freplaceplanid | int8 | 64 |  | √ | 0 |  |

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
