# 齐套分配-mpdm_kiiting_assignment

## 齐套分配-主表 t_mpdm_kittingassignment

- **表名称：** 齐套分配-主表
- **表名：** t_mpdm_kittingassignment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fkittingid | 齐套ID | int8 | 64 |  | √ | 0 | 齐套ID |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 7 | fsubunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 14 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 18 | fbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 23 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 24 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 26 | fassignmentbaseqty | 分配基本数量 | numeric | 23 | 10 | √ | 0 | 分配基本数量 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fassignmentsubqty | 分配子项数量 | numeric | 23 | 10 | √ | 0 | 分配子项数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_kitting_assignmeng |  | fid |
| 2 | idx_kitting_a_kittingid |  | fkittingid |
