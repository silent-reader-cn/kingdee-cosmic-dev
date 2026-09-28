# 委外用料计划处理-om_mftstockplan

## 组件明细-子表 t_om_stockplanentry

- **表名称：** 组件明细-子表
- **表名：** t_om_stockplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [BOM版本 bd_bomversion](../basedata_files/bd_bomversion.md) |
| 3 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | fpriority | 替代优先级 | int4 | 32 |  | √ | 0 | 替代优先级 |
| 6 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 7 | fissuemode | 领送料方式 | varchar | 30 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 8 | flocation | 供货仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 11 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 12 | fentryconfiguredcodeid | 组件配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 13 | foutsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 16 | freplaceplan | 组件替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 17 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 18 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 19 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 20 | fworkplanid | 工序计划分录ID | int8 | 64 |  | √ | 0 | 工序计划分录ID |
| 21 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 22 | foutorgunitid | 调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0 | 提前期偏置(天) |
| 24 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 25 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 26 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 27 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 28 | fqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 29 | fqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 30 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 31 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 32 | fchildbomid | 子项BOM | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 mpdm_mftbomtpl |
| 33 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 36 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 37 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 38 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 39 | fsupplymode | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org : bd_customer :客户 bd_supplier :供应商 |
| 40 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 41 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 42 | fchildbomversion | 子项BOM版本 | varchar | 50 |  | √ | ' ' | 子项BOM版本 |
| 43 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 44 | fdemandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 45 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_stocry_fseq |  | fseq |
| 2 | idx_om_stocry_fsrcbillentryid |  | fsrcbillid,fsrcbillentryid |
| 3 | idx_om_stocry_matmasterid |  | fmaterialid,fmaterielmasterid |
| 4 | idx_om_stocry_fid |  | fid |
| 5 | pk_t_om_stockplanentry |  | fentryid |

---

## 委外用料计划处理-主表 t_om_mftstockplan

- **表名称：** 委外用料计划处理-主表
- **表名：** t_om_mftstockplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 10 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fbomid | BOM | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 mpdm_mftbomtpl |
| 12 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fmftdeptorgid | fmftdeptorgid | int8 | 64 |  | √ | 0 |  |
| 27 | fpurapplyseq | 采购申请行号 | varchar | 50 |  | √ | ' ' | 采购申请行号 |
| 28 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 29 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 30 | fpurapplybillid | 采购申请单号 | int8 | 64 |  | √ | 0 | [委外采购申请单f7 om_outpurapplybill_f7](../om_files/om_outpurapplybill_f7.md) |
| 31 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 32 | fbillauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_om_mftstockplan |  | fid |
| 2 | idx_om_mftspl_purapplyid |  | fpurapplybillid |
| 3 | idx_om_mftpsan_createtime |  | fcreatetime |
| 4 | idx_om_mftsan_fbillno |  | fbillno |
| 5 | idx_om_mftspl_pmsterialid |  | fmaterialid,fproductmasterid |

---

## 委外用料计划处理-多语言表 t_om_mftstockplan_l

- **表名称：** 委外用料计划处理-多语言表
- **表名：** t_om_mftstockplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mftsanl_fid |  | fid,flocaleid |
| 2 | pk_t_om_mftstockplan_l |  | fpkid |

---

## 组件明细-多语言表 t_om_stockplanentry_l

- **表名称：** 组件明细-多语言表
- **表名：** t_om_stockplanentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fchildremarks | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fsetuplocation | 安装位置 | varchar | 100 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_stocryl_fentryid |  | fentryid,flocaleid |
| 2 | pk_t_om_stockplanentry_l |  | fpkid |
