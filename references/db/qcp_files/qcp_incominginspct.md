# 来料检验单-qcp_incominginspct

## 检验明细-子表 t_qcp_inspsubresproj

- **表名称：** 检验明细-子表
- **表名：** t_qcp_inspsubresproj

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetectiontype | 检测值类型 | int8 | 64 |  | √ | 0 | [检测值类型 qcbd_detectiontype](../qcbd_files/qcbd_detectiontype.md) |
| 2 | fprojckval | 实测值(数量) | numeric | 23 | 10 | √ | 0 | 实测值(数量) |
| 3 | finspectioncontent | 检验内容 | varchar | 255 |  | √ | ' ' | 检验内容 |
| 4 | fnormtype | 指标类型 | varchar | 5 |  | √ | ' ' | 指标类型,枚举: A :定量 B :定性 |
| 5 | fspecvalue | 标准值 | varchar | 50 |  | √ | ' ' | 标准值 |
| 6 | fprojckresult | 项目检验结果 | varchar | 5 |  | √ | ' ' | 项目检验结果,枚举: Y :合格 N :不合格 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftopvalue | 上限值 | numeric | 23 | 10 |  | null | 上限值 |
| 9 | fjoininspentryid | 联合检验单分录id | int8 | 64 |  | √ | 0 | 联合检验单分录id |
| 10 | fmeasureddeter | 实测值(定性) | varchar | 50 |  | √ | ' ' | 实测值(定性) |
| 11 | fsrcitementity | 检验项来源实体 | varchar | 30 |  | √ | ' ' | 检验项来源实体 |
| 12 | finspeccomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 13 | fmeasuredration | 实测值(定量) | numeric | 23 | 10 |  | null | 实测值(定量) |
| 14 | fprojrejectqty | 项目拒收数（弃用） | numeric | 23 | 10 | √ | 0 | 项目拒收数（弃用） |
| 15 | fstandevia | 标准差（弃用） | varchar | 100 |  | √ | ' ' | 标准差（弃用） |
| 16 | fjoininspectstatus | 联合检验状态 | varchar | 5 |  | √ | ' ' | 联合检验状态,枚举: P :计划 Y :已完成 |
| 17 | finspectinstruct | 检验仪器 | int8 | 64 |  | √ | 0 | [检验仪器 qcbd_inspectioninstru](../qcbd_files/qcbd_inspectioninstru.md) |
| 18 | fprojsampqty | 项目样本数量 | numeric | 23 | 10 | √ | 0 | 项目样本数量 |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | finspectfreq | 检验频率 | int8 | 64 |  | √ | 0 | [检验频率 qcbd_inspectionfreq](../qcbd_files/qcbd_inspectionfreq.md) |
| 21 | fprojqualifiyqty | 项目样本合格数 | numeric | 23 | 10 | √ | 0 | 项目样本合格数 |
| 22 | finspsubentryextf | 检验项目扩展值 | varchar | 50 |  | √ | ' ' | 检验项目扩展值,枚举: A :非检验标准携带 |
| 23 | fdownvalue | 下限值 | numeric | 23 | 10 |  | null | 下限值 |
| 24 | fmaxvalue | 最大值（弃用） | varchar | 100 |  | √ | ' ' | 最大值（弃用） |
| 25 | fcomparison | 比较符 | int8 | 64 |  | √ | 0 | [比较符 qcbd_matchflag](../qcbd_files/qcbd_matchflag.md) |
| 26 | fisjoininspect | 联合检验项 | bpchar | 1 |  | √ | '0' | 联合检验项 |
| 27 | fuquuid | 唯一标识 | varchar | 50 |  | √ | ' ' | 唯一标识 |
| 28 | fsrcitementryid | 检验项来源分录id | int8 | 64 |  | √ | 0 | 检验项来源分录id |
| 29 | fexamples | 实测值导入过程字段 | varchar | 255 |  | √ | ' ' | 实测值导入过程字段 |
| 30 | finspecunitid | 检验项目单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fprojacceptqty | 项目允收数 | numeric | 23 | 10 | √ | 0 | 项目允收数 |
| 32 | finspectionitem | 检验项目 | int8 | 64 |  | √ | 0 | [检验项目 qcbd_inspectionitems](../qcbd_files/qcbd_inspectionitems.md) |
| 33 | fminvalue | 最小值（弃用） | varchar | 100 |  | √ | ' ' | 最小值（弃用） |
| 34 | finspectmethod | 检验方法 | int8 | 64 |  | √ | 0 | [检验方法 qcbd_inspectionmethod](../qcbd_files/qcbd_inspectionmethod.md) |
| 35 | fkeyquality | 特性分类 | varchar | 5 |  | √ | ' ' | 特性分类,枚举: A :关键特性 C :重要特性 B :一般特性 |
| 36 | fprojsampid | 项目抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 37 | finspectbasis | 检验依据 | int8 | 64 |  | √ | 0 | [检验依据 qcbd_inspectioncrit](../qcbd_files/qcbd_inspectioncrit.md) |
| 38 | fchoosesampqty | 选择样本数量 | numeric | 23 | 10 | √ | 0 | 选择样本数量 |
| 39 | favevalue | 平均值（弃用） | varchar | 100 |  | √ | ' ' | 平均值（弃用） |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 41 | fprojunqualifiyqty | 项目样本不合格数 | numeric | 23 | 10 | √ | 0 | 项目样本不合格数 |
| 42 | fexamples_tag | 实测值导入过程字段_详情 | text | 0 |  |  | null | 实测值导入过程字段_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_inspsubresproj |  | fdetailid |
| 2 | idx_qcp_inspoj_fseq |  | fseq |
| 3 | idx_qcp_inspoj_fentryid |  | fentryid |

---

## 序列号分录-子表 t_qcp_serialnumber

- **表名称：** 序列号分录-子表
- **表名：** t_qcp_serialnumber

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcheckhandtypedefalut | 检验处理方式合格(隐藏，用于业务规则合格时赋值) | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 2 | frowindex | 行号索引 | int4 | 32 |  | √ | 0 | 行号索引 |
| 3 | fisspotcheck | 是否抽检 | bpchar | 1 |  | √ | '0' | 是否抽检 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcheckhandtypeunqualiqty | 检验处理方式不合格(隐藏，用于业务规则合格时赋值) | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fsnnumber | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
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
| 1 | pk_qcp_serialnumber |  | fdetailid |
| 2 | idx_qcbd_serialnumber |  | fsnnumber |
| 3 | idx_qcp_serial_eidsno |  | fentryid,fsnnumber |

---

## 不良处理信息-子表 t_qcp_inspsubbaddeal

- **表名称：** 不良处理信息-子表
- **表名：** t_qcp_inspsubbaddeal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fresponorg | 责任组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fbaddealauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fbaddealmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fresponuser | 责任人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | frowindexrelationsn | 行号索引关联序列号行号索引 | int4 | 32 |  | √ | 0 | 行号索引关联序列号行号索引 |
| 6 | fdiscountamount | 折让金额 | numeric | 23 | 10 | √ | 0 | 折让金额 |
| 7 | fsecondbaseqty | 二次检验关联基本数量 | numeric | 23 | 10 | √ | 0 | 二次检验关联基本数量 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fenablemrb | MRB评审 | bpchar | 1 |  | √ | '0' | MRB评审 |
| 10 | fbaddealcomment | 备注 | varchar | 50 |  | √ | '' | 备注 |
| 11 | fdisprocureorgfield | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fdissettlementorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbaddeallotnumber | 批号 | varchar | 50 |  | √ | '' | 批号 |
| 14 | fbaddealunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fbaddealchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 16 | funqualitype | 不良品问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 17 | fbaddealsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 18 | fbaddealchkobjentryid | 检验对象行ID | int8 | 64 |  | √ | 0 | 检验对象行ID |
| 19 | fisdiscount | 是否折让 | bpchar | 1 |  | √ | '0' | 是否折让 |
| 20 | fbaddealmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 21 | fapplystatus | 申请状态 | varchar | 1 |  | √ | ' ' | 申请状态,枚举: 0 :未开始 1 :进行中 2 :已完成 |
| 22 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 23 | fsecondqty | 二次检验关联数量 | numeric | 23 | 10 | √ | 0 | 二次检验关联数量 |
| 24 | fbaddealbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 25 | fmrbbillid | MRB评审单内码 | int8 | 64 |  | √ | 0 | MRB评审单内码 |
| 26 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 27 | funqualireason | 不良原因 | varchar | 255 |  | √ | '' | 不良原因 |
| 28 | fdiscountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | funqualitime | 发现日期 | timestamp | 0 |  |  | null | 发现日期 |
| 30 | fjoinbaddealbaseqty | 基本单位关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位关联数量 |
| 31 | fmrbqty | MRB关联基本数量 | numeric | 23 | 10 |  | null | MRB关联基本数量 |
| 32 | fbadhandmode | 处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 33 | fjoinbaddealqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 34 | fyieldrecapply | 让步接收申请 | bpchar | 1 |  | √ | '0' | 让步接收申请 |
| 35 | fmrbstatus | MRB评审状态 | bpchar | 1 |  |  | null | MRB评审状态,枚举: A :进行中 B :已完成 |
| 36 | frespondepart | 责任部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | fbaddealqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 38 | fbaddealbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 39 | fbaddealsnnumber | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_inspsubbaddeal |  | fdetailid |
| 2 | idx_qcp_inspsubbaddeal_fk |  | fentryid |

---

## 关联子实体-子表 t_qcp_inspecbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_inspecbill_lk

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
| 1 | idx_qcp_inspecbill_lk_fk |  | fid |
| 2 | t_qcp_inspecbill_lk_pkey |  | fpkid |

---

## 检验结果_样本-子表 t_qcp_inspsubressamp

- **表名称：** 检验结果_样本-子表
- **表名：** t_qcp_inspsubressamp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 2 | fsampleres | 样本检验结果 | varchar | 5 |  | √ | ' ' | 样本检验结果,枚举: Y :合格 N :不合格 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fsamplenum | 样本编号 | varchar | 50 |  | √ | ' ' | 样本编号 |
| 5 | fsampckval | 实测值（数量） | numeric | 23 | 10 | √ | 0 | 实测值（数量） |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fsamplenumid | 样本编号ID | int8 | 64 |  | √ | 0 | 样本编号ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_inspmp_fseq |  | fseq |
| 2 | idx_qcp_inspmp_fentryid |  | fentryid |
| 3 | pk_qcp_inspsubressamp |  | fdetailid |

---

## 来料检验单-关联追踪表 t_qcp_inspecbill_tc

- **表名称：** 来料检验单-关联追踪表
- **表名：** t_qcp_inspecbill_tc

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
| 1 | t_qcp_inspecbill_tc_pkey |  | fid |
| 2 | idx_qcp_inspecbill_tc_tbill |  | ftbillid |
| 3 | idx_qcp_inspecbill_tc_tid |  | ftid |

---

## 来料检验单-多语言表 t_qcp_inspbill_l

- **表名称：** 来料检验单-多语言表
- **表名：** t_qcp_inspbill_l

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
| 1 | idx_qcp_insplll_fcomment |  | fcomment |
| 2 | pk_qcp_inspbill_l |  | fpkid |
| 3 | idx_qcp_insplll_fid |  | fid,flocaleid |

---

## 缺陷记录-多语言表 t_qcp_inspctdef_l

- **表名称：** 缺陷记录-多语言表
- **表名：** t_qcp_inspctdef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |
| 4 | fdefectremark | 缺陷记录备注 | varchar | 2000 |  | √ | ' ' | 缺陷记录备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_inspctdef_l |  | fpkid |

---

## 物料信息-子表 t_qcp_inspentry

- **表名称：** 物料信息-子表
- **表名：** t_qcp_inspentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyorg | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fconvertunqty | 换算不合格数量 | numeric | 23 | 10 | √ | 0 | 换算不合格数量 |
| 5 | fsrcsnnumberentryid | 来源序列号分录ID | int8 | 64 |  | √ | 0 | 来源序列号分录ID |
| 6 | fchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 7 | fsrcsnnumberbillid | 来源序列号单据ID | int8 | 64 |  | √ | 0 | 来源序列号单据ID |
| 8 | fformula | 公式 | varchar | 50 |  | √ | ' ' | 公式 |
| 9 | fmaterialqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | fre | 拒收数 | int8 | 64 |  | √ | 0 | 拒收数 |
| 11 | fordertype | 核心单据类型（废弃） | varchar | 50 |  | √ | ' ' | 核心单据类型（废弃） |
| 12 | ftaskstatus | 任务状态 | varchar | 10 |  | √ | ' ' | 任务状态,枚举: 0 :进行中 1 :已完成 2 :未开始 3 :已关闭 |
| 13 | fwbbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 14 | fsourcebillno | 来源单据编号 | varchar | 500 |  | √ | ' ' | 来源单据编号 |
| 15 | fwbbillentryid | 核心单据分录ID | varchar | 50 |  | √ | ' ' | 核心单据分录ID |
| 16 | funqualifiedqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 17 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 18 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 21 | finspectproid | 检验方案 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 22 | fwbbillentityentity | 核心单据单据体实体 | varchar | 50 |  | √ | ' ' | 核心单据单据体实体 |
| 23 | fsubcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fshowtype | 展示方式（隐藏） | varchar | 5 |  | √ | ' ' | 展示方式（隐藏）,枚举: 1 :按样本 0 :按检验项目 |
| 26 | fbasesampuqlyqty | 基本单位样本不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本不合格数 |
| 27 | fbasejoinqty | 基本单位关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位关联数量 |
| 28 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 29 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 30 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 31 | fwbbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 32 | fmanudate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 33 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 35 | fvaluerecqty | 样本记录数量 | int4 | 32 |  | √ | 0 | 样本记录数量 |
| 36 | fresultstatus | 结果状态 | varchar | 10 |  | √ | ' ' | 结果状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 |
| 37 | fsuspiciousstatus | 可疑件状态 | varchar | 5 |  | √ | ' ' | 可疑件状态,枚举: A :可疑件 B :非可疑件 |
| 38 | fwbbillentryseq | 核心单据分录序号 | varchar | 50 |  | √ | ' ' | 核心单据分录序号 |
| 39 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 40 | fduedate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 41 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 42 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 43 | fsettlorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | frinsqty | 样本数量 | numeric | 23 | 10 | √ | 0 | 样本数量 |
| 45 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | [移动质检任务单 qcmp_taskinfo](../qcbd_files/qcmp_taskinfo.md) |
| 46 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 47 | facceptno | 验收编号 | varchar | 30 |  | √ | ' ' | 验收编号 |
| 48 | fsamplingsizeqty | 样本量 | numeric | 23 | 10 | √ | 0 | 样本量 |
| 49 | fchkobjentryid | 检验对象行ID | int8 | 64 |  | √ | 0 | 检验对象行ID |
| 50 | finspectionlot | 检验批次 | varchar | 50 |  | √ | ' ' | 检验批次 |
| 51 | finspfirstentrykey | 首次检验分录唯一标识 | varchar | 50 |  | √ | ' ' | 首次检验分录唯一标识 |
| 52 | fwsstageid | 宽严度检验阶段 | int8 | 64 |  | √ | 0 | [宽严度阶段 qcbd_widstrict_stage](../qcbd_files/qcbd_widstrict_stage.md) |
| 53 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 54 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 55 | fbasequaliqty | 基本单位合格数 | numeric | 23 | 10 | √ | 0 | 基本单位合格数 |
| 56 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 57 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 58 | finsdepartment | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 59 | fsampingunqualqty | 样本不合格数 | numeric | 23 | 10 | √ | 0 | 样本不合格数 |
| 60 | fsourcebilltype | 来源单据类型（已废弃） | varchar | 50 |  | √ | ' ' | 来源单据类型（已废弃） |
| 61 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 62 | fheadbillno | fheadbillno | varchar | 80 |  | √ | ' ' |  |
| 63 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 64 | fsettlcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 65 | fsampingqualqty | 样本合格数 | numeric | 23 | 10 | √ | 0 | 样本合格数 |
| 66 | forderno | 核心单据编号（废弃） | varchar | 50 |  | √ | ' ' | 核心单据编号（废弃） |
| 67 | femergency | 是否加急 | varchar | 5 |  | √ | ' ' | 是否加急,枚举: A :是 B :否 |
| 68 | fwbbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 69 | fsampscheme | 抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 70 | facstr | 允收数 | varchar | 50 |  | √ | ' ' | 允收数 |
| 71 | fprocureorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 72 | finspectionstd | 检验标准 | int8 | 64 |  | √ | 0 | [检验标准 qcbd_inspectionstd](../qcbd_files/qcbd_inspectionstd.md) |
| 73 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 74 | fisexistsnnumber | 是否存在序列号 | bpchar | 1 |  | √ | '0' | 是否存在序列号 |
| 75 | fsupplieid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 76 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 77 | fsamppercentage | 抽样百分比% | numeric | 23 | 10 | √ | 0 | 抽样百分比% |
| 78 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 79 | fproposer | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 80 | fwsruleid | 宽严度转换方案 | int8 | 64 |  | √ | 0 | [宽严度转换方案 qcbd_widstrict_rule](../qcbd_files/qcbd_widstrict_rule.md) |
| 81 | fbaddealsnnumberbotp | 序列号(不良品处理单下推过来的) | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 82 | fdamagebear | 样本破坏承担方 | bpchar | 1 |  | √ | ' ' | 样本破坏承担方,枚举: A :供应商 B :我方 |
| 83 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 84 | fqualifiedqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 85 | fsuppliermasterid | 供应商(主数据内码) | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 86 | facceptid | 验收单据内码 | int8 | 64 |  | √ | 0 | 验收单据内码 |
| 87 | fbaddeal | 不良品处理 | varchar | 5 |  | √ | 'B' | 不良品处理,枚举: 0 :检验单 1 :不良品处理单 |
| 88 | fsubinspector | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 89 | fdamageqtybasic | 样本破坏数（基本） | numeric | 23 | 10 | √ | 0 | 样本破坏数（基本） |
| 90 | fconvertqty | 换算数量 | numeric | 23 | 10 | √ | 0 | 换算数量 |
| 91 | fbasesampqlyqty | 基本单位样本合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本合格数 |
| 92 | fqualinsporg | 质检组 | int8 | 64 |  | √ | 0 | [质检业务组 qcbd_qualityorg](../qcbd_files/qcbd_qualityorg.md) |
| 93 | fsrcunitid | 来源单单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 94 | fenterresult | 录入实测值 | bpchar | 1 |  | √ | '0' | 录入实测值 |
| 95 | fsupplydep | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 96 | fbaseunqlyqty | 基本单位不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位不合格数 |
| 97 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 98 | fdamageqty | 样本破坏数 | numeric | 23 | 10 | √ | 0 | 样本破坏数 |
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

## 检验明细-多语言表 t_qcp_inspsubresproj_l

- **表名称：** 检验明细-多语言表
- **表名：** t_qcp_inspsubresproj_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finspeccomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_inspsubresproj_l |  | fpkid |
| 2 | idx_qcp_inspojl_comment |  | finspeccomment |
| 3 | idx_qcp_inspojl_fdetailid |  | fdetailid,flocaleid |

---

## 样本检验结果_项目样本关系-子表 t_qcp_inspsubresrela

- **表名称：** 样本检验结果_项目样本关系-子表
- **表名：** t_qcp_inspsubresrela

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalratstr | 实测值(定量) | varchar | 50 |  | √ | ' ' | 实测值(定量) |
| 2 | fvaldeter | 实测值（定性） | varchar | 50 |  | √ | ' ' | 实测值（定性） |
| 3 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 4 | fsamp_seq | 按项目录入-样本实测值流水号 | int4 | 32 |  | √ | 0 | 按项目录入-样本实测值流水号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fprojuuid | 按项目分录唯一标识 | varchar | 50 |  | √ | ' ' | 按项目分录唯一标识 |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fjudge | 实测值判定结果 | varchar | 5 |  | √ | ' ' | 实测值判定结果,枚举: Y :合格 N :不合格 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fexmapleid | 样本编号ID | int8 | 64 |  | √ | 0 | 样本编号ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_inspsubresrela |  | fdetailid |
| 2 | idx_qcp_inspla_fentryid |  | fentryid |
| 3 | idx_qcp_inspla_fseq |  | fseq |

---

## 检验方案匹配维度-多选基础资料表 t_qcp_promatchdimo

- **表名称：** 检验方案匹配维度-多选基础资料表
- **表名：** t_qcp_promatchdimo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [检验方案匹配维度 qcbd_promatchdimo](../qcbd_files/qcbd_promatchdimo.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_promatchdimo_fpkid |  | fpkid |
| 2 | pk_qcp_promatchdimo |  | fpkid |

---

## 缺陷记录-子表 t_qcp_inspctdef

- **表名称：** 缺陷记录-子表
- **表名：** t_qcp_inspctdef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdefectdegree | 缺陷程度 | bpchar | 1 |  | √ | ' ' | 缺陷程度,枚举: A :轻度缺陷 B :严重缺陷 C :致命缺陷 |
| 2 | fdefecttype | 缺陷类型 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 3 | fdefectreason | 缺陷原因 | int8 | 64 |  | √ | 0 | [缺陷原因 qcbd_defectreason](../qcbd_files/qcbd_defectreason.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fdefectqty | 缺陷数量 | numeric | 23 | 10 | √ | 0 | 缺陷数量 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fdefectunit | 缺陷单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fdefectresult | 缺陷后果 | int8 | 64 |  | √ | 0 | [缺陷后果 qcbd_defectresult](../qcbd_files/qcbd_defectresult.md) |
| 10 | fdefectremark | 缺陷记录备注 | varchar | 2000 |  | √ | ' ' | 缺陷记录备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_inspctdef |  | fdetailid |

---

## 序列号-多选基础资料表 t_qcp_inspctdefsn

- **表名称：** 序列号-多选基础资料表
- **表名：** t_qcp_inspctdefsn

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [序列号主档 bd_snmainfile](../sbd_files/bd_snmainfile.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_inspctdefsn |  | fpkid |

---

## 关联子实体-子表 t_qcp_matintoentity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcp_matintoentity_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasequaliqty | 基本单位合格数_确认携带值 | numeric | 23 | 10 |  | null | 基本单位合格数_确认携带值 |
| 2 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fbasequaliqty_old | 基本单位合格数_原始携带值 | numeric | 23 | 10 |  | null | 基本单位合格数_原始携带值 |
| 8 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_matintoentity_lk_fk |  | fentryid |
| 2 | t_qcp_matintoentity_lk_pkey |  | fpkid |

---

## 样本检测-无检验项目时显示-多语言表 t_qcp_samplecheck_l

- **表名称：** 样本检测-无检验项目时显示-多语言表
- **表名：** t_qcp_samplecheck_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsccomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_scid_l |  | fpkid |

---

## 来料检验单-反写记录表 t_qcp_inspecbill_wb

- **表名称：** 来料检验单-反写记录表
- **表名：** t_qcp_inspecbill_wb

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
| 1 | t_qcp_inspecbill_wb_pkey |  | fentryid |
| 2 | idx_qcp_inspecbill_wb_fk |  | fid |

---

## 物料信息-多语言表 t_qcp_inspentry_l

- **表名称：** 物料信息-多语言表
- **表名：** t_qcp_inspentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsubcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_inspentry_l |  | fpkid |
| 2 | idx_qcp_inspryl_fsubcomment |  | fsubcomment |
| 3 | idx_qcp_inspryl_fentryid |  | fentryid,flocaleid |

---

## 物料信息-分表 t_qcp_inspentry_a

- **表名称：** 物料信息-分表
- **表名：** t_qcp_inspentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furgentqty | 紧急放行数量 | numeric | 23 | 10 | √ | 0 | 紧急放行数量 |
| 3 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 4 | furgentjoinbaseqty | 紧急放行关联基本数量 | numeric | 23 | 10 | √ | 0 | 紧急放行关联基本数量 |
| 5 | finspectstatus | 质检状态 | varchar | 30 |  | √ | 'INSPECTING' | 质检状态,枚举: INSPECTING :质检中 INSPECTED :质检完成 |
| 6 | furgentjoinqty | 紧急放行关联数量 | numeric | 23 | 10 | √ | 0 | 紧急放行关联数量 |
| 7 | furgentbaseqty | 紧急放行基本数量 | numeric | 23 | 10 | √ | 0 | 紧急放行基本数量 |
| 8 | fentryextf | 单据体扩展值 | varchar | 50 |  | √ | ' ' | 单据体扩展值,枚举: A :赠品 B :合并检验 |
| 9 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 10 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 11 | fexpectcompletedate | 期望完成日期 | timestamp | 0 |  |  | null | 期望完成日期 |
| 12 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 13 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 15 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 17 | fursaveunwrite | 紧急放行保存反写 | bpchar | 1 |  | √ | '0' | 紧急放行保存反写 |
| 18 | freturnnumber | 自动下推退料单编码 | varchar | 80 |  | √ | ' ' | 自动下推退料单编码 |
| 19 | finstocknumber | 自动下推入库单编码 | varchar | 80 |  | √ | ' ' | 自动下推入库单编码 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_qcp_inspentry_a |  | fentryid |
| 2 | index_qcp_inspectma_a |  | fid |

---

## 来料检验单-主表 t_qcp_inspbill

- **表名称：** 来料检验单-主表
- **表名：** t_qcp_inspbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fisyieldrecieve | 让步接收流程 | bpchar | 1 |  | √ | '0' | 让步接收流程 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | finspectorid | 质检员（弃用） | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fconfirmauxpty | 确认辅助属性 | int4 | 32 |  | √ | 0 | 确认辅助属性 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | finspestartdate | 检验开始日期 | timestamp | 0 |  |  | null | 检验开始日期 |
| 13 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fprintcount | 打印次数 | int4 | 32 |  | √ | 0 | 打印次数 |
| 16 | finspeenddate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 17 | fjoininspectflag | 启用联合检验 | bpchar | 1 |  | √ | '0' | 启用联合检验 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | finspedeptid | 质检部门（弃用） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qcp_inspll_fbillno |  | fbillno |
| 2 | idx_qcp_inspll_fcreatetime |  | fcreatetime |
| 3 | pk_qcp_inspbill |  | fid |

---

## 不良处理信息-多语言表 t_qcp_inspsubbaddeal_l

- **表名称：** 不良处理信息-多语言表
- **表名：** t_qcp_inspsubbaddeal_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 3 | fbaddealcomment | 备注 | varchar | 50 |  | √ | '' | 备注 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | '' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_inspsubbaddeal_l |  | fpkid |
| 2 | idx_qcp_inspsubbaddeal_l_0 |  | fdetailid,flocaleid |

---

## 样本检测-无检验项目时显示-子表 t_qcp_samplecheck

- **表名称：** 样本检测-无检验项目时显示-子表
- **表名：** t_qcp_samplecheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fscqty | 不合格样本数量 | numeric | 23 | 10 | √ | 0 | 不合格样本数量 |
| 2 | fsccomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fscbadreason | 不良原因 | varchar | 255 |  | √ | ' ' | 不良原因 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | fscbadtype | 不良问题分类 | int8 | 64 |  | √ | 0 | [不良品问题分类 qcbd_unquaproblem](../qcbd_files/qcbd_unquaproblem.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fscbaseqty | 不合格样本基本数量 | numeric | 23 | 10 | √ | 0 | 不合格样本基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcp_scid |  | fdetailid |
