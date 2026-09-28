# 生产不良品处理单-qcpp_manubaddeal

## 关联子实体-子表 t_qcp_baddealent_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_baddealent_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_baddealent_lk_fk |  | fentryid |
| 2 | t_qcp_baddealent_lk_pkey |  | fpkid |

---

## 不良处理信息-分表 t_qcpp_baddealentry_a

- **表名称：** 不良处理信息-分表
- **表名：** t_qcpp_baddealentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryextf | 单据体扩展值 | varchar | 50 |  | √ | ' ' | 单据体扩展值,枚举: A :赠品 B :合并检验 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_qcpp_baddealm_a |  | fid |
| 2 | pk_t_qcpp_baddealentry_a |  | fentryid |

---

## 生产不良品处理单-多语言表 t_qcpp_baddeal_l

- **表名称：** 生产不良品处理单-多语言表
- **表名：** t_qcpp_baddeal_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_baddall_fcomment |  | fcomment |
| 2 | pk_qcpp_baddeal_l |  | fpkid |
| 3 | idx_qcpp_baddall_fid |  | fid,flocaleid |

---

## 不良处理信息-子表 t_qcpp_baddealentry

- **表名称：** 不良处理信息-子表
- **表名：** t_qcpp_baddealentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 3 | fresponuser | 责任人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fchkobjentryid | 检验对象行ID | int8 | 64 |  | √ | 0 | 检验对象行ID |
| 5 | fdrawcapnum | 下推纠正预防措施报告次数 | int4 | 32 |  | √ | 0 | 下推纠正预防措施报告次数 |
| 6 | finspfirstentrykey | 首次检验分录唯一标识 | varchar | 50 |  | √ | ' ' | 首次检验分录唯一标识 |
| 7 | fsecondbaseqty | 二次检验关联基本数量 | numeric | 23 | 10 | √ | 0 | 二次检验关联基本数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 11 | funqualitype | 不良品问题分类 | int8 | 64 |  | √ | 0 | 不良品问题分类 qcbd_unquaproblem |
| 12 | fisdiscount | 是否折让 | bpchar | 1 |  | √ | '0' | 是否折让 |
| 13 | fbaddealsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fsrcsubbillentryseq | 来源子单据体分录序号 | int8 | 64 |  | √ | 0 | 来源子单据体分录序号 |
| 15 | freporttype | 汇报类型 | varchar | 54 |  | √ | ' ' | 汇报类型,枚举: A :正常 B :返工 |
| 16 | fhandmethed | 处理方式(旧) | varchar | 5 |  | √ | ' ' | 处理方式(旧),枚举: A :返工 B :报废 C :让步接收 T :挑选 E :返修 G :工废 L :料废 |
| 17 | fapplystatus | 申请状态 | varchar | 1 |  | √ | ' ' | 申请状态,枚举: 0 :未开始 1 :进行中 2 :已完成 |
| 18 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fwbbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 20 | fsecondqty | 二次检验关联数量 | numeric | 23 | 10 | √ | 0 | 二次检验关联数量 |
| 21 | fmanufactureorder | 核心单据编号（废弃） | varchar | 80 |  | √ | ' ' | 核心单据编号（废弃） |
| 22 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 23 | fwbbillentryid | 核心单据分录ID | varchar | 50 |  | √ | ' ' | 核心单据分录ID |
| 24 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | foproperation | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序定义(废弃) mpdm_workprocedure |
| 26 | funqualiqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | 物料质检信息 bd_inspect_cfg |
| 29 | funqualitime | 发现日期 | timestamp | 0 |  |  | null | 发现日期 |
| 30 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 32 | fwbbillentityentity | 核心单据单据体实体 | varchar | 50 |  | √ | ' ' | 核心单据单据体实体 |
| 33 | fdrawpronoticenum | 下推质量问题通知次数 | int4 | 32 |  | √ | 0 | 下推质量问题通知次数 |
| 34 | fmrbqty | MRB关联基本数量 | numeric | 23 | 10 |  | null | MRB关联基本数量 |
| 35 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | 工作中心定义(废弃) mpdm_workcentre |
| 36 | fwbbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 37 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 38 | frespondepart | 责任部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fqrouteid | 工艺路线编码 | int8 | 64 |  | √ | 0 | 质量工艺路线 qcbd_qmcroute |
| 40 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 41 | foprworkshop | 生产部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 44 | fprocessseq | 工序序列号 | varchar | 50 |  | √ | ' ' | 工序序列号 |
| 45 | fresponorg | 责任组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 47 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 48 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 49 | fhandtime | 处理日期 | timestamp | 0 |  |  | null | 处理日期 |
| 50 | fprounit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 51 | fdiscountamount | 折让金额 | numeric | 23 | 10 | √ | 0 | 折让金额 |
| 52 | fenablemrb | MRB评审 | bpchar | 1 |  | √ | '0' | MRB评审 |
| 53 | fsecondinspec | 二次检验（作废） | bpchar | 1 |  | √ | '0' | 二次检验（作废） |
| 54 | fsrcsubbillentryid | 来源子单据体分录行ID | int8 | 64 |  | √ | 0 | 来源子单据体分录行ID |
| 55 | fmaterielid | 物料主数据 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 56 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 57 | fdisprocureorgfield | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 58 | fnewhandid | 处理方式 | int8 | 64 |  | √ | 0 | 不良品处理方式 bd_badhandmode |
| 59 | fdissettlementorg | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 60 | fsrcunqualiqty | 来源不良品数量 | numeric | 23 | 10 | √ | 0 | 来源不良品数量 |
| 61 | fexpiredate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 62 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 63 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 64 | fwbbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 65 | fmanudate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 66 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 67 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 68 | freporderno | 汇报单编号 | varchar | 80 |  | √ | ' ' | 汇报单编号 |
| 69 | fresultstatus | 结果状态 | varchar | 10 |  | √ | ' ' | 结果状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 modified :审批修改 |
| 70 | fmrbbillid | MRB评审单内码 | int8 | 64 |  | √ | 0 | MRB评审单内码 |
| 71 | fconvertqty | 换算数量 | numeric | 23 | 10 | √ | 0 | 换算数量 |
| 72 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 73 | funqualireason | 不良原因 | varchar | 255 |  | √ | ' ' | 不良原因 |
| 74 | fdiscountcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 75 | fwbbillentryseq | 核心单据分录序号 | varchar | 50 |  | √ | ' ' | 核心单据分录序号 |
| 76 | fdrawqctopicnum | 下推QC课题管理次数 | int4 | 32 |  | √ | 0 | 下推QC课题管理次数 |
| 77 | fsrcunitid | 源单单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 78 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 79 | fproducttype | 产品类型 | varchar | 54 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 80 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 81 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 82 | fyieldrecapply | 让步接收申请 | bpchar | 1 |  | √ | '0' | 让步接收申请 |
| 83 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 84 | fmrbstatus | MRB评审状态 | bpchar | 1 |  |  | null | MRB评审状态,枚举: A :进行中 B :已完成 |
| 85 | fsrcordernum | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 86 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | 物料组织公共信息 bd_materialcommon |
| 87 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 88 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 89 | fsrcordertype | 来源单据类型（已废弃） | varchar | 50 |  | √ | ' ' | 来源单据类型（已废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_baddry_fmat |  | fmaterielid |
| 2 | idx_qcpp_baddry_fseq |  | fseq |
| 3 | pk_qcpp_baddealentry |  | fentryid |
| 4 | idx_qcpp_baddry_fid |  | fid |
| 5 | idx_qcpp_baddry_fmatcfg |  | fmaterialcfg |

---

## 生产不良品处理单-反写记录表 t_qcp_baddeal_wb

- **表名称：** 生产不良品处理单-反写记录表
- **表名：** t_qcp_baddeal_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_baddeal_wb_fk |  | fid |
| 2 | t_qcp_baddeal_wb_pkey |  | fentryid |

---

## 生产不良品处理单-主表 t_qcpp_baddeal

- **表名称：** 生产不良品处理单-主表
- **表名：** t_qcpp_baddeal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fhanddate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 4 | fisautogenfrominspct | 根据检验单不良处理信息自动生成 | varchar | 1 |  | √ | '0' | 根据检验单不良处理信息自动生成 |
| 5 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fisyieldrecieve | 让步接收流程 | bpchar | 1 |  | √ | '0' | 让步接收流程 |
| 10 | finspedepartment | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fconfirmauxpty | 确认辅助属性 | int4 | 32 |  | √ | 0 | 确认辅助属性 |
| 13 | finspector | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcpp_baddal_fbillno |  | fbillno |
| 2 | idx_qcpp_baddal_fcreatetime |  | fcreatetime |
| 3 | pk_qcpp_baddeal |  | fid |

---

## 生产不良品处理单-关联追踪表 t_qcp_baddeal_tc

- **表名称：** 生产不良品处理单-关联追踪表
- **表名：** t_qcp_baddeal_tc

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
| 1 | idx_qcp_baddeal_tc_tbill |  | ftbillid |
| 2 | idx_qcp_baddeal_tc_tid |  | ftid |
| 3 | t_qcp_baddeal_tc_pkey |  | fid |

---

## 关联子实体-子表 t_qcp_baddeal_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_baddeal_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_baddeal_lk_fk |  | fid |
| 2 | t_qcp_baddeal_lk_pkey |  | fpkid |
