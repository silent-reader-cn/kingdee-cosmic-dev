# 生产领料申请单(废弃)-im_mdc_mftreqbill

## 生产领料申请单(废弃)-关联追踪表 t_im_mdc_mftreqbill_tc

- **表名称：** 生产领料申请单(废弃)-关联追踪表
- **表名：** t_im_mdc_mftreqbill_tc

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
| 1 | pk_im_mdc_mftreqbill_tc |  | fid |
| 2 | idx_im_mdc_mftreqbill_tc_tbill |  | ftbillid |
| 3 | idx_im_mdc_mftreqbill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_im_mdc_mftreqentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mdc_mftreqentry_lk

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
| 1 | pk_im_mdc_mftreqentry_lk |  | fpkid |
| 2 | idx_im_mdc_mftreqentry_lk_fk |  | fentryid |

---

## 生产领料申请单(废弃)-反写记录表 t_im_mdc_mftreqbill_wb

- **表名称：** 生产领料申请单(废弃)-反写记录表
- **表名：** t_im_mdc_mftreqbill_wb

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
| 1 | idx_im_mdc_mftreqbill_wb_fk |  | fid |
| 2 | pk_im_mdc_mftreqbill_wb |  | fentryid |

---

## 生产领料申请单(废弃)-多语言表 t_im_mdc_mftreqbills_l

- **表名称：** 生产领料申请单(废弃)-多语言表
- **表名：** t_im_mdc_mftreqbills_l

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
| 1 | idx_im_mdc_mftreqbills_fid |  | fid,flocaleid |
| 2 | pk_im_mdc_mftreqbills_l |  | fpkid |

---

## 生产领料申请单(废弃)-主表 t_im_mdc_mftreqbills

- **表名称：** 生产领料申请单(废弃)-主表
- **表名：** t_im_mdc_mftreqbills

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 4 | fheadproject | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 5 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | finvorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 11 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | 'NULL' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fdeptid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 17 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 18 | fsettlecurrency | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fbillcretype | 单据生成类型 | varchar | 50 |  | √ | ' ' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 23 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fmaterialtype | 领料类型 | varchar | 50 |  | √ | ' ' | 领料类型,枚举: A :标准生产 B :检修生产 C :委外生产 |
| 25 | fprofessiona | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_mftreqbills_forgid |  | forgid |
| 2 | pk_im_mdc_mftreqbills |  | fid |
| 3 | idx_mdc_mftreqbills_fbillno |  | fbillno |

---

## 物料明细-子表 t_im_mdc_mftreqentry

- **表名称：** 物料明细-子表
- **表名：** t_im_mdc_mftreqentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 3 | flogisticsbill | 物流单据 | bpchar | 1 |  | √ | '0' | 物流单据 |
| 4 | flength | 长度 | numeric | 23 | 10 | √ | 0 | 长度 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | ffilenumber | 文件编码 | varchar | 50 |  | √ | ' ' | 文件编码 |
| 10 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 13 | freplacegroup | 替代组 | varchar | 50 |  | √ | ' ' | 替代组 |
| 14 | fdeliverdate | 配送日期 | timestamp | 0 |  |  | null | 配送日期 |
| 15 | fauditqty | 审批数量 | numeric | 23 | 10 | √ | 0 | 审批数量 |
| 16 | frowstatus | 行状态 | varchar | 50 |  | √ | ' ' | 行状态,枚举: A :暂存 B :已提交 C :已审核 D :已关闭 |
| 17 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 20 | forderentryseq | 工单行号 | varchar | 50 |  | √ | ' ' | 工单行号 |
| 21 | fqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 22 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 23 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 24 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 27 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 28 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 30 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 31 | forderno | 工单号 | varchar | 50 |  | √ | ' ' | 工单号 |
| 32 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 34 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 35 | flengthunit | 尺寸单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fqtyunit2nd | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 37 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 50 |  | √ | ' ' | 来源系统单据分录ID |
| 38 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 39 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 40 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 43 | fmaterialname | 物料名称(历史) | varchar | 255 |  | √ | ' ' | 物料名称(历史) |
| 44 | fmaterialgroup | 物料分组 | int8 | 64 |  | √ | 0 | 物料分组 |
| 45 | foutqty | 下推领料数量 | numeric | 23 | 10 | √ | 0 | 下推领料数量 |
| 46 | fbigintfield | 工单id | int8 | 64 |  | √ | 0 | 工单id |
| 47 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 48 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 49 | fuseoutbaseqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 50 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 51 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 52 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 53 | fwmssstatus | 配送状态 | varchar | 50 |  | √ | ' ' | 配送状态,枚举: A :打开 B :待拣货 C :拣货中 D :已拣货 E :配送中 F :已配送 G :已接收 H :已拒绝 I :已取消 |
| 54 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 55 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 56 | forderentryid | 工单分录id | int8 | 64 |  | √ | 0 | 工单分录id |
| 57 | freplaceplan | 组件替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 58 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 59 | fworkcard | 工卡 | int8 | 64 |  | √ | 0 | [工卡 mpdm_mrocardroute](../mpdm_files/mpdm_mrocardroute.md) |
| 60 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 61 | fuseoutqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 62 | ffullsize | 全尺寸 | bpchar | 1 |  | √ | '0' | 全尺寸 |
| 63 | foutinvorg | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 64 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 65 | fpickbaseqty | 已拣货基本数量 | numeric | 23 | 10 | √ | 0 | 已拣货基本数量 |
| 66 | fwidth | 宽度 | numeric | 23 | 10 | √ | 0 | 宽度 |
| 67 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 68 | foutbaseqty | 下推领料基本数量 | numeric | 23 | 10 | √ | 0 | 下推领料基本数量 |
| 69 | fauditbaseqty | 审批基本数量 | numeric | 23 | 10 | √ | 0 | 审批基本数量 |
| 70 | fdelivercycle | 配送周期 | int8 | 64 |  | √ | 0 | [配送周期 mpdm_deliverycycle](../mpdm_files/mpdm_deliverycycle.md) |
| 71 | flocationid | 供货仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 72 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 73 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 74 | fdoctype | 文件类型 | int8 | 64 |  | √ | 0 | [文件类型 mpdm_doctype](../mpdm_files/mpdm_doctype.md) |
| 75 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 76 | fheight | 高度 | numeric | 23 | 10 | √ | 0 | 高度 |
| 77 | fbaseqty | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 78 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 79 | fwarehousechange | 供货仓库手工修改 | bpchar | 1 |  | √ | '0' | 供货仓库手工修改 |
| 80 | fsrcsysbillid | 来源系统单据ID | varchar | 50 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mdc_req_fmainbillid |  | fmainbillid |
| 2 | idx_mdc_req_fmainbillentryid |  | fmainbillentryid |
| 3 | pk_im_mdc_mftreqentry |  | fentryid |
| 4 | idx_mdc_req_fid |  | fid |
| 5 | idx_mdc_req_fmaterielmasterid |  | fmaterielmasterid |

---

## 关联子实体-子表 t_im_mdc_mftreqbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_im_mdc_mftreqbill_lk

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
| 1 | pk_im_mdc_mftreqbill_lk |  | fpkid |
| 2 | idx_im_mdc_mftreqbill_lk_fk |  | fid |
