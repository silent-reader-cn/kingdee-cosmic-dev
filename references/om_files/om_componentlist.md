# 简单委外组件清单（废弃）-om_componentlist

## 简单委外组件清单（废弃）-多语言表 t_om_component_l

- **表名称：** 简单委外组件清单（废弃）-多语言表
- **表名：** t_om_component_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_component_l_0 |  | fid,flocaleid |
| 2 | pk_om_component_l |  | fpkid |

---

## 简单委外组件清单（废弃）-关联追踪表 t_om_component_tc

- **表名称：** 简单委外组件清单（废弃）-关联追踪表
- **表名：** t_om_component_tc

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
| 1 | idx_om_component_tc_tid |  | ftid |
| 2 | pk_om_component_tc |  | fid |
| 3 | idx_om_component_tc_tbill |  | ftbillid |

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

## 组件明细-子表 t_om_componententry

- **表名称：** 组件明细-子表
- **表名：** t_om_componententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funissueqty | 未领基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未领基本数量 |
| 3 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 4 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fwastagerateformula | 损耗计算公式 | varchar | 30 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 6 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 标准基本数量 |
| 7 | fissuemode | 领送料方式 | varchar | 30 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 8 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 9 | flocation | 供货仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 12 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 13 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fworkplanid | 工序计划分录ID | int8 | 64 |  | √ | 0 | 工序计划分录ID |
| 15 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 16 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 17 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 18 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 使用比例(%) |
| 20 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 21 | fqtydenominator | 分母 | numeric | 23 | 10 | √ | 0.0000000000 | 分母 |
| 22 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 23 | fchildbomid | 子项BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 24 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 25 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 27 | fsupplymode | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 29 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | fchildbomversion | 子项BOM版本 | varchar | 50 |  | √ | ' ' | 子项BOM版本 |
| 31 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fentrychangetype | 变更方式 | varchar | 30 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 34 | foutqty | 下推领料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 下推领料基本数量 |
| 35 | fbigintfield | fbigintfield | int8 | 64 |  | √ | 0 |  |
| 36 | freservebaseqty | 库存预留基本数量 | numeric | 23 | 10 | √ | 0 | 库存预留基本数量 |
| 37 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 38 | fentryconfiguredcodeid | 组件配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 39 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 40 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 41 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 42 | fuseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已消耗基本数量 |
| 43 | factissueqty | 实发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 实发基本数量 |
| 44 | foutorgunitid | 调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | favbbaseqty | 库存可用基本数量 | numeric | 23 | 10 | √ | 0 | 库存可用基本数量 |
| 46 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 47 | fqtynumerator | 分子 | numeric | 23 | 10 | √ | 0.0000000000 | 分子 |
| 48 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 49 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 50 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 51 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 52 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_componententry_fk |  | fid |
| 2 | pk_om_componententry |  | fentryid |

---

## 简单委外组件清单（废弃）-主表 t_om_component

- **表名称：** 简单委外组件清单（废弃）-主表
- **表名：** t_om_component

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
| 10 | fomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 13 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 14 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 21 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fischanged | 是否存在未审核变更单 | bpchar | 1 |  | √ | '0' | 是否存在未审核变更单 |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | forderno | 委外订单编号 | varchar | 50 |  | √ | ' ' | 委外订单编号 |
| 31 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | 分组基础资料带组织模板 mpdm_processroute |
| 32 | fmftinqty | 最新完工入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 最新完工入库数量 |
| 33 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 34 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 35 | fbillauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_component |  | fid |
| 2 | idx_om_component_fmaterialid |  | fmaterialid |

---

## 组件明细-分表 t_om_componententry_a

- **表名称：** 组件明细-分表
- **表名：** t_om_componententry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscrapqty | 报废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废基本数量 |
| 3 | fallotqty | 调拨基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 调拨基本数量 |
| 4 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 5 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 6 | fbackflushtime | 倒冲时机 | varchar | 30 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :汇报倒冲 |
| 7 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 8 | fisbackflush | 倒冲 | varchar | 30 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 9 | ffeedingqty | 补料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 补料基本数量 |
| 10 | flackraitioqty | 领料下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 领料下限基本数量 |
| 11 | fpromaterentryid | 工序物料分配分录ID | int8 | 64 |  | √ | 0 | 工序物料分配分录ID |
| 12 | frejectedqty | 退料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 退料基本数量 |
| 13 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 14 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 15 | freplaceplan | 组件替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 16 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 在制基本数量 |
| 17 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 18 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0.0000000000 | 提前期偏置(天) |
| 19 | foverissuecontrl | 超发控制 | varchar | 30 |  | √ | ' ' | 超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 20 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 领料上限基本数量 |
| 21 | fissinlowlimit | 领料下限允差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 领料下限允差(%) |
| 22 | fcansendqty | 可发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 可发基本数量 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fissinhighlimit | 领料上限允差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 领料上限允差(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_componententry_a_fk |  | fid |
| 2 | pk_om_componententry_a |  | fentryid |

---

## 组件明细-多语言表 t_om_componententry_l

- **表名称：** 组件明细-多语言表
- **表名：** t_om_componententry_l

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
| 1 | pk_om_componententry_l |  | fpkid |
| 2 | idx_om_componententry_l_0 |  | fentryid,flocaleid |

---

## 简单委外组件清单（废弃）-反写记录表 t_om_component_wb

- **表名称：** 简单委外组件清单（废弃）-反写记录表
- **表名：** t_om_component_wb

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
| 1 | idx_om_component_wb_fk |  | fid |
| 2 | pk_om_component_wb |  | fentryid |

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
