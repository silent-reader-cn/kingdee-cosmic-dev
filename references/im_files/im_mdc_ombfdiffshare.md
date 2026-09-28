# 委外领料差异分摊-im_mdc_ombfdiffshare

## 委外领料差异分摊-主表 t_im_mdc_omdifshare

- **表名称：** 委外领料差异分摊-主表
- **表名：** t_im_mdc_omdifshare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | findatestart | 入库期间.开始 | timestamp | 0 |  |  | null | 入库期间.开始 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fisshare | 是否分摊 | bpchar | 1 |  | √ | ' ' | 是否分摊 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fisassagin | 是否生成 | bpchar | 1 |  | √ | ' ' | 是否生成 |
| 11 | fproducedept | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fsupplierid | 委外加工商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fematerial | 物料编码至 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | finvorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fisrelchildmaterial | 工单关联子项物料 | bpchar | 1 |  | √ | '0' | 工单关联子项物料 |
| 18 | fpushnum | 下推条数 | int8 | 64 |  | √ | 0 | 下推条数 |
| 19 | fsharedate | 分摊日期 | timestamp | 0 |  |  | null | 分摊日期 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 23 | findateend | 入库期间.结束 | timestamp | 0 |  |  | null | 入库期间.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omdifshare |  | fid |
| 2 | idx_im_mdc_omdifshare_billno |  | fbillno |

---

## 仓位-多选基础资料表 t_im_mdc_location

- **表名称：** 仓位-多选基础资料表
- **表名：** t_im_mdc_location

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 仓位 bd_location |
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

## 分摊明细-子表 t_im_mdc_omdifshareentry

- **表名称：** 分摊明细-子表
- **表名：** t_im_mdc_omdifshareentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmadebasenum | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 3 | fassignnum | 已生成数量 | numeric | 23 | 10 | √ | 0 | 已生成数量 |
| 4 | fsharenum | 应分摊数量 | numeric | 23 | 10 | √ | 0 | 应分摊数量 |
| 5 | fshinvtype | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 6 | fshproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 7 | fshorderentryid | 委外工单行f7 | int8 | 64 |  | √ | 0 | 委外工单分录F7 om_mftorder_f7 |
| 8 | fsharebasenum | 应分摊基本数量 | numeric | 23 | 10 | √ | 0 | 应分摊基本数量 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fshbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fassignstauts | 生成情况 | varchar | 50 |  | √ | ' ' | 生成情况,枚举: A :未生成 C :已生成 |
| 12 | fshauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fshinvstatus | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 14 | fdiffshareremark_tag | 分摊描述_详情 | text | 0 |  |  | null | 分摊描述_详情 |
| 15 | fshexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 16 | fshstockno | 委外用料清单编号 | varchar | 50 |  | √ | ' ' | 委外用料清单编号 |
| 17 | fpickbasenum | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 18 | fsharestatus | 分摊情况 | varchar | 50 |  | √ | ' ' | 分摊情况,枚举: A :未分摊 B :部分分摊 C :完全分摊 |
| 19 | fshisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 20 | fshmaterial | 子项物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 21 | finvunit | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fshwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 23 | fshownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 24 | fshkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 25 | fshkeeper | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fshowner | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fstockid | 委外用料清单id | int8 | 64 |  | √ | 0 | 委外用料清单id |
| 28 | factsharebasenum | 实际分摊基本数量 | numeric | 23 | 10 | √ | 0 | 实际分摊基本数量 |
| 29 | fstockentryid | 委外用料清单分录id | int8 | 64 |  | √ | 0 | 委外用料清单分录id |
| 30 | fassignremark | 生成描述 | varchar | 255 |  | √ | ' ' | 生成描述 |
| 31 | fshproject | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 32 | factsharenum | 实际分摊数量 | numeric | 23 | 10 | √ | 0 | 实际分摊数量 |
| 33 | fshqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 34 | fshlotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 35 | fshmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 36 | fdiffshareremark | 分摊描述 | varchar | 255 |  | √ | ' ' | 分摊描述 |
| 37 | fassignremark_tag | 生成描述_详情 | text | 0 |  |  | null | 生成描述_详情 |
| 38 | fshorderno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 39 | fshlocation2 | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fshdiffshareid | 库存信息分录id | int8 | 64 |  | √ | 0 | 库存信息分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omdifshareentry |  | fentryid |
| 2 | idx_im_mdc_omdifshareentry_fid |  | fid |

---

## 仓库-多选基础资料表 t_im_mdc_warehouse

- **表名称：** 仓库-多选基础资料表
- **表名：** t_im_mdc_warehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
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

## 物料编码从-多选基础资料表 t_im_mdc_material

- **表名称：** 物料编码从-多选基础资料表
- **表名：** t_im_mdc_material

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 班次 mpdm_workshifts |
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

## 工单信息-子表 t_im_mdc_omdiforderentry

- **表名称：** 工单信息-子表
- **表名：** t_im_mdc_omdiforderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fordernum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 3 | finbasenum | 入库基本数量 | numeric | 23 | 10 | √ | 0 | 入库基本数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 6 | fbasenum | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 7 | forderno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 8 | forderentryid | 委外工单行f7 | int8 | 64 |  | √ | 0 | 委外工单分录F7 om_mftorder_f7 |
| 9 | fordmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 10 | forderunit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fdifshare1 | 分摊 | bpchar | 1 |  | √ | ' ' | 分摊 |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 13 | forderbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omdiforderentry |  | fentryid |
| 2 | idx_im_mdc_omdiforderentry_fid |  | fid |

---

## 库存信息-子表 t_im_mdc_omdifinventry

- **表名称：** 库存信息-子表
- **表名：** t_im_mdc_omdifinventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassignnum | 已生成数量 | numeric | 23 | 10 | √ | 0 | 已生成数量 |
| 3 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fassignstauts | 生成状态 | varchar | 50 |  | √ | ' ' | 生成状态,枚举: A :未生成 B :部分生成 C :完全生成 |
| 9 | finvstatusid | 库存状态 | int8 | 64 |  | √ | 0 | 库存状态 bd_invstatus |
| 10 | finvtype | 库存类型 | int8 | 64 |  | √ | 0 | 库存类型 bd_invtype |
| 11 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 13 | fkeeperid | 保管者 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fsharestatus | 分摊状态 | varchar | 50 |  | √ | ' ' | 分摊状态,枚举: A :未分摊 B :部分分摊 C :完全分摊 |
| 15 | fisadd | 手工新增 | bpchar | 1 |  | √ | ' ' | 手工新增 |
| 16 | fdifnum | 差异数量 | numeric | 23 | 10 | √ | 0 | 差异数量 |
| 17 | fwaitsharenum | 待分摊数量 | numeric | 23 | 10 | √ | 0 | 待分摊数量 |
| 18 | fdifshare | 分摊 | bpchar | 1 |  | √ | ' ' | 分摊 |
| 19 | fischange | 盘点值改变 | bpchar | 1 |  | √ | ' ' | 盘点值改变 |
| 20 | finventory | 盘点数量 | numeric | 23 | 10 | √ | 0 | 盘点数量 |
| 21 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 22 | fkeepertype | 保管者类型 | varchar | 50 |  | √ | ' ' | 保管者类型,枚举: bos_org :库存组织 bd_supplier :供应商 bd_customer :客户 |
| 23 | funitfield | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | finvaccnum | 即时库存 | numeric | 23 | 10 | √ | 0 | 即时库存 |
| 25 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 26 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 28 | fexpirydate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 29 | fproject | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fproducedate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_im_mdc_omdifinventry |  | fentryid |
| 2 | idx_im_mdc_omdifinventry_fid |  | fid |
