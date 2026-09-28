# 生产用料清单分录f7-pom_mftstockentryf7

## 生产用料清单分录f7-分表 t_pom_manustockentry_b

- **表名称：** 生产用料清单分录f7-分表
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
| 11 | fbusactissueqty | 实发数量 | numeric | 23 | 10 | √ | 0 | 实发数量 |
| 12 | factreceivebaseqty | 实领基本数量 | numeric | 23 | 10 | √ | 0 | 实领基本数量 |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fparentmaterialid | fparentmaterialid | int8 | 64 |  | √ | 0 |  |
| 15 | factreceiveqty | 实领数量 | numeric | 23 | 10 | √ | 0 | 实领数量 |
| 16 | ftopmaterialid | ftopmaterialid | int8 | 64 |  | √ | 0 |  |
| 17 | fbadincomerejectedqty | fbadincomerejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 18 | fbusbadtaskrejectedqty | fbusbadtaskrejectedqty | numeric | 23 | 10 | √ | 0 |  |
| 19 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 20 | fbusstandqty | fbusstandqty | numeric | 23 | 10 | √ | 0 |  |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 22 | fisjumplevel | fisjumplevel | bpchar | 1 |  | √ | '0' |  |
| 23 | favbinvqty | favbinvqty | numeric | 23 | 10 | √ | 0 |  |
| 24 | fisentryexpandone | fisentryexpandone | varchar | 5 |  | √ | '0' |  |
| 25 | fbusoutqty | fbusoutqty | numeric | 23 | 10 | √ | 0 |  |
| 26 | fbususeqty | fbususeqty | numeric | 23 | 10 | √ | 0 |  |
| 27 | fbusunissueqty | fbusunissueqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | fneedbaseqty | fneedbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 29 | fbusdemandqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
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

## 生产用料清单分录f7-分表 t_pom_manustockentry_a

- **表名称：** 生产用料清单分录f7-分表
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
| 8 | fprocessplan | fprocessplan | varchar | 50 |  | √ | ' ' |  |
| 9 | fbasetransapplyqty | fbasetransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 10 | fqcppqty | fqcppqty | numeric | 23 | 10 | √ | 0 |  |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 13 | fqcppjoinqty | fqcppjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 14 | fprocessnumber | fprocessnumber | int4 | 32 |  | √ | 0 |  |
| 15 | fissinlowlimit | fissinlowlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fisreplace | fisreplace | bpchar | 1 |  | √ | '0' |  |
| 17 | fscrapqty | fscrapqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 18 | ftagnum | ftagnum | varchar | 255 |  | √ | ' ' |  |
| 19 | ftransapplyqty | ftransapplyqty | numeric | 23 | 10 | √ | 0 |  |
| 20 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 21 | frejectedqty | frejectedqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 22 | finvtransdictqty | finvtransdictqty | numeric | 23 | 10 | √ | 0 |  |
| 23 | fiskeypart | fiskeypart | bpchar | 1 |  | √ | '0' |  |
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
| 37 | fprocesssequence | fprocesssequence | int4 | 32 |  | √ | 0 |  |
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
| 52 | fleadtime | fleadtime | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 53 | foverissuecontrl | foverissuecontrl | varchar | 30 |  | √ | ' ' |  |
| 54 | ftransapplyrelqty | ftransapplyrelqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fissinhighlimit | fissinhighlimit | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 56 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 57 | fbusrejectedqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 58 | fismainreplace | fismainreplace | bpchar | 1 |  | √ | '0' |  |
| 59 | fisbackflush | fisbackflush | bpchar | 1 |  | √ | '0' |  |
| 60 | fbusfeedingqty | 补料数量 | numeric | 23 | 10 | √ | 0 | 补料数量 |
| 61 | flackraitioqty | flackraitioqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 62 | ftotalleadtime | ftotalleadtime | numeric | 23 | 10 | √ | 0 |  |
| 63 | fbasetransdictrelqty | fbasetransdictrelqty | numeric | 23 | 10 | √ | 0 |  |
| 64 | fisbulkmaterial | fisbulkmaterial | bpchar | 1 |  | √ | '0' |  |
| 65 | fbusscrapqty | fbusscrapqty | numeric | 23 | 10 | √ | 0 |  |
| 66 | fbasetransdictnonqty | fbasetransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 67 | finvtransdictnonqty | finvtransdictnonqty | numeric | 23 | 10 | √ | 0 |  |
| 68 | fcansendqty | fcansendqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 69 | fisbackflushnew | fisbackflushnew | varchar | 30 |  | √ | ' ' |  |
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

## 生产用料清单分录f7-主表 t_pom_manustockentry

- **表名称：** 生产用料清单分录f7-主表
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
| 10 | foutlocation | foutlocation | int8 | 64 |  | √ | 0 |  |
| 11 | fscraprate | fscraprate | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | foperatemrp | foperatemrp | bpchar | 1 |  | √ | '0' |  |
| 14 | fisreturninspect | fisreturninspect | bpchar | 1 |  | √ | 0 |  |
| 15 | fworkplanid | fworkplanid | int8 | 64 |  | √ | 0 |  |
| 16 | fownertype | fownertype | varchar | 30 |  | √ | ' ' |  |
| 17 | fisstockallot | fisstockallot | bpchar | 1 |  | √ | '0' |  |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | frework | frework | bpchar | 1 |  | √ | '0' |  |
| 21 | fecostcenterid | fecostcenterid | int8 | 64 |  | √ | 0 |  |
| 22 | fuseratio | fuseratio | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 23 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 24 | fqtydenominator | fqtydenominator | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 26 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 27 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 28 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 30 | fworkstation | fworkstation | int8 | 64 |  | √ | 0 |  |
| 31 | fisstep | fisstep | bpchar | 1 |  | √ | '0' |  |
| 32 | fk_bj73_ylbillid | fk_bj73_ylbillid | varchar | 50 |  | √ | ' ' |  |
| 33 | fsupplymode | fsupplymode | varchar | 30 |  | √ | ' ' |  |
| 34 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 35 | flotid | flotid | int8 | 64 |  | √ | 0 |  |
| 36 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | fchildbomversion | fchildbomversion | varchar | 50 |  | √ | ' ' |  |
| 38 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | foutsqty | foutsqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | foutqty | foutqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fsupplytype | fsupplytype | varchar | 30 |  | √ | ' ' |  |
| 43 | freservebaseqty | freservebaseqty | numeric | 23 | 10 | √ | 0 |  |
| 44 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 45 | fk_bj73_qtyfield | fk_bj73_qtyfield | numeric | 23 | 10 |  | null |  |
| 46 | fentryconfiguredcodeid | fentryconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 47 | fk_bj73_zfl | fk_bj73_zfl | numeric | 23 | 10 |  | null |  |
| 48 | fmaterielmasterid | fmaterielmasterid | int8 | 64 |  | √ | 0 |  |
| 49 | fuseqty | fuseqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | factissueqty | 实发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 实发基本数量 |
| 51 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 52 | foutorgunitid | foutorgunitid | int8 | 64 |  | √ | 0 |  |
| 53 | favbbaseqty | favbbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 54 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型 |
| 55 | fqtynumerator | fqtynumerator | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 56 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 57 | ffixscrap | ffixscrap | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 58 | foutwarehouseid | foutwarehouseid | int8 | 64 |  | √ | 0 |  |
| 59 | fprovideorgid | fprovideorgid | int8 | 64 |  | √ | 0 |  |
| 60 | fdemandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应发基本数量 |

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
| 5 | idx_stocken_feconfiguredcode |  | fentryconfiguredcodeid |
| 6 | idx_pom_mse_fentryid |  | fentryid |
| 7 | idx_stocken_mid |  | fmaterielmasterid |
