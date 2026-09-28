# 序列号主档-bd_snmainfile

## 多维度序列号-子表 t_bd_sndimensionentry

- **表名称：** 多维度序列号-子表
- **表名：** t_bd_sndimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsndimitem | 维度项 | int8 | 64 |  | √ | 0 | [序列号维度 bd_sndimension](../sbd_files/bd_sndimension.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fsndimnumber | 维度值 | varchar | 50 |  | √ | ' ' | 维度值 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_sndimensionentry |  | fentryid |
| 2 | idx_bd_sndimensionentry_st |  | fsndimitem |
| 3 | idx_bd_sndimensionentry_id |  | fid |
| 4 | idx_bd_sndimensionentry_sn |  | fsndimnumber |

---

## 序列号主档-主表 t_bd_snmainfile

- **表名称：** 序列号主档-主表
- **表名：** t_bd_snmainfile

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstockdate | 进货日期 | timestamp | 0 |  |  | null | 进货日期 |
| 3 | flotnumber | 创建批号 | varchar | 200 |  | √ | ' ' | 创建批号 |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fdescustomerid | 去向客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 6 | fbizhappendate | 业务发生日期 | timestamp | 0 |  |  | null | 业务发生日期 |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fsbillinvfluctuation | 源单库存变化 | bpchar | 1 |  | √ | '0' | 源单库存变化,枚举: 0 :无变化 1 :增加 2 :减少 3 :减少和增加 |
| 10 | ffinalaudittrailid | 最后审核轨迹ID | int8 | 64 |  | √ | 0 | 最后审核轨迹ID |
| 11 | foccupybillentryid | 占用单据分录ID | int8 | 64 |  | √ | 0 | 占用单据分录ID |
| 12 | fkeeporgid | 库存组织(列表) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmasterfiletypeid | 类型 | int8 | 64 |  | √ | '1401417099242528768' | [批号/序列号类型 bd_masterfile_type](../sbd_files/bd_masterfile_type.md) |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fenddate | 保修结束日期 | timestamp | 0 |  |  | null | 保修结束日期 |
| 16 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsourcebillentrytype | 源单单据分录类型 | varchar | 50 |  | √ | ' ' | 源单单据分录类型 |
| 20 | fsnstatus | 序列号状态 | varchar | 5 |  | √ | ' ' | 序列号状态,枚举: A :待入库 B :在库 C :待出库 D :出库 E :调拨在途 |
| 21 | fsubstractinvcounter | 减少库存次数 | int8 | 64 |  | √ | 0 | 减少库存次数 |
| 22 | fshipmentdate | 出货日期 | timestamp | 0 |  |  | null | 出货日期 |
| 23 | fisimport | 非单据生成 | bpchar | 1 |  | √ | '0' | 非单据生成 |
| 24 | foccupybillentrytype | 占用单据分录类型 | varchar | 50 |  | √ | ' ' | 占用单据分录类型 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fsourcebillentryid | 源单单据分录ID | int8 | 64 |  | √ | 0 | 源单单据分录ID |
| 28 | fsourcebilltype | 源单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 29 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fnowinvaccid | 现即时库存ID | int8 | 64 |  | √ | 0 | 现即时库存ID |
| 32 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 33 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | ftraincreaseinvcounter | 调拨增加库存次数 | int8 | 64 |  | √ | 0 | 调拨增加库存次数 |
| 35 | fwarehouseid | 仓库(列表) | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 36 | fsrcsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 37 | fsuppliersn | 供应商/自产序列号 | varchar | 100 |  | √ | ' ' | 供应商/自产序列号 |
| 38 | finvorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | ftrasubstractinvcounter | 调拨减少库存次数 | int8 | 64 |  | √ | 0 | 调拨减少库存次数 |
| 40 | flotid | 批号ID | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 41 | flocationid | 仓位(列表) | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 42 | foccupybillid | 占用单据ID | int8 | 64 |  | √ | 0 | 占用单据ID |
| 43 | fstartdate | 保修开始日期 | timestamp | 0 |  |  | null | 保修开始日期 |
| 44 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 45 | fincreaseinvcounter | 增加库存次数 | int8 | 64 |  | √ | 0 | 增加库存次数 |
| 46 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 47 | fnumber | 序列号 | varchar | 100 |  | √ | ' ' | 序列号 |
| 48 | foccupybilltype | 占用单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_snmainfile_number |  | fnumber |
| 2 | t_bd_snmainfile_pkey |  | fid |
| 3 | idx_bd_snmainfile_finvorgid |  | finvorgid |
| 4 | idx_bd_snmainfile_material |  | fmaterialid |
| 5 | idx_bd_snmainfile_occupybillid |  | foccupybillid |
| 6 | idx_bd_snmainfile_ftra |  | ffinalaudittrailid |
