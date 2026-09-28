# 工程变更单分录F7-pdm_bom_eco_entryf7

## 工程变更单分录F7-主表 t_pdm_bomecopentry

- **表名称：** 工程变更单分录F7-主表
- **表名：** t_pdm_bomecopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 工程变更单F7 | int8 | 64 |  | √ | 0 | [工程变更单F7 pdm_bom_eco_headf7](../pdm_files/pdm_bom_eco_headf7.md) |
| 2 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 3 | fecn | fecn | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fiscoproduct | fiscoproduct | bpchar | 1 |  | √ | '0' |  |
| 6 | fyieldrate | fyieldrate | numeric | 23 | 10 | √ | 0 |  |
| 7 | fchangetype | 变更类型 | varchar | 5 |  | √ | ' ' | 变更类型,枚举: A :立即变更 B :用完旧料 C :指定日期变更 |
| 8 | fmftbomid | fmftbomid | varchar | 50 |  | √ | ' ' |  |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 10 | febomid | febomid | varchar | 50 |  | √ | ' ' |  |
| 11 | fproentrymaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 12 | fisretainrepmat | fisretainrepmat | bpchar | 1 |  | √ | '0' |  |
| 13 | fisparticipatedeval | 已参与变更评估 | bpchar | 1 |  | √ | '0' | 已参与变更评估 |
| 14 | foldversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fvaliddate | fvaliddate | timestamp | 0 |  |  | null |  |
| 16 | fecreasonid | 变更原因 | int8 | 64 |  | √ | 0 | [变更原因 pdm_ecnreason](../pdm_files/pdm_ecnreason.md) |
| 17 | fexecmode | fexecmode | varchar | 30 |  | √ | ' ' |  |
| 18 | fentryversioncontrol | 生成新BOM | varchar | 30 |  | √ | ' ' | 生成新BOM,枚举: B :是 A :否 |
| 19 | fplmecnentryid | fplmecnentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fecnversionid | fecnversionid | int8 | 64 |  | √ | 0 |  |
| 21 | fexecdate | fexecdate | timestamp | 0 |  |  | null |  |
| 22 | fbomuse | fbomuse | varchar | 36 |  | √ | ',A,B,C,D,' |  |
| 23 | fspecifynewbomnum | fspecifynewbomnum | varchar | 100 |  | √ | ' ' |  |
| 24 | fnewversionid | fnewversionid | int8 | 64 |  | √ | 0 |  |
| 25 | fnewbom | fnewbom | int8 | 64 |  | √ | 0 |  |
| 26 | fexecstatus | fexecstatus | varchar | 30 |  | √ | ' ' |  |
| 27 | fbomauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | fecoapplybillno | fecoapplybillno | varchar | 50 |  | √ | '' |  |
| 29 | fecobomid | 变更BOMID | int8 | 64 |  | √ | 0 | 变更BOMID |
| 30 | fisdisableoldbom | 禁用旧BOM | bpchar | 1 |  | √ | '0' | 禁用旧BOM |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pdm_bomecopentry |  | fentryid |
| 2 | idx_pdm_bomecopentry_fid |  | fid |
