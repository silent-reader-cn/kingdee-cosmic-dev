# 物料试用单号-srm_materialbillno

## 物料试用单号-主表 t_pur_material

- **表名称：** 物料试用单号-主表
- **表名：** t_pur_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 4 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 7 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 9 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 10 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 |
| 11 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 12 | fcertifiapplyid | fcertifiapplyid | int8 | 64 |  | √ | 0 |  |
| 13 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 14 | ftype | ftype | bpchar | 1 |  | √ | '1' |  |
| 15 | ftryresult | ftryresult | bpchar | 1 |  | √ | ' ' |  |
| 16 | faptitudenoid | 资审单号 | int8 | 64 |  | √ | 0 | [资质审查单号 srm_aptitudebillno](../srm_files/srm_aptitudebillno.md) |
| 17 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_material_fbilldate |  | fbilldate |
| 2 | idx_pur_material_fbillno |  | fbillno |
| 3 | idx_pur_material_aptitudeid |  | faptitudenoid |
| 4 | t_pur_material_pkey |  | fid |
