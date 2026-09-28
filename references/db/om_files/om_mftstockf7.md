# 委外用料清单分录f7-om_mftstockf7

## 委外用料清单分录f7-主表 t_om_mftstockentry

- **表名称：** 委外用料清单分录f7-主表
- **表名：** t_om_mftstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funissueqty | funissueqty | numeric | 23 | 10 | √ | 0 |  |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fwastagerateformula | fwastagerateformula | varchar | 50 |  | √ | ' ' |  |
| 5 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 6 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 7 | fbackflushtime | fbackflushtime | varchar | 50 |  | √ | ' ' |  |
| 8 | fiscannegative | fiscannegative | bpchar | 1 |  | √ | '0' |  |
| 9 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | foutlocation | foutlocation | int8 | 64 |  | √ | 0 |  |
| 12 | fscraprate | fscraprate | numeric | 23 | 10 | √ | 0 |  |
| 13 | ffeedingqty | ffeedingqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fdemanddate | fdemanddate | timestamp | 0 |  |  | null |  |
| 15 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | fsupplier | fsupplier | int8 | 64 |  | √ | 0 |  |
| 17 | fworkplanid | fworkplanid | int8 | 64 |  | √ | 0 |  |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 19 | fisstockallot | fisstockallot | bpchar | 1 |  | √ | '0' |  |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | fissinlowlimit | fissinlowlimit | numeric | 23 | 10 | √ | 0 |  |
| 22 | frework | frework | bpchar | 1 |  | √ | '0' |  |
| 23 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 24 | fuseratio | fuseratio | numeric | 23 | 10 | √ | 0 |  |
| 25 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 27 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 28 | fqtydenominator | fqtydenominator | numeric | 23 | 10 | √ | 0 |  |
| 29 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 30 | fchildbomid | fchildbomid | int8 | 64 |  | √ | 0 |  |
| 31 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 32 | frejectedqty | frejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 34 | fiskeypart | fiskeypart | bpchar | 1 |  | √ | '0' |  |
| 35 | fworkstation | fworkstation | int8 | 64 |  | √ | 0 |  |
| 36 | fisstep | fisstep | bpchar | 1 |  | √ | '0' |  |
| 37 | foprworkcenter | foprworkcenter | int8 | 64 |  | √ | 0 |  |
| 38 | fsupplymode | fsupplymode | varchar | 50 |  | √ | ' ' |  |
| 39 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 40 | foperationdesc | foperationdesc | varchar | 50 |  | √ | ' ' |  |
| 41 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 42 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0 | 在制基本数量 |
| 43 | fchildbomversion | fchildbomversion | varchar | 50 |  | √ | ' ' |  |
| 44 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 45 | fextraratioqty | fextraratioqty | numeric | 23 | 10 | √ | 0 |  |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 47 | fentrychangetype | fentrychangetype | varchar | 50 |  | √ | ' ' |  |
| 48 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 49 | foutqty | foutqty | numeric | 23 | 10 | √ | 0 |  |
| 50 | fallotqty | fallotqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | freservebaseqty | freservebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 53 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 54 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 55 | fentryconfiguredcodeid | fentryconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 56 | fpromaterentryid | fpromaterentryid | int8 | 64 |  | √ | 0 |  |
| 57 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 58 | freplaceplan | freplaceplan | int8 | 64 |  | √ | 0 |  |
| 59 | fmachiningtype | fmachiningtype | varchar | 50 |  | √ | ' ' |  |
| 60 | foprno | foprno | varchar | 50 |  | √ | ' ' |  |
| 61 | fisbomextend | fisbomextend | bpchar | 1 |  | √ | '0' |  |
| 62 | fuseqty | fuseqty | numeric | 23 | 10 | √ | 0 |  |
| 63 | fworkprocedureid | fworkprocedureid | int8 | 64 |  | √ | 0 |  |
| 64 | factissueqty | 实发基本数量 | numeric | 23 | 10 | √ | 0 | 实发基本数量 |
| 65 | fbomentryid | fbomentryid | int8 | 64 |  | √ | 0 |  |
| 66 | foutorgunitid | foutorgunitid | int8 | 64 |  | √ | 0 |  |
| 67 | fleadtime | fleadtime | numeric | 23 | 10 | √ | 0 |  |
| 68 | foverissuecontrl | foverissuecontrl | varchar | 50 |  | √ | ' ' |  |
| 69 | fissinhighlimit | fissinhighlimit | numeric | 23 | 10 | √ | 0 |  |
| 70 | favbbaseqty | favbbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 71 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型 |
| 72 | fqtynumerator | fqtynumerator | numeric | 23 | 10 | √ | 0 |  |
| 73 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 74 | fisbackflush | fisbackflush | varchar | 50 |  | √ | ' ' |  |
| 75 | flackraitioqty | flackraitioqty | numeric | 23 | 10 | √ | 0 |  |
| 76 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 77 | ffixscrap | ffixscrap | numeric | 23 | 10 | √ | 0 |  |
| 78 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 79 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 80 | fdemandqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 81 | fcansendqty | 未领基本数量 | numeric | 23 | 10 | √ | 0 | 未领基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mesen_fmaterielmasterid |  | fmaterielmasterid |
| 2 | idx_om_mftstockentry_fk |  | fentryid |
| 3 | pk_om_mftstockentry |  | fdetailid |

---

## 委外用料清单分录f7-分表 t_om_mftstockentry_b

- **表名称：** 委外用料清单分录f7-分表
- **表名：** t_om_mftstockentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbusdenominator | fbusdenominator | numeric | 23 | 10 | √ | 0 |  |
| 2 | fbusbadincomerejectedqty | fbusbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fbusgoodrejectedqty | fbusgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fbadtaskrejectedqty | fbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fgoodrejectedqty | fgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | finvmatunitid | finvmatunitid | int8 | 64 |  | √ | 0 |  |
| 7 | fbusactissueqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 8 | fbadincomerejectedqty | fbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 10 | fbusbadtaskrejectedqty | fbusbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 12 | fbusstandqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 14 | fisjumplevel | fisjumplevel | bpchar | 1 |  | √ | '0' |  |
| 15 | fbusoutqty | fbusoutqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fbususeqty | fbususeqty | numeric | 23 | 10 | √ | 0 |  |
| 17 | fbusunissueqty | fbusunissueqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fbusdemandqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 19 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fsrctype | fsrctype | bpchar | 1 |  | √ | 'A' |  |
| 21 | fbusnumerator | fbusnumerator | numeric | 23 | 10 | √ | 0 |  |
| 22 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 23 | fpushdownmatqty | fpushdownmatqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fchildmatunitqty | fchildmatunitqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_b |  | fdetailid |
| 2 | idx_om_mftstockentry_b |  | fentryid |

---

## 委外用料清单分录f7-分表 t_om_mftstockentry_a

- **表名称：** 委外用料清单分录f7-分表
- **表名：** t_om_mftstockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftransdictrelqty | ftransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 2 | ftransdictqty | ftransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | fqcppbaseqty | fqcppbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | freplacegroup | freplacegroup | int8 | 64 |  | √ | 0 |  |
| 5 | fisreturninspect | fisreturninspect | bpchar | 1 |  | √ | 0 |  |
| 6 | fqcppbasejoinqty | fqcppbasejoinqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fbasetransapplyqty | fbasetransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 9 | fqcppqty | fqcppqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 12 | fqcppjoinqty | fqcppjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 13 | ftransapplyrelqty | ftransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 15 | fbusrejectedqty | fbusrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 17 | ftransapplyqty | ftransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 19 | fbusfeedingqty | fbusfeedingqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | finvtransdictqty | finvtransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | ftotalleadtime | ftotalleadtime | numeric | 23 | 10 | √ | 0 |  |
| 22 | fbasetransapplyrelqty | fbasetransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | ftransdictnonqty | ftransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fbasetransdictrelqty | fbasetransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fbuscansendqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 26 | fbusallotqty | fbusallotqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fbusscrapqty | fbusscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | fbasetransdictnonqty | fbasetransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | finvtransdictnonqty | finvtransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | finvtransdictrelqty | finvtransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fbomexpandpath | fbomexpandpath | varchar | 500 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_a |  | fdetailid |
| 2 | idx_om_mftstockentry_a |  | fentryid |
