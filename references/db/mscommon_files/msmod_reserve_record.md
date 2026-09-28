# 预留记录（旧）-msmod_reserve_record

## 预留记录（旧）-主表 t_msmod_reserverecord

- **表名称：** 预留记录（旧）-主表
- **表名：** t_msmod_reserverecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faggregateid | 总量预留id | int8 | 64 |  | √ | 0 | 总量预留id |
| 3 | fbalentryid | 供应分录ID | int8 | 64 |  | √ | 0 | 供应分录ID |
| 4 | f_s_project | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | f_base_qty | 预留基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预留基本数量 |
| 6 | f_s_warehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 7 | f_billentry_id | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 8 | freservemethod | 预留方式 | varchar | 50 |  | √ | ' ' | 预留方式,枚举: 1 :单据预留 2 :对象预留 3 :无对象预留 |
| 9 | f_create_date | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 10 | f_qty | 预留数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预留数量 |
| 11 | f_s_billnum | 供应单据编号 | varchar | 50 |  | √ | ' ' | 供应单据编号 |
| 12 | freservesource | 预留来源 | varchar | 20 |  | √ | ' ' | 预留来源 |
| 13 | fupdater | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | f_s_unit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | f_s_invstatus | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 16 | f_s_location | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 17 | f_s_org | 供应库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | freserveobj | 预留对象 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 19 | f_r_invorg | 需求库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | f_s_owner_type | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 21 | f_creater_id | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | f_r_sale_operator | 需求业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 23 | f_s_materiel | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 24 | fispredict | 预计入 | bpchar | 1 |  | √ | '0' | 预计入 |
| 25 | f_bal_source | 供应来源 | bpchar | 1 |  | √ | ' ' | 供应来源,枚举: 1 :苍穹 2 :非苍穹 |
| 26 | f_r_sale_org | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | f_bill_id | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |
| 28 | f_s_owner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | f_s_invtype | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 30 | freserveobjtype | 预留对象类型 | varchar | 50 |  | √ | ' ' | 预留对象类型,枚举: bd_customer :客户 bd_operator :业务员 bos_adminorg :部门 |
| 31 | fcomputeid | 运算标识 | int8 | 64 |  | √ | 0 | 运算标识 |
| 32 | f_s_lotnum | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 33 | f_s_entryseq | 供应分录序号 | int8 | 64 |  | √ | 0 | 供应分录序号 |
| 34 | f_entry_name | 需求单据分录标识 | varchar | 10 |  | √ | ' ' | 需求单据分录标识 |
| 35 | fexpiredate | 预留到期日期 | timestamp | 0 |  |  | null | 预留到期日期 |
| 36 | f_s_auxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 37 | f_bill_obj_id | 需求单据 | varchar | 36 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 38 | fupdatedate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 39 | fgenerateid | 创建MRP运算标识 | int8 | 64 |  | √ | 0 | 创建MRP运算标识 |
| 40 | f_s_keeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 41 | fcansplit | 是否可分拆 | bpchar | 1 |  | √ | '0' | 是否可分拆 |
| 42 | f_r_customer | 需求客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 43 | f_bill_souce | 需求单据来源 | bpchar | 1 |  | √ | ' ' | 需求单据来源,枚举: 1 :苍穹 2 :非苍穹 |
| 44 | f_s_baseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 45 | f_s_unit2nd | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 46 | f_bill_no | 需求单据编号 | varchar | 80 |  | √ | ' ' | 需求单据编号 |
| 47 | f_s_keeper_type | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_customer :客户 bd_supplier :供应商 |
| 48 | f_bal_id | 供应ID | int8 | 64 |  | √ | 0 | 供应ID |
| 49 | freserveprctype | 预留产生类型 | bpchar | 1 |  | √ | ' ' | 预留产生类型,枚举: 0 :自动预留 1 :手工预留 2 :预留转移 3 :预留替换 |
| 50 | f_bal_obj_id | 供应对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 51 | f_s_configuredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 52 | f_r_biz_date | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 53 | f_r_sale_dept | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | f_billentry_seq | 需求单据分录序号 | int8 | 64 |  | √ | 0 | 需求单据分录序号 |
| 55 | f_reserve_scheme_id | 预留方案 | int8 | 64 |  | √ | 0 | [预留方案 msmod_reserve_scheme](../mscommon_files/msmod_reserve_scheme.md) |
| 56 | fisweak | 弱预留 | bpchar | 1 |  | √ | '0' | 弱预留 |
| 57 | f_qty2nd | 预留辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 预留辅助数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msmod_reserverecord |  | fid |
| 2 | idx_msmod_reservererd_fbillid |  | f_bill_id,f_billentry_id |
| 3 | idx_msmod_reservererd_billno |  | f_bill_no |
| 4 | idx_msmod_reservererd_balentryid |  | fbalentryid |
| 5 | idx_msmod_reservererd_billno2 |  | f_bal_id |
| 6 | idx_msmod_reservererd_balobjid |  | f_bal_obj_id |
