# 调拨计划处理-pom_allocationplan

## 关联子实体-子表 t_pom_allocationplan_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_allocationplan_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fpushedbaseqty | 已下推基本数量_确认携带值 | numeric | 23 | 10 |  | null | 已下推基本数量_确认携带值 |
| 3 | fallocationqty | 已调拨数量_确认携带值 | numeric | 23 | 10 |  | null | 已调拨数量_确认携带值 |
| 4 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 5 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 6 | fpushedbaseqty_old | 已下推基本数量_原始携带值 | numeric | 23 | 10 |  | null | 已下推基本数量_原始携带值 |
| 7 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fallocationqty_old | 已调拨数量_原始携带值 | numeric | 23 | 10 |  | null | 已调拨数量_原始携带值 |
| 10 | fallocbaseqty_old | 已调拨基本数量_原始携带值 | numeric | 23 | 10 |  | null | 已调拨基本数量_原始携带值 |
| 11 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 12 | fallocbaseqty | 已调拨基本数量_确认携带值 | numeric | 23 | 10 |  | null | 已调拨基本数量_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_allocationplan_lk |  | fpkid |
| 2 | idx_pom_allocationplan_lk_fk |  | fid |

---

## 调拨计划处理-关联追踪表 t_pom_allocationplan_tc

- **表名称：** 调拨计划处理-关联追踪表
- **表名：** t_pom_allocationplan_tc

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
| 1 | idx_pom_allocationplan_tc_tbill |  | ftbillid |
| 2 | pk_pom_allocationplan_tc |  | fid |
| 3 | idx_pom_allocationplan_tc_tid |  | ftid |

---

## 调拨计划处理-主表 t_pom_allocationplan

- **表名称：** 调拨计划处理-主表
- **表名：** t_pom_allocationplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequestbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 3 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 5 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 6 | finwarehouse | 调入仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 7 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 8 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | frequestdate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 10 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: A :手工 B :发料计划运算 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fpushedbaseqty | 已下推基本数量 | numeric | 23 | 10 | √ | 0 | 已下推基本数量 |
| 13 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 14 | fallocationqty | 已调拨数量 | numeric | 23 | 10 | √ | 0 | 已调拨数量 |
| 15 | fstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :正常 B :手工关闭 C :自动关闭 D :运算关闭 |
| 16 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 19 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fupperbillid_tag | 上游单据主键_详情 | text | 0 |  |  | null | 上游单据主键_详情 |
| 22 | fstockunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | frequestauxqty | 需求辅助数量 | numeric | 23 | 10 | √ | 0 | 需求辅助数量 |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fmplanbaseqty | 计划调拨基本数量 | numeric | 23 | 10 | √ | 0 | 计划调拨基本数量 |
| 28 | foutwarehouse | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | fupperbillid | 上游单据主键 | varchar | 255 |  | √ | ' ' | 上游单据主键 |
| 30 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fsupplymode | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 32 | fcloser | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fmplanqty | 计划调拨数量 | numeric | 23 | 10 | √ | 0 | 计划调拨数量 |
| 34 | fmplanauxqty | 计划调拨辅助数量 | numeric | 23 | 10 | √ | 0 | 计划调拨辅助数量 |
| 35 | finlocation | 调入仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 36 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | finstockorg | 调入库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | frequestqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 39 | foutstockorg | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fallocbaseqty | 已调拨基本数量 | numeric | 23 | 10 | √ | 0 | 已调拨基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pom_allocationplan |  | fid |
| 2 | idx_pom_allocationplan |  | forgid,fbillno |
| 3 | idx_allocplan_ftracknumber |  | ftracknumberid |
| 4 | idx_allocplan_fconfiguredcode |  | fconfiguredcodeid |

---

## 调拨计划处理-反写记录表 t_pom_allocationplan_wb

- **表名称：** 调拨计划处理-反写记录表
- **表名：** t_pom_allocationplan_wb

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
| 1 | idx_pom_allocationplan_wb_fk |  | fid |
| 2 | pk_pom_allocationplan_wb |  | fentryid |
