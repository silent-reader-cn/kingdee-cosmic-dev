# 组织间需求单-mrp_collaborativeorder

## 组织间需求单-主表 t_mrp_rativeorder

- **表名称：** 组织间需求单-主表
- **表名：** t_mrp_rativeorder

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
| 10 | fdemandbillentryid | 需求单据分录ID | varchar | 50 |  | √ | ' ' | 需求单据分录ID |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fenddate | 确认到货完工日期 | timestamp | 0 |  |  | null | 确认到货完工日期 |
| 13 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | finwardept | 入库组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fismrpcal | 已计划运算 | bpchar | 1 |  | √ | '0' | 已计划运算 |
| 17 | fdemandbillno | 需求单据编码 | varchar | 80 |  | √ | ' ' | 需求单据编码 |
| 18 | fbaseremainqty | 基本剩余需求数量 | numeric | 23 | 10 | √ | 0 | 基本剩余需求数量 |
| 19 | fownertype | 货主类型 | varchar | 30 |  | √ | 'bos_org' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 20 | fdemandbillentryseq | 需求单据分录行号 | int4 | 32 |  | √ | 0 | 需求单据分录行号 |
| 21 | fplantags | 计划标识 | int8 | 64 |  | √ | 0 | 计划标识 mpdm_plantag |
| 22 | fplanoperatenum | 计划运算号 | varchar | 100 |  | √ | ' ' | 计划运算号 |
| 23 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 24 | fbasedemandqty | 基本单位净需求数量 | numeric | 23 | 10 | √ | 0 | 基本单位净需求数量 |
| 25 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 26 | fmaterialplanid | 物料编码 | int8 | 64 |  | √ | 0 | 物料计划信息 mpdm_materialplan |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbizdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 29 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fbizunitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fbillstatus | 单据状态 | varchar | 60 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fismpsonly | 只算MPS | bpchar | 1 |  | √ | '0' | 只算MPS |
| 34 | fbizremainqty | 剩余需求数量 | numeric | 23 | 10 | √ | 0 | 剩余需求数量 |
| 35 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 36 | fclosestatus | 关闭状态 | varchar | 30 |  | √ | 'A' | 关闭状态,枚举: A :正常 B :关闭 |
| 37 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fbaseorderqty | 基本确认订单数量 | numeric | 23 | 10 | √ | 0 | 基本确认订单数量 |
| 39 | fbizorderqty | 确认订单量 | numeric | 23 | 10 | √ | 0 | 确认订单量 |
| 40 | fdatasource | 数据来源 | varchar | 60 |  | √ | ' ' | 数据来源,枚举: A :手工新增 B :计算产生 |
| 41 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | fdemandqty | 基本单位需求数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位需求数量 |
| 43 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 44 | fsupplyorgid | 接收组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fdemandbillentity | 需求单据实体 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 47 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 48 | fdemandbillid | 需求单据ID | varchar | 50 |  | √ | ' ' | 需求单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_rativeorder |  | fid |
| 2 | idx_mrp_rativeorder |  | fbillno,forgid |
