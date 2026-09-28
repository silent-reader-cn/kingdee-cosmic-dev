# 采购计划编制-ssm_masterschedule

## 采购协议列表-子表 t_ssm_masterschdinfo

- **表名称：** 采购协议列表-子表
- **表名：** t_ssm_masterschdinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupplier | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 3 | ffullfillsupplier | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 4 | ffakeorderlist | 采购计划协议 | int8 | 64 |  | √ | 0 | 采购计划协议 ssm_purschdorder |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_masterschdinfo |  | fentryid |
| 2 | idx_ssm_masterschdinfo_fk |  | fid |

---

## 采购计划编制-主表 t_ssm_masterschedule

- **表名称：** 采购计划编制-主表
- **表名：** t_ssm_masterschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhidenonworkday | 仅显示有计划日 | bpchar | 1 |  | √ | '0' | 仅显示有计划日 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fasofdate | asofdate | timestamp | 0 |  |  | null | asofdate |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_masterschedule |  | fid |
| 2 | idx_ssm_masterschedule_m0 |  | fbillno |

---

## -子表 t_ssm_masterschddetail

- **表名称：** -子表
- **表名：** t_ssm_masterschddetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplanqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 2 | fstorageqty | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 3 | fasnqty | 收货通知数量 | numeric | 23 | 10 | √ | 0 | 收货通知数量 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpurplanid | 计划id | varchar | 50 |  | √ | ' ' | 计划id |
| 6 | fdemandforecast | 需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 7 | fdatetime | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 8 | fdatefield | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fplanrowindex | 计划行序列 | int8 | 64 |  | √ | 0 | 计划行序列 |
| 10 | fasnbaseqty | 收货通知基本数量 | numeric | 23 | 10 | √ | 0 | 收货通知基本数量 |
| 11 | fpurlineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 12 | fdateunit | 日期单位 | varchar | 50 |  | √ | ' ' | 日期单位 |
| 13 | fbaseunitmeasure | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fplantype | 计划类型 | varchar | 50 |  | √ | ' ' | 计划类型 |
| 15 | fstoragebaseqty | 入库基本数量 | numeric | 23 | 10 | √ | 0 | 入库基本数量 |
| 16 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 17 | freference | 参考值 | varchar | 50 |  | √ | ' ' | 参考值 |
| 18 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 20 | fpurunitmeasure | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssm_masterschddetail_fk |  | fentryid |
| 2 | pk_ssm_masterschddetail |  | fdetailid |

---

## 树形子单据体-子表 t_ssm_masterschdtree

- **表名称：** 树形子单据体-子表
- **表名：** t_ssm_masterschdtree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fplandayv | 计划日数 | int8 | 64 |  | √ | 0 | 计划日数 |
| 2 | fpurlinenov | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | ffirmdaysv | 计划固定日数 | int8 | 64 |  | √ | 0 | 计划固定日数 |
| 4 | fsftyltdaysv | 安全日数 | int8 | 64 |  | √ | 0 | 安全日数 |
| 5 | fmaterialversionv | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fminorderqtyv | 单次起送量 | int8 | 64 |  | √ | 0 | 单次起送量 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbaseunitmeasurev | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | freleaseidv | 当前生效计划id | int8 | 64 |  | √ | 0 | 当前生效计划id |
| 10 | fmasmaterielv | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 11 | flogid | 日志编号 | int8 | 64 |  | √ | 0 | 应用日志 ssm_log |
| 12 | fsdpcodev | sdpcode | int8 | 64 |  | √ | 0 | [SDP代码 amccsa_sdpcode](../amccsa_files/amccsa_sdpcode.md) |
| 13 | fsdpedigroupv | EDI报文标准 | varchar | 50 |  | √ | ' ' | EDI报文标准,枚举: 0 :EDIFACT 1 :X12 2 :其他 |
| 14 | fpurorderlineidv | 协议行id | varchar | 50 |  | √ | ' ' | 协议行id |
| 15 | fdemandorgv | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fstdpackqtyv | 最小包装数 | int8 | 64 |  | √ | 0 | 最小包装数 |
| 17 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 18 | fintransitqty | 在途数量 | numeric | 23 | 10 | √ | 0 | 在途数量 |
| 19 | fsupplierv | 订货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 20 | freleasenoveff | 生效发放号 | varchar | 50 |  | √ | ' ' | 生效发放号 |
| 21 | freleasenov | 发放号 | varchar | 50 |  | √ | ' ' | 发放号 |
| 22 | fauxiliarypropertyv | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 23 | fpurorderidv | 协议id | varchar | 50 |  | √ | ' ' | 协议id |
| 24 | forgv | 收料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fplanmonthv | 计划月数 | int8 | 64 |  | √ | 0 | 计划月数 |
| 26 | fpurorgv | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fmaterialcodev | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 28 | flinestartdate | 行起始日期 | timestamp | 0 |  |  | null | 行起始日期 |
| 29 | fplantypev | 计划类型 | varchar | 50 |  | √ | ' ' | 计划类型,枚举: ssm_require_schedule :滚动收货 ssm_ship_schedule :供应商交货 ssm_plan_schedule :供应商预测 |
| 30 | fpurunitmeasurev | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fplanweekv | 计划周数 | int8 | 64 |  | √ | 0 | 计划周数 |
| 32 | ffullfillsupplierv | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 33 | flineenddate | 行截止日期 | timestamp | 0 |  |  | null | 行截止日期 |
| 34 | fpurplanidv | 当前计划id | varchar | 50 |  | √ | ' ' | 当前计划id |
| 35 | fplanstatusv | 计划编制状态 | varchar | 50 |  | √ | ' ' | 计划编制状态,枚举: A :新增 B :修改 C :暂存 D :已审核 |
| 36 | fstatusv | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 STAGING :暂存 |
| 37 | fparentdetailid | fparentdetailid | int8 | 64 |  | √ | 0 | pid |
| 38 | fsendstatus | 发送状态 | varchar | 50 |  | √ | ' ' | 发送状态,枚举: 0 :未发送 1 :已发送 |
| 39 | freceivedqtyv | 累计已入库数量 | numeric | 23 | 10 | √ | 0 | 累计已入库数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_masterschdtree |  | fdetailid |
| 2 | idx_ssm_masterschdtree_fk |  | fentryid |
