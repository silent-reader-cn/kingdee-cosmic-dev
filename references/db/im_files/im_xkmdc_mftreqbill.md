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
| 2 | frequserid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fsupplyowner | 供应货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fbizorgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 12 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsupplyownertype | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | flastupdateuserid | flastupdateuserid | int8 | 64 |  | √ | 0 |  |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 |
| 24 | flastupdatetime | flastupdatetime | timestamp | 0 |  |  | null |  |
| 25 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | ' ' | 关闭状态,枚举: A :正常 B :已关闭 |
| 26 | fbizdeptid | 申请部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

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
| 2 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 4 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 9 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsrcseq | 来源编号 | varchar | 255 |  | √ | ' ' | 来源编号 |
| 11 | fprdunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 15 | fquantity | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 16 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 18 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 20 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 21 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 22 | fprdqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 23 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 24 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 25 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 26 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 27 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 28 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 29 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 31 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 34 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |

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
| 3 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foutownerid | 出库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 8 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 9 | foutinvtypeid | 出库库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 10 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | foutkeeperid | 出库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 13 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 14 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 16 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 17 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 19 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 20 | foutinvstatusid | 出库库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 21 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 22 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 23 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0 | 领料上限基本数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 26 | fmaterialname | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 27 | fprdownerid | 产品货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fmanuentryid | 生产工单行ID | int8 | 64 |  | √ | 0 | 生产工单行ID |
| 29 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 30 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 31 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 32 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 33 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 34 | foutkeepertype | 出库保管者类型 | varchar | 30 |  | √ | ' ' | 出库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 35 | fprdunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 37 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 38 | fquantity | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 39 | fmanuentry | 生产工单行号 | varchar | 50 |  | √ | ' ' | 生产工单行号 |
| 40 | foutownertype | 出库货主类型 | varchar | 30 |  | √ | ' ' | 出库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 41 | fprdownertype | 产品货主类型 | varchar | 30 |  | √ | ' ' | 产品货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 42 | fmanubillid | 生产工单ID | int8 | 64 |  | √ | 0 | 生产工单ID |
| 43 | fprdqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 44 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 45 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 46 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 47 | fqtyunit3rd | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 48 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 49 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | 项目任务F7 mpm_task_f7 |
| 50 | fbaseqty | 实发基本数量 | numeric | 23 | 10 | √ | 0 | 实发基本数量 |
| 51 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 52 | fmanubill | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |

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
