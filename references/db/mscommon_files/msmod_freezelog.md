# 冻结记录-msmod_freezelog

## 冻结记录-主表 t_msmod_freezelog

- **表名称：** 冻结记录-主表
- **表名：** t_msmod_freezelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffreezeentryseq | 冻结单据行号 | int8 | 64 |  | √ | 0 | 冻结单据行号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | ffreezeentrynumber | 冻结单据分录标识 | varchar | 50 |  | √ | ' ' | 冻结单据分录标识 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | ffreezeentryid | 冻结单据行ID | int8 | 64 |  | √ | 0 | 冻结单据行ID |
| 9 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fproviderentityid | 供应实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 12 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ffreezeentityid | 冻结单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 17 | funit3rd | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | ffreezedate | 冻结日期 | timestamp | 0 |  |  | null | 冻结日期 |
| 21 | flotnum | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 22 | ffreezebillno | 冻结单据编号 | varchar | 50 |  | √ | ' ' | 冻结单据编号 |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 28 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 31 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 32 | ffreezebillid | 冻结单据ID | int8 | 64 |  | √ | 0 | 冻结单据ID |
| 33 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_freezelog_ffree |  | ffreezebillid |
| 2 | idx_msmod_freezelog_org_ml_wh |  | forgid,fmaterialid,fwarehouseid |
| 3 | pk_t_msmod_freezelog |  | fid |
| 4 | idx_msmod_freezelog_fe_pe |  | ffreezeentityid,fproviderentityid |
