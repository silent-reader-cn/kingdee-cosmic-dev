# 委外调拨申请单-om_transapply

## 委外加工商-多选基础资料表 t_om_tappselsuppliers

- **表名称：** 委外加工商-多选基础资料表
- **表名：** t_om_tappselsuppliers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_tappselsuppliers |  | fpkid |
| 2 | idx_om_tappselsuppliers_fid |  | fid |

---

## 产品编码-多选基础资料表 t_om_tappselmaterials

- **表名称：** 产品编码-多选基础资料表
- **表名：** t_om_tappselmaterials

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_tappselmtrls_fid |  | fid |
| 2 | pk_om_tappselmaterials |  | fpkid |

---

## 工单明细-子表 t_om_tapporderentrys

- **表名称：** 工单明细-子表
- **表名：** t_om_tapporderentrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 备料套数 | numeric | 23 | 10 | √ | 0 | 备料套数 |
| 3 | fkittingqty | 齐套数量 | numeric | 23 | 10 | √ | 0 | 齐套数量 |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | forderid | 委外工单F7 | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |
| 6 | forderqty | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | forderno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 10 | forderentryseq | 委外工单行号 | varchar | 30 |  | √ | '0' | 委外工单行号 |
| 11 | funit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | forderentryid | 委外工单分录F7 | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_tapporderentrys |  | fentryid |
| 2 | idx_om_tapporderentry_fid |  | fid |

---

## 委外工单-多选基础资料表 t_om_tappselorders

- **表名称：** 委外工单-多选基础资料表
- **表名：** t_om_tappselorders

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_tappselorders_fid |  | fid |
| 2 | pk_om_tappselorders |  | fpkid |

---

## 物料明细-子表 t_om_tappmaterialentrys

- **表名称：** 物料明细-子表
- **表名：** t_om_tappmaterialentrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 5 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fbaseapplyqty | 申请基本数量 | numeric | 23 | 10 | √ | 0 | 申请基本数量 |
| 7 | fbasepushedqty | 已调基本数量 | numeric | 23 | 10 | √ | 0 | 已调基本数量 |
| 8 | facctqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 9 | finvtype | 调出库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 10 | fbaseremainqty | 未调拨基本数量 | numeric | 23 | 10 | √ | 0 | 未调拨基本数量 |
| 11 | fownertype | 调出货主类型 | varchar | 36 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 12 | flot | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 13 | fininvstatus | 调入库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 14 | fppbomid | 用料清单F7 | int8 | 64 |  | √ | 0 | [委外用料清单f7 om_mftstock_headf7](../om_files/om_mftstock_headf7.md) |
| 15 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 18 | finowner | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | finorgunit | 调入组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fininvtype | 调入库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 21 | fsumentryid | 汇总行内码 | int8 | 64 |  | √ | 0 | 汇总行内码 |
| 22 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 23 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 24 | fmaterialinvinfo | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 25 | foutinvstatus | 调出库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 26 | flinetype | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 27 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fbaseacctqty | 实发基本数量 | numeric | 23 | 10 | √ | 0 | 实发基本数量 |
| 30 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | fremainqty | 未调拨数量 | numeric | 23 | 10 | √ | 0 | 未调拨数量 |
| 32 | fbasejoinqty | 关联调拨基本数量 | numeric | 23 | 10 | √ | 0 | 关联调拨基本数量 |
| 33 | finvmatunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 34 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 35 | forderentryid | 委外工单分录F7 | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |
| 36 | fauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 38 | fjoinqty | 关联调拨数量 | numeric | 23 | 10 | √ | 0 | 关联调拨数量 |
| 39 | foutorgunitid | 调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fsubmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 41 | finlocationid | 调入仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 42 | fauxunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 44 | fowner | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fchildauxpropertid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 46 | fsubmatunitqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 47 | fppbomentryid | 用料清单分录f7 | int8 | 64 |  | √ | 0 | [委外用料清单分录f7 om_mftstockf7](../om_files/om_mftstockf7.md) |
| 48 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 49 | fapplyqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 50 | fpushedqty | 已调数量 | numeric | 23 | 10 | √ | 0 | 已调数量 |
| 51 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 52 | finownertype | 调入货主类型 | varchar | 36 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_tappmaterialentrys |  | fentryid |
| 2 | idx_om_tappmatentry_fid |  | fid |

---

## 委外调拨申请单-多语言表 t_om_transapply_l

- **表名称：** 委外调拨申请单-多语言表
- **表名：** t_om_transapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_transapply_l_fid |  | fid |
| 2 | pk_om_transapply_l |  | fpkid |

---

## 物料汇总-子表 t_om_tappsumentrys

- **表名称：** 物料汇总-子表
- **表名：** t_om_tappsumentrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 5 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fbasepushedqty | 已调基本数量 | numeric | 23 | 10 | √ | 0 | 已调基本数量 |
| 7 | facctqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 8 | fsupplier | 委外加工商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | finvtype | 调出库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 10 | fbaseremainqty | 未调拨基本数量 | numeric | 23 | 10 | √ | 0 | 未调拨基本数量 |
| 11 | fownertype | 调出货主类型 | varchar | 36 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 12 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 13 | flot | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 14 | fininvstatus | 调入库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 15 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 17 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 18 | finowner | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | finorgunit | 调入组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fininvtype | 调入库存类型 | int8 | 64 |  | √ | 0 | [库存类型 bd_invtype](../sbd_files/bd_invtype.md) |
| 21 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 22 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 23 | fmaterialinvinfo | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 24 | foutinvstatus | 调出库存状态 | int8 | 64 |  | √ | 0 | [库存状态 bd_invstatus](../sbd_files/bd_invstatus.md) |
| 25 | flinetype | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 26 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fbasesupplierinvqty | 供应商可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 供应商可用库存基本数量 |
| 29 | fbaseacctqty | 实发基本数量 | numeric | 23 | 10 | √ | 0 | 实发基本数量 |
| 30 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | fremainqty | 未调拨数量 | numeric | 23 | 10 | √ | 0 | 未调拨数量 |
| 32 | fbaseneedtransqty | 需调基本数量 | numeric | 23 | 10 | √ | 0 | 需调基本数量 |
| 33 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 34 | fbasejoinqty | 关联调拨基本数量 | numeric | 23 | 10 | √ | 0 | 关联调拨基本数量 |
| 35 | fsupplierinvqty | 供应商可用库存数量 | numeric | 23 | 10 | √ | 0 | 供应商可用库存数量 |
| 36 | fbaseintransitqty | 在途基本数量 | numeric | 23 | 10 | √ | 0 | 在途基本数量 |
| 37 | finvmatunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 38 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 39 | fauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | finwarehouseid | 调入仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 41 | fjoinqty | 关联调拨数量 | numeric | 23 | 10 | √ | 0 | 关联调拨数量 |
| 42 | fneedtransqty | 需调数量 | numeric | 23 | 10 | √ | 0 | 需调数量 |
| 43 | foutorgunitid | 调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fsugtransqty | 本次建议调拨数量 | numeric | 23 | 10 | √ | 0 | 本次建议调拨数量 |
| 45 | fintransitqty | 在途数量 | numeric | 23 | 10 | √ | 0 | 在途数量 |
| 46 | finlocationid | 调入仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 47 | fauxunit2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 48 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 49 | fowner | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 50 | fsubmatunitqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 51 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 52 | fapplyqty | 申请数量 | numeric | 23 | 10 | √ | 0 | 申请数量 |
| 53 | fpushedqty | 已调数量 | numeric | 23 | 10 | √ | 0 | 已调数量 |
| 54 | fbasesugtransqty | 本次建议调拨基本数量 | numeric | 23 | 10 | √ | 0 | 本次建议调拨基本数量 |
| 55 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 56 | finownertype | 调入货主类型 | varchar | 36 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_tappsumentrys |  | fentryid |
| 2 | idx_om_tappsumentrys_fid |  | fid |

---

## 委外调拨申请单-主表 t_om_transapply

- **表名称：** 委外调拨申请单-主表
- **表名：** t_om_transapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fanalysed | 已分析 | bpchar | 1 |  | √ | '0' | 已分析 |
| 3 | fclosetype | 关闭类型 | varchar | 10 |  | √ | '0' | 关闭类型,枚举: 0 :自动关闭 1 :手工关闭 |
| 4 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fclosedate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 7 | fproirity | 优先顺序 | varchar | 10 |  | √ | '0' | 优先顺序,枚举: 0 :需求日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 10 | fsupplier | fsupplier | int8 | 64 |  | √ | 0 |  |
| 11 | ftranspolicy | 调拨策略 | varchar | 10 |  | √ | '0' | 调拨策略,枚举: 0 :补足供应商库存 |
| 12 | fplanbegindates | 计划开工日期.开始 | timestamp | 0 |  |  | null | 计划开工日期.开始 |
| 13 | fintransit | 考虑在途 | bpchar | 1 |  | √ | '1' | 考虑在途 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fpushtype | 调拨方式 | varchar | 10 |  | √ | '0' | 调拨方式,枚举: 0 :按明细调拨 1 :按汇总调拨 |
| 16 | fmaterialscope | 物料范围 | varchar | 10 |  | √ | '0' | 物料范围,枚举: 0 :全部物料 1 :倒冲物料 2 :非倒冲物料 3 :关键物料 |
| 17 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 18 | fmaterial | fmaterial | int8 | 64 |  | √ | 0 |  |
| 19 | fcloserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fplanenddates | 计划完工日期.开始 | timestamp | 0 |  |  | null | 计划完工日期.开始 |
| 24 | fbillstatus | 单据状态 | varchar | 10 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fplanbegindatee | 计划开工日期.结束 | timestamp | 0 |  |  | null | 计划开工日期.结束 |
| 26 | finventory | 考虑存量 | bpchar | 1 |  | √ | '1' | 考虑存量 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fdept | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fclosestatus | 关闭状态 | varchar | 10 |  | √ | '0' | 关闭状态,枚举: 0 :正常 1 :已关闭 |
| 33 | fplanenddatee | 计划完工日期.结束 | timestamp | 0 |  |  | null | 计划完工日期.结束 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_transapply_billno |  | fbillno |
| 2 | idx_om_transapply_date |  | fdate |
| 3 | pk_om_transapply |  | fid |
