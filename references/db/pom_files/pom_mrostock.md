# 检修组件清单-pom_mrostock

## 检修组件清单-关联追踪表 t_pom_mrostock_tc

- **表名称：** 检修组件清单-关联追踪表
- **表名：** t_pom_mrostock_tc

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
| 1 | idx_pom_mrostock_tc_tbill |  | ftbillid |
| 2 | pk_pom_mrostock_tc |  | fid |
| 3 | idx_pom_mrostock_tc_tid |  | ftid |

---

## 关联子实体-子表 t_pom_mrostock_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mrostock_lk

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
| 1 | pk_pom_mrostock_lk |  | fpkid |
| 2 | idx_pom_mrostock_lk_fk |  | fid |

---

## 检修组件清单-多语言表 t_pom_mrostock_l

- **表名称：** 检修组件清单-多语言表
- **表名：** t_pom_mrostock_l

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
| 1 | idx_pom_mrostockl_fid |  | fid,flocaleid |
| 2 | pk_pom_mrostock_l |  | fpkid |

---

## 组件明细-子表 t_pom_mrostockentry

- **表名称：** 组件明细-子表
- **表名：** t_pom_mrostockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | funissueqty | 未领基本数量 | numeric | 23 | 10 | √ | 0 | 未领基本数量 |
| 3 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | BOM版本 bd_bomversion |
| 4 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 5 | fwastagerateformula | 损耗计算公式 | varchar | 50 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 6 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 7 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 8 | fbackflushtime | 倒冲时机 | varchar | 50 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :汇报倒冲 |
| 9 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 10 | flocation | 供货仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 13 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 14 | ffeedingqty | 补料基本数量 | numeric | 23 | 10 | √ | 0 | 补料基本数量 |
| 15 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 16 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | fworkplanid | 工序计划分录ID | int8 | 64 |  | √ | 0 | 工序计划分录ID |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 19 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 20 | fissinlowlimit | 领料下限允差(%) | numeric | 23 | 10 | √ | 0 | 领料下限允差(%) |
| 21 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 22 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 23 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 24 | fscrapqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 25 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 26 | fqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | fchildbomid | 子项BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 29 | fwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 30 | frejectedqty | 退料基本数量 | numeric | 23 | 10 | √ | 0 | 退料基本数量 |
| 31 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 33 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 34 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 35 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 36 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0 | 在制基本数量 |
| 38 | fchildbomversion | 子项BOM版本 | varchar | 50 |  | √ | ' ' | 子项BOM版本 |
| 39 | fsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0 | 领料上限基本数量 |
| 41 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 42 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 43 | foutqty | 下推领料基本数量 | numeric | 23 | 10 | √ | 0 | 下推领料基本数量 |
| 44 | fallotqty | 调拨基本数量 | numeric | 23 | 10 | √ | 0 | 调拨基本数量 |
| 45 | fmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 46 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 47 | fentryconfiguredcodeid | 组件配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 48 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 49 | freplaceplan | 组件替代方案 | int8 | 64 |  | √ | 0 | 物料替代方案 mpdm_replaceplan |
| 50 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 51 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 52 | fuseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 53 | factissueqty | 实发基本数量 | numeric | 23 | 10 | √ | 0 | 实发基本数量 |
| 54 | foutorgunitid | 调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 55 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0 | 提前期偏置(天) |
| 56 | foverissuecontrl | 超发控制 | varchar | 50 |  | √ | ' ' | 超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 57 | fstocksource | 组件来源 | varchar | 50 |  | √ | ' ' | 组件来源,枚举: A :手工新增 B :工卡物料需求 C :生产领料申请 |
| 58 | fissinhighlimit | 领料上限允差(%) | numeric | 23 | 10 | √ | 0 | 领料上限允差(%) |
| 59 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 60 | fqtynumerator | 单位基本数量 | numeric | 23 | 10 | √ | 0 | 单位基本数量 |
| 61 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 62 | fisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 63 | flackraitioqty | 领料下限基本数量 | numeric | 23 | 10 | √ | 0 | 领料下限基本数量 |
| 64 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 65 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 66 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 67 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 68 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 69 | fcansendqty | 可发基本数量 | numeric | 23 | 10 | √ | 0 | 可发基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrostocken_fsrcbillentryid |  | fsrcbillentryid |
| 2 | pk_pom_mrostockentry |  | fentryid |
| 3 | idx_mrostocken_fmatmasterid |  | fmaterielmasterid |
| 4 | idx_mrostocken_fsrcbillid |  | fsrcbillid |

---

## 检修组件清单-反写记录表 t_pom_mrostock_wb

- **表名称：** 检修组件清单-反写记录表
- **表名：** t_pom_mrostock_wb

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
| 1 | pk_pom_mrostock_wb |  | fentryid |
| 2 | idx_pom_mrostock_wb_fk |  | fid |

---

## 组件明细-多语言表 t_pom_mrostockentry_l

- **表名称：** 组件明细-多语言表
- **表名：** t_pom_mrostockentry_l

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
| 1 | idx_pom_mrostockl_fentryid |  | fentryid,flocaleid |
| 2 | pk_pom_mrostockentry_l |  | fpkid |

---

## 检修组件清单-主表 t_pom_mrostock

- **表名称：** 检修组件清单-主表
- **表名：** t_pom_mrostock

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forderid | 检修工单ID | varchar | 50 |  | √ | ' ' | 检修工单ID |
| 6 | forderidnew | 检修工单主id | int8 | 64 |  | √ | 0 | 检修工单主id |
| 7 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fworkcardid | 工卡号 | int8 | 64 |  | √ | 0 | 工卡 mpdm_mrocardroute |
| 9 | fconfiguredcodeid | 产品配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 10 | forderentryid | 检修工单行号 | int8 | 64 |  | √ | 0 | 检修工单分录F7 pom_mroorder_f7 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 15 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 21 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 24 | fischanged | 是否存在未审核变更单 | bpchar | 1 |  | √ | '0' | 是否存在未审核变更单 |
| 25 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | forderno | 检修工单编号 | varchar | 50 |  | √ | ' ' | 检修工单编号 |
| 33 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 34 | fmftinqty | 最新完工入库数量 | numeric | 23 | 10 | √ | 0 | 最新完工入库数量 |
| 35 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 36 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
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
| 1 | pk_pom_mrostock |  | fid |
| 2 | idx_pom_mrostock_forderentryid |  | forderentryid |
| 3 | idx_pom_mrostock_forderid |  | forderid |
| 4 | idx_pom_mrostock_fsourcebillid |  | fsourcebillid |

---

## 关联子实体-子表 t_pom_mrostockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mrostockentry_lk

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
| 1 | pk_pom_mrostockentry_lk |  | fpkid |
| 2 | idx_pom_mrostockentry_lk_fk |  | fentryid |
