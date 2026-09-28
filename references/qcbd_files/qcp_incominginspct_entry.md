# 来料检验单分录基础资料-qcp_incominginspct_entry

## 来料检验单分录基础资料-主表 t_qcp_inspentry

- **表名称：** 来料检验单分录基础资料-主表
- **表名：** t_qcp_inspentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 来料检验单单头f7 | int8 | 64 |  | √ | 0 | 来料检验单单头F7 qcp_incominginspct_f7 |
| 2 | fsupplyorg | fsupplyorg | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录序号 | int4 | 32 |  | √ | 0 | 分录序号 |
| 4 | fconvertunqty | fconvertunqty | numeric | 23 | 10 | √ | 0 |  |
| 5 | fsrcsnnumberentryid | fsrcsnnumberentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fchkobjid | fchkobjid | int8 | 64 |  | √ | 0 |  |
| 7 | fsrcsnnumberbillid | fsrcsnnumberbillid | int8 | 64 |  | √ | 0 |  |
| 8 | fformula | fformula | varchar | 50 |  | √ | ' ' |  |
| 9 | fmaterialqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | fre | fre | int8 | 64 |  | √ | 0 |  |
| 11 | fordertype | fordertype | varchar | 50 |  | √ | ' ' |  |
| 12 | ftaskstatus | ftaskstatus | varchar | 10 |  | √ | ' ' |  |
| 13 | fwbbillid | fwbbillid | varchar | 50 |  | √ | ' ' |  |
| 14 | fsourcebillno | fsourcebillno | varchar | 500 |  | √ | ' ' |  |
| 15 | fwbbillentryid | fwbbillentryid | varchar | 50 |  | √ | ' ' |  |
| 16 | funqualifiedqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 17 | fsrcbillid | fsrcbillid | int8 | 64 |  | √ | 0 |  |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fmversion | fmversion | int8 | 64 |  | √ | 0 |  |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 21 | finspectproid | 检验方案 | int8 | 64 |  | √ | 0 | 检验方案 qcbd_inspectpro |
| 22 | fwbbillentityentity | fwbbillentityentity | varchar | 50 |  | √ | ' ' |  |
| 23 | fsubcomment | fsubcomment | varchar | 512 |  | √ | ' ' |  |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fshowtype | fshowtype | varchar | 5 |  | √ | ' ' |  |
| 26 | fbasesampuqlyqty | 基本单位样本不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本不合格数 |
| 27 | fbasejoinqty | fbasejoinqty | numeric | 23 | 10 | √ | 0 |  |
| 28 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 29 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 30 | fjoinqty | fjoinqty | numeric | 23 | 10 | √ | 0 |  |
| 31 | fwbbillentity | fwbbillentity | varchar | 50 |  | √ | ' ' |  |
| 32 | fmanudate | fmanudate | timestamp | 0 |  |  | null |  |
| 33 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fsrcbillentity | fsrcbillentity | varchar | 50 |  | √ | ' ' |  |
| 35 | fvaluerecqty | fvaluerecqty | int4 | 32 |  | √ | 0 |  |
| 36 | fresultstatus | fresultstatus | varchar | 10 |  | √ | ' ' |  |
| 37 | fsuspiciousstatus | fsuspiciousstatus | varchar | 5 |  | √ | ' ' |  |
| 38 | fwbbillentryseq | fwbbillentryseq | varchar | 50 |  | √ | ' ' |  |
| 39 | fsrcbillentryid | fsrcbillentryid | int8 | 64 |  | √ | 0 |  |
| 40 | fduedate | fduedate | timestamp | 0 |  |  | null |  |
| 41 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 42 | fscsystem | fscsystem | varchar | 50 |  | √ | ' ' |  |
| 43 | fsettlorg | fsettlorg | int8 | 64 |  | √ | 0 |  |
| 44 | frinsqty | 样本数量 | numeric | 23 | 10 | √ | 0 | 样本数量 |
| 45 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 移动质检任务单 qcmp_taskinfo |
| 46 | fauxpty | fauxpty | int8 | 64 |  | √ | 0 |  |
| 47 | facceptno | facceptno | varchar | 30 |  | √ | ' ' |  |
| 48 | fsamplingsizeqty | fsamplingsizeqty | numeric | 23 | 10 | √ | 0 |  |
| 49 | fchkobjentryid | fchkobjentryid | int8 | 64 |  | √ | 0 |  |
| 50 | finspectionlot | finspectionlot | varchar | 50 |  | √ | ' ' |  |
| 51 | finspfirstentrykey | finspfirstentrykey | varchar | 50 |  | √ | ' ' |  |
| 52 | fwsstageid | fwsstageid | int8 | 64 |  | √ | 0 |  |
| 53 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 54 | fsrcbillentryseq | fsrcbillentryseq | int8 | 64 |  | √ | 0 |  |
| 55 | fbasequaliqty | 基本单位合格数 | numeric | 23 | 10 | √ | 0 | 基本单位合格数 |
| 56 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 57 | fpriceandtax | fpriceandtax | numeric | 23 | 10 | √ | 0 |  |
| 58 | finsdepartment | finsdepartment | int8 | 64 |  | √ | 0 |  |
| 59 | fsampingunqualqty | 样本不合格数 | numeric | 23 | 10 | √ | 0 | 样本不合格数 |
| 60 | fsourcebilltype | fsourcebilltype | varchar | 50 |  | √ | ' ' |  |
| 61 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 62 | fheadbillno | 单据编号（不可编辑） | varchar | 80 |  | √ | ' ' | 单据编号（不可编辑） |
| 63 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | 物料质检信息 bd_inspect_cfg |
| 64 | fsettlcurrency | fsettlcurrency | int8 | 64 |  | √ | 0 |  |
| 65 | fsampingqualqty | 样本合格数 | numeric | 23 | 10 | √ | 0 | 样本合格数 |
| 66 | forderno | forderno | varchar | 50 |  | √ | ' ' |  |
| 67 | femergency | 是否加急 | varchar | 5 |  | √ | ' ' | 是否加急,枚举: A :是 B :否 |
| 68 | fwbbillno | fwbbillno | varchar | 50 |  | √ | ' ' |  |
| 69 | fsampscheme | 抽样方案 | int8 | 64 |  | √ | 0 | 抽样方案 qcbd_sampscheme |
| 70 | facstr | facstr | varchar | 50 |  | √ | ' ' |  |
| 71 | fprocureorg | fprocureorg | int8 | 64 |  | √ | 0 |  |
| 72 | finspectionstd | finspectionstd | int8 | 64 |  | √ | 0 |  |
| 73 | fsrcbilltype | fsrcbilltype | int8 | 64 |  | √ | 0 |  |
| 74 | fisexistsnnumber | fisexistsnnumber | bpchar | 1 |  | √ | '0' |  |
| 75 | fsupplieid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 76 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 77 | fsamppercentage | fsamppercentage | numeric | 23 | 10 | √ | 0 |  |
| 78 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 79 | fproposer | fproposer | int8 | 64 |  | √ | 0 |  |
| 80 | fwsruleid | fwsruleid | int8 | 64 |  | √ | 0 |  |
| 81 | fbaddealsnnumberbotp | fbaddealsnnumberbotp | int8 | 64 |  | √ | 0 |  |
| 82 | fdamagebear | fdamagebear | bpchar | 1 |  | √ | ' ' |  |
| 83 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 84 | fqualifiedqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 85 | fsuppliermasterid | fsuppliermasterid | int8 | 64 |  | √ | 0 |  |
| 86 | facceptid | facceptid | int8 | 64 |  | √ | 0 |  |
| 87 | fbaddeal | 不良品处理 | varchar | 5 |  | √ | 'B' | 不良品处理,枚举: 0 :检验单 1 :不良品处理单 |
| 88 | fsubinspector | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 89 | fdamageqtybasic | fdamageqtybasic | numeric | 23 | 10 | √ | 0 |  |
| 90 | fconvertqty | fconvertqty | numeric | 23 | 10 | √ | 0 |  |
| 91 | fbasesampqlyqty | 基本单位样本合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本合格数 |
| 92 | fqualinsporg | fqualinsporg | int8 | 64 |  | √ | 0 |  |
| 93 | fsrcunitid | fsrcunitid | int8 | 64 |  | √ | 0 |  |
| 94 | fenterresult | fenterresult | bpchar | 1 |  | √ | '0' |  |
| 95 | fsupplydep | fsupplydep | int8 | 64 |  | √ | 0 |  |
| 96 | fbaseunqlyqty | 基本单位不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位不合格数 |
| 97 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 98 | fdamageqty | fdamageqty | numeric | 23 | 10 | √ | 0 |  |
| 99 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_inspry_fseq |  | fseq |
| 2 | idx_qcp_inspry_fmat |  | fmaterialid |
| 3 | idx_qcp_inspry_fid |  | fid |
| 4 | pk_qcp_inspentry |  | fentryid |
| 5 | idx_qcp_inspry_fmatcfg |  | fmaterialcfg |

---

## 来料检验单分录基础资料-分表 t_qcp_inspentry_a

- **表名称：** 来料检验单分录基础资料-分表
- **表名：** t_qcp_inspentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomer | fcustomer | int8 | 64 |  | √ | 0 |  |
| 3 | fentryextf | fentryextf | varchar | 50 |  | √ | ' ' |  |
| 4 | freturnnumber | freturnnumber | varchar | 80 |  | √ | ' ' |  |
| 5 | fexpectcompletedate | 期望完成日期 | timestamp | 0 |  |  | null | 期望完成日期 |
| 6 | finstocknumber | finstocknumber | varchar | 80 |  | √ | ' ' |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_inspentry_a |  | fentryid |
| 2 | index_qcp_inspectma_a |  | fid |
