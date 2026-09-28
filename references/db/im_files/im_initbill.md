# 初始库存单-im_initbill

## 初始库存单-多语言表 t_im_initbill_l

- **表名称：** 初始库存单-多语言表
- **表名：** t_im_initbill_l

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
| 1 | idx_im_initbill_l_fid |  | fid,flocaleid |
| 2 | t_im_initbill_l_pkey |  | fpkid |

---

## 物料明细-子表 t_im_initbillentry

- **表名称：** 物料明细-子表
- **表名：** t_im_initbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fystartqtyunit3rd | 年初辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 年初辅助数量(2) |
| 3 | fentryinvschemeid | fentryinvschemeid | int8 | 64 |  | √ | 0 |  |
| 4 | fnoupdateinvfields | 不更新库存字段 | varchar | 100 |  | √ | ' ' | 不更新库存字段 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fserialqty | fserialqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | finvstatusid | 入库库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 9 | fentrydc | fentrydc | varchar | 5 |  | √ | ' ' |  |
| 10 | fysendqtyunit2nd | 年发出辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年发出辅助数量 |
| 11 | foutinvtypeid | foutinvtypeid | int8 | 64 |  | √ | 0 |  |
| 12 | funitrate | funitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fownertype | 入库货主类型 | varchar | 36 |  | √ | ' ' | 入库货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 bd_customer :客户 |
| 14 | fkeeperid | 入库保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fyreceiveqtyunit2nd | 年收入辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年收入辅助数量 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fpriceunitrate | fpriceunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | fqty | 期初数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初数量 |
| 19 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 20 | fserialunitid | fserialunitid | int8 | 64 |  | √ | 0 |  |
| 21 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | funitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 24 | fkeepertype | 入库保管者类型 | varchar | 36 |  | √ | ' ' | 入库保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 25 | fwarehouseid | 入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 26 | fpriceqty | fpriceqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 27 | foutinvstatusid | foutinvstatusid | int8 | 64 |  | √ | 0 |  |
| 28 | fmaterialmasterid | 物料业务策略主内码 | int8 | 64 |  | √ | 0 | 物料业务策略主内码 |
| 29 | finvunitid | finvunitid | int8 | 64 |  | √ | 0 |  |
| 30 | fqtyunit2nd | 期初辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初辅助数量 |
| 31 | fownerid | 入库货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 33 | fqtyinvunit | fqtyinvunit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 34 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 37 | fmaterialname | fmaterialname | varchar | 100 |  | √ | ' ' |  |
| 38 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 39 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 40 | fystartqtyunit2nd | 年初辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年初辅助数量 |
| 41 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 42 | funit2ndid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | funit2ndrate | funit2ndrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | fserialunitrate | fserialunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 45 | funit3rdrate | funit3rdrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | fystartbaseqty | 年初基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年初基本数量 |
| 47 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 48 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 49 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 50 | fysendqty | 年发出数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年发出数量 |
| 51 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 52 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 53 | fysendqtyunit3rd | 年发出辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 年发出辅助数量(2) |
| 54 | fyreceiveqty | 年收入数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年收入数量 |
| 55 | fyreceiveqtyunit3rd | 年收入辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 年收入辅助数量(2) |
| 56 | fysendbaseqty | 年发出基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年发出基本数量 |
| 57 | finvtypeid | 入库库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 58 | finvunitrate | finvunitrate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 59 | fentryorgid | fentryorgid | int8 | 64 |  | √ | 0 |  |
| 60 | fpriceunitid | fpriceunitid | int8 | 64 |  | √ | 0 |  |
| 61 | fyreceivebaseqty | 年收入基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年收入基本数量 |
| 62 | flocationid | 入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 63 | fstockindate | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |
| 64 | fqtyunit3rd | 期初辅助数量(2) | numeric | 23 | 10 | √ | 0.0000000000 | 期初辅助数量(2) |
| 65 | fentrycomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 66 | funit3rdid | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 67 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 68 | fbaseqty | 期初基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 期初基本数量 |
| 69 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 70 | fystartqty | 年初数量 | numeric | 23 | 10 | √ | 0.0000000000 | 年初数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_initbillentry_wh |  | fwarehouseid |
| 2 | idx_t_im_initbillentry_fid |  | fid |
| 3 | t_im_initbillentry_pkey |  | fentryid |
| 4 | idx_t_im_initbillentry_mmt |  | fmaterialmasterid |

---

## 初始库存单-主表 t_im_initbill

- **表名称：** 初始库存单-主表
- **表名：** t_im_initbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvdc | finvdc | varchar | 5 |  | √ | ' ' |  |
| 3 | foperatorid | 库管员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 4 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fheadwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fbizoperatorid | 业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 9 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fasyncstatus | 异步状态 | bpchar | 1 |  | √ | 'B' | 异步状态,枚举: A :处理中 B :已完成 |
| 13 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fdeptid | 库管部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 19 | foperatorgroupid | 库管组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fbizoperatorgroupid | 业务组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 24 | fbillcretype | 单据生成类型 | bpchar | 1 |  | √ | '0' | 单据生成类型,枚举: 0 :手工生成 1 :导入生成 2 :后台生成 3 :webApi生成 9 :迁移生成 |
| 25 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 27 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 28 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 29 | fbizdeptid | 业务部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_initbill_bktorgno |  | fbookdate,forgid,fbillno |
| 2 | idx_im_initbill_forgbillno |  | fbillno,forgid |
| 3 | t_im_initbill_pkey |  | fid |
| 4 | idx_im_initbill_org |  | forgid |
| 5 | idx_im_initbill_biztorgno |  | fbiztime,forgid,fbillno |

---

## 物料明细-分表 t_im_initbillentry_r

- **表名称：** 物料明细-分表
- **表名：** t_im_initbillentry_r

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 3 | fsrcsystem | 来源系统 | varchar | 100 |  | √ | ' ' | 来源系统 |
| 4 | fsrcsysbillentryid | 来源系统单据分录ID | varchar | 100 |  | √ | ' ' | 来源系统单据分录ID |
| 5 | flogisticsbill | 跨组织业务 | bpchar | 1 |  | √ | '0' | 跨组织业务 |
| 6 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 7 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fsrcbillentity | 来源单据实体 | varchar | 80 |  | √ | ' ' | 来源单据实体 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | fsrcsysbillid | 来源系统单据ID | varchar | 100 |  | √ | ' ' | 来源系统单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_initbillentry_r_fid |  | fid |
| 2 | t_im_initbillentry_r_pkey |  | fentryid |
