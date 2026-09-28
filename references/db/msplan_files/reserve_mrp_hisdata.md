# MRP预留记录(历史数据)-reserve_mrp_hisdata

## MRP预留记录(历史数据)-主表 t_reserve_mrp_hisdata

- **表名称：** MRP预留记录(历史数据)-主表
- **表名：** t_reserve_mrp_hisdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freservetype | 预留类型 | varchar | 5 |  | √ | '0' | 预留类型,枚举: 1 :强预留 0 :弱预留 |
| 3 | f_s_project | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fdemandpriority | 需求优先级 | int4 | 32 |  | √ | 0 | 需求优先级 |
| 5 | f_base_qty | 预留基本数量 | numeric | 23 | 10 | √ | 0 | 预留基本数量 |
| 6 | f_bal_entryid | 供应分录ID | int8 | 64 |  | √ | 0 | 供应分录ID |
| 7 | f_billdetail_id | 需求单据子分录ID | int8 | 64 |  | √ | 0 | 需求单据子分录ID |
| 8 | f_s_warehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | f_billentry_id | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 10 | freservemethod | 预留方式 | varchar | 10 |  | √ | ' ' | 预留方式,枚举: 1 :单据预留 2 :对象预留 3 :无对象预留 |
| 11 | f_create_date | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | f_bal_detailid | 供应子分录ID | int8 | 64 |  | √ | 0 | 供应子分录ID |
| 13 | f_s_billnum | 供应单据编号 | varchar | 128 |  | √ | ' ' | 供应单据编号 |
| 14 | freservesource | 预留来源 | varchar | 32 |  | √ | ' ' | 预留来源 |
| 15 | fupdater | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | f_stock_billnum | 入库单据编号 | varchar | 128 |  | √ | ' ' | 入库单据编号 |
| 17 | f_s_invstatus | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 18 | f_s_location | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 19 | freserveinvaliddate | 预留至日期 | timestamp | 0 |  |  | null | 预留至日期 |
| 20 | f_s_org | 供应库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | freserveobj | 预留对象 | int8 | 64 |  | √ | '0' | 客户 bd_customer |
| 22 | f_r_invorg | 需求库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | f_s_owner_type | 货主类型 | varchar | 36 |  | √ | ' ' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 24 | f_stock_obj_id | 入库对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 25 | f_stock_id | 入库ID | int8 | 64 |  | √ | 0 | 入库ID |
| 26 | f_creater_id | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | f_s_materiel | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 28 | f_r_sale_operator | 需求业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 29 | fispredict | 预计入 | bpchar | 1 |  | √ | '0' | 预计入 |
| 30 | f_bal_source | 供应来源 | varchar | 10 |  | √ | ' ' | 供应来源,枚举: 1 :苍穹 2 :非苍穹 |
| 31 | f_r_sale_org | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | f_stock_entryid | 入库分录ID | int8 | 64 |  | √ | 0 | 入库分录ID |
| 33 | f_bill_id | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |
| 34 | f_s_owner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | f_s_invtype | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 36 | freserveobjtype | 预留对象类型 | varchar | 36 |  | √ | ' ' | 预留对象类型,枚举: bd_customer :客户 bd_operator :业务员 bos_adminorg :部门 |
| 37 | fcomputeid | 运算标识 | varchar | 50 |  | √ | ' ' | 运算标识 |
| 38 | f_s_lotnum | 批号 | varchar | 128 |  | √ | ' ' | 批号 |
| 39 | f_s_entryseq | 供应分录序号 | int4 | 32 |  | √ | 0 | 供应分录序号 |
| 40 | f_entry_name | 需求单据分录标识 | varchar | 50 |  | √ | ' ' | 需求单据分录标识 |
| 41 | fexpiredate | 预留到期日期 | timestamp | 0 |  |  | null | 预留到期日期 |
| 42 | f_s_auxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 43 | f_bill_obj_id | 需求单据 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 44 | fupdatedate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 45 | fgenerateid | 创建运算标识 | varchar | 50 |  | √ | ' ' | 创建运算标识 |
| 46 | f_s_keeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | fcansplit | 是否可分拆 | bpchar | 1 |  | √ | '0' | 是否可分拆 |
| 48 | f_r_customer | 需求客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 49 | f_s_baseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 50 | f_bill_souce | 需求单据来源 | varchar | 10 |  | √ | ' ' | 需求单据来源,枚举: 1 :苍穹 2 :非苍穹 |
| 51 | f_s_keeper_type | 保管者类型 | varchar | 36 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_customer :客户 bd_supplier :供应商 |
| 52 | f_bill_no | 需求单据编号 | varchar | 128 |  | √ | ' ' | 需求单据编号 |
| 53 | f_bal_id | 供应ID | int8 | 64 |  | √ | 0 | 供应ID |
| 54 | freserveprctype | 预留产生类型 | varchar | 10 |  | √ | ' ' | 预留产生类型,枚举: 0 :自动预留 1 :手工预留 2 :预留转移 3 :预留替换 4 :下推创建 5 :MRP运算 6 :齐套产生 7 :下级工单预留 |
| 55 | f_bal_obj_id | 供应对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 56 | f_s_configuredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 57 | f_r_sale_dept | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 58 | f_r_biz_date | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 59 | f_billentry_seq | 需求单据分录序号 | int4 | 32 |  | √ | 0 | 需求单据分录序号 |
| 60 | f_reserve_scheme_id | 预留方案 | int8 | 64 |  | √ | 0 | [预留方案 reserve_scheme](../msplan_files/reserve_scheme.md) |
| 61 | f_stock_entryseq | 入库分录序号 | int4 | 32 |  | √ | 0 | 入库分录序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_reserve_mrp_hisdata |  | fid |
| 2 | idx_reserve_hisdata_dno |  | f_bill_no |
| 3 | idx_reserve_hisdata_deid |  | f_billentry_id |
| 4 | idx_reserve_hisdata_seid |  | f_bal_entryid |
| 5 | idx_reserve_hisdata_sno |  | f_s_billnum |
| 6 | idx_reserve_hisdata_steid |  | f_stock_entryid |
