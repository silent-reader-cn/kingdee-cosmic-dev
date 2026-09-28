# 供应商预测计划-ssm_plan_schedule

## 供应商预测计划-主表 t_ssm_planschedule

- **表名称：** 供应商预测计划-主表
- **表名：** t_ssm_planschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 3 | fbaseum | fbaseum | int8 | 64 |  | √ | 0 |  |
| 4 | fprocureorderid | 采购计划协议 | int8 | 64 |  | √ | 0 | 采购计划协议 ssm_purschdorder |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | frelease | frelease | varchar | 50 |  | √ | ' ' |  |
| 9 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 11 | fsenddatetime | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 12 | fbillno | 发放号 | varchar | 30 |  | √ | ' ' | 发放号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | freleasestatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fpriorcumdate | 前期累计截止日 | timestamp | 0 |  |  | null | 前期累计截止日 |
| 19 | ffullfillsupplier | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 20 | fstartdatetime | 计划起始日 | timestamp | 0 |  |  | null | 计划起始日 |
| 21 | fsendstatus | 发送状态 | varchar | 50 |  | √ | ' ' | 发送状态,枚举: 0 :未发送 1 :已发送 |
| 22 | fprocureorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fpriorcumreq | 前期累计需求量 | numeric | 23 | 10 | √ | 0 | 前期累计需求量 |
| 26 | fum | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ssm_planschedule |  | fprocureorderid,flineno,fid |
| 2 | pk_ssm_planschedule |  | fid |

---

## 单据体-子表 t_ssm_plansch_detail

- **表名称：** 单据体-子表
- **表名：** t_ssm_plansch_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybaseum | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fprocureqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 4 | fstorageqty | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fasnqty | 收货通知数量 | numeric | 23 | 10 | √ | 0 | 收货通知数量 |
| 7 | fdemandforecast | 需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 8 | fdatetime | 日期 | timestamp | 0 |  |  | null | 日期 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | finterval | 日期单位 | varchar | 50 |  | √ | ' ' | 日期单位,枚举: D :日 W :周 M :月 Q :季 Y :年 |
| 11 | faccumulateqty | 累计数量 | numeric | 23 | 10 | √ | 0 | 累计数量 |
| 12 | fasnbaseqty | 收货通知基本数量 | numeric | 23 | 10 | √ | 0 | 收货通知基本数量 |
| 13 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdate | fdate | timestamp | 0 |  |  | null |  |
| 15 | freference | 参考值 | varchar | 50 |  | √ | ' ' | 参考值 |
| 16 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 17 | fstoragebaseqty | 入库基本数量 | numeric | 23 | 10 | √ | 0 | 入库基本数量 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | flineclosestatus | 行关闭状态 | varchar | 10 |  | √ | 'A' | 行关闭状态,枚举: A :正常 B :已关闭 |
| 20 | fentryum | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ssm_plansch_detail |  | fid,fentryid |
| 2 | pk_t_ssm_plansch_detail |  | fentryid |
