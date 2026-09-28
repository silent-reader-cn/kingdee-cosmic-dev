# 序列号移动轨迹-bd_snmovetrack

## 序列号移动轨迹-主表 t_bd_snmovetrack

- **表名称：** 序列号移动轨迹-主表
- **表名：** t_bd_snmovetrack

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcwarehouseid | 出库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fbizhappendate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fbillentrytype | 单据分录类型 | varchar | 50 |  | √ | ' ' | 单据分录类型 |
| 6 | fbalancetype | 余额表类型 | varchar | 50 |  | √ | ' ' | [余额表 bal_balanceinfo](../bal_files/bal_balanceinfo.md) |
| 7 | fkeeporgid | 入库库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsrcinvaccid | 原即时库存ID | int8 | 64 |  | √ | 0 | 原即时库存ID |
| 9 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 10 | fownertype | 货主类型 | varchar | 20 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | fbllentityid | 单据名称 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fsnunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已删除 |
| 18 | fdesdeptid | 去向部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | ftraincreaseinvcounter | 调拨增加次数 | int8 | 64 |  | √ | 0 | 调拨增加次数 |
| 21 | fkeepertype | 保管者类型 | varchar | 20 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | fdeswarehouseid | 去向仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 23 | fwarehouseid | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fsrcsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 26 | ftrasubstractinvcounter | 调拨减少次数 | int8 | 64 |  | √ | 0 | 调拨减少次数 |
| 27 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fmovedirect | 移动方向 | varchar | 5 |  | √ | ' ' | 移动方向,枚举: A :来源 B :去向 |
| 29 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 30 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 31 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 32 | fdeslocationid | 去向仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 33 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 35 | fstockdate | 进货日期 | timestamp | 0 |  |  | null | 进货日期 |
| 36 | fdescustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 37 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | fsrcinvorgid | 出库库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | finlotnum | 入库批号 | varchar | 100 |  | √ | ' ' | 入库批号 |
| 40 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 41 | fdesbizorgid | 去向业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fsubstractinvcounter | 库存减少次数 | int8 | 64 |  | √ | 0 | 库存减少次数 |
| 43 | fshipmentdate | 出货日期 | timestamp | 0 |  |  | null | 出货日期 |
| 44 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 45 | fsnmainfileid | 序列号主档 | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 46 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 47 | fsrcbizorgid | 出库业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | fsrclocationid | 出库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 49 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 50 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 51 | fnowinvaccid | 即时库存ID | int8 | 64 |  | √ | 0 | 即时库存ID |
| 52 | fsrcdeptid | 出库部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 54 | fsuppliersn | 供应商/自产序列号 | varchar | 100 |  | √ | ' ' | 供应商/自产序列号 |
| 55 | flocationid | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 56 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 57 | foutlotnum | 出库批号 | varchar | 100 |  | √ | ' ' | 出库批号 |
| 58 | fmovedate | 移动日期 | timestamp | 0 |  |  | null | 移动日期 |
| 59 | fincreaseinvcounter | 库存增加次数 | int8 | 64 |  | √ | 0 | 库存增加次数 |
| 60 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 61 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_snmovetrack_bill |  | fbllentityid,fbillentrytype,fbillid,fbillentryid |
| 2 | t_bd_snmovetrack_pkey |  | fid |
| 3 | idx_bd_snmovetrack_nivc |  | fnowinvaccid |
| 4 | idx_bd_snmovetrack_sn |  | fsnmainfileid |
| 5 | idx_bd_snmovetrack_billid |  | fbillid |
| 6 | idx_bd_snmovetrack_kw |  | fkeeporgid,fwarehouseid |
