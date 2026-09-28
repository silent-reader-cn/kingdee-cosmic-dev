# 滚动收货计划-ssm_require_schedule

## 单据体-子表 t_ssm_requiresc_detail

- **表名称：** 单据体-子表
- **表名：** t_ssm_requiresc_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybaseum | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | fprocureqty | 采购数量 | numeric | 23 | 10 | √ | 0 | 采购数量 |
| 4 | fstorageqty | 入库数量 | numeric | 23 | 10 | √ | 0 | 入库数量 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fasnqty | 收货通知数量 | numeric | 23 | 10 | √ | 0 | 收货通知数量 |
| 7 | fdemandforecast | 需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 8 | fdatetime | 日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 日期 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | finterval | 日期单位 | varchar | 8 |  | √ | ' ' | 日期单位,枚举: D :日 W :周 M :月 Q :季 Y :年 |
| 11 | faccumulateqty | 累计数量 | numeric | 23 | 10 | √ | 0 | 累计数量 |
| 12 | fasnbaseqty | 收货通知基本数量 | numeric | 23 | 10 | √ | 0 | 收货通知基本数量 |
| 13 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
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
| 1 | idx_t_ssm_requiresc_detail |  | fid,fentryid |
| 2 | pk_t_ssm_requiresc_detail |  | fentryid |

---

## 滚动收货计划-主表 t_ssm_requireschedule

- **表名称：** 滚动收货计划-主表
- **表名：** t_ssm_requireschedule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 3 | fbaseum | fbaseum | int8 | 64 |  | √ | 0 |  |
| 4 | flogid | 日志编号 | int8 | 64 |  | √ | 0 | 应用日志 ssm_log |
| 5 | fprocureorderid | 采购计划协议 | int8 | 64 |  | √ | 0 | 采购计划协议 ssm_purschdorder |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsupplier | 订货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | frelease | frelease | varchar | 50 |  | √ | ' ' |  |
| 10 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 11 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 12 | fsenddatetime | 发送时间 | timestamp | 0 |  |  | null | 发送时间 |
| 13 | fbillno | 发放号 | varchar | 30 |  | √ | ' ' | 发放号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | freleasestatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fpriorcumdate | 前期累计截止日 | timestamp | 0 |  |  | null | 前期累计截止日 |
| 20 | ffullfillsupplier | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fstartdatetime | 计划起始日 | timestamp | 0 |  |  | null | 计划起始日 |
| 22 | fsendstatus | 发送状态 | varchar | 50 |  | √ | ' ' | 发送状态,枚举: 0 :未发送 1 :已发送 |
| 23 | fprocureorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fpriorcumreq | 前期累计需求量 | numeric | 23 | 10 | √ | 0 | 前期累计需求量 |
| 27 | fum | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ssm_requireschedule |  | fprocureorderid,flineno,fid |
| 2 | pk_ssm_requireschedule |  | fid |
