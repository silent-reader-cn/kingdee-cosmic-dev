# 生产检验单-qcpp_manuinspec

## 样本检验结果_项目样本关系-子表 t_qcpp_inspsubresrela

- **表名称：** 样本检验结果_项目样本关系-子表
- **表名：** t_qcpp_inspsubresrela

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
| 1 | idx_qcpp_inspla_fseq |  | fseq |
| 2 | idx_qcpp_inspla_fentryid |  | fentryid |
| 3 | pk_qcpp_inspsubresrela |  | fdetailid |

---

## 不良处理信息-子表 t_qcpp_inspsubbaddeal

- **表名称：** 不良处理信息-子表
- **表名：** t_qcpp_inspsubbaddeal

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
| 27 | fbaddealproqyt | 不良品生产数量 | numeric | 23 | 10 | √ | 0 | 不良品生产数量 |
| 28 | funqualireason | 不良原因 | varchar | 255 |  | √ | '' | 不良原因 |
| 29 | fdiscountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 30 | funqualitime | 发现日期 | timestamp | 0 |  |  | null | 发现日期 |
| 31 | fbaddealprounit | 不良品生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | fjoinbaddealbaseqty | 基本单位关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位关联数量 |
| 33 | fmrbqty | MRB关联基本数量 | numeric | 23 | 10 |  | null | MRB关联基本数量 |
| 34 | fbadhandmode | 处理方式 | int8 | 64 |  | √ | 0 | [不良品处理方式 bd_badhandmode](../basedata_files/bd_badhandmode.md) |
| 35 | fjoinbaddealqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 36 | fyieldrecapply | 让步接收申请 | bpchar | 1 |  | √ | '0' | 让步接收申请 |
| 37 | fmrbstatus | MRB评审状态 | bpchar | 1 |  |  | null | MRB评审状态,枚举: A :进行中 B :已完成 |
| 38 | frespondepart | 责任部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fbaddealqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 40 | fbaddealbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 41 | fbaddealsnnumber | 序列号 | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcpp_inspsubbaddeal |  | fdetailid |
| 2 | idx_qcpp_inspsubbaddeal_fk |  | fentryid |

---

## 检验明细-子表 t_qcpp_inspsubresproj

- **表名称：** 检验明细-子表
- **表名：** t_qcpp_inspsubresproj

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
| 1 | idx_qcpp_inspoj_fseq |  | fseq |
| 2 | pk_qcpp_inspsubresproj |  | fdetailid |
| 3 | idx_qcpp_inspoj_fentryid |  | fentryid |

---

## 物料信息-子表 t_qcpp_inspentry

- **表名称：** 物料信息-子表
- **表名：** t_qcpp_inspentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplyorg | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fproductionworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconvertunqty | 换算不合格数量 | numeric | 23 | 10 | √ | 0 | 换算不合格数量 |
| 6 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 7 | fsrcsnnumberentryid | 来源序列号分录ID | int8 | 64 |  | √ | 0 | 来源序列号分录ID |
| 8 | fchkobjid | 检验对象ID | int8 | 64 |  | √ | 0 | 检验对象ID |
| 9 | fsrcsnnumberbillid | 来源序列号单据ID | int8 | 64 |  | √ | 0 | 来源序列号单据ID |
| 10 | fformula | 公式 | varchar | 50 |  | √ | ' ' | 公式 |
| 11 | fmaterialqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 12 | fre | 拒收数 | int8 | 64 |  | √ | 0 | 拒收数 |
| 13 | freporttype | 汇报类型 | varchar | 54 |  | √ | ' ' | 汇报类型,枚举: A :正常 B :返工 |
| 14 | ftaskstatus | 任务状态 | varchar | 10 |  | √ | ' ' | 任务状态,枚举: 0 :进行中 1 :已完成 2 :未开始 3 :已关闭 |
| 15 | fwbbillid | 核心单据ID | varchar | 50 |  | √ | ' ' | 核心单据ID |
| 16 | fsourcebillno | 来源单据编号 | varchar | 500 |  | √ | ' ' | 来源单据编号 |
| 17 | fwbbillentryid | 核心单据分录ID | varchar | 50 |  | √ | ' ' | 核心单据分录ID |
| 18 | funqualifiedqty | 不合格数 | numeric | 23 | 10 | √ | 0 | 不合格数 |
| 19 | foproperation | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 20 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fmversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 23 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 24 | finspectproid | 检验方案 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 25 | fwbbillentityentity | 核心单据单据体实体 | varchar | 50 |  | √ | ' ' | 核心单据单据体实体 |
| 26 | fproqyt | 生产数量 | numeric | 23 | 10 | √ | 0 | 生产数量 |
| 27 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 28 | fsubcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fshowtype | 展示方式（隐藏） | varchar | 5 |  | √ | ' ' | 展示方式（隐藏）,枚举: 1 :按样本 0 :按检验项目 |
| 31 | fprocessseq | 工序序列号 | varchar | 50 |  | √ | ' ' | 工序序列号 |
| 32 | fbasesampuqlyqty | 基本单位样本不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本不合格数 |
| 33 | fbasejoinqty | 基本单位关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位关联数量 |
| 34 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 35 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 36 | fexpiredate | 有效期至 | timestamp | 0 |  |  | null | 有效期至 |
| 37 | fjoinqty | 关联数量 | numeric | 23 | 10 | √ | 0 | 关联数量 |
| 38 | fwbbillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 39 | fmanudate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 40 | flocationorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 42 | fvaluerecqty | 样本记录数量 | int4 | 32 |  | √ | 0 | 样本记录数量 |
| 43 | freporderno | 汇报单编号 | varchar | 500 |  | √ | ' ' | 汇报单编号 |
| 44 | fresultstatus | 结果状态 | varchar | 10 |  | √ | ' ' | 结果状态,枚举: created :已创建 completed :已完成 executing :正在处理 received :已经接收准备处理 errored :异常 |
| 45 | fisfirstinsp | 首检 | bpchar | 1 |  | √ | ' ' | 首检 |
| 46 | fwbbillentryseq | 核心单据分录序号 | varchar | 50 |  | √ | ' ' | 核心单据分录序号 |
| 47 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 48 | fproducttype | 产品类型 | varchar | 54 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 49 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 50 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 51 | fscsystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 52 | fsettlorg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | frinsqty | 样本数量 | numeric | 23 | 10 | √ | 0 | 样本数量 |
| 54 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | [移动质检任务单 qcmp_taskinfo](../qcbd_files/qcmp_taskinfo.md) |
| 55 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 56 | fsamplingsizeqty | 样本量 | numeric | 23 | 10 | √ | 0 | 样本量 |
| 57 | fchkobjentryid | 检验对象行ID | int8 | 64 |  | √ | 0 | 检验对象行ID |
| 58 | finspectionlot | 检验批次 | varchar | 50 |  | √ | ' ' | 检验批次 |
| 59 | finspfirstentrykey | 首次检验分录唯一标识 | varchar | 50 |  | √ | ' ' | 首次检验分录唯一标识 |
| 60 | fwsstageid | 宽严度检验阶段 | int8 | 64 |  | √ | 0 | [宽严度阶段 qcbd_widstrict_stage](../qcbd_files/qcbd_widstrict_stage.md) |
| 61 | fsamplingresult | 质量判定 | varchar | 5 |  | √ | ' ' | 质量判定,枚举: B :接受 C :不接受 |
| 62 | fsrcbillentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 63 | fbasequaliqty | 基本单位合格数 | numeric | 23 | 10 | √ | 0 | 基本单位合格数 |
| 64 | fprocessdepartid | 加工部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 65 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 66 | fmanufactureorder | 核心单据编号（废弃） | varchar | 80 |  | √ | ' ' | 核心单据编号（废弃） |
| 67 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 68 | finsdepartment | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 69 | fsampingunqualqty | 样本不合格数 | numeric | 23 | 10 | √ | 0 | 样本不合格数 |
| 70 | fsourcebilltype | 来源单据类型（已废弃） | varchar | 50 |  | √ | ' ' | 来源单据类型（已废弃） |
| 71 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 72 | fheadbillno | fheadbillno | varchar | 80 |  | √ | ' ' |  |
| 73 | fmaterialcfg | 物料编码 | int8 | 64 |  | √ | 0 | [物料质检信息 bd_inspect_cfg](../sbd_files/bd_inspect_cfg.md) |
| 74 | fsettlcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 75 | fsampingqualqty | 样本合格数 | numeric | 23 | 10 | √ | 0 | 样本合格数 |
| 76 | femergency | 是否加急 | varchar | 5 |  | √ | ' ' | 是否加急,枚举: A :是 B :否 |
| 77 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 78 | fwbbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 79 | fqrouteid | 工艺路线编码 | int8 | 64 |  | √ | 0 | [质量工艺路线 qcbd_qmcroute](../qcbd_files/qcbd_qmcroute.md) |
| 80 | fsampscheme | 抽样方案 | int8 | 64 |  | √ | 0 | [抽样方案 qcbd_sampscheme](../qcbd_files/qcbd_sampscheme.md) |
| 81 | facstr | 允收数 | varchar | 50 |  | √ | ' ' | 允收数 |
| 82 | fprocureorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 83 | finspectionstd | 检验标准 | int8 | 64 |  | √ | 0 | [检验标准 qcbd_inspectionstd](../qcbd_files/qcbd_inspectionstd.md) |
| 84 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 85 | fisexistsnnumber | 是否存在序列号 | bpchar | 1 |  | √ | '0' | 是否存在序列号 |
| 86 | foprworkshop | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 87 | foperationno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 88 | fsecondck | 二次检验 | bpchar | 1 |  | √ | '0' | 二次检验 |
| 89 | fsamppercentage | 抽样百分比% | numeric | 23 | 10 | √ | 0 | 抽样百分比% |
| 90 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 91 | fprounit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 92 | fproposer | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 93 | fwsruleid | 宽严度转换方案 | int8 | 64 |  | √ | 0 | [宽严度转换方案 qcbd_widstrict_rule](../qcbd_files/qcbd_widstrict_rule.md) |
| 94 | fbaddealsnnumberbotp | 序列号(不良品处理单下推过来的) | int8 | 64 |  | √ | 0 | [序列号记录 qcbd_serialnumber](../qcbd_files/qcbd_serialnumber.md) |
| 95 | fdamagebear | 样本破坏承担方 | bpchar | 1 |  | √ | ' ' | 样本破坏承担方,枚举: A :供应商 B :我方 C :协作组织 |
| 96 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 97 | fqualifiedqty | 合格数 | numeric | 23 | 10 | √ | 0 | 合格数 |
| 98 | fbaddeal | 不良品处理 | varchar | 5 |  | √ | 'B' | 不良品处理,枚举: 0 :检验单 1 :不良品处理单 |
| 99 | fsubinspector | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 100 | fdamageqtybasic | 样本破坏数（基本） | numeric | 23 | 10 | √ | 0 | 样本破坏数（基本） |
| 101 | fconvertqty | 换算数量 | numeric | 23 | 10 | √ | 0 | 换算数量 |
| 102 | fbasesampqlyqty | 基本单位样本合格数 | numeric | 23 | 10 | √ | 0 | 基本单位样本合格数 |
| 103 | fqualinsporg | 质检组 | int8 | 64 |  | √ | 0 | [质检业务组 qcbd_qualityorg](../qcbd_files/qcbd_qualityorg.md) |
| 104 | fsrcunitid | 来源单单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 105 | fenterresult | 录入实测值 | bpchar | 1 |  | √ | '0' | 录入实测值 |
| 106 | fsupplydep | 申请部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 107 | fbaseunqlyqty | 基本单位不合格数 | numeric | 23 | 10 | √ | 0 | 基本单位不合格数 |
| 108 | fmaterialcomid | 物料公共信息 | int8 | 64 |  | √ | 0 | [物料组织公共信息 bd_materialcommon](../basedata_files/bd_materialcommon.md) |
| 109 | fdamageqty | 样本破坏数 | numeric | 23 | 10 | √ | 0 | 样本破坏数 |
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

## 缺陷记录-子表 t_qcpp_inspctdef

- **表名称：** 缺陷记录-子表
- **表名：** t_qcpp_inspctdef

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
| 1 | pk_t_qcpp_inspctdef |  | fdetailid |

---

## 关联子实体-子表 t_qcpp_inspentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcpp_inspentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialqty_old | 数量_原始携带值 | numeric | 23 | 10 | √ | 0 | 数量_原始携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fmaterialqty | 数量_确认携带值 | numeric | 23 | 10 | √ | 0 | 数量_确认携带值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcpp_inspentry_lk |  | fpkid |
| 2 | idx_qcpp_inspentry_lk_fk |  | fentryid |

---

## 检验结果_样本-子表 t_qcpp_inspsubressamp

- **表名称：** 检验结果_样本-子表
- **表名：** t_qcpp_inspsubressamp

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
| 1 | idx_qcpp_inspmp_fentryid |  | fentryid |
| 2 | pk_qcpp_inspsubressamp |  | fdetailid |
| 3 | idx_qcpp_inspmp_fseq |  | fseq |

---

## 样本检测-无检验项目时显示-子表 t_qcpp_samplecheck

- **表名称：** 样本检测-无检验项目时显示-子表
- **表名：** t_qcpp_samplecheck

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
| 1 | pk_qcpp_scid |  | fdetailid |

---

## 样本检测-无检验项目时显示-多语言表 t_qcpp_samplecheck_l

- **表名称：** 样本检测-无检验项目时显示-多语言表
- **表名：** t_qcpp_samplecheck_l

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
| 1 | pk_qcpp_scid_l |  | fpkid |

---

## 生产检验单-关联追踪表 t_qcpp_inspecbill_tc

- **表名称：** 生产检验单-关联追踪表
- **表名：** t_qcpp_inspecbill_tc

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
| 1 | pk_qcpp_inspecbill_tc |  | fid |
| 2 | idx_qcpp_inspecbill_tc_tbill |  | ftbillid |
| 3 | idx_qcpp_inspecbill_tc_tid |  | ftid |

---

## 序列号分录-子表 t_qcpp_serialnumber

- **表名称：** 序列号分录-子表
- **表名：** t_qcpp_serialnumber

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
| 1 | idx_qcpp_serial_sno |  | fsnnumber |
| 2 | pk_qcpp_serialnumber |  | fdetailid |
| 3 | idx_qcpp_serial_eidsno |  | fentryid,fsnnumber |

---

## 生产检验单-多语言表 t_qcpp_inspbill_l

- **表名称：** 生产检验单-多语言表
- **表名：** t_qcpp_inspbill_l

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
| 1 | idx_qcpp_inspbill_fcomment |  | fcomment |
| 2 | idx_qcpp_inspbill_fid |  | fid,flocaleid |
| 3 | pk_qcpp_inspbill_l |  | fpkid |

---

## 检验方案匹配维度-多选基础资料表 t_qcpp_promatchdimo

- **表名称：** 检验方案匹配维度-多选基础资料表
- **表名：** t_qcpp_promatchdimo

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
| 1 | pk_qcpp_promatchdimo |  | fpkid |
| 2 | idx_qcpp_promatchdimo_fpkid |  | fpkid |

---

## 关联子实体-子表 t_qcpp_inspbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcpp_inspbill_lk

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
| 1 | idx_qcpp_inspbill_lk_fk |  | fid |
| 2 | pk_qcpp_inspbill_lk |  | fpkid |

---

## 不良处理信息-多语言表 t_qcpp_inspsubbaddeal_l

- **表名称：** 不良处理信息-多语言表
- **表名：** t_qcpp_inspsubbaddeal_l

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
| 1 | idx_qcpp_inspsubbaddeal_l_0 |  | fdetailid,flocaleid |
| 2 | pk_qcpp_inspsubbaddeal_l |  | fpkid |

---

## 生产检验单-反写记录表 t_qcpp_inspecbill_wb

- **表名称：** 生产检验单-反写记录表
- **表名：** t_qcpp_inspecbill_wb

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
| 1 | idx_qcpp_inspecbill_wb_fk |  | fid |
| 2 | pk_qcpp_inspecbill_wb |  | fentryid |

---

## 检验明细-多语言表 t_qcpp_inspsubresproj_l

- **表名称：** 检验明细-多语言表
- **表名：** t_qcpp_inspsubresproj_l

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
| 1 | idx_qcpp_inspojl_comment |  | finspeccomment |
| 2 | idx_qcpp_inspojl_fdetailid |  | fdetailid,flocaleid |
| 3 | pk_qcpp_inspsubresproj_l |  | fpkid |

---

## 缺陷记录-多语言表 t_qcpp_inspctdef_l

- **表名称：** 缺陷记录-多语言表
- **表名：** t_qcpp_inspctdef_l

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
| 1 | pk_t_qcpp_inspctdef_l |  | fpkid |

---

## 物料信息-多语言表 t_qcpp_inspentry_l

- **表名称：** 物料信息-多语言表
- **表名：** t_qcpp_inspentry_l

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
| 1 | idx_qcpp_inspryl_fsubcomment |  | fsubcomment |
| 2 | idx_qcpp_inspryl_fentryid |  | fentryid,flocaleid |
| 3 | pk_qcpp_inspentry_l |  | fpkid |

---

## 物料信息-分表 t_qcpp_inspentry_a

- **表名称：** 物料信息-分表
- **表名：** t_qcpp_inspentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | furgentqty | 紧急放行数量 | numeric | 23 | 10 | √ | 0 | 紧急放行数量 |
| 3 | furgentjoinbaseqty | 紧急放行关联基本数量 | numeric | 23 | 10 | √ | 0 | 紧急放行关联基本数量 |
| 4 | finspectstatus | 质检状态 | varchar | 30 |  | √ | 'INSPECTING' | 质检状态,枚举: INSPECTING :质检中 INSPECTED :质检完成 |
| 5 | furgentjoinqty | 紧急放行关联数量 | numeric | 23 | 10 | √ | 0 | 紧急放行关联数量 |
| 6 | furgentbaseqty | 紧急放行基本数量 | numeric | 23 | 10 | √ | 0 | 紧急放行基本数量 |
| 7 | fentryextf | 单据体扩展值 | varchar | 50 |  | √ | ' ' | 单据体扩展值,枚举: A :赠品 B :合并检验 |
| 8 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 9 | furgentrelease | 紧急放行 | bpchar | 1 |  | √ | '0' | 紧急放行 |
| 10 | fexpectcompletedate | 期望完成日期 | timestamp | 0 |  |  | null | 期望完成日期 |
| 11 | fassqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 12 | fassunit2id | 辅助单位(2) | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fassunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 15 | fassqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 16 | fursaveunwrite | 紧急放行保存反写 | bpchar | 1 |  | √ | '0' | 紧急放行保存反写 |
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

---

## 序列号-多选基础资料表 t_qcpp_inspctdefsn

- **表名称：** 序列号-多选基础资料表
- **表名：** t_qcpp_inspctdefsn

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
| 1 | pk_t_qcpp_inspctdefsn |  | fpkid |

---

## 生产检验单-主表 t_qcpp_inspbill

- **表名称：** 生产检验单-主表
- **表名：** t_qcpp_inspbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcomment | 备注 | varchar | 512 |  | √ | '' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fisyieldrecieve | 让步接收流程 | bpchar | 1 |  | √ | '0' | 让步接收流程 |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | finspectorid | 质检员（弃用） | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fconfirmauxpty | 确认辅助属性 | int4 | 32 |  | √ | 0 | 确认辅助属性 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | finspestartdate | 检验开始日期 | timestamp | 0 |  |  | null | 检验开始日期 |
| 13 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 14 | fprocessorg | 加工组织（用于过滤委托质检） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fprintcount | 打印次数 | int4 | 32 |  | √ | 0 | 打印次数 |
| 17 | finspeenddate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 18 | fjoininspectflag | 启用联合检验 | bpchar | 1 |  | √ | '0' | 启用联合检验 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | finspedeptid | 质检部门（弃用） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_qcpp_inspbill |  | fid |
| 2 | idx_qcpp_inspbill_fbillno |  | fbillno |
| 3 | idx_qcpp_inspbill_fcreatetime |  | fcreatetime |
