# 追料计划-pur_chasing_plan

## 追料计划明细-子表 t_pur_chasing_planentry

- **表名称：** 追料计划明细-子表
- **表名：** t_pur_chasing_planentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrynote | 明细备注 | varchar | 512 |  | √ | ' ' | 明细备注 |
| 3 | fchaseqty | 追料数量 | numeric | 23 | 10 | √ | 0 | 追料数量 |
| 4 | fbasicunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | festimateddeliverydate | 供应商预计发货日期 | timestamp | 0 |  |  | null | 供应商预计发货日期 |
| 7 | flocation | 收货仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fnote | 采购备注 | varchar | 512 |  | √ | ' ' | 采购备注 |
| 10 | fsrcbillentryseq | 来源单据行号 | varchar | 50 |  | √ | ' ' | 来源单据行号 |
| 11 | fsuppliercfmdate | 供应商确认时间 | timestamp | 0 |  |  | null | 供应商确认时间 |
| 12 | fchasedate | 追料日期 | timestamp | 0 |  |  | null | 追料日期 |
| 13 | fqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 14 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fpurorderdate | 采购订单日期 | timestamp | 0 |  |  | null | 采购订单日期 |
| 16 | fpromisedate | 供应商确认到货日期 | timestamp | 0 |  |  | null | 供应商确认到货日期 |
| 17 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 18 | finvqty | 已入库数量 | numeric | 23 | 10 | √ | 0 | 已入库数量 |
| 19 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fwarehouse | 收货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | foriginbillentryid | 原追料计划行ID | varchar | 50 |  | √ | ' ' | 原追料计划行ID |
| 22 | fpoentryseq | 采购订单行号 | int4 | 32 |  | √ | 0 | 采购订单行号 |
| 23 | fpromiseqty | 供应商确认到货数量 | numeric | 23 | 10 | √ | 0 | 供应商确认到货数量 |
| 24 | fbusinesstypeid | 采购业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 25 | fsrcbilltype | 来源单据类型 | varchar | 80 |  | √ | ' ' | 来源单据类型 |
| 26 | fmaterialdesc | fmaterialdesc | varchar | 255 |  | √ | ' ' |  |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | freceiveqty | 已收货数量 | numeric | 23 | 10 | √ | 0 | 已收货数量 |
| 30 | fpurcfmdate | 企业方确认时间 | timestamp | 0 |  |  | null | 企业方确认时间 |
| 31 | fsrcbillno | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 32 | fsupplytype | 供应商类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 33 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 34 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 35 | fsuppliercfmid | 供应商确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fchasenote | 追料备注 | varchar | 512 |  | √ | ' ' | 追料备注 |
| 37 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 38 | fpurcfmid | 企业方确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fentitymodifier | fentitymodifier | int8 | 64 |  | √ | 0 |  |
| 40 | fpobillid | 采购订单ID | varchar | 50 |  | √ | ' ' | 采购订单ID |
| 41 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 42 | fmftorderentryseq | 工单行号 | varchar | 20 |  | √ | ' ' | 工单行号 |
| 43 | fsupplierremark | 供应商确认说明 | varchar | 512 |  | √ | ' ' | 供应商确认说明 |
| 44 | fisadjust | 是否调整 | bpchar | 1 |  | √ | '0' | 是否调整 |
| 45 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fentitymodifydate | fentitymodifydate | timestamp | 0 |  |  | null |  |
| 47 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 48 | fissplit | 是否拆分 | bpchar | 1 |  | √ | '0' | 是否拆分 |
| 49 | fmftorderentryid | 工单行ID | varchar | 50 |  | √ | ' ' | 工单行ID |
| 50 | fentryreqdeptid | 需求部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 51 | fsrcbillentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 52 | fpoentryid | 采购订单行ID | varchar | 50 |  | √ | ' ' | 采购订单行ID |
| 53 | fcfmstatus | 供应商确认状态 | bpchar | 1 |  | √ | '0' | 供应商确认状态,枚举: A :待确认 B :已确认 |
| 54 | fproductmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 55 | fpobillno | 采购订单编号 | varchar | 80 |  | √ | ' ' | 采购订单编号 |
| 56 | fmftordernumber | 工单编号 | varchar | 80 |  | √ | ' ' | 工单编号 |
| 57 | fpurcfmstatus | 企业方确认状态 | bpchar | 1 |  | √ | '0' | 企业方确认状态,枚举: A :待确认 B :已确认 C :已打回 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_chasing_planentry_fid |  | fid,fseq |
| 2 | idx_pur_chasing_plane_pobillid |  | fpobillid |
| 3 | pk_pur_chasing_planentry |  | fentryid |
| 4 | idx_pur_chasing_plane_poentry |  | fpoentryid |

---

## 追料计划-主表 t_pur_chasing_plan

- **表名称：** 追料计划-主表
- **表名：** t_pur_chasing_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 10 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | '2' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsendbillno | 推送单号 | varchar | 80 |  | √ | ' ' | 推送单号 |
| 15 | fsenddate | 推送日期 | timestamp | 0 |  |  | null | 推送日期 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_chasing_plan |  | fid |
| 2 | idx_pur_chasing_plan_fbilldate |  | fbilldate |
| 3 | idx_pur_chasing_plan_fbillno |  | fbillno |
| 4 | idx_pur_chasing_plan_bizpid |  | fbizpartnerid |

---

## 追料计划-关联追踪表 t_pur_chasing_plan_tc

- **表名称：** 追料计划-关联追踪表
- **表名：** t_pur_chasing_plan_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_chasing_plan_tc_tid |  | ftid |
| 2 | idx_pur_chasing_plan_tc_tbill |  | ftbillid |
| 3 | pk_pur_chasing_plan_tc |  | fid |

---

## 追料计划-多语言表 t_pur_chasing_plan_l

- **表名称：** 追料计划-多语言表
- **表名：** t_pur_chasing_plan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_chasing_plan_l |  | fpkid |
| 2 | idx_pur_chasing_plan_l |  | fid,flocaleid |

---

## 关联子实体-子表 t_pur_chasing_planentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_chasing_planentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_chasing_planentry_lk_fk |  | fentryid |
| 2 | pk_pur_chasing_planentry_lk |  | fpkid |

---

## 追料计划-反写记录表 t_pur_chasing_plan_wb

- **表名称：** 追料计划-反写记录表
- **表名：** t_pur_chasing_plan_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_chasing_plan_wb |  | fentryid |
| 2 | idx_pur_chasing_plan_wb_fk |  | fid |
