# 生产领料申请单-im_xkmdc_mftreqbill

## 生产领料申请单-多语言表 t_im_xkmdc_mftreqbill_l

- **表名称：** 生产领料申请单-多语言表
- **表名：** t_im_xkmdc_mftreqbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_xkmdc_mftreqbill_l |  | fpkid |
| 2 | idx_t_im_xkmdc_mftqb_l_fid |  | fid,flocaleid |

---

## 关联子实体-子表 t_im_xkmdc_mftqbentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_xkmdc_mftqbentry_lk

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
| 1 | pk_im_xkmdc_mftqbentry_lk |  | fpkid |
| 2 | idx_im_xkmdc_mftqbentry_lk_fk |  | fentryid |

---

## 生产领料申请单-关联追踪表 t_im_xkmdc_mftreqbill_tc

- **表名称：** 生产领料申请单-关联追踪表
- **表名：** t_im_xkmdc_mftreqbill_tc

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
| 1 | idx_im_xkmdc_mftreqbill_tc_tid |  | ftid |
| 2 | idx_im_xkmdc_mftreqbill_tc_tbill |  | ftbillid |
| 3 | pk_im_xkmdc_mftreqbill_tc |  | fid |

---

## 生产领料申请单-反写记录表 t_im_xkmdc_mftreqbill_wb

- **表名称：** 生产领料申请单-反写记录表
- **表名：** t_im_xkmdc_mftreqbill_wb

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
| 1 | idx_im_xkmdc_mftreqbill_wb_fk |  | fid |
| 2 | pk_im_xkmdc_mftreqbill_wb |  | fentryid |

---

## 关联子实体-子表 t_im_xkmdc_mftreqbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_xkmdc_mftreqbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_xkmdc_mftreqbill_lk |  | fpkid |
| 2 | idx_im_xkmdc_mftreqbill_lk_fk |  | fid |

---

## 生产领料申请单-主表 t_im_xkmdc_mftreqbill

- **表名称：** 生产领料申请单-主表
- **表名：** t_im_xkmdc_mftreqbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frequserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsupplytype | 发料方式 | varchar | 5 |  | √ | 'A' | 发料方式,枚举: A :一次发料 B :多次发料 |
| 4 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 5 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsupplyowner | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 8 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbizorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsupplyownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 26 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 27 | fsupplierid | 委外供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 28 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 29 | fbizdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_xkmdc_mftreqbill |  | fid |
| 2 | idx_im_xkmdc_mqbl_fno |  | fbillno |

---

## 物料汇总明细-子表 t_im_xkmdc_mftqbmrgentry

- **表名称：** 物料汇总明细-子表
- **表名：** t_im_xkmdc_mftqbmrgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funissueqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 5 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 10 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 12 | fsrcseq | 来源编号 | varchar | 255 |  | √ | ' ' | 来源编号 |
| 13 | fprdunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 15 | factissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fquantity | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 19 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 21 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 23 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fprdqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 26 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 28 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 29 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 30 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 31 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 32 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 33 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 35 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 37 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 38 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 39 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_xkmdc_mftqbmrgentry |  | fentryid |
| 2 | idx_im_xkmdc_mqb_me_fid |  | fid |

---

## 关联子实体-子表 t_im_xkmdc_mftqbentrymg_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_xkmdc_mftqbentrymg_lk

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
| 1 | pk_im_xkmdc_mftqbentrymg_lk |  | fpkid |
| 2 | idx_im_xkmdc_mftqbentrymg_lk_fk |  | fentryid |

---

## 物料明细-子表 t_im_xkmdc_mftqbentry

- **表名称：** 物料明细-子表
- **表名：** t_im_xkmdc_mftqbentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasequantity | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 3 | funissueqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 6 | forderid | 生产工单F7 | int8 | 64 |  | √ | 0 | [生产工单单据头F7 pom_mftorder_headf7](../pom_files/pom_mftorder_headf7.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 11 | fprocessplanentryf7id | 工序计划分录F7 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 12 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 13 | fprocessplan | 工序计划 | varchar | 50 |  | √ | ' ' | 工序计划 |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 16 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fprocessplanf7id | 工序计划F7 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 18 | fqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 19 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 22 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 23 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 25 | fproductmasterid | 产品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 26 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 27 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 28 | fstockentryid | 生产用料清单分录F7 | int8 | 64 |  | √ | 0 | [生产用料清单分录f7 pom_mftstockentryf7](../pom_files/pom_mftstockentryf7.md) |
| 29 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 30 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 31 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 32 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0 | 领料上限基本数量 |
| 33 | funissuebaseqty | 未领基本数量 | numeric | 23 | 10 | √ | 0 | 未领基本数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 35 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 36 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 37 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 38 | fprocesssequence | 工序序列 | int4 | 32 |  | √ | 0 | 工序序列 |
| 39 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 40 | foutqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 41 | fprdownerid | 产品货主（废弃） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | fmanuentryid | 生产工单行ID | int8 | 64 |  | √ | 0 | 生产工单行ID |
| 43 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 44 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 45 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 46 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 48 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 49 | forderentryid | 生产工单分录F7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 50 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 51 | fmachiningtype | 加工类型 | varchar | 5 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 52 | fprdunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 53 | factissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 54 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 55 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 56 | fquantity | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 57 | fmanuentry | 生产工单行号 | varchar | 50 |  | √ | ' ' | 生产工单行号 |
| 58 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 59 | fprdownertype | 产品货主类型（废弃） | varchar | 30 |  | √ | ' ' | 产品货主类型（废弃）,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 60 | fmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 61 | fprdqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 62 | fstockid | 生产用料清单F7 | int8 | 64 |  | √ | 0 | [生产用料清单f7 pom_mftstockf7](../pom_files/pom_mftstockf7.md) |
| 63 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 64 | foutbaseqty | 关联领料基本数量 | numeric | 23 | 10 | √ | 0 | 关联领料基本数量 |
| 65 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 66 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 67 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 68 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 69 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 70 | fbaseqty | 实发基本数量 | numeric | 23 | 10 | √ | 0 | 实发基本数量 |
| 71 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 72 | fmanubill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 73 | factissuebaseqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_xkmdc_mqb_e_fmid |  | fmaterialid |
| 2 | pk_t_im_xkmdc_mftqbentry |  | fentryid |
| 3 | idx_im_xkmdc_mqb_e_fid |  | fid |
| 4 | idx_im_xkmdc_mqb_e_fmmid |  | fmaterialname |
| 5 | idx_im_xkmdc_mqb_e_fsrc |  | fsrcbillid,fsrcbillentity |
