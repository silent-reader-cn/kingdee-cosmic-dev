# 生产检验单分录基础资料-qcpp_manuinspec_entry

## 生产检验单分录基础资料-主表 t_qcpp_inspentry

- **表名称：** 生产检验单分录基础资料-主表
- **表名：** t_qcpp_inspentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 生产检验单单头f7 | int8 | 64 |  | √ | 0 | [生产检验单单头F7 qcpp_manuinspec_f7](../qcbd_files/qcpp_manuinspec_f7.md) |
| 2 | fsupplyorg | fsupplyorg | int8 | 64 |  | √ | 0 |  |
| 3 | fproductionworkshopid | fproductionworkshopid | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录序号 | int4 | 32 |  | √ | 0 | 分录序号 |
| 5 | fconvertunqty | fconvertunqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 7 | fsrcsnnumberentryid | fsrcsnnumberentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fchkobjid | fchkobjid | int8 | 64 |  | √ | 0 |  |
| 9 | fsrcsnnumberbillid | fsrcsnnumberbillid | int8 | 64 |  | √ | 0 |  |
| 10 | fformula | fformula | varchar | 50 |  | √ | ' ' |  |
| 11 | fmaterialqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fre | fre | int8 | 64 |  | √ | 0 |  |
| 13 | freporttype | 汇报类型 | varchar | 54 |  | √ | ' ' | 汇报类型,枚举: A :正常 B :返工 |
| 14 | ftaskstatus | ftaskstatus | varchar | 10 |  | √ | ' ' |  |
| 15 | fwbbillid | fwbbillid | varchar | 50 |  | √ | ' ' |  |
| 16 | fsourcebillno | fsourcebillno | varchar | 500 |  | √ | ' ' |  |
| 17 | fwbbillentryid | fwbbillentryid | varchar | 50 |  | √ | ' ' |  |
| 18 | funqualifiedqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 19 | foproperation | foproperation | int8 | 64 |  | √ | 0 |  |
| 20 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fmversion | fmversion | int8 | 64 |  | √ | 0 |  |
| 23 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 24 | finspectproid | 检验方案 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 25 | fwbbillentityentity | fwbbillentityentity | varchar | 50 |  | √ | ' ' |  |
| 26 | fproqyt | fproqyt | numeric | 23 | 10 | √ | 0 |  |
| 27 | foperationdesc | foperationdesc | varchar | 50 |  | √ | ' ' |  |
| 28 | fsubcomment | fsubcomment | varchar | 512 |  | √ | ' ' |  |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fshowtype | fshowtype | varchar | 5 |  | √ | ' ' |  |
| 31 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 32 | fbasesampuqlyqty | 基本单位样本不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本不合格数 |
| 33 | fbasejoinqty | fbasejoinqty | numeric | 23 | 10 | √ | 0 |  |
| 34 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 35 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 36 | fexpiredate | fexpiredate | timestamp | 0 |  |  | null |  |
| 37 | fjoinqty | fjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 38 | fwbbillentity | fwbbillentity | varchar | 50 |  | √ | ' ' |  |
| 39 | fmanudate | fmanudate | timestamp | 0 |  |  | null |  |
| 40 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 42 | fvaluerecqty | fvaluerecqty | int4 | 32 |  | √ | 0 |  |
| 43 | freporderno | freporderno | varchar | 500 |  | √ | ' ' |  |
| 44 | fresultstatus | fresultstatus | varchar | 10 |  | √ | ' ' |  |
| 45 | fisfirstinsp | fisfirstinsp | bpchar | 1 |  | √ | ' ' |  |
| 46 | fwbbillentryseq | fwbbillentryseq | varchar | 50 |  | √ | ' ' |  |
| 47 | fproplanentryid | fproplanentryid | int8 | 64 |  | √ | 0 |  |
| 48 | fproducttype | 产品类型 | varchar | 54 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 49 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 50 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 51 | fscsystem | fscsystem | varchar | 50 |  | √ | ' ' |  |
| 52 | fsettlorg | fsettlorg | int8 | 64 |  | √ | 0 |  |
| 53 | frinsqty | 样本数量 | numeric | 23 | 10 | √ | 0 | 样本数量 |
| 54 | ftaskid | ftaskid | int8 | 64 |  | √ | 0 |  |
| 55 | fauxpty | fauxpty | int8 | 64 |  | √ | 0 |  |
| 56 | fsamplingsizeqty | fsamplingsizeqty | numeric | 23 | 10 | √ | 0 |  |
| 57 | fchkobjentryid | fchkobjentryid | int8 | 64 |  | √ | 0 |  |
| 58 | finspectionlot | finspectionlot | varchar | 50 |  | √ | ' ' |  |
| 59 | finspfirstentrykey | finspfirstentrykey | varchar | 50 |  | √ | ' ' |  |
| 60 | fwsstageid | fwsstageid | int8 | 64 |  | √ | 0 |  |
| 61 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 62 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 63 | fbasequaliqty | 基本单位合格数 | numeric | 23 | 10 | √ | 0 | 基本单位合格数 |
| 64 | fprocessdepartid | fprocessdepartid | int8 | 64 |  | √ | 0 |  |
| 65 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 66 | fmanufactureorder | fmanufactureorder | varchar | 80 |  | √ | ' ' |  |
| 67 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0 |  |
| 68 | finsdepartment | finsdepartment | int8 | 64 |  | √ | 0 |  |
| 69 | fsampingunqualqty | 样本不合格数 | numeric | 23 | 10 | √ | 0 | 样本不合格数 |
| 70 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 71 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 72 | fheadbillno | 单据编号（不可编辑） | varchar | 80 |  | √ | ' ' | 单据编号（不可编辑） |
| 73 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 74 | fsettlcurrency | fsettlcurrency | int8 | 64 |  | √ | 0 |  |
| 75 | fsampingqualqty | 样本合格数 | numeric | 23 | 10 | √ | 0 | 样本合格数 |
| 76 | femergency | 是否加急 | varchar | 5 |  | √ | ' ' | 是否加急,枚举: A :是 B :否 |
| 77 | foprworkcenter | foprworkcenter | int8 | 64 |  | √ | 0 |  |
| 78 | fwbbillno | fwbbillno | varchar | 50 |  | √ | ' ' |  |
| 79 | fqrouteid | fqrouteid | int8 | 64 |  | √ | 0 |  |
| 80 | fsampscheme | 抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 81 | facstr | facstr | varchar | 50 |  | √ | ' ' |  |
| 82 | fprocureorg | fprocureorg | int8 | 64 |  | √ | 0 |  |
| 83 | finspectionstd | finspectionstd | int8 | 64 |  | √ | 0 |  |
| 84 | fsrcbilltype | fsrcbilltype | int8 | 64 |  | √ | 0 |  |
| 85 | fisexistsnnumber | fisexistsnnumber | bpchar | 1 |  | √ | '0' |  |
| 86 | foprworkshop | foprworkshop | int8 | 64 |  | √ | 0 |  |
| 87 | foperationno | foperationno | varchar | 50 |  | √ | ' ' |  |
| 88 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 89 | fsamppercentage | fsamppercentage | numeric | 23 | 10 | √ | 0 |  |
| 90 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 91 | fprounit | fprounit | int8 | 64 |  | √ | 0 |  |
| 92 | fproposer | fproposer | int8 | 64 |  | √ | 0 |  |
| 93 | fwsruleid | fwsruleid | int8 | 64 |  | √ | 0 |  |
| 94 | fbaddealsnnumberbotp | fbaddealsnnumberbotp | int8 | 64 |  | √ | 0 |  |
| 95 | fdamagebear | fdamagebear | bpchar | 1 |  | √ | ' ' |  |
| 96 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 97 | fqualifiedqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 98 | fbaddeal | 不良品处理 | varchar | 5 |  | √ | 'B' | 不良品处理,枚举: 0 :检验单 1 :不良品处理单 |
| 99 | fsubinspector | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 100 | fdamageqtybasic | fdamageqtybasic | numeric | 23 | 10 | √ | 0 |  |
| 101 | fconvertqty | fconvertqty | numeric | 23 | 10 | √ | 0 |  |
| 102 | fbasesampqlyqty | 基本单位样本合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本合格数 |
| 103 | fqualinsporg | fqualinsporg | int8 | 64 |  | √ | 0 |  |
| 104 | fsrcunitid | fsrcunitid | int8 | 64 |  | √ | 0 |  |
| 105 | fenterresult | fenterresult | bpchar | 1 |  | √ | '0' |  |
| 106 | fsupplydep | fsupplydep | int8 | 64 |  | √ | 0 |  |
| 107 | fbaseunqlyqty | 基本单位不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位不合格数 |
| 108 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 109 | fdamageqty | fdamageqty | numeric | 23 | 10 | √ | 0 |  |
| 110 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcpp_inspentry |  | fentryid |
| 2 | idx_qcpp_inspry_fid |  | fid |
| 3 | idx_qcpp_inspry_fmat |  | fmaterialid |
| 4 | idx_qcpp_inspry_fseq |  | fseq |
| 5 | idx_qcpp_inspry_fmatcfg |  | fmaterialcfg |

---

## 生产检验单分录基础资料-分表 t_qcpp_inspentry_a

- **表名称：** 生产检验单分录基础资料-分表
- **表名：** t_qcpp_inspentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furgentqty | furgentqty | numeric | 23 | 10 | √ | 0 |  |
| 3 | furgentjoinbaseqty | furgentjoinbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 4 | finspectstatus | finspectstatus | varchar | 30 |  | √ | 'INSPECTING' |  |
| 5 | furgentjoinqty | furgentjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | furgentbaseqty | furgentbaseqty | numeric | 23 | 10 | √ | 0 |  |
| 7 | fentryextf | fentryextf | varchar | 50 |  | √ | ' ' |  |
| 8 | flicensenoid | flicensenoid | int8 | 64 |  | √ | 0 |  |
| 9 | furgentrelease | furgentrelease | bpchar | 1 |  | √ | '0' |  |
| 10 | fexpectcompletedate | 期望完成日期 | timestamp | 0 |  |  | null | 期望完成日期 |
| 11 | fassqty2 | fassqty2 | numeric | 23 | 10 | √ | 0 |  |
| 12 | fassunit2id | fassunit2id | int8 | 64 |  | √ | 0 |  |
| 13 | fbonded | fbonded | bpchar | 1 |  | √ | '0' |  |
| 14 | fassunitid | fassunitid | int8 | 64 |  | √ | 0 |  |
| 15 | fassqty | fassqty | numeric | 23 | 10 | √ | 0 |  |
| 16 | fursaveunwrite | fursaveunwrite | bpchar | 1 |  | √ | '0' |  |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_qcpp_inspectma_a |  | fid |
| 2 | pk_t_qcpp_inspentry_a |  | fentryid |
