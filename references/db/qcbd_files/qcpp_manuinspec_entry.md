# 生产检验单分录基础资料-qcpp_manuinspec_entry

## 生产检验单分录基础资料-主表 t_qcpp_inspentry

- **表名称：** 生产检验单分录基础资料-主表
- **表名：** t_qcpp_inspentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 生产检验单单头f7 | int8 | 64 |  | √ | 0 | 生产检验单单头F7 qcpp_manuinspec_f7 |
| 2 | fsupplyorg | fsupplyorg | int8 | 64 |  | √ | 0 |  |
| 3 | fproductionworkshopid | fproductionworkshopid | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录序号 | int4 | 32 |  | √ | 0 | 分录序号 |
| 5 | fconvertunqty | fconvertunqty | numeric | 23 | 10 | √ | 0 |  |
| 6 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 7 | fchkobjid | fchkobjid | int8 | 64 |  | √ | 0 |  |
| 8 | fformula | fformula | varchar | 50 |  | √ | ' ' |  |
| 9 | fmaterialqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | fre | fre | int8 | 64 |  | √ | 0 |  |
| 11 | freporttype | 汇报类型 | varchar | 54 |  | √ | ' ' | 汇报类型,枚举: A :正常 B :返工 |
| 12 | ftaskstatus | ftaskstatus | varchar | 10 |  | √ | ' ' |  |
| 13 | fwbbillid | fwbbillid | varchar | 50 |  | √ | ' ' |  |
| 14 | fsourcebillno | fsourcebillno | varchar | 500 |  | √ | ' ' |  |
| 15 | fwbbillentryid | fwbbillentryid | varchar | 50 |  | √ | ' ' |  |
| 16 | funqualifiedqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 17 | foproperation | foproperation | int8 | 64 |  | √ | 0 |  |
| 18 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 19 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fmversion | fmversion | int8 | 64 |  | √ | 0 |  |
| 21 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 22 | finspectproid | 检验方案 | int8 | 64 |  | √ | 0 | 检验方案 qcbd_inspectpro |
| 23 | fwbbillentityentity | fwbbillentityentity | varchar | 50 |  | √ | ' ' |  |
| 24 | fproqyt | fproqyt | numeric | 23 | 10 | √ | 0 |  |
| 25 | foperationdesc | foperationdesc | varchar | 50 |  | √ | ' ' |  |
| 26 | fsubcomment | fsubcomment | varchar | 512 |  | √ | ' ' |  |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fshowtype | fshowtype | varchar | 5 |  | √ | ' ' |  |
| 29 | fprocessseq | fprocessseq | varchar | 50 |  | √ | ' ' |  |
| 30 | fbasesampuqlyqty | 基本单位样本不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本不合格数 |
| 31 | fbasejoinqty | fbasejoinqty | numeric | 23 | 10 | √ | 0 |  |
| 32 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 33 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 34 | fexpiredate | fexpiredate | timestamp | 0 |  |  | null |  |
| 35 | fjoinqty | fjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 36 | fwbbillentity | fwbbillentity | varchar | 50 |  | √ | ' ' |  |
| 37 | fmanudate | fmanudate | timestamp | 0 |  |  | null |  |
| 38 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 40 | fvaluerecqty | fvaluerecqty | int4 | 32 |  | √ | 0 |  |
| 41 | freporderno | freporderno | varchar | 500 |  | √ | ' ' |  |
| 42 | fresultstatus | fresultstatus | varchar | 10 |  | √ | ' ' |  |
| 43 | fisfirstinsp | fisfirstinsp | bpchar | 1 |  | √ | ' ' |  |
| 44 | fwbbillentryseq | fwbbillentryseq | varchar | 50 |  | √ | ' ' |  |
| 45 | fproplanentryid | fproplanentryid | int8 | 64 |  | √ | 0 |  |
| 46 | fproducttype | 产品类型 | varchar | 54 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 47 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 48 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 49 | fscsystem | fscsystem | varchar | 50 |  | √ | ' ' |  |
| 50 | fsettlorg | fsettlorg | int8 | 64 |  | √ | 0 |  |
| 51 | frinsqty | 样本数量 | numeric | 23 | 10 | √ | 0 | 样本数量 |
| 52 | ftaskid | ftaskid | int8 | 64 |  | √ | 0 |  |
| 53 | fauxpty | fauxpty | int8 | 64 |  | √ | 0 |  |
| 54 | fsamplingsizeqty | fsamplingsizeqty | numeric | 23 | 10 | √ | 0 |  |
| 55 | fchkobjentryid | fchkobjentryid | int8 | 64 |  | √ | 0 |  |
| 56 | finspectionlot | finspectionlot | varchar | 50 |  | √ | ' ' |  |
| 57 | finspfirstentrykey | finspfirstentrykey | varchar | 50 |  | √ | ' ' |  |
| 58 | fwsstageid | fwsstageid | int8 | 64 |  | √ | 0 |  |
| 59 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 60 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 61 | fbasequaliqty | 基本单位合格数 | numeric | 23 | 10 | √ | 0 | 基本单位合格数 |
| 62 | fprocessdepartid | fprocessdepartid | int8 | 64 |  | √ | 0 |  |
| 63 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 64 | fmanufactureorder | fmanufactureorder | varchar | 80 |  | √ | ' ' |  |
| 65 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0 |  |
| 66 | finsdepartment | finsdepartment | int8 | 64 |  | √ | 0 |  |
| 67 | fsampingunqualqty | 样本不合格数 | numeric | 23 | 10 | √ | 0 | 样本不合格数 |
| 68 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 69 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 70 | fheadbillno | 单据编号（不可编辑） | varchar | 80 |  | √ | ' ' | 单据编号（不可编辑） |
| 71 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | 物料质检信息 bd_inspect_cfg |
| 72 | fsettlcurrency | fsettlcurrency | int8 | 64 |  | √ | 0 |  |
| 73 | fsampingqualqty | 样本合格数 | numeric | 23 | 10 | √ | 0 | 样本合格数 |
| 74 | femergency | 是否加急 | varchar | 5 |  | √ | ' ' | 是否加急,枚举: A :是 B :否 |
| 75 | foprworkcenter | foprworkcenter | int8 | 64 |  | √ | 0 |  |
| 76 | fwbbillno | fwbbillno | varchar | 50 |  | √ | ' ' |  |
| 77 | fqrouteid | fqrouteid | int8 | 64 |  | √ | 0 |  |
| 78 | fsampscheme | 抽样方案 | int8 | 64 |  | √ | 0 | 抽样方案 qcbd_sampscheme |
| 79 | facstr | facstr | varchar | 50 |  | √ | ' ' |  |
| 80 | fprocureorg | fprocureorg | int8 | 64 |  | √ | 0 |  |
| 81 | finspectionstd | finspectionstd | int8 | 64 |  | √ | 0 |  |
| 82 | fsrcbilltype | fsrcbilltype | int8 | 64 |  | √ | 0 |  |
| 83 | foprworkshop | foprworkshop | int8 | 64 |  | √ | 0 |  |
| 84 | foperationno | foperationno | varchar | 50 |  | √ | ' ' |  |
| 85 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 86 | fsamppercentage | fsamppercentage | numeric | 23 | 10 | √ | 0 |  |
| 87 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 88 | fprounit | fprounit | int8 | 64 |  | √ | 0 |  |
| 89 | fproposer | fproposer | int8 | 64 |  | √ | 0 |  |
| 90 | fwsruleid | fwsruleid | int8 | 64 |  | √ | 0 |  |
| 91 | fdamagebear | fdamagebear | bpchar | 1 |  | √ | ' ' |  |
| 92 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 93 | fqualifiedqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 94 | fbaddeal | 不良品处理 | varchar | 5 |  | √ | 'B' | 不良品处理,枚举: 0 :检验单 1 :不良品处理单 |
| 95 | fsubinspector | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 96 | fdamageqtybasic | fdamageqtybasic | numeric | 23 | 10 | √ | 0 |  |
| 97 | fconvertqty | fconvertqty | numeric | 23 | 10 | √ | 0 |  |
| 98 | fbasesampqlyqty | 基本单位样本合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本合格数 |
| 99 | fqualinsporg | fqualinsporg | int8 | 64 |  | √ | 0 |  |
| 100 | fsrcunitid | fsrcunitid | int8 | 64 |  | √ | 0 |  |
| 101 | fenterresult | fenterresult | bpchar | 1 |  | √ | '0' |  |
| 102 | fsupplydep | fsupplydep | int8 | 64 |  | √ | 0 |  |
| 103 | fbaseunqlyqty | 基本单位不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位不合格数 |
| 104 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 105 | fdamageqty | fdamageqty | numeric | 23 | 10 | √ | 0 |  |
| 106 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

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
| 2 | fentryextf | fentryextf | varchar | 50 |  | √ | ' ' |  |
| 3 | fexpectcompletedate | 期望完成日期 | timestamp | 0 |  |  | null | 期望完成日期 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_qcpp_inspectma_a |  | fid |
| 2 | pk_t_qcpp_inspentry_a |  | fentryid |
