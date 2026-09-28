# 模拟组织间需求单-mrp_simcolorder

## 模拟组织间需求单-主表 t_mrp_simcolorder

- **表名称：** 模拟组织间需求单-主表
- **表名：** t_mrp_simcolorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbomversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 3 | fplanprogram | 计划方案 | int8 | 64 |  | √ | 0 | 计划方案 mrp_planscheme |
| 4 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 6 | fmaterielid | 物料主档 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fbaseunit | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdemanddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 10 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fplantags | 计划标识 | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
| 13 | fplanoperatenum | 计划运算号 | varchar | 50 |  | √ | ' ' | 计划运算号 |
| 14 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 15 | fbasedemandqty | 基本单位净需求数量 | numeric | 23 | 10 | √ | 0 | 基本单位净需求数量 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fmaterialplanid | 物料编码 | int8 | 64 |  | √ | 0 | 物料计划信息 mpdm_materialplan |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fismpsonly | 只算MPS | bpchar | 1 |  | √ | '0' | 只算MPS |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 |
| 25 | fdemandqty | 基本单位需求数量 | numeric | 23 | 10 | √ | 0 | 基本单位需求数量 |
| 26 | fsupplyorgid | 接收组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_simcolorder |  | fid |
| 2 | idx_mrp_simcolorder |  | forgid,fbillno |
