# 改善单号-srm_imporvebillno

## 改善单号-主表 t_pur_improve

- **表名称：** 改善单号-主表
- **表名：** t_pur_improve

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | freplydate | 要求回复时间 | timestamp | 0 |  |  | null | 要求回复时间 |
| 3 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fconfirmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待处理 B :打回 C :改善中 D :改善提交 E :改善通过 F :改善驳回 |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fother | fother | varchar | 510 |  |  | ' ' |  |
| 7 | ffinishstatus | ffinishstatus | bpchar | 1 |  | √ | ' ' |  |
| 8 | fauditstatus | fauditstatus | bpchar | 1 |  | √ | ' ' |  |
| 9 | fenddate | 要求改善完成时间 | timestamp | 0 |  |  | null | 要求改善完成时间 |
| 10 | fquality | fquality | varchar | 510 |  |  | ' ' |  |
| 11 | fsrcbillname | fsrcbillname | varchar | 80 |  | √ | ' ' |  |
| 12 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fremark | fremark | varchar | 2000 |  | √ | ' ' |  |
| 15 | fsubject | 改善主题 | varchar | 255 |  | √ | ' ' | 改善主题 |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 17 | fsupservice | fsupservice | varchar | 510 |  |  | ' ' |  |
| 18 | fexpectdate | fexpectdate | timestamp | 0 |  |  | null |  |
| 19 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 20 | fdescription | fdescription | varchar | 510 |  |  | ' ' |  |
| 21 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 23 | ffinishdate | ffinishdate | timestamp | 0 |  |  | null |  |
| 24 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 25 | fsupquality | fsupquality | varchar | 510 |  |  | ' ' |  |
| 26 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 27 | fservice | fservice | varchar | 510 |  |  | ' ' |  |
| 28 | flinkmanid | flinkmanid | int8 | 64 |  | √ | 0 |  |
| 29 | fimprovetypeid | 改善类型 | int8 | 64 |  | √ | 0 | [供应商辅助资料 srm_extdata](../pbd_files/srm_extdata.md) |
| 30 | fsupreply | fsupreply | varchar | 510 |  |  | ' ' |  |
| 31 | fsupother | fsupother | varchar | 510 |  |  | ' ' |  |
| 32 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_improve_fbillno |  | fbillno |
| 2 | t_pur_improve_pkey |  | fid |
| 3 | idx_pur_improve_fbilldate |  | fbilldate |
