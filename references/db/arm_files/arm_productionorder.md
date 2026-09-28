# 重复生产工单-arm_productionorder

## 重复生产工单-反写记录表 t_arm_productionorder_wb

- **表名称：** 重复生产工单-反写记录表
- **表名：** t_arm_productionorder_wb

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
| 1 | idx_arm_productionorder_wb_fk |  | fid |
| 2 | pk_arm_productionorder_wb |  | fentryid |

---

## 关联子实体-子表 t_arm_productionorder_lk

- **表名称：** 关联子实体-子表
- **表名：** t_arm_productionorder_lk

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
| 1 | idx_arm_productionorder_lk_fk |  | fid |
| 2 | pk_arm_productionorder_lk |  | fpkid |

---

## 重复生产工单-关联追踪表 t_arm_productionorder_tc

- **表名称：** 重复生产工单-关联追踪表
- **表名：** t_arm_productionorder_tc

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
| 1 | idx_arm_productionorder_tc_tid |  | ftid |
| 2 | idx_arm_productionorder_tc_tbill |  | ftbillid |
| 3 | pk_arm_productionorder_tc |  | fid |

---

## 用料清单-子表 t_arm_prodorderentry

- **表名称：** 用料清单-子表
- **表名：** t_arm_prodorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmasterid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fxferfromlocationid | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 4 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 5 | freplaceparts | 替代件 | bpchar | 1 |  | √ | ' ' | 替代件 |
| 6 | fistransferrequired | 备料调拨 | bpchar | 1 |  | √ | ' ' | 备料调拨 |
| 7 | fissuemode | 领送料方式 | varchar | 8 |  | √ | ' ' | 领送料方式,枚举: 11010 :生产领料 11030 :看板 11050 :直送 11040 :不领料 |
| 8 | fbackflushtime | 倒冲时机 | varchar | 8 |  | √ | ' ' | 倒冲时机,枚举: |
| 9 | fissuedqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | freppriority | 替代优先级 | int4 | 32 |  | √ | 0 | 替代优先级 |
| 12 | fnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 13 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 14 | fkeyparts | 关键件 | bpchar | 1 |  | √ | ' ' | 关键件 |
| 15 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 16 | frequireddatetime | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 17 | freplaceplan | 替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 18 | fdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 19 | freplacegroup | 替代组号 | int4 | 32 |  | √ | 0 | 替代组号 |
| 20 | fassociatepickqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 21 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | ' ' | 来源于BOM展开 |
| 22 | fstandardqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 23 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 24 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 25 | fxferfromorgid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 27 | fcompauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 28 | fcompbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 29 | fbackflush | 倒冲 | bpchar | 1 |  | √ | ' ' | 倒冲 |
| 30 | fqtytype | 用量类型 | varchar | 8 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 31 | fcompunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | fissueorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fcomptracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 34 | fcompmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 35 | fusagerate | 使用比例% | numeric | 23 | 10 | √ | 0 | 使用比例% |
| 36 | fissuelocationid | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 37 | fmatcommon | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 38 | fcomponentid | 子项编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 39 | fxferfromwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 40 | fissuewarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 41 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | fleadtimeoffset | 提前期偏置(天) | int4 | 32 |  | √ | 0 | 提前期偏置(天) |
| 43 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 44 | fsupplyorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 46 | frequiredqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 47 | fproductrtinsp | 生产退料检验 | bpchar | 1 |  | √ | ' ' | 生产退料检验 |
| 48 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_prodorderentry_fid |  | fid |
| 2 | pk_t_arm_prodorderentry |  | fentryid |

---

## 重复生产工单-主表 t_arm_productionorder

- **表名称：** 重复生产工单-主表
- **表名：** t_arm_productionorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpushtag | 投放工单 | int4 | 32 |  | √ | 0 | 投放工单 |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | flocation | 完工入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 6 | fsrcentryseq | 来源单据分录 | varchar | 50 |  | √ | ' ' | 来源单据分录 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsrcbillname | 来源单据标识 | varchar | 50 |  | √ | ' ' | 来源单据标识 |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 10 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | forderstatus | 状态 | varchar | 8 |  | √ | ' ' | 状态,枚举: P :计划 F :计划确认 E :锁定 R :下达 C :关闭 |
| 12 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 13 | fdemandbilltype | 需求单据类型 | varchar | 50 |  | √ | ' ' | 需求单据类型 |
| 14 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fqtytoscrap | 预计报废数量 | numeric | 23 | 10 | √ | 0 | 预计报废数量 |
| 16 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fdemandentryseqid | 需求单据分录ID | int8 | 64 |  | √ | 0 | 需求单据分录ID |
| 18 | fversion | 版本号 | int4 | 32 |  | √ | 1 | 版本号 |
| 19 | fincompleteqty | 未入库良品数 | numeric | 23 | 10 | √ | 0 | 未入库良品数 |
| 20 | fsrcbillnumber | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 21 | fdemandbillnumber | 需求单据编码 | varchar | 50 |  | √ | ' ' | 需求单据编码 |
| 22 | fmaterialno | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 23 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fdemandbillname | 需求单据标识 | varchar | 50 |  | √ | ' ' | 需求单据标识 |
| 31 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 32 | funreportqty | 未汇报数量 | numeric | 23 | 10 | √ | 0 | 未汇报数量 |
| 33 | fwarehouse | 完工入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fproductionlineid | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 35 | fyieldpercent | 成品率% | numeric | 23 | 10 | √ | 0 | 成品率% |
| 36 | fproductionseq | 生产顺序 | numeric | 23 | 10 | √ | 0 | 生产顺序 |
| 37 | fstartdatetime | 计划开工日期 | timestamp | 0 |  |  | null | 计划开工日期 |
| 38 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 39 | fdemandbillid | 需求单据ID | int8 | 64 |  | √ | 0 | 需求单据ID |
| 40 | fqtytocomplete | 预计完工数量 | numeric | 23 | 10 | √ | 0 | 预计完工数量 |
| 41 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 42 | fneeddate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 43 | fshift | fshift | varchar | 50 |  |  | ' ' |  |
| 44 | fworkshopid | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fdemandentryseq | 需求单据分录 | varchar | 50 |  | √ | ' ' | 需求单据分录 |
| 46 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 47 | fleadtime | 提前期 | int4 | 32 |  | √ | 0 | 提前期 |
| 48 | fduedatetime | 计划完工日期 | timestamp | 0 |  |  | null | 计划完工日期 |
| 49 | fremark | 备注 | varchar | 510 |  |  | null | 备注 |
| 50 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fcompletebaseqty | 入库基本数量 | numeric | 23 | 10 | √ | 0 | 入库基本数量 |
| 53 | fbaseqtytostart | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 54 | freportqty | 汇报数量 | numeric | 23 | 10 | √ | 0 | 汇报数量 |
| 55 | fcompleteqty | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 56 | fsrcentryseqid | 来源单据分录行ID | int8 | 64 |  | √ | 0 | 来源单据分录行ID |
| 57 | fqtytostart | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 58 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 59 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_productionorder_org |  | forgid |
| 2 | pk_t_arm_productionorder |  | fid |
