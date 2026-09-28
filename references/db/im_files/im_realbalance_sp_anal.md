# 即时余额SP集-im_realbalance_sp_anal

## 即时余额SP集-主表 t_im_realbalance_sp_anal

- **表名称：** 即时余额SP集-主表
- **表名：** t_im_realbalance_sp_anal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fqty2nd_sp | 辅助数量sp | numeric | 23 | 10 | √ | 0 | 辅助数量sp |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fqty_sp | 数量sp | numeric | 23 | 10 | √ | 0 | 数量sp |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fmversionid | fmversionid | int8 | 64 |  | √ | 0 |  |
| 9 | fqty3rd_sp | 辅助数量(2)sp | numeric | 23 | 10 | √ | 0 | 辅助数量(2)sp |
| 10 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 11 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 14 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 15 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 17 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fisnew | fisnew | varchar | 50 |  | √ | ' ' |  |
| 20 | fupdateruleid | 更新规则ID | varchar | 50 |  | √ | ' ' | 更新规则ID |
| 21 | fbillno | 单据编码 | varchar | 50 |  | √ | ' ' | 单据编码 |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | flotnum | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fupdatetype | 更新方向 | int8 | 64 |  | √ | 0 | 更新方向 |
| 26 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 27 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fbaseqty_sp | 基本数量sp | numeric | 23 | 10 | √ | 0 | 基本数量sp |
| 29 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 30 | fentryseq | 分录序号 | int8 | 64 |  | √ | 0 | 分录序号 |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | fbillname | 单据实体名称 | varchar | 50 |  | √ | ' ' | 单据实体名称 |
| 33 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fqty2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 35 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 36 | fupdatetime | 更新流水号 | int8 | 64 |  | √ | 0 | 更新流水号 |
| 37 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 38 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 39 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 41 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 42 | fqty3rd | fqty3rd | numeric | 23 | 10 | √ | 0 |  |
| 43 | fentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 44 | fkeycol | keycol | varchar | 50 |  | √ | ' ' | keycol |
| 45 | fdatatype | 收发类型 | varchar | 50 |  | √ | ' ' | 收发类型,枚举: "0" :收入 "1" :发出 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_realbalance_sp_anal |  | fid |
| 2 | idx_im_realbalance_sp_anal_fkey |  | fkeycol |
