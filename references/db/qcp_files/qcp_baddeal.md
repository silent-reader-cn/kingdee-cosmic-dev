# 来料不良品处理单-qcp_baddeal

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
| 1 | t_qcp_baddealent_lk_pkey |  | fpkid |
| 2 | idx_qcp_baddealent_lk_fk |  | fentryid |

---

## 来料不良品处理单-多语言表 t_qcp_baddealn_l

- **表名称：** 来料不良品处理单-多语言表
- **表名：** t_qcp_baddealn_l

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
| 1 | idx_qcp_baddlnl_fid |  | fid,flocaleid |
| 2 | idx_qcp_baddlnl_fcomment |  | fcomment |
| 3 | pk_qcp_baddealn_l |  | fpkid |

---

## 来料不良品处理单-主表 t_qcp_baddealn

- **表名称：** 来料不良品处理单-主表
- **表名：** t_qcp_baddealn

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
| 9 | fisyieldrecieve | 让步接收流程 | bpchar | 1 |  | √ | '0' | 让步接收流程 |
| 10 | finspedepartment | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fconfirmauxpty | 确认辅助属性 | int4 | 32 |  | √ | 0 | 确认辅助属性 |
| 13 | finspector | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
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
| 1 | idx_qcp_baddln_fcreatetime |  | fcreatetime |
| 2 | pk_qcp_baddealn |  | fid |
| 3 | idx_qcp_baddln_fbillno |  | fbillno |

---

## 来料不良品处理单-关联追踪表 t_qcp_baddeal_tc

- **表名称：** 来料不良品处理单-关联追踪表
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

## 不良处理信息-分表 t_qcp_baddealnentry_a

- **表名称：** 不良处理信息-分表
- **表名：** t_qcp_baddealnentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 3 | fentryextf | 单据体扩展值 | varchar | 50 |  | √ | ' ' | 单据体扩展值,枚举: A :赠品 B :合并检验 |
| 4 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 5 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 6 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 7 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 11 | freturnnumber | 自动下推退料单编码 | varchar | 80 |  | √ | ' ' | 自动下推退料单编码 |
| 12 | finstocknumber | 自动下推入库单编码 | varchar | 80 |  | √ | ' ' | 自动下推入库单编码 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_baddealnentry_a |  | fentryid |
| 2 | index_qcp_baddealm_a |  | fid |

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

---

## 不良处理信息-子表 t_qcp_baddealnentry

- **表名称：** 不良处理信息-子表
- **表名：** t_qcp_baddealnentry

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
| 10 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fsrcsnnumberentryid | 来源序列号分录ID | int8 | 64 |  | √ | 0 | 来源序列号分录ID |
| 12 | fchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 13 | fsrcsnnumberbillid | 来源序列号单据ID | int8 | 64 |  | √ | 0 | 来源序列号单据ID |
| 14 | funqualitype | 不良品问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 15 | fisdiscount | 是否折让 | bpchar | 1 |  | √ | '0' | 是否折让 |
| 16 | fordertype | 核心单据类型（废弃） | varchar | 50 |  | √ | ' ' | 核心单据类型（废弃） |
| 17 | fsrcsubbillentryseq | 来源子单据体分录序号 | int8 | 64 |  | √ | 0 | 来源子单据体分录序号 |
| 18 | fhandmethed | 处理方式(旧) | varchar | 5 |  | √ | ' ' | 处理方式(旧),枚举: A :退货 B :报废 C :让步接收 T :挑选 |
| 19 | fapplystatus | 申请状态 | varchar | 1 |  | √ | ' ' | 申请状态,枚举: 0 :未开始 1 :进行中 2 :已完成 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fwbbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 22 | fsecondqty | 二次检验关联数量 | numeric | 23 | 10 | √ | 0 | 二次检验关联数量 |
| 23 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 24 | fwbbillentryid | 核心单据分录ID | varchar | 50 |  | √ | ' ' | 核心单据分录ID |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | funqualiqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 29 | funqualitime | 发现日期 | timestamp | 0 |  |  | null | 发现日期 |
| 30 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 31 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 32 | fwbbillentityentity | 核心单据单据体实体 | varchar | 50 |  | √ | ' ' | 核心单据单据体实体 |
| 33 | fdrawpronoticenum | 下推质量问题通知次数 | int4 | 32 |  | √ | 0 | 下推质量问题通知次数 |
| 34 | fmrbqty | MRB关联基本数量 | numeric | 23 | 10 |  | null | MRB关联基本数量 |
| 35 | fwbbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 36 | fmanutime | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 37 | frespondepart | 责任部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 39 | fisexistsnnumber | 是否存在序列号 | bpchar | 1 |  | √ | '0' | 是否存在序列号 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | fexpiretime | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
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
| 53 | fdisprocureorgfield | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | fnewhandid | 处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 55 | fdissettlementorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fsrcunqualiqty | 来源不良品数量 | numeric | 23 | 10 | √ | 0 | 来源不良品数量 |
| 57 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 58 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 59 | fwbbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 60 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 61 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 62 | fresultstatus | 结果状态 | varchar | 10 |  | √ | ' ' | 结果状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 modified :审批修改 |
| 63 | fmrbbillid | MRB评审单内码 | int8 | 64 |  | √ | 0 | MRB评审单内码 |
| 64 | fconvertqty | 换算数量 | numeric | 23 | 10 | √ | 0 | 换算数量 |
| 65 | fjoinbaseqty | 关联基本数量 | numeric | 23 | 10 | √ | 0 | 关联基本数量 |
| 66 | funqualireason | 不良原因 | varchar | 255 |  | √ | ' ' | 不良原因 |
| 67 | fdiscountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 68 | fwbbillentryseq | 核心单据分录序号 | varchar | 50 |  | √ | ' ' | 核心单据分录序号 |
| 69 | fdrawqctopicnum | 下推QC课题管理次数 | int4 | 32 |  | √ | 0 | 下推QC课题管理次数 |
| 70 | fsrcunitid | 源单单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 71 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 72 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 73 | fsrcinspectbillentryid | 来源检验单单据行ID（冗余字段，方便查询反写） | int8 | 64 |  | √ | 0 | 来源检验单单据行ID（冗余字段，方便查询反写） |
| 74 | fyieldrecapply | 让步接收申请 | bpchar | 1 |  | √ | '0' | 让步接收申请 |
| 75 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 76 | fmrbstatus | MRB评审状态 | bpchar | 1 |  |  | null | MRB评审状态,枚举: A :进行中 B :已完成 |
| 77 | fsrcordernum | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 78 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 79 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 80 | fsnnumber | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 81 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 82 | fsrcordertype | 来源单据类型（已废弃） | varchar | 50 |  | √ | ' ' | 来源单据类型（已废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_baddry_fid |  | fid |
| 2 | pk_qcp_baddealnentry |  | fentryid |
| 3 | idx_qcp_baddry_fmat |  | fmaterielid |
| 4 | idx_qcp_baddry_fmatcfg |  | fmaterialcfg |
| 5 | idx_qcp_baddry_fseq |  | fseq |

---

## 序列号分录-子表 t_qcp_badserialnumber

- **表名称：** 序列号分录-子表
- **表名：** t_qcp_badserialnumber

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
| 1 | idx_qcp_badser_eidsno |  | fentryid,fsnnumberrecord |
| 2 | pk_qcp_badserialnumber |  | fdetailid |
| 3 | idx_qcp_badserialnumber |  | fsnnumberrecord |

---

## 来料不良品处理单-反写记录表 t_qcp_baddeal_wb

- **表名称：** 来料不良品处理单-反写记录表
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
