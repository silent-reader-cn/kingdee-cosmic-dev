# 采购追料计划单-pm_chasematerialbill

## 单据体-子表 t_pm_chasematerialentry

- **表名称：** 单据体-子表
- **表名：** t_pm_chasematerialentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqty | 已收货数量 | numeric | 23 | 10 | √ | 0 | 已收货数量 |
| 3 | forderbillentryid | 订单单据行ID | int8 | 64 |  | √ | 0 | 订单单据行ID |
| 4 | forderbilltype | 采购单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 5 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsupplytype | 供应商类型 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | forderbillno | 采购订单编号 | varchar | 80 |  | √ | ' ' | 采购订单编号 |
| 8 | fchaseqty | 追料数量 | numeric | 23 | 10 | √ | 0 | 追料数量 |
| 9 | fentcfmtime | 企业确认时间 | timestamp | 0 |  |  | null | 企业确认时间 |
| 10 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 11 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fentcfmuser | 企业确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 14 | fchasecomment | 追料备注 | varchar | 512 |  |  | ' ' | 追料备注 |
| 15 | fentryentcfmstatus | 企业确认状态 | bpchar | 1 |  | √ | '0' | 企业确认状态,枚举: 0 :未确认 1 :已确认 2 :已退回 |
| 16 | fsrcbillentryseq | 工单行号 | int8 | 64 |  | √ | 0 | 工单行号 |
| 17 | fsupshipmentdate | 供应商预计发货日期 | timestamp | 0 |  |  | null | 供应商预计发货日期 |
| 18 | fentryrecorgid | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 21 | fordercomment | 订单备注 | varchar | 512 |  |  | ' ' | 订单备注 |
| 22 | fchasedate | 追料日期 | timestamp | 0 |  |  | null | 追料日期 |
| 23 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fismodify | 是否调整 | bpchar | 1 |  | √ | '0' | 是否调整 |
| 25 | fsrcbillnumber | 工单编号 | varchar | 80 |  | √ | ' ' | 工单编号 |
| 26 | fqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 27 | fsuparrivaldate | 供应商确认到货日期 | timestamp | 0 |  |  | null | 供应商确认到货日期 |
| 28 | forderbiztype | 采购业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 29 | fsuparrivalqty | 供应商确认到货数量 | numeric | 23 | 10 | √ | 0 | 供应商确认到货数量 |
| 30 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 31 | fsrcmaterial | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fsrcbillentryid | 工单行ID | int8 | 64 |  | √ | 0 | 工单行ID |
| 36 | fentrysupcfmstatus | 供应商确认状态 | bpchar | 1 |  | √ | '0' | 供应商确认状态 |
| 37 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 38 | fisupdateplan | 已更新交货计划 | bpchar | 1 |  | √ | '0' | 已更新交货计划 |
| 39 | forderbillentryseq | 采购订单行号 | int8 | 64 |  | √ | 0 | 采购订单行号 |
| 40 | fentrycomment | 订单明细备注 | varchar | 512 |  |  | ' ' | 订单明细备注 |
| 41 | fsupcfmuser | 供应商确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | forderbillid | 订单单据ID | int8 | 64 |  | √ | 0 | 订单单据ID |
| 43 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 44 | fsupcfmtime | 供应商确认时间 | timestamp | 0 |  |  | null | 供应商确认时间 |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | forderbiztime | 采购订单日期 | timestamp | 0 |  |  | null | 采购订单日期 |
| 47 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_chasematerialentry_oei |  | forderbillentryid |
| 2 | idx_chasematerialentry_mo |  | fmaterialid,fid |
| 3 | pk_t_pm_chasematerialentry |  | fentryid |

---

## 采购追料计划单-多语言表 t_pm_chasematerialbill_l

- **表名称：** 采购追料计划单-多语言表
- **表名：** t_pm_chasematerialbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_chasematerialbill_l |  | fpkid |
| 2 | idx_pm_chasematerialbill_l |  | fid,flocaleid |

---

## 采购追料计划单-主表 t_pm_chasematerialbill

- **表名称：** 采购追料计划单-主表
- **表名：** t_pm_chasematerialbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpushbillno | 推送单号 | varchar | 512 |  |  | null | 推送单号 |
| 5 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 7 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 8 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fpushdate | 推送日期 | timestamp | 0 |  |  | null | 推送日期 |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fentcfmstatus | 企业确认状态 | varchar | 5 |  | √ | ' ' | 企业确认状态,枚举: A :未确认 B :部分确认 C :全部确认 D :已退回 |
| 14 | fbiztime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 15 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsupcfmstatus | 供应商确认状态 | varchar | 5 |  | √ | ' ' | 供应商确认状态,枚举: A :未确认 B :部分确认 C :全部确认 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_chasematerialbill_org |  | forgid |
| 2 | idx_chasematerialbill_biztime |  | fbiztime |
| 3 | idx_chasematerialbill_sup |  | fsupplierid |
| 4 | pk_t_pm_chasematerialbill |  | fid |
