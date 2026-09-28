# 工程变更申请单分录F7-pdm_bom_ecoapply_entryf7

## 工程变更申请单分录F7-主表 t_pdm_bomecoapplyentry

- **表名称：** 工程变更申请单分录F7-主表
- **表名：** t_pdm_bomecoapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 工程变更申请单F7 | int8 | 64 |  | √ | 1 | [工程变更申请单F7 pdm_bom_ecoapply_headf7](../pdm_files/pdm_bom_ecoapply_headf7.md) |
| 2 | fremark | 备注 | varchar | 2000 |  |  | null | 备注 |
| 3 | fchangeorgid | 变更组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 1 | 分录行号 |
| 5 | fmaterialversion | 物料版本 | int8 | 64 |  |  | null | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | forbiddenoldbom | 禁用BOM | bpchar | 1 |  |  | null | 禁用BOM |
| 7 | fchangetype | 变更类型 | varchar | 5 |  | √ | ' ' | 变更类型,枚举: A :立即变更 B :用完旧料 C :指定日期变更 |
| 8 | flinkchange | 已关联变更单 | bpchar | 1 |  |  | null | 已关联变更单 |
| 9 | fecobillno | 工程变更单 | varchar | 50 |  |  | null | 工程变更单 |
| 10 | fbom | BOM编码 | int8 | 64 |  |  | null | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 11 | fecobomid | fecobomid | int8 | 64 |  | √ | 0 |  |
| 12 | fentryreasonid | 变更原因 | int8 | 64 |  |  | null | [变更原因 pdm_ecnreason](../pdm_files/pdm_ecnreason.md) |
| 13 | fisparticipatedeval | 已参与变更评估 | bpchar | 1 |  | √ | '0' | 已参与变更评估 |
| 14 | fmaterial | 物料编码 | int8 | 64 |  |  | null | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 15 | fauxpropertyid | 辅助属性 | int8 | 64 |  |  | null | null 001 |
| 16 | flinestatus | 行状态 | bpchar | 1 |  |  | null | 行状态,枚举: A :未关闭 B :已关闭 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 1 | id |
| 18 | fversioncontrol | 生成新BOM | bpchar | 1 |  |  | null | 生成新BOM,枚举: B :是 A :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pdm_bomecoappent_material |  | fmaterial |
| 2 | pk_pdm_bomecoapplyentry |  | fentryid |
| 3 | idx_pdm_bomecoappentry_id_seq |  | fid |
