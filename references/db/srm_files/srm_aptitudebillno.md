# 资质审查单号-srm_aptitudebillno

## 资质审查单号-主表 t_pur_aptitude

- **表名称：** 资质审查单号-主表
- **表名：** t_pur_aptitude

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 2 | fgroupid | fgroupid | int8 | 64 |  | √ | 0 |  |
| 3 | ftaxrate | ftaxrate | numeric | 19 | 6 | √ | 0.000000 |  |
| 4 | forgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fentertypeid | 准入类型 | int8 | 64 |  | √ | 0 | 准入类型 srm_biztype |
| 6 | fhassample | 已样品确认 | bpchar | 1 |  | √ | ' ' | 已样品确认 |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fisapprove | 需要供应商生效 | bpchar | 1 |  | √ | '0' | 需要供应商生效 |
| 9 | fhasmaterial | 已物料试用 | bpchar | 1 |  | √ | ' ' | 已物料试用 |
| 10 | fauditstatus | 审批状态 | bpchar | 1 |  | √ | ' ' | 审批状态,枚举: A :拟定 B :提交审批 C :审批通过 D :审批驳回 E :已完成 |
| 11 | fbiztype | fbiztype | bpchar | 1 |  | √ | ' ' |  |
| 12 | fisautopush | fisautopush | bpchar | 1 |  | √ | '1' |  |
| 13 | fispurorg | fispurorg | bpchar | 1 |  | √ | ' ' |  |
| 14 | fischgflow | fischgflow | bpchar | 1 |  | √ | ' ' |  |
| 15 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 16 | fisscene | 需要现场评审 | bpchar | 1 |  | √ | '0' | 需要现场评审 |
| 17 | fhasapprove | 已供应商生效 | bpchar | 1 |  | √ | ' ' | 已供应商生效 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 20 | fcurrid | fcurrid | int8 | 64 |  | √ | 0 |  |
| 21 | fhasscene | 已现场评审 | bpchar | 1 |  | √ | ' ' | 已现场评审 |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已作废 |
| 23 | fpaycondid | fpaycondid | int8 | 64 |  | √ | 0 |  |
| 24 | fisshopmall | 允许入驻商城 | bpchar | 1 |  | √ | ' ' | 允许入驻商城 |
| 25 | fresultremark | fresultremark | text | 0 |  |  | ' ' |  |
| 26 | fissample | 需要样品确认 | bpchar | 1 |  | √ | '0' | 需要样品确认 |
| 27 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 28 | fbizpartnerid | fbizpartnerid | int8 | 64 |  | √ | 0 |  |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 srm_supplier |
| 30 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 31 | fsettletypeid | fsettletypeid | int8 | 64 |  | √ | 0 |  |
| 32 | fcfmstatus | fcfmstatus | bpchar | 1 |  | √ | ' ' |  |
| 33 | fiscategory | fiscategory | bpchar | 1 |  | √ | ' ' |  |
| 34 | fcertifiapplyid | fcertifiapplyid | int8 | 64 |  | √ | 0 |  |
| 35 | fexamresult | 资审结果 | bpchar | 1 |  | √ | ' ' | 资审结果,枚举: 0 :通过 1 :不通过 |
| 36 | ftype | ftype | bpchar | 1 |  | √ | '1' |  |
| 37 | fismaterial | 需要物料试用 | bpchar | 1 |  | √ | '0' | 需要物料试用 |
| 38 | fissuppcolla | 启用协同 | bpchar | 1 |  | √ | '0' | 启用协同 |
| 39 | fnextauditor | fnextauditor | varchar | 100 |  | √ | ' ' |  |
| 40 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_aptitude_fbillno |  | fbillno |
| 2 | t_pur_aptitude_pkey |  | fid |
| 3 | idx_pur_aptitude_fbilldate |  | fbilldate |
