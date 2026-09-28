# 委外用料清单分录f7-om_mftstockf7

## 委外用料清单分录f7-主表 t_om_mftstockentry

- **表名称：** 委外用料清单分录f7-主表
- **表名：** t_om_mftstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funissueqty | funissueqty | numeric | 23 | 10 | √ | 0 |  |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fmaterielinv | fmaterielinv | int8 | 64 |  | √ | 0 |  |
| 4 | fwastagerateformula | fwastagerateformula | varchar | 50 |  | √ | ' ' |  |
| 5 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 6 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 7 | fbackflushtime | fbackflushtime | varchar | 50 |  | √ | ' ' |  |
| 8 | fiscannegative | fiscannegative | bpchar | 1 |  | √ | '0' |  |
| 9 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | foutlocation | foutlocation | int8 | 64 |  | √ | 0 |  |
| 12 | fscraprate | fscraprate | numeric | 23 | 10 | √ | 0 |  |
| 13 | ffeedingqty | ffeedingqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 15 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | foperatemrp | foperatemrp | bpchar | 1 |  | √ | '0' |  |
| 17 | fsupplier | fsupplier | int8 | 64 |  | √ | 0 |  |
| 18 | fworkplanid | fworkplanid | int8 | 64 |  | √ | 0 |  |
| 19 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 20 | fisstockallot | fisstockallot | bpchar | 1 |  | √ | '0' |  |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 22 | fissinlowlimit | fissinlowlimit | numeric | 23 | 10 | √ | 0 |  |
| 23 | frework | frework | bpchar | 1 |  | √ | '0' |  |
| 24 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 25 | fuseratio | fuseratio | numeric | 23 | 10 | √ | 0 |  |
| 26 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 28 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 29 | fqtydenominator | fqtydenominator | numeric | 23 | 10 | √ | 0 |  |
| 30 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 31 | fchildbomid | fchildbomid | int8 | 64 |  | √ | 0 |  |
| 32 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 33 | frejectedqty | frejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 35 | fiskeypart | fiskeypart | bpchar | 1 |  | √ | '0' |  |
| 36 | fworkstation | fworkstation | int8 | 64 |  | √ | 0 |  |
| 37 | fisstep | fisstep | bpchar | 1 |  | √ | '0' |  |
| 38 | foprworkcenter | foprworkcenter | int8 | 64 |  | √ | 0 |  |
| 39 | fsupplymode | fsupplymode | varchar | 50 |  | √ | ' ' |  |
| 40 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 41 | foperationdesc | foperationdesc | varchar | 50 |  | √ | ' ' |  |
| 42 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0 | 在制基本数量 |
| 44 | fchildbomversion | fchildbomversion | varchar | 50 |  | √ | ' ' |  |
| 45 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fextraratioqty | fextraratioqty | numeric | 23 | 10 | √ | 0 |  |
| 47 | fentryid | 用料清单id | int8 | 64 |  | √ | 0 | 用料清单id |
| 48 | fentrychangetype | fentrychangetype | varchar | 50 |  | √ | ' ' |  |
| 49 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 50 | foutqty | foutqty | numeric | 23 | 10 | √ | 0 |  |
| 51 | fallotqty | fallotqty | numeric | 23 | 10 | √ | 0 |  |
| 52 | freservebaseqty | freservebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 53 | fsupplytype | fsupplytype | varchar | 30 |  | √ | ' ' |  |
| 54 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 55 | fpriority | fpriority | int8 | 64 |  | √ | 0 |  |
| 56 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 57 | fentryconfiguredcodeid | fentryconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 58 | fpromaterentryid | fpromaterentryid | int8 | 64 |  | √ | 0 |  |
| 59 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 60 | freplaceplan | freplaceplan | int8 | 64 |  | √ | 0 |  |
| 61 | fmachiningtype | fmachiningtype | varchar | 50 |  | √ | ' ' |  |
| 62 | foprno | foprno | varchar | 50 |  | √ | ' ' |  |
| 63 | fisbomextend | fisbomextend | bpchar | 1 |  | √ | '0' |  |
| 64 | fuseqty | fuseqty | numeric | 23 | 10 | √ | 0 |  |
| 65 | fworkprocedureid | fworkprocedureid | int8 | 64 |  | √ | 0 |  |
| 66 | factissueqty | 实发基本数量 | numeric | 23 | 10 | √ | 0 | 实发基本数量 |
| 67 | fbomentryid | fbomentryid | int8 | 64 |  | √ | 0 |  |
| 68 | foutorgunitid | foutorgunitid | int8 | 64 |  | √ | 0 |  |
| 69 | fleadtime | fleadtime | numeric | 23 | 10 | √ | 0 |  |
| 70 | foverissuecontrl | foverissuecontrl | varchar | 50 |  | √ | ' ' |  |
| 71 | fissinhighlimit | fissinhighlimit | numeric | 23 | 10 | √ | 0 |  |
| 72 | favbbaseqty | favbbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 73 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型 |
| 74 | fqtynumerator | fqtynumerator | numeric | 23 | 10 | √ | 0 |  |
| 75 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 76 | fisbackflush | fisbackflush | varchar | 50 |  | √ | ' ' |  |
| 77 | flackraitioqty | flackraitioqty | numeric | 23 | 10 | √ | 0 |  |
| 78 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 79 | ffixscrap | ffixscrap | numeric | 23 | 10 | √ | 0 |  |
| 80 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 81 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 82 | fdemandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 83 | fcansendqty | 未领基本数量 | numeric | 23 | 10 | √ | 0 | 未领基本数量 |

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
| 3 | fretoverdrawnbaseqty | fretoverdrawnbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | fretoverdrawnqty | fretoverdrawnqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fbusgoodrejectedqty | fbusgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | fneedqty | fneedqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fbadtaskrejectedqty | fbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 8 | fgoodrejectedqty | fgoodrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fisentryexpand | fisentryexpand | varchar | 5 |  | √ | '0' |  |
| 10 | finvmatunitid | finvmatunitid | int8 | 64 |  | √ | 0 |  |
| 11 | fbusactissueqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 12 | factreceivebaseqty | 实领基本数量 | numeric | 23 | 10 | √ | 0 | 实领基本数量 |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fparentmaterialid | fparentmaterialid | int8 | 64 |  | √ | 0 |  |
| 15 | factreceiveqty | 实领数量 | numeric | 23 | 10 | √ | 0 | 实领数量 |
| 16 | ftopmaterialid | ftopmaterialid | int8 | 64 |  | √ | 0 |  |
| 17 | fbadincomerejectedqty | fbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 19 | fbusbadtaskrejectedqty | fbusbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusstandqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 22 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 23 | fisjumplevel | fisjumplevel | bpchar | 1 |  | √ | '0' |  |
| 24 | favbinvqty | favbinvqty | numeric | 23 | 10 | √ | 0 |  |
| 25 | fisentryexpandone | fisentryexpandone | varchar | 5 |  | √ | '0' |  |
| 26 | fbusoutqty | fbusoutqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fbususeqty | fbususeqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fbusunissueqty | fbusunissueqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fneedbaseqty | fneedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 30 | fbusdemandqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 31 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | favbinvbaseqty | favbinvbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 33 | fsrctype | fsrctype | bpchar | 1 |  | √ | 'A' |  |
| 34 | fbusnumerator | fbusnumerator | numeric | 23 | 10 | √ | 0 |  |
| 35 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 36 | fpushdownmatqty | fpushdownmatqty | numeric | 23 | 10 | √ | 0 |  |
| 37 | fchildmatunitqty | fchildmatunitqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fmpmtaskno | fmpmtaskno | int8 | 64 |  | √ | 0 |  |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

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
| 1 | ftagnum_tag | ftagnum_tag | text | 0 |  |  | null |  |
| 2 | freplacemode | freplacemode | varchar | 5 |  | √ | ' ' |  |
| 3 | ftransdictrelqty | ftransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | ftransdictqty | ftransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fqcppbaseqty | fqcppbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 7 | fisreturninspect | fisreturninspect | bpchar | 1 |  | √ | 0 |  |
| 8 | fqcppbasejoinqty | fqcppbasejoinqty | numeric | 23 | 10 | √ | 0 |  |
| 9 | fbasetransapplyqty | fbasetransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 11 | fqcppqty | fqcppqty | numeric | 23 | 10 | √ | 0 |  |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 14 | fqcppjoinqty | fqcppjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 15 | ftransapplyrelqty | ftransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 17 | fbusrejectedqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 18 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 19 | ftagnum | ftagnum | varchar | 255 |  | √ | ' ' |  |
| 20 | ftransapplyqty | ftransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 22 | fbusfeedingqty | 补料数量 | numeric | 23 | 10 | √ | 0 | 补料数量 |
| 23 | finvtransdictqty | finvtransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | ftotalleadtime | ftotalleadtime | numeric | 23 | 10 | √ | 0 |  |
| 25 | fbasetransapplyrelqty | fbasetransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | ftransdictnonqty | ftransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fbasetransdictrelqty | fbasetransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fbuscansendqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 29 | freplacestrategy | freplacestrategy | varchar | 5 |  | √ | ' ' |  |
| 30 | fbusallotqty | fbusallotqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fbusscrapqty | fbusscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fbasetransdictnonqty | fbasetransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | finvtransdictnonqty | finvtransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 35 | finvtransdictrelqty | finvtransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fbomexpandpath | fbomexpandpath | varchar | 500 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_a |  | fdetailid |
| 2 | idx_om_mftstockentry_a |  | fentryid |
