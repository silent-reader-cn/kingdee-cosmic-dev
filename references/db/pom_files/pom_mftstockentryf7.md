# 生产组件清单分录f7-pom_mftstockentryf7

## 生产组件清单分录f7-分表 t_pom_manustockentry_b

- **表名称：** 生产组件清单分录f7-分表
- **表名：** t_pom_manustockentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbusdenominator | fbusdenominator | numeric | 23 | 10 | √ | 1 |  |
| 2 | fbusbadincomerejectedqty | fbusbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fbusunissueqty | fbusunissueqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fbusgoodrejectedqty | fbusgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fbusdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 6 | fbadtaskrejectedqty | fbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fgoodrejectedqty | fgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | finvmatunitid | finvmatunitid | int8 | 64 |  | √ | 0 |  |
| 10 | fbusactissueqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 11 | fsrctype | fsrctype | bpchar | 1 |  | √ | 'A' |  |
| 12 | fbusnumerator | fbusnumerator | numeric | 23 | 10 | √ | 0 |  |
| 13 | fbadincomerejectedqty | fbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fbusbadtaskrejectedqty | fbusbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 16 | fbusstandqty | fbusstandqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 19 | fisjumplevel | fisjumplevel | bpchar | 1 |  | √ | '0' |  |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusoutqty | fbusoutqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | fbususeqty | fbususeqty | numeric | 23 | 10 | √ | 0 |  |

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

## 生产组件清单分录f7-分表 t_pom_manustockentry_a

- **表名称：** 生产组件清单分录f7-分表
- **表名：** t_pom_manustockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbackflushtime | fbackflushtime | varchar | 30 |  | √ | ' ' |  |
| 2 | ffeedingqty | ffeedingqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 3 | fdemanddate | fdemanddate | timestamp | 0 |  |  | null |  |
| 4 | fqcppbaseqty | fqcppbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 6 | fsupplier | fsupplier | int8 | 64 |  | √ | 0 |  |
| 7 | fqcppbasejoinqty | fqcppbasejoinqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fbasetransapplyqty | fbasetransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fqcppqty | fqcppqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 11 | fqcppjoinqty | fqcppjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fissinlowlimit | fissinlowlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 14 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | ftransapplyqty | ftransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 17 | frejectedqty | frejectedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | finvtransdictqty | finvtransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fiskeypart | fiskeypart | bpchar | 1 |  | √ | '0' |  |
| 20 | foprworkcenter | foprworkcenter | int8 | 64 |  | √ | 0 |  |
| 21 | fbasetransapplyrelqty | fbasetransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 22 | ftransdictnonqty | ftransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | foperationdesc | foperationdesc | varchar | 50 |  | √ | ' ' |  |
| 24 | fbuscansendqty | fbuscansendqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 在制基本数量 |
| 26 | fbusallotqty | fbusallotqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fextraratioqty | fextraratioqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 29 | fentrychangetype | fentrychangetype | varchar | 30 |  | √ | ' ' |  |
| 30 | fleadtimeunit | fleadtimeunit | varchar | 30 |  | √ | ' ' |  |
| 31 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 32 | fallotqty | fallotqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 33 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 34 | fpromaterentryid | fpromaterentryid | int8 | 64 |  | √ | 0 |  |
| 35 | ftransdictrelqty | ftransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | ftransdictqty | ftransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fmachiningtype | fmachiningtype | varchar | 30 |  | √ | ' ' |  |
| 38 | freplaceplan | freplaceplan | int8 | 64 |  | √ | 0 |  |
| 39 | foprno | foprno | varchar | 50 |  | √ | ' ' |  |
| 40 | fisbomextend | fisbomextend | bpchar | 1 |  | √ | '0' |  |
| 41 | fworkprocedureid | fworkprocedureid | int8 | 64 |  | √ | 0 |  |
| 42 | fbomentryid | fbomentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fleadtime | fleadtime | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | foverissuecontrl | foverissuecontrl | varchar | 30 |  | √ | ' ' |  |
| 45 | ftransapplyrelqty | ftransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | fissinhighlimit | fissinhighlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 48 | fbusrejectedqty | fbusrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 50 | fisbackflush | fisbackflush | bpchar | 1 |  | √ | '0' |  |
| 51 | fbusfeedingqty | fbusfeedingqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | flackraitioqty | flackraitioqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 53 | ftotalleadtime | ftotalleadtime | numeric | 23 | 10 | √ | 0 |  |
| 54 | fbasetransdictrelqty | fbasetransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 56 | fbusscrapqty | fbusscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 57 | fbasetransdictnonqty | fbasetransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 58 | finvtransdictnonqty | finvtransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 59 | fcansendqty | fcansendqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 60 | fisbackflushnew | fisbackflushnew | varchar | 30 |  | √ | ' ' |  |
| 61 | finvtransdictrelqty | finvtransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 62 | fbomexpandpath | fbomexpandpath | varchar | 500 |  | √ | ' ' |  |

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

## 生产组件清单分录f7-主表 t_pom_manustockentry

- **表名称：** 生产组件清单分录f7-主表
- **表名：** t_pom_manustockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funissueqty | funissueqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fwastagerateformula | fwastagerateformula | varchar | 30 |  | √ | ' ' |  |
| 5 | fstandqty | fstandqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fissuemode | 领送料方式 | varchar | 30 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 7 | fiscannegative | fiscannegative | bpchar | 1 |  | √ | '0' |  |
| 8 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | foutlocation | foutlocation | int8 | 64 |  | √ | 0 |  |
| 11 | fscraprate | fscraprate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fisreturninspect | fisreturninspect | bpchar | 1 |  | √ | 0 |  |
| 14 | fworkplanid | fworkplanid | int8 | 64 |  | √ | 0 |  |
| 15 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 16 | fisstockallot | fisstockallot | bpchar | 1 |  | √ | '0' |  |
| 17 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | frework | frework | bpchar | 1 |  | √ | '0' |  |
| 20 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 21 | fuseratio | fuseratio | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 23 | fqtydenominator | fqtydenominator | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 24 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 25 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 26 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 27 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 28 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 29 | fworkstation | fworkstation | int8 | 64 |  | √ | 0 |  |
| 30 | fisstep | fisstep | bpchar | 1 |  | √ | '0' |  |
| 31 | fsupplymode | fsupplymode | varchar | 30 |  | √ | ' ' |  |
| 32 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 33 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 34 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fchildbomversion | fchildbomversion | varchar | 50 |  | √ | ' ' |  |
| 36 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 38 | foutsqty | foutsqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 39 | foutqty | foutqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 40 | fsupplytype | fsupplytype | varchar | 30 |  | √ | ' ' |  |
| 41 | freservebaseqty | freservebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 42 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 43 | fentryconfiguredcodeid | fentryconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 44 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 45 | fuseqty | fuseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | factissueqty | 实发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 实发基本数量 |
| 47 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 48 | foutorgunitid | foutorgunitid | int8 | 64 |  | √ | 0 |  |
| 49 | favbbaseqty | favbbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型 |
| 51 | fqtynumerator | fqtynumerator | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 52 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 53 | ffixscrap | ffixscrap | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 54 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 55 | fprovideorgid | fprovideorgid | int8 | 64 |  | √ | 0 |  |
| 56 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 需求基本数量 |

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
