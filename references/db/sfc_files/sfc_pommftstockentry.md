# 生产用料清单分录-sfc_pommftstockentry

## 生产用料清单分录-分表 t_pom_manustockentry_b

- **表名称：** 生产用料清单分录-分表
- **表名：** t_pom_manustockentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbusdenominator | fbusdenominator | numeric | 23 | 10 | √ | 1 |  |
| 2 | fbusbadincomerejectedqty | fbusbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fretoverdrawnbaseqty | fretoverdrawnbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fretoverdrawnqty | fretoverdrawnqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fbusgoodrejectedqty | fbusgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | fneedqty | fneedqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fbadtaskrejectedqty | fbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fgoodrejectedqty | fgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fisentryexpand | fisentryexpand | varchar | 5 |  | √ | '0' |  |
| 10 | finvmatunitid | finvmatunitid | int8 | 64 |  | √ | 0 |  |
| 11 | fbusactissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 12 | factreceivebaseqty | 实领基本数量 | numeric | 23 | 10 | √ | 0 | 实领基本数量 |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fparentmaterialid | fparentmaterialid | int8 | 64 |  | √ | 0 |  |
| 15 | factreceiveqty | 实领数量 | numeric | 23 | 10 | √ | 0 | 实领数量 |
| 16 | ftopmaterialid | ftopmaterialid | int8 | 64 |  | √ | 0 |  |
| 17 | fbadincomerejectedqty | fbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fbusbadtaskrejectedqty | fbusbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 20 | fbusstandqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 22 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 23 | favbinvqty | favbinvqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fisentryexpandone | fisentryexpandone | varchar | 5 |  | √ | '0' |  |
| 25 | fbusoutqty | fbusoutqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fbususeqty | fbususeqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fbusunissueqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 28 | fneedbaseqty | fneedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fbusdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 30 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | favbinvbaseqty | favbinvbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fsrctype | fsrctype | bpchar | 1 |  | √ | 'A' |  |
| 33 | fbusnumerator | fbusnumerator | numeric | 23 | 10 | √ | 0 |  |
| 34 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_manustockentry_b |  | fdetailid |
| 2 | idx_pom_manustockentry_b_eid |  | fentryid |

---

## 生产用料清单分录-分表 t_pom_manustockentry_a

- **表名称：** 生产用料清单分录-分表
- **表名：** t_pom_manustockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbackflushtime | 倒冲时机 | varchar | 30 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :汇报倒冲 |
| 2 | ffeedingqty | ffeedingqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 4 | fqcppbaseqty | fqcppbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 6 | fsupplier | fsupplier | int8 | 64 |  | √ | 0 |  |
| 7 | fqcppbasejoinqty | fqcppbasejoinqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fprocessplan | 工序计划 | varchar | 50 |  | √ | ' ' | 工序计划 |
| 9 | fbasetransapplyqty | fbasetransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fqcppqty | fqcppqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 13 | fqcppjoinqty | fqcppjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 15 | fissinlowlimit | fissinlowlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 17 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | ftagnum | ftagnum | varchar | 255 |  | √ | ' ' |  |
| 19 | ftransapplyqty | ftransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 21 | frejectedqty | frejectedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | finvtransdictqty | finvtransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 24 | foprworkcenter | foprworkcenter | int8 | 64 |  | √ | 0 |  |
| 25 | fbasetransapplyrelqty | fbasetransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | ftransdictnonqty | ftransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | foperationdesc | foperationdesc | varchar | 50 |  | √ | ' ' |  |
| 28 | fbuscansendqty | fbuscansendqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 在制基本数量 |
| 30 | freplacestrategy | freplacestrategy | varchar | 5 |  | √ | ' ' |  |
| 31 | fbusallotqty | fbusallotqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fextraratioqty | fextraratioqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 34 | fentrychangetype | fentrychangetype | varchar | 30 |  | √ | ' ' |  |
| 35 | fleadtimeunit | fleadtimeunit | varchar | 30 |  | √ | ' ' |  |
| 36 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 37 | fprocesssequence | 工序序列 | int4 | 32 |  | √ | 0 | 工序序列 |
| 38 | fallotqty | fallotqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | fisoutmachining | fisoutmachining | bpchar | 1 |  | √ | '0' |  |
| 40 | ftagnum_tag | ftagnum_tag | text | 0 |  |  | null |  |
| 41 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 42 | freplacemode | freplacemode | varchar | 5 |  | √ | ' ' |  |
| 43 | fpromaterentryid | fpromaterentryid | int8 | 64 |  | √ | 0 |  |
| 44 | ftransdictrelqty | ftransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 45 | ftransdictqty | ftransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | fmachiningtype | fmachiningtype | varchar | 30 |  | √ | ' ' |  |
| 47 | freplaceplan | freplaceplan | int8 | 64 |  | √ | 0 |  |
| 48 | foprno | foprno | varchar | 50 |  | √ | ' ' |  |
| 49 | fisbomextend | fisbomextend | bpchar | 1 |  | √ | '0' |  |
| 50 | fworkprocedureid | fworkprocedureid | int8 | 64 |  | √ | 0 |  |
| 51 | fbomentryid | fbomentryid | int8 | 64 |  | √ | 0 |  |
| 52 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0.0000000000 | 提前期偏置(天) |
| 53 | foverissuecontrl | foverissuecontrl | varchar | 30 |  | √ | ' ' |  |
| 54 | ftransapplyrelqty | ftransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fissinhighlimit | fissinhighlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 56 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 57 | fbusrejectedqty | fbusrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 58 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 59 | fisbackflush | fisbackflush | bpchar | 1 |  | √ | '0' |  |
| 60 | fbusfeedingqty | fbusfeedingqty | numeric | 23 | 10 | √ | 0 |  |
| 61 | flackraitioqty | flackraitioqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 62 | ftotalleadtime | ftotalleadtime | numeric | 23 | 10 | √ | 0 |  |
| 63 | fbasetransdictrelqty | fbasetransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 64 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 65 | fbusscrapqty | fbusscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 66 | fbasetransdictnonqty | fbasetransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 67 | finvtransdictnonqty | finvtransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 68 | fcansendqty | fcansendqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 69 | fisbackflushnew | 倒冲 | varchar | 30 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 70 | finvtransdictrelqty | finvtransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fbomexpandpath | fbomexpandpath | varchar | 500 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_manustockentry_a_pkey |  | fdetailid |
| 2 | idx_pom_msea_fentryid |  | fentryid |

---

## 生产用料清单分录-多语言表 t_pom_manustockentry_l

- **表名称：** 生产用料清单分录-多语言表
- **表名：** t_pom_manustockentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fchildremarks | fchildremarks | varchar | 250 |  | √ | ' ' |  |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fsetuplocation | 安装位置 | varchar | 100 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_msel_fdetailid |  | fdetailid,flocaleid |
| 2 | t_pom_manustockentry_l_pkey |  | fpkid |

---

## 生产用料清单分录-主表 t_pom_manustockentry

- **表名称：** 生产用料清单分录-主表
- **表名：** t_pom_manustockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funissueqty | funissueqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fwastagerateformula | fwastagerateformula | varchar | 30 |  | √ | ' ' |  |
| 5 | fstandqty | fstandqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fissuemode | 领送料方式 | varchar | 30 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 7 | fiscannegative | fiscannegative | bpchar | 1 |  | √ | '0' |  |
| 8 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 11 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 12 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | foperatemrp | foperatemrp | bpchar | 1 |  | √ | '0' |  |
| 14 | fisreturninspect | 生产退料检验 | bpchar | 1 |  | √ | 0 | 生产退料检验 |
| 15 | fworkplanid | fworkplanid | int8 | 64 |  | √ | 0 |  |
| 16 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 17 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 21 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 使用比例(%) |
| 23 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 24 | fqtydenominator | fqtydenominator | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 26 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 27 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 28 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 30 | fworkstation | fworkstation | int8 | 64 |  | √ | 0 |  |
| 31 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 32 | fk_bj73_ylbillid | fk_bj73_ylbillid | varchar | 50 |  | √ | ' ' |  |
| 33 | fsupplymode | fsupplymode | varchar | 30 |  | √ | ' ' |  |
| 34 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 35 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 36 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | fchildbomversion | fchildbomversion | varchar | 50 |  | √ | ' ' |  |
| 38 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fentryid | 单据头内码 | int8 | 64 |  | √ | 0 | 单据头内码 |
| 40 | foutsqty | foutsqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | foutqty | foutqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fsupplytype | 供应类型 | varchar | 30 |  | √ | ' ' | 供应类型,枚举: 10040 :外购 10030 :自制 10050 :委外 |
| 43 | freservebaseqty | freservebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 45 | fk_bj73_qtyfield | fk_bj73_qtyfield | numeric | 23 | 10 |  | null |  |
| 46 | fentryconfiguredcodeid | fentryconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 47 | fk_bj73_zfl | fk_bj73_zfl | numeric | 23 | 10 |  | null |  |
| 48 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 49 | fuseqty | fuseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已领基本数量 |
| 51 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 52 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | favbbaseqty | favbbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型 |
| 55 | fqtynumerator | fqtynumerator | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 56 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 57 | ffixscrap | ffixscrap | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 58 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 59 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 60 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mse_fseq |  | fseq |
| 2 | idx_stocken_mftid |  | fmaterialid |
| 3 | t_pom_manustockentry_pkey |  | fdetailid |
| 4 | idx_stocken_fsrcbillentryid |  | fsrcbillentryid |
| 5 | idx_pom_mse_fentryid |  | fentryid |
| 6 | idx_stocken_feconfiguredcode |  | fentryconfiguredcodeid |
| 7 | idx_stocken_mid |  | fmaterielmasterid |
