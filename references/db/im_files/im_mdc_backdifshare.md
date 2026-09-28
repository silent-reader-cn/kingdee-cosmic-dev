# 领料差异分摊（废弃）-im_mdc_backdifshare

## 领料差异分摊（废弃）-主表 t_im_mdc_backdifshare

- **表名称：** 领料差异分摊（废弃）-主表
- **表名：** t_im_mdc_backdifshare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmftdept | fmftdept | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fisassagin | 是否生成 | bpchar | 1 |  | √ | '0' | 是否生成 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | finvorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | faccessnode | faccessnode | varchar | 10 |  | √ | 'start' |  |
| 10 | fisrelchildmaterial | 工单关联子项物料 | bpchar | 1 |  | √ | '0' | 工单关联子项物料 |
| 11 | fpushnum | 下推条数 | int8 | 64 |  | √ | 500 | 下推条数 |
| 12 | fsharedate | 分摊日期 | timestamp | 0 |  |  | null | 分摊日期 |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | findateend | 入库期间.结束 | timestamp | 0 |  |  | null | 入库期间.结束 |
| 15 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | findatestart | 入库期间.开始 | timestamp | 0 |  |  | null | 入库期间.开始 |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fisshare | 是否分摊 | bpchar | 1 |  | √ | '0' | 是否分摊 |
| 21 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 22 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | finvquerycondition | finvquerycondition | varchar | 5 |  | √ | 'A' |  |
| 24 | finvdate | finvdate | timestamp | 0 |  |  | null |  |
| 25 | fematerial | 物料编码至 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 26 | fexcludeenddate | fexcludeenddate | bpchar | 1 |  | √ | '1' |  |
| 27 | fbasedatafield | fbasedatafield | int8 | 64 |  | √ | 0 |  |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_backdifshare |  | fid |
| 2 | idx_t_im_mdc_backdifshare |  | fbillno |

---

## 仓位-多选基础资料表 t_im_mdc_location

- **表名称：** 仓位-多选基础资料表
- **表名：** t_im_mdc_location

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_im_mdc_location_mul |  | fid |
| 2 | pk_t_im_mdc_location |  | fpkid |

---

## 仓库-多选基础资料表 t_im_mdc_warehouse

- **表名称：** 仓库-多选基础资料表
- **表名：** t_im_mdc_warehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_warehouse |  | fpkid |
| 2 | idx_t_im_mdc_warehouse_mul |  | fid |

---

## 生产工单-子表 t_im_mdc_mftbackdifshare

- **表名称：** 生产工单-子表
- **表名：** t_im_mdc_mftbackdifshare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fordernum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | finbasenum | 入库基本数量 | numeric | 23 | 10 | √ | 0 | 入库基本数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbasenum | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 6 | fconfiguredcodeid | 配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 7 | forderno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 8 | forderentryid | 生产工单行f7 | int8 | 64 |  | √ | 0 | [生产工单分录f7 im_mdc_mftorderf7](../im_files/im_mdc_mftorderf7.md) |
| 9 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 10 | fordmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 11 | forderunit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fdifshare1 | 分摊 | bpchar | 1 |  | √ | '0' | 分摊 |
| 13 | forderbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_mftbackdifshare |  | fentryid |
| 2 | idx_t_im_mdc_mftbackdifshare |  | fid |

---

## 物料编码从-多选基础资料表 t_im_mdc_material

- **表名称：** 物料编码从-多选基础资料表
- **表名：** t_im_mdc_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_material |  | fpkid |
| 2 | idx_t_im_mdc_material_mul |  | fid |

---

## 班次-多选基础资料表 t_im_mdc_mulshift

- **表名称：** 班次-多选基础资料表
- **表名：** t_im_mdc_mulshift

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [班次 mpdm_workshifts](../mpdm_files/mpdm_workshifts.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_mulshift |  | fpkid |
| 2 | idx_t_im_mdc_mulshift_mul |  | fid |

---

## 库存信息-子表 t_im_mdc_invbackdifshare

- **表名称：** 库存信息-子表
- **表名：** t_im_mdc_invbackdifshare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fassignstauts | 生成状态 | varchar | 50 |  | √ | ' ' | 生成状态,枚举: A :未生成 B :部分生成 C :完全生成 |
| 5 | foutownerid | foutownerid | int8 | 64 |  | √ | 0 |  |
| 6 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 7 | flocation2 | flocation2 | int8 | 64 |  | √ | 0 |  |
| 8 | finvdatenum | finvdatenum | numeric | 23 | 10 | √ | 0 |  |
| 9 | finvtype | 库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 10 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 11 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fisadd | 手工新增 | bpchar | 1 |  | √ | '0' | 手工新增 |
| 13 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 14 | fdifnum | 差异数量 | numeric | 23 | 10 | √ | 0 | 差异数量 |
| 15 | foutkeeperid | foutkeeperid | int8 | 64 |  | √ | 0 |  |
| 16 | fwaitsharenum | 待分摊数量 | numeric | 23 | 10 | √ | 0 | 待分摊数量 |
| 17 | fbusinvassignnum | fbusinvassignnum | numeric | 23 | 10 | √ | 0 |  |
| 18 | fischange | 盘点值改变 | bpchar | 1 |  | √ | '0' | 盘点值改变 |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | funitfield | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 22 | finvaccnum | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |
| 23 | foutinvstatusid | foutinvstatusid | int8 | 64 |  | √ | 0 |  |
| 24 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fbusinvaccnum | fbusinvaccnum | numeric | 23 | 10 | √ | 0 |  |
| 26 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 28 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | flicenseno | flicenseno | int8 | 64 |  | √ | 0 |  |
| 31 | fassignnum | 已生成数量 | numeric | 23 | 10 | √ | 0 | 已生成数量 |
| 32 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 33 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 34 | fbuswaitsharenum | fbuswaitsharenum | numeric | 23 | 10 | √ | 0 |  |
| 35 | fbusinventorynum | fbusinventorynum | numeric | 23 | 10 | √ | 0 |  |
| 36 | fbusunitid | fbusunitid | int8 | 64 |  | √ | 0 |  |
| 37 | foutkeepertype | foutkeepertype | varchar | 50 |  | √ | ' ' |  |
| 38 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 39 | factissueqty | factissueqty | numeric | 23 | 10 | √ | 0 |  |
| 40 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 41 | fbusdifnum | fbusdifnum | numeric | 23 | 10 | √ | 0 |  |
| 42 | fsharestatus | 分摊状态 | varchar | 50 |  | √ | ' ' | 分摊状态,枚举: A :未分摊 B :部分分摊 C :完全分摊 |
| 43 | fqtyfield5 | fqtyfield5 | numeric | 23 | 10 | √ | 0 |  |
| 44 | fdifshare | 分摊 | bpchar | 1 |  | √ | '0' | 分摊 |
| 45 | foutownertype | foutownertype | varchar | 50 |  | √ | ' ' |  |
| 46 | finventory | 盘点数量 | numeric | 23 | 10 | √ | 0 | 盘点数量 |
| 47 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 48 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 49 | fcansendqty | fcansendqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | finvstatus | finvstatus | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_im_mdc_invbackdifshare |  | fentryid |
| 2 | idx_t_im_mdc_invback_a |  | fid |
