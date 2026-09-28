# 现场评审单号-srm_scenebillno

## 现场评审单号-主表 t_pur_scene

- **表名称：** 现场评审单号-主表
- **表名：** t_pur_scene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fcaapplyid | fcaapplyid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsuplinkmobile | fsuplinkmobile | varchar | 255 |  | √ | ' ' |  |
| 5 | fschemeid | fschemeid | int8 | 64 |  | √ | 0 |  |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fsceneresult | 现场评审结论 | bpchar | 1 |  | √ | ' ' | 现场评审结论,枚举: 1 :通过 4 :不通过 3 :整改复评 |
| 8 | fevaplanbatchbillno | fevaplanbatchbillno | varchar | 100 |  | √ | ' ' |  |
| 9 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 |
| 10 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 11 | fsuplinkemail | fsuplinkemail | varchar | 255 |  | √ | ' ' |  |
| 12 | fchargeman | fchargeman | int8 | 64 |  | √ | 0 |  |
| 13 | fscenescore | fscenescore | numeric | 19 | 6 | √ | 0.000000 |  |
| 14 | fapplytype | fapplytype | bpchar | 1 |  | √ | '1' |  |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fscenenoid | fscenenoid | int8 | 64 |  | √ | 0 |  |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 19 | fsupplierlinkman | fsupplierlinkman | varchar | 255 |  | √ | ' ' |  |
| 20 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 21 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 srm_supplier](../srm_files/srm_supplier.md) |
| 23 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 24 | ffinishdate | ffinishdate | timestamp | 0 |  |  | LOCALTIMESTAMP |  |
| 25 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 26 | fscoremethod | fscoremethod | varchar | 30 |  | √ | 'offline' |  |
| 27 | fevaplanbatchid | fevaplanbatchid | varchar | 80 |  | √ | ' ' |  |
| 28 | fchargemanid | fchargemanid | int8 | 64 |  | √ | 0 |  |
| 29 | fbillstatusfield | fbillstatusfield | bpchar | 1 |  | √ | ' ' |  |
| 30 | fscenenote | fscenenote | varchar | 255 |  | √ | ' ' |  |
| 31 | fexamtype | fexamtype | bpchar | 1 |  | √ | ' ' |  |
| 32 | faptitudenoid | 资审单号 | int8 | 64 |  | √ | 0 | [资质审查单号 srm_aptitudebillno](../srm_files/srm_aptitudebillno.md) |
| 33 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 34 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_scene_fbilldate |  | fbilldate |
| 2 | idx_pur_scene_aptitudeid |  | faptitudenoid |
| 3 | idx_pur_scene_fbillno |  | fbillno |
| 4 | t_pur_scene_pkey |  | fid |
