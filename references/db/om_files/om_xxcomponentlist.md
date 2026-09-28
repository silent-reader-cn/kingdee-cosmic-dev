# 简单委外组件清单变更单（废弃）-om_xxcomponentlist

## 组件明细-多语言表 t_om_xxcomponententry_l

- **表名称：** 组件明细-多语言表
- **表名：** t_om_xxcomponententry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fchildremarks | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fsetuplocation | 安装位置 | varchar | 100 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_xxcomponententry_l |  | fpkid |
| 2 | idx_t_om_xxcomponententry_l |  | fentryid,flocaleid |

---

## 组件明细-子表 t_om_xxcomponententry

- **表名称：** 组件明细-子表
- **表名：** t_om_xxcomponententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funissueqty | 未领基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未领基本数量 |
| 3 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 4 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fwastagerateformula | 损耗计算公式 | varchar | 50 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） C : |
| 6 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 标准基本数量 |
| 7 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 8 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 9 | flocation | 供货仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 12 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 13 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fworkplanid | 工序计划分录ID | int8 | 64 |  | √ | 0 | 工序计划分录ID |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 16 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 17 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 18 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 使用比例(%) |
| 20 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 21 | fqtydenominator | 分母 | numeric | 23 | 10 | √ | 0.0000000000 | 分母 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fchildbomid | 子项BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 24 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fstockentryid | fstockentryid | varchar | 50 |  | √ | ' ' |  |
| 27 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 28 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 29 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 30 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fchildbomversion | 子项BOM版本 | varchar | 50 |  | √ | ' ' | 子项BOM版本 |
| 32 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 35 | foutqty | 下推领料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推领料基本数量 |
| 36 | freservebaseqty | 库存预留基本数量 | numeric | 23 | 10 | √ | 0 | 库存预留基本数量 |
| 37 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 38 | fconfiguredcodeid | 产品配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 39 | fentryconfiguredcodeid | 组件配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 40 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 41 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 42 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 43 | fuseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已消耗基本数量 |
| 44 | factissueqty | 实发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 实发基本数量 |
| 45 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 46 | foutorgunitid | 调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | favbbaseqty | 库存可用基本数量 | numeric | 23 | 10 | √ | 0 | 库存可用基本数量 |
| 48 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 49 | fqtynumerator | 分子 | numeric | 23 | 10 | √ | 0.0000000000 | 分子 |
| 50 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 51 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 52 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 53 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 54 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_om_xxcomponententry |  | fid |
| 2 | pk_om_xxcomponententry |  | fentryid |

---

## 组件明细-分表 t_om_xxcomponententry_b

- **表名称：** 组件明细-分表
- **表名：** t_om_xxcomponententry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fislead | 是否引入 | bpchar | 1 |  | √ | '0' | 是否引入 |
| 3 | fstockentryseq | 委外组件清单行号 | varchar | 50 |  | √ | ' ' | 委外组件清单行号 |
| 4 | fproducttransid | 委外事务类型 | int8 | 64 |  | √ | 0 | 简单委外事务类型 mpdm_transactout |
| 5 | fproductbaseunit | 产品基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 6 | fstockid | 委外组件清单ID | varchar | 50 |  | √ | ' ' | 委外组件清单ID |
| 7 | fentryproductid | 产品编码 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 8 | fentryorderentryid | 委外订单行id | int8 | 64 |  | √ | 0 | 委外订单分录f7 om_outsourcef7 |
| 9 | fstockentryid | 委外组件清单分录ID | varchar | 50 |  | √ | ' ' | 委外组件清单分录ID |
| 10 | fstockno | 委外组件清单编号 | varchar | 50 |  | √ | ' ' | 委外组件清单编号 |
| 11 | fcomponentlistnnum | fcomponentlistnnum | varchar | 50 |  | √ | ' ' |  |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 13 | fproductbaseqty | 产品基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 产品基本数量 |
| 14 | fcomponentno | 委外订单号 | varchar | 50 |  | √ | ' ' | 委外订单号 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 16 | fcomponentlistentryseq | fcomponentlistentryseq | varchar | 50 |  | √ | ' ' |  |
| 17 | fentryproductqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_xxcomponententry_b |  | fentryid |
| 2 | idx_t_om_xxcomponententry_b |  | fid |

---

## 组件明细-分表 t_om_xxcomponententry_a

- **表名称：** 组件明细-分表
- **表名：** t_om_xxcomponententry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fallotqty | 调拨基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调拨基本数量 |
| 3 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 4 | fbackflushtime | 倒冲时机 | varchar | 50 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :汇报倒冲 |
| 5 | ffeedingqty | 补料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 补料基本数量 |
| 6 | fpromaterentryid | 工序物料分配分录ID | int8 | 64 |  | √ | 0 | 工序物料分配分录ID |
| 7 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 8 | freplaceplan | 组件替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 9 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 11 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0.0000000000 | 提前期偏置(天) |
| 12 | foverissuecontrl | 超发控制 | varchar | 50 |  | √ | ' ' | 超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 13 | fissinlowlimit | 领料下限允差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 领料下限允差(%) |
| 14 | fissinhighlimit | 领料上限允差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 领料上限允差(%) |
| 15 | fscrapqty | 报废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废基本数量 |
| 16 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 17 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 18 | fisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 19 | flackraitioqty | 领料下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 领料下限基本数量 |
| 20 | frejectedqty | 退料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 退料基本数量 |
| 21 | fentrychangestatus | 变更类型 | varchar | 50 |  | √ | ' ' | 变更类型,枚举: A :新增 B :变更前 C :变更后 |
| 22 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 23 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 在制基本数量 |
| 24 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 领料上限基本数量 |
| 25 | fcansendqty | 可发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 可发基本数量 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_om_xxcomponententry_a |  | fid |
| 2 | pk_om_xxcomponententry_a |  | fentryid |

---

## 关联子实体-子表 t_om_component_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_component_lk

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
| 1 | pk_om_component_lk |  | fpkid |
| 2 | idx_om_component_lk_fk |  | fid |

---

## 简单委外组件清单变更单（废弃）-反写记录表 t_om_xxcomponentlist_wb

- **表名称：** 简单委外组件清单变更单（废弃）-反写记录表
- **表名：** t_om_xxcomponentlist_wb

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
| 1 | pk_om_xxcomponentlist_wb |  | fentryid |
| 2 | idx_om_xxcomponentlist_wb_fk |  | fid |

---

## 简单委外组件清单变更单（废弃）-主表 t_om_xxcomponentlist

- **表名称：** 简单委外组件清单变更单（废弃）-主表
- **表名：** t_om_xxcomponentlist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料采购信息 bd_materialpurchaseinfo |
| 4 | forgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forderid | 委外订单ID | varchar | 50 |  | √ | ' ' | 委外订单ID |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fconfiguredcodeid | 产品配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 8 | forderentryid | 委外订单行号 | int8 | 64 |  | √ | 0 | 委外订单分录f7 om_outsourcef7 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ftextfield | 变更原因 | varchar | 50 |  | √ | ' ' | 变更原因 |
| 11 | fomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 12 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 14 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 15 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fischanged | 是否存在未审核变更单 | bpchar | 1 |  | √ | '0' | 是否存在未审核变更单 |
| 25 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 32 | forderno | 委外订单编号 | varchar | 50 |  | √ | ' ' | 委外订单编号 |
| 33 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 mpdm_processroute |
| 34 | fmftinqty | 最新完工入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 最新完工入库数量 |
| 35 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 36 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 37 | fbillauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_om_xxcomponentlist |  | fbillno |
| 2 | pk_om_xxcomponentlist |  | fid |

---

## 简单委外组件清单变更单（废弃）-多语言表 t_om_xxcomponentlist_l

- **表名称：** 简单委外组件清单变更单（废弃）-多语言表
- **表名：** t_om_xxcomponentlist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_om_xxcomponentlist_l |  | fid,flocaleid |
| 2 | pk_om_xxcomponentlist_l |  | fpkid |

---

## 简单委外组件清单变更单（废弃）-关联追踪表 t_om_xxcomponentlist_tc

- **表名称：** 简单委外组件清单变更单（废弃）-关联追踪表
- **表名：** t_om_xxcomponentlist_tc

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
| 1 | idx_om_xxcomponentlist_tc_tid |  | ftid |
| 2 | pk_om_xxcomponentlist_tc |  | fid |
| 3 | idx_om_xxcomponentlist_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_om_componententry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_componententry_lk

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
| 1 | pk_om_componententry_lk |  | fpkid |
| 2 | idx_om_componententry_lk_fk |  | fentryid |
