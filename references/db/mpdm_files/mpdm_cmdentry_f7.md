# 工卡物料需求分录F7-mpdm_cmdentry_f7

## 工卡物料需求分录F7-主表 t_mpdm_cmaterialcmdentry

- **表名称：** 工卡物料需求分录F7-主表
- **表名：** t_mpdm_cmaterialcmdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | parentid | int8 | 64 |  | √ | 0 | parentid |
| 2 | fentrybaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | finvaliddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fsupplyorg | fsupplyorg | int8 | 64 |  | √ | 0 |  |
| 5 | fentryownertype | fentryownertype | varchar | 50 |  | √ | ' ' |  |
| 6 | flocation | flocation | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 8 | foutlocation | foutlocation | int8 | 64 |  | √ | 0 |  |
| 9 | fisrequireqtyset | fisrequireqtyset | bpchar | 1 |  | √ | '0' |  |
| 10 | ffissuemode | ffissuemode | varchar | 50 |  | √ | ' ' |  |
| 11 | fentryprofessionaid | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 12 | fentryqty | fentryqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | fentrymaterial | 物料编码(隐藏) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 14 | fisreplacement | fisreplacement | bpchar | 1 |  | √ | '0' |  |
| 15 | fvaliddate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 16 | fentryresptype | fentryresptype | varchar | 50 |  | √ | ' ' |  |
| 17 | fmaterialattr | 物料属性 | varchar | 50 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :虚拟 10020 :委外 |
| 18 | fparamremark | fparamremark | varchar | 255 |  | √ | ' ' |  |
| 19 | fentryresp | fentryresp | int8 | 64 |  | √ | 0 |  |
| 20 | fisbackflush | fisbackflush | varchar | 50 |  | √ | ' ' |  |
| 21 | foutwarehouse | foutwarehouse | int8 | 64 |  | √ | 0 |  |
| 22 | fentryiskey | fentryiskey | bpchar | 1 |  | √ | '0' |  |
| 23 | fisentryqtylimit | fisentryqtylimit | bpchar | 1 |  | √ | '0' |  |
| 24 | fwarehouse | fwarehouse | int8 | 64 |  | √ | 0 |  |
| 25 | foutorg | foutorg | int8 | 64 |  | √ | 0 |  |
| 26 | fisstockalloc | fisstockalloc | bpchar | 1 |  | √ | '0' |  |
| 27 | fmaterialmftid | 组件编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 28 | fcabinconfigsen | fcabinconfigsen | bpchar | 1 |  | √ | '0' |  |
| 29 | fentrylimittop | fentrylimittop | numeric | 23 | 10 | √ | 0 |  |
| 30 | fcardoperationnoid | fcardoperationnoid | int8 | 64 |  | √ | 0 |  |
| 31 | fentrytype | 组件类型 | varchar | 50 |  | √ | ' ' | 组件类型,枚举: |
| 32 | fmaterielmtc | fmaterielmtc | int8 | 64 |  | √ | 0 |  |
| 33 | fentryunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fentryowner | fentryowner | int8 | 64 |  | √ | 0 |  |
| 35 | fentryremark | fentryremark | varchar | 255 |  | √ | ' ' |  |
| 36 | fbaseqty | fbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fentrylimitlow | fentrylimitlow | numeric | 23 | 10 | √ | 0 |  |
| 38 | fentryid | entryid | int8 | 64 |  | √ | 0 | entryid |
| 39 | fentrysn | fentrysn | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cmaterialcmdentry_mid |  | fentrymaterial |
| 2 | pk_mpdm_cmaterialcmdentry |  | fentryid |
| 3 | idx_cmaterialcmdentry_mft |  | fmaterialmftid |
| 4 | idx_mpdm_cmaterialcmdentry_fk |  | fid |
