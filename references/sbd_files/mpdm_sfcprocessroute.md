# 工艺路线-mpdm_sfcprocessroute

## 工序-子表 t_bd_processentry

- **表名称：** 工序-子表
- **表名：** t_bd_processentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | 【工序信息】页签的序列号 | int8 | 64 |  | √ | 0 | 【工序信息】页签的序列号 |
| 3 | freworksection | 【工序信息】返工工序段 | varchar | 1000 |  | √ | ' ' | 【工序信息】返工工序段 |
| 4 | frelationid | 工序分录唯一ID，用于与计划信息、活动后台表关联的ID | int8 | 64 |  | √ | 0 | 工序分录唯一ID，用于与计划信息、活动后台表关联的ID |
| 5 | fislastprocess | 末序 | bpchar | 1 |  | √ | '0' | 末序 |
| 6 | fprocesscontrolcode | 【工序信息】页签的工序控制码 | int8 | 64 |  | √ | 0 | 工序控制码 mpdm_processcontrolcode |
| 7 | fsequencetype | 【工序信息】序列类型 | bpchar | 1 |  | √ | ' ' | 【工序信息】序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 8 | fupprocessid | 上工序id | varchar | 1000 |  | √ | ' ' | 上工序id |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fgroupnumber | fgroupnumber | int8 | 64 |  | √ | 0 |  |
| 11 | fheadunitfield | 【计划信息】页签的生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 12 | fprocessinstructions | 【工序信息】页签的工序说明 | varchar | 512 |  |  | ' ' | 【工序信息】页签的工序说明 |
| 13 | fupprocesstype | 上工序类型 | varchar | 30 |  |  | ' ' | 上工序类型,枚举: A :单个 B :多个 C :群组 |
| 14 | fisfirstprocess | 首序 | bpchar | 1 |  | √ | '0' | 首序 |
| 15 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序 mpdm_normprocess |
| 16 | fprocessqtyfield | 【计划信息】页签的工序数量 | numeric | 23 | 10 |  | null | 【计划信息】页签的工序数量 |
| 17 | fprocessdepartid | 【工序信息】页签的加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fprocessnumber | 【工序信息】页签的工序号 | int8 | 64 |  | √ | 0 | 【工序信息】页签的工序号 |
| 19 | fprocessunitfield | 【计划信息】页签的工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fbaseqtyfield | 【计划信息】页签的基本批量 | numeric | 23 | 10 |  | null | 【计划信息】页签的基本批量 |
| 21 | fnextprocessid | 下工序id | varchar | 1000 |  | √ | ' ' | 下工序id |
| 22 | fprocessorg | 【工序信息】页签的加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | freworksequence | 【工序信息】返工来源序列 | int8 | 64 |  | √ | 0 | 【工序信息】返工来源序列 |
| 24 | fismilestone | 里程碑 | bpchar | 1 |  | √ | '0' | 里程碑 |
| 25 | freportdownlimit | 汇报下限允差（%） | numeric | 23 | 10 |  | null | 汇报下限允差（%） |
| 26 | fismainprocess | 主工序 | bpchar | 1 |  | √ | '1' | 主工序 |
| 27 | fpromethod | 加工类型 | varchar | 10 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fprocesscenter | 【工序信息】页签的工作中心 | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 30 | freportupperlimit | 汇报上限允差（%） | numeric | 23 | 10 |  | null | 汇报上限允差（%） |
| 31 | fgrouptype | fgrouptype | varchar | 30 |  | √ | ' ' |  |
| 32 | freworkprocesses | 【工序信息】返工来源工序 | int8 | 64 |  | √ | 0 | 【工序信息】返工来源工序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processentry |  | fentryid |

---

## 子单据体-子表 t_bd_subprocessactive

- **表名称：** 子单据体-子表
- **表名：** t_bd_subprocessactive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | factivity | 活动名称 | varchar | 30 |  | √ | ' ' | 活动名称,枚举: A :准备活动 B :加工活动 C :其他活动一 D :其他活动二 |
| 2 | factunitid | 活动单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | 资源 mpdm_resourceinfo |
| 4 | factivityreport | 汇报活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 5 | fpformulaid | 计划活动量公式 | int8 | 64 |  | √ | 0 | 活动公式 mpdm_activityformula |
| 6 | factivitytype | 活动类型 | varchar | 30 |  | √ | ' ' | 活动类型,枚举: 0 :机器 1 :人工 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdefaultqty | 基本数量 | numeric | 23 | 10 |  | null | 基本数量 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | factivityexpress | 活动汇报量公式 | varchar | 30 |  | √ | ' ' | 活动汇报量公式,枚举: A :准备活动 B :加工活动*CEIL(工序汇报.合格数量/工序计划.基本批量) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_subprocessactive |  | fdetailid |

---

## 工艺路线-多语言表 t_bd_processroute_l

- **表名称：** 工艺路线-多语言表
- **表名：** t_bd_processroute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工艺路线名称 | varchar | 255 |  |  | ' ' | 工艺路线名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processroutel |  | fpkid |

---

## 工艺路线-使用范围表 t_bd_processroute_u

- **表名称：** 工艺路线-使用范围表
- **表名：** t_bd_processroute_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_processroute_u_uo |  | fuseorgid |
| 2 | pk_t_bd_processroute_u |  | fdataid,fuseorgid |

---

## 工艺路线-主表 t_bd_processroute

- **表名称：** 工艺路线-主表
- **表名：** t_bd_processroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprocesscentershow | fprocesscentershow | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmaterielfield | 物料主数据（暂时隐藏） | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fprocessinstructionsshow | fprocessinstructionsshow | varchar | 512 |  |  | ' ' |  |
| 7 | fworkshop | 车间(隐藏) | int8 | 64 |  | √ | 0 | 车间设置 mpdm_workshopsetup |
| 8 | fbatchendqtyfield | 批量至 | numeric | 23 | 10 |  | null | 批量至 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fbaseqtyfieldshow | 基本批量 | numeric | 23 | 10 |  | null | 基本批量 |
| 12 | fbatchstartqtyfield | 批量从 | numeric | 23 | 10 |  | null | 批量从 |
| 13 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 16 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fflexfield | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 22 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 24 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 25 | fprocessunitfieldshow | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 26 | fprocessorgshow | fprocessorgshow | int8 | 64 |  | √ | 0 |  |
| 27 | fheadunitfieldshow | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 28 | fprocesscontrolcodeshow | fprocesscontrolcodeshow | int8 | 64 |  | √ | 0 |  |
| 29 | fprojnoid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 30 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 31 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 32 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 34 | fmaterialver | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 35 | fonebaseqty | 表头数量（隐藏） | numeric | 23 | 10 | √ | 1 | 表头数量（隐藏） |
| 36 | funitfield | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 37 | ferpmaterielfield | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 38 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 39 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 40 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 42 | fprocessnumbershow | fprocessnumbershow | int8 | 64 |  | √ | 0 |  |
| 43 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 44 | fismain | 默认工艺路线 | bpchar | 1 |  | √ | '1' | 默认工艺路线 |
| 45 | fnumber | 工艺路线编码 | varchar | 100 |  | √ | ' ' | 工艺路线编码 |
| 46 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 47 | fcombofield | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: A :物料 B :物料组 C :通用工艺 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processroute |  | fid |
| 2 | idx_t_bd_processroute_master |  | fmasterid |
| 3 | idx_t_bd_processroute_createorg |  | fcreateorgid |

---

## 上工序-多选基础资料表 t_bd_upprocessentry

- **表名称：** 上工序-多选基础资料表
- **表名：** t_bd_upprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工序信息F7 mpdm_routeprocess |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_upprocessentry |  | fpkid |

---

## 工序-分表 t_bd_processentry_a

- **表名称：** 工序-分表
- **表名：** t_bd_processentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproinspect | 【检验信息】工序质检 | bpchar | 1 |  | √ | '0' | 【检验信息】工序质检 |
| 3 | fpurchasegroupid | 【委外信息】采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 4 | foutsourcepriceandtax | 【委外信息】委外含税单价 | numeric | 23 | 10 | √ | 0 | 【委外信息】委外含税单价 |
| 5 | fworkwasteprice | 【委外信息】工废单价 | numeric | 23 | 10 | √ | 0 | 【委外信息】工废单价 |
| 6 | fprounitfactor | 【计划信息】页签工序单位换算系数 | int4 | 32 |  | √ | 0 | 【计划信息】页签工序单位换算系数 |
| 7 | fchargeunitid | 【委外信息】计价单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fpurchaseorgid | 【委外信息】采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsupplierid | 【委外信息】供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fheadunitfactor | 【计划信息】页签生产单位换算系数 | int4 | 32 |  | √ | 0 | 【计划信息】页签生产单位换算系数 |
| 11 | funitprice | funitprice | numeric | 23 | 10 | √ | 0 |  |
| 12 | fscrapwasteprice | 【委外信息】料废单价 | numeric | 23 | 10 | √ | 0 | 【委外信息】料废单价 |
| 13 | finspectuserid | 【检验信息】质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | finspectplan | 【检验信息】检验方案(废弃) | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 15 | fworkwastepriceandtax | 【委外信息】工废含税单价 | numeric | 23 | 10 | √ | 0 | 【委外信息】工废含税单价 |
| 16 | ftaxrateid | 【委外信息】税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 17 | finspectdepid | 【检验信息】质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fscrapwastepriceandtax | 【委外信息】料废含税单价 | numeric | 23 | 10 | √ | 0 | 【委外信息】料废含税单价 |
| 19 | finspectorg | 【检验信息】质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | foutsourceprice | 【委外信息】委外单价 | numeric | 23 | 10 | √ | 0 | 【委外信息】委外单价 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | fcurrencyid | 【委外信息】币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processentry_a |  | fentryid |
| 2 | t_bd_processentry_a_id |  | fid |

---

## 下工序-多选基础资料表 t_bd_nextprocessentry

- **表名称：** 下工序-多选基础资料表
- **表名：** t_bd_nextprocessentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工序信息F7 mpdm_routeprocess |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_nextprocessentry |  | fpkid |

---

## 工序-多语言表 t_bd_processentry_l

- **表名称：** 工序-多语言表
- **表名：** t_bd_processentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessinstructions | 【工序信息】页签的工序说明 | varchar | 512 |  |  | ' ' | 【工序信息】页签的工序说明 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_processentryl |  | fpkid |
