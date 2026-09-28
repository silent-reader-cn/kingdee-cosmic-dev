# 库存请检单-qcnp_invinspectplan

## 关联子实体-子表 t_qcnp_appinsentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcnp_appinsentry_lk

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
| 1 | pk_qcnp_appinsentry_lk |  | fpkid |
| 2 | idx_qcnp_appinsentry_lk_fk |  | fentryid |

---

## 物料信息-子表 t_qcnp_appinsentry

- **表名称：** 物料信息-子表
- **表名：** t_qcnp_appinsentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialcfgid | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 3 | fcheckcomstatus | 完成状态 | varchar | 5 |  | √ | ' ' | 完成状态,枚举: A :质检完成 B :进行中 C :计划 |
| 4 | fqualifqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 5 | fauxptyid | 辅助属性 (分录) | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fmainbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fownertypeid | 货主类型 (分录) | varchar | 255 |  | √ | ' ' | 货主类型 (分录),枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 9 | fqualifbaseqty | 合格数(基本) | numeric | 23 | 10 | √ | 0 | 合格数(基本) |
| 10 | fenshipmentsqty | 合格品发货数量 (分录) | numeric | 23 | 10 | √ | 0 | 合格品发货数量 (分录) |
| 11 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 13 | fenscrapqty | 检验报废数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验报废数量 (分录) |
| 14 | fenunshipmentsqty | 不合格可销售发货数量 (分录) | numeric | 23 | 10 | √ | 0 | 不合格可销售发货数量 (分录) |
| 15 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 16 | fassunitid | fassunitid | int8 | 64 |  | √ | 0 |  |
| 17 | fproductdate | 生产日期 (分录) | timestamp | 0 |  |  | null | 生产日期 (分录) |
| 18 | funqualifqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 19 | fenunshipmentsbaseqty | 不合格可销售发货基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 不合格可销售发货基本数量 (分录) |
| 20 | fkeeperid | 保管者 (分录) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | farrdate | 有效期至 (分录) | timestamp | 0 |  |  | null | 有效期至 (分录) |
| 23 | fenqualifiedbaseqty | 检验合格基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验合格基本数量 (分录) |
| 24 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 25 | fenfreezeqty | 检验冻结数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验冻结数量 (分录) |
| 26 | fincheck | 是否在检 | bpchar | 1 |  | √ | '0' | 是否在检 |
| 27 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 29 | fmainbillnumber | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 30 | finvqty | 可用库存数量 (分录) | numeric | 23 | 10 | √ | 0 | 可用库存数量 (分录) |
| 31 | fencheckqty | 请检冻结数量 (分录) | numeric | 23 | 10 | √ | 0 | 请检冻结数量 (分录) |
| 32 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | finvtargetstatus | 原库存状态（用于反审核恢复） | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 34 | funqualifbaseqty | 不合格数(基本) | numeric | 23 | 10 | √ | 0 | 不合格数(基本) |
| 35 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 36 | fenscrapbaseqty | 检验报废基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验报废基本数量 (分录) |
| 37 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 38 | fbattconvertqty | 形态转换数量（基本） | numeric | 23 | 10 | √ | 0 | 形态转换数量（基本） |
| 39 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 40 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fownerid | 货主 (分录) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | finvunitid | 库存单位 (分录) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fattconvertqty | 形态转换数量 | numeric | 23 | 10 | √ | 0 | 形态转换数量 |
| 44 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 45 | fenshipmentsbaseqty | 合格品发货基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 合格品发货基本数量 (分录) |
| 46 | fsrcbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 47 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 48 | fenfreezebaseqty | 检验冻结基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验冻结基本数量 (分录) |
| 49 | fbasejoinqty | 关联数量（基本） | numeric | 23 | 10 | √ | 0 | 关联数量（基本） |
| 50 | fmainbillentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 51 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 52 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 53 | fnewarrdate | fnewarrdate | timestamp | 0 |  |  | null |  |
| 54 | fencorrelationqty | 关联检验数量 (分录) | numeric | 23 | 10 | √ | 0 | 关联检验数量 (分录) |
| 55 | finvfrezstatus | 库存冻结状态 | varchar | 5 |  | √ | ' ' | 库存冻结状态,枚举: A :已冻结 |
| 56 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 57 | fisfrezzinv | 是否冻结库存 | varchar | 5 |  | √ | ' ' | 是否冻结库存,枚举: A :是 B :否 |
| 58 | fenunfreezeqty | 检验解冻数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验解冻数量 (分录) |
| 59 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 60 | fenunsalesbaseqty | 检验不合格可销售基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验不合格可销售基本数量 (分录) |
| 61 | fenunqualifiedqty | 检验不合格数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验不合格数量 (分录) |
| 62 | fmaterialinv | 物料库存 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 63 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 64 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 65 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 66 | fencheckbaseqty | 请检冻结基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 请检冻结基本数量 (分录) |
| 67 | fchecklibrary | 在库检验 | varchar | 1 |  | √ | '0' | 在库检验 |
| 68 | flotnumberid | 批号（新） | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 69 | finvtypeid | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 70 | fexeccasenum | 执行方案编码 | int8 | 64 |  | √ | 0 | [执行方案 qcbd_invimpschem](../qcbd_files/qcbd_invimpschem.md) |
| 71 | fcheckcomqty | 完成数量 | numeric | 23 | 10 | √ | 0 | 完成数量 |
| 72 | fbcheckcomqty | 完成数量（基本） | numeric | 23 | 10 | √ | 0 | 完成数量（基本） |
| 73 | fkeepertypeid | 保管者类型 (分录) | varchar | 255 |  | √ | ' ' | 保管者类型 (分录),枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 74 | fenunfreezebaseqty | 检验解冻基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验解冻基本数量 (分录) |
| 75 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 76 | fenunsalesqty | 检验不合格可销售数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验不合格可销售数量 (分录) |
| 77 | fenunqualifiedbaseqty | 检验不合格基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验不合格基本数量 (分录) |
| 78 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 79 | fmainbillentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |
| 80 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 81 | fresqty | 预留数量（分录） | numeric | 23 | 10 | √ | 0 | 预留数量（分录） |
| 82 | fapplyqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 83 | fenqualifiedqty | 检验合格数量 (分录) | numeric | 23 | 10 | √ | 0 | 检验合格数量 (分录) |
| 84 | fnowinvid | 即时库存ID | int8 | 64 |  | √ | 0 | 即时库存ID |
| 85 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 86 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 87 | fencorrelationbaseqty | 关联检验基本数量 (分录) | numeric | 23 | 10 | √ | 0 | 关联检验基本数量 (分录) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcnp_appiry_fmatcfg |  | fmaterialcfgid |
| 2 | idx_qcnp_appiry_fid |  | fid |
| 3 | idx_qcnp_appiry_fseq |  | fseq |
| 4 | idx_qcnp_appiry_fmat |  | fmaterialid |
| 5 | pk_qcnp_appinsentry |  | fentryid |

---

## 关联子实体-子表 t_qcnp_invapplyins_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcnp_invapplyins_lk

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
| 1 | idx_qcnp_invapplyins_lk_fk |  | fid |
| 2 | pk_qcnp_invapplyins_lk |  | fpkid |

---

## 库存请检单-主表 t_qcnp_invapplyins

- **表名称：** 库存请检单-主表
- **表名：** t_qcnp_invapplyins

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finspecorgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fapplytime | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fapplyuserid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fqualityorgid | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 18 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcnp_invapplyins |  | fid |
| 2 | idx_qcnp_invans_fbillno |  | fbillno |
| 3 | idx_qcnp_invans_fcreatetime |  | fcreatetime |

---

## 库存请检单-多语言表 t_qcnp_invapplyins_l

- **表名称：** 库存请检单-多语言表
- **表名：** t_qcnp_invapplyins_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcnp_invapplyins_l |  | fpkid |
| 2 | idx_qcnp_invansl_fid |  | fid,flocaleid |
| 3 | idx_qcnp_invansl_fcomment |  | fcomment |

---

## 库存请检单-反写记录表 t_qcnp_invapplyins_wb

- **表名称：** 库存请检单-反写记录表
- **表名：** t_qcnp_invapplyins_wb

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
| 1 | idx_qcnp_invapplyins_wb_fk |  | fid |
| 2 | pk_qcnp_invapplyins_wb |  | fentryid |

---

## 物料信息-分表 t_qcnp_appinsentry_q

- **表名称：** 物料信息-分表
- **表名：** t_qcnp_appinsentry_q

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 4 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcnp_appentry_q |  | fentryid |

---

## 库存请检单-关联追踪表 t_qcnp_invapplyins_tc

- **表名称：** 库存请检单-关联追踪表
- **表名：** t_qcnp_invapplyins_tc

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
| 1 | idx_qcnp_invapplyins_tc_tbill |  | ftbillid |
| 2 | idx_qcnp_invapplyins_tc_tid |  | ftid |
| 3 | pk_qcnp_invapplyins_tc |  | fid |

---

## 检验信息-子表 t_qcnp_applyinssub

- **表名称：** 检验信息-子表
- **表名：** t_qcnp_applyinssub

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnewarrdate | 新有效期至 | timestamp | 0 |  |  | null | 新有效期至 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdealqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 4 | fsninfo_tag | 反写序列号信息_详情 | text | 0 |  |  | null | 反写序列号信息_详情 |
| 5 | finspresult | 检验结果 | varchar | 5 |  | √ | '' | 检验结果,枚举: A :合格 B :不合格 |
| 6 | fhandmethodid | 处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 7 | fsninfo | 反写序列号信息 | varchar | 2000 |  | √ | ' ' | 反写序列号信息 |
| 8 | fdealqtybase | 检验数量（基本） | numeric | 23 | 10 | √ | 0 | 检验数量（基本） |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | finvmodqtybase | 库存调整数量（基本） | numeric | 23 | 10 | √ | 0 | 库存调整数量（基本） |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 12 | finvtargettype | 库存目标状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 13 | finvmodqty | 库存调整数量 | numeric | 23 | 10 | √ | 0 | 库存调整数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcnp_applub_fentryid |  | fentryid |
| 2 | pk_qcnp_applyinssub |  | fdetailid |
| 3 | idx_qcnp_applub_fseq |  | fseq |
