# 销售不良品处理单-qcas_salebaddeal

## 序列号分录-子表 t_qcas_badserialnumber

- **表名称：** 序列号分录-子表
- **表名：** t_qcas_badserialnumber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcheckhandtypedefalut | 检验处理方式合格(隐藏，用于业务规则合格时赋值) | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 2 | frowindex | 行号索引 | int4 | 32 |  | √ | 0 | 行号索引 |
| 3 | fisspotcheck | 是否抽检 | bpchar | 1 |  | √ | '0' | 是否抽检 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcheckhandtypeunqualiqty | 检验处理方式不合格(隐藏，用于业务规则合格时赋值) | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fsnnumberrecord | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 8 | fcheckstate | 检验状态 | varchar | 10 |  | √ | ' ' | 检验状态,枚举: 0 :合格 1 :不合格 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fcheckhandtype | 检验处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcas_badserialnumber |  | fsnnumberrecord |
| 2 | idx_qcas_badser_eidsno |  | fentryid,fsnnumberrecord |
| 3 | pk_qcas_badserialnumber |  | fdetailid |

---

## 销售不良品处理单-主表 t_qcas_baddeal

- **表名称：** 销售不良品处理单-主表
- **表名：** t_qcas_baddeal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fhanddate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 4 | fisautogenfrominspct | 根据检验单不良处理信息自动生成 | varchar | 1 |  | √ | '0' | 根据检验单不良处理信息自动生成 |
| 5 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | finspedepartment | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fconfirmauxpty | 确认辅助属性 | int4 | 32 |  | √ | 0 | 确认辅助属性 |
| 12 | finspector | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fadjustbillid | 关联的形态转换单ID（隐藏） | int8 | 64 |  | √ | 0 | 关联的形态转换单ID（隐藏） |
| 15 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcas_baddal_fbillno |  | fbillno |
| 2 | pk_qcas_baddeal |  | fid |
| 3 | idx_qcas_baddal_fcreatetime |  | fcreatetime |

---

## 销售不良品处理单-反写记录表 t_qcas_baddeal_wb

- **表名称：** 销售不良品处理单-反写记录表
- **表名：** t_qcas_baddeal_wb

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
| 1 | idx_qcas_baddeal_wb_fk |  | fid |
| 2 | pk_qcas_baddeal_wb |  | fentryid |

---

## 销售不良品处理单-多语言表 t_qcas_baddeal_l

- **表名称：** 销售不良品处理单-多语言表
- **表名：** t_qcas_baddeal_l

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
| 1 | idx_qcas_baddall_fcomment |  | fcomment |
| 2 | idx_qcas_baddall_fid |  | fid,flocaleid |
| 3 | pk_qcas_baddeal_l |  | fpkid |

---

## 关联子实体-子表 t_qcas_baddeal_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcas_baddeal_lk

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
| 1 | pk_qcas_baddeal_lk |  | fpkid |
| 2 | idx_qcas_baddeal_lk_fk |  | fid |

---

## 不良处理信息-分表 t_qcas_baddealentry_a

- **表名称：** 不良处理信息-分表
- **表名：** t_qcas_baddealentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | freceiveprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 5 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcas_badentry_a |  | fentryid |

---

## 销售不良品处理单-关联追踪表 t_qcas_baddeal_tc

- **表名称：** 销售不良品处理单-关联追踪表
- **表名：** t_qcas_baddeal_tc

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
| 1 | idx_qcas_baddeal_tc_tid |  | ftid |
| 2 | pk_qcas_baddeal_tc |  | fid |
| 3 | idx_qcas_baddeal_tc_tbill |  | ftbillid |

---

## 不良处理信息-子表 t_qcas_baddealentry

- **表名称：** 不良处理信息-子表
- **表名：** t_qcas_baddealentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresponuser | 责任人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fchkobjentryid | 检验对象行ID | int8 | 64 |  | √ | 0 | 检验对象行ID |
| 4 | fdrawcapnum | 下推纠正预防措施报告次数 | int4 | 32 |  | √ | 0 | 下推纠正预防措施报告次数 |
| 5 | finspfirstentrykey | 首次检验分录唯一标识 | varchar | 50 |  | √ | ' ' | 首次检验分录唯一标识 |
| 6 | fordernum | 核心单据编号（废弃） | varchar | 80 |  | √ | ' ' | 核心单据编号（废弃） |
| 7 | fsecondbaseqty | 二次检验关联基本数量 | numeric | 23 | 10 | √ | 0 | 二次检验关联基本数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 10 | fsrcsnnumberentryid | 来源序列号分录ID | int8 | 64 |  | √ | 0 | 来源序列号分录ID |
| 11 | fchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 12 | fsrcsnnumberbillid | 来源序列号单据ID | int8 | 64 |  | √ | 0 | 来源序列号单据ID |
| 13 | funqualitype | 不良品问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 14 | fisdiscount | 是否折让 | bpchar | 1 |  | √ | '0' | 是否折让 |
| 15 | fsrcsubbillentryseq | 来源子单据体分录序号 | int8 | 64 |  | √ | 0 | 来源子单据体分录序号 |
| 16 | fhandmethed | 处理方式(旧) | varchar | 5 |  | √ | ' ' | 处理方式(旧),枚举: C :让步接收 F :让步放行 B :报废 T :挑选 |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fwbbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 19 | fsecondqty | 二次检验关联数量 | numeric | 23 | 10 | √ | 0 | 二次检验关联数量 |
| 20 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 21 | fwbbillentryid | 核心单据分录ID | varchar | 50 |  | √ | ' ' | 核心单据分录ID |
| 22 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 23 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | funqualiqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 25 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 26 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 27 | finvtargetstatus | finvtargetstatus | int8 | 64 |  | √ | 0 |  |
| 28 | funqualitime | 发现日期 | timestamp | 0 |  |  | null | 发现日期 |
| 29 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 30 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | fwbbillentityentity | 核心单据单据体实体 | varchar | 50 |  | √ | ' ' | 核心单据单据体实体 |
| 33 | fdrawpronoticenum | 下推质量问题通知次数 | int4 | 32 |  | √ | 0 | 下推质量问题通知次数 |
| 34 | fmrbqty | MRB关联基本数量 | numeric | 23 | 10 |  | null | MRB关联基本数量 |
| 35 | fwbbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 36 | frespondepart | 责任部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fdisqualsales | 不合格可销售 | varchar | 1 |  | √ | '0' | 不合格可销售 |
| 38 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 39 | fisexistsnnumber | 是否存在序列号 | bpchar | 1 |  | √ | '0' | 是否存在序列号 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | ferexpenditemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 43 | fresponorg | 责任组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 45 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 46 | fhandtime | 处理日期 | timestamp | 0 |  |  | null | 处理日期 |
| 47 | fdiscountamount | 折让金额 | numeric | 23 | 10 | √ | 0 | 折让金额 |
| 48 | fenablemrb | MRB评审 | bpchar | 1 |  | √ | '0' | MRB评审 |
| 49 | fsecondinspec | 二次检验（作废） | bpchar | 1 |  | √ | '0' | 二次检验（作废） |
| 50 | fsrcsubbillentryid | 来源子单据体分录行ID | int8 | 64 |  | √ | 0 | 来源子单据体分录行ID |
| 51 | fmaterielid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 52 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 53 | fdisprocureorgfield | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fnewhandid | 处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 55 | fdissettlementorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 57 | fsrcunqualiqty | 来源不良品数量 | numeric | 23 | 10 | √ | 0 | 来源不良品数量 |
| 58 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 59 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 60 | fwbbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 61 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 63 | fresultstatus | 结果状态 | varchar | 10 |  | √ | ' ' | 结果状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 modified :审批修改 |
| 64 | fmrbbillid | MRB评审单内码 | int8 | 64 |  | √ | 0 | MRB评审单内码 |
| 65 | fsalesreturn | 是否退货 | varchar | 1 |  | √ | '0' | 是否退货 |
| 66 | fconvertqty | 换算数量 | numeric | 23 | 10 | √ | 0 | 换算数量 |
| 67 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 68 | feadjustbillid | 形态转换单ID | int8 | 64 |  | √ | 0 | 形态转换单ID |
| 69 | funqualireason | 不良原因 | varchar | 255 |  | √ | ' ' | 不良原因 |
| 70 | fdiscountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 71 | fwbbillentryseq | 核心单据分录序号 | varchar | 50 |  | √ | ' ' | 核心单据分录序号 |
| 72 | fdrawqctopicnum | 下推QC课题管理次数 | int4 | 32 |  | √ | 0 | 下推QC课题管理次数 |
| 73 | fsrcunitid | 源单单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 74 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 75 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 76 | fsrcinspectbillentryid | 来源检验单单据行ID（冗余字段，方便查询反写） | int8 | 64 |  | √ | 0 | 来源检验单单据行ID（冗余字段，方便查询反写） |
| 77 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 78 | fmrbstatus | MRB评审状态 | bpchar | 1 |  |  | null | MRB评审状态,枚举: A :进行中 B :已完成 |
| 79 | fsrcordernum | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 80 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 81 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 82 | fsnnumber | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 83 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 84 | fsrcordertype | 来源单据类型（已废弃） | varchar | 50 |  | √ | ' ' | 来源单据类型（已废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcas_baddry_fmatcfg |  | fmaterialcfg |
| 2 | idx_qcas_baddry_fseq |  | fseq |
| 3 | pk_qcas_baddealentry |  | fentryid |
| 4 | idx_qcas_baddry_fid |  | fid |
| 5 | idx_qcas_baddry_fmat |  | fmaterielid |

---

## 关联子实体-子表 t_qcas_baddealentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcas_baddealentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcas_baddealentry_lk |  | fpkid |
| 2 | idx_qcas_baddealentry_lk_fk |  | fentryid |
