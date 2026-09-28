# 重复生产汇报平台-arm_report_workbanch

## 重复生产汇报平台-主表 t_arm_report_workbanch

- **表名称：** 重复生产汇报平台-主表
- **表名：** t_arm_report_workbanch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frealprodtime | 实际生产总工时 | numeric | 23 | 2 | √ | 0 | 实际生产总工时 |
| 3 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 4 | fmaterialid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fprdunqualifiedqty | 不合格品数量 | numeric | 23 | 10 | √ | 0 | 不合格品数量 |
| 6 | fbosusers | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fenddatetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fprdscrapqty | 报废品数量 | numeric | 23 | 10 | √ | 0 | 报废品数量 |
| 10 | flocation | 完工入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 11 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 12 | fpretimeunit | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 13 | forg | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fproductinvbillno | 重复生产完工入库单 | varchar | 50 |  | √ | ' ' | 重复生产完工入库单 |
| 15 | fbiztime | 业务日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 业务日期 |
| 16 | fisusestdtime | 使用标准准备工时 | bpchar | 1 |  | √ | '0' | 使用标准准备工时 |
| 17 | fdetail | 查看详情 | varchar | 50 |  | √ | ' ' | 查看详情 |
| 18 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbackflushid | 交互式倒冲ID | int8 | 64 |  | √ | 0 | 交互式倒冲ID |
| 21 | fqualifiedqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 22 | fscrapreason | 报废原因 | int8 | 64 |  | √ | 0 | 报废原因 arm_screason |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fpickoutbillno | 重复生产领料单 | varchar | 50 |  | √ | ' ' | 重复生产领料单 |
| 25 | fmanupreptime | 人工准备工时 | numeric | 23 | 2 | √ | 0 | 人工准备工时 |
| 26 | fmaterialno | 物料 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 27 | fscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 28 | fteamgroup | 班组 | int8 | 64 |  | √ | 0 | 班组 mpdm_classgroup |
| 29 | fprdqualifiedqty | 合格品数量 | numeric | 23 | 10 | √ | 0 | 合格品数量 |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fmachpreptime | 机器准备工时 | numeric | 23 | 2 | √ | 0 | 机器准备工时 |
| 32 | fwarehouse | 完工入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 33 | frealtimeunit | 时间单位 | varchar | 50 |  |  | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 34 | fprdunit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 35 | fmanurealtime | 人工实作工时 | numeric | 23 | 2 | √ | 0 | 人工实作工时 |
| 36 | freportstatus | freportstatus | bpchar | 1 |  | √ | ' ' |  |
| 37 | fuaiqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 38 | fstartdatetime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 39 | fworkhoursreportbillno | 工时汇报单 | varchar | 50 |  | √ | ' ' | 工时汇报单 |
| 40 | freworkqty | 返工数量 | numeric | 23 | 10 | √ | 0 | 返工数量 |
| 41 | fmachrealtime | 机器实作工时 | numeric | 23 | 2 | √ | 0 | 机器实作工时 |
| 42 | fbookdate | 记账日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 记账日期 |
| 43 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_report_wb |  | fmaterialno,fmaterialversion,fauxpty |
| 2 | pk_t_arm_report_workbanch |  | fid |

---

## 单据体-子表 t_arm_scrapreportentry

- **表名称：** 单据体-子表
- **表名：** t_arm_scrapreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffentryscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 3 | fscrapdescription | fscrapdescription | varchar | 50 |  | √ | ' ' |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryscrapreason | 报废原因 | int8 | 64 |  | √ | 0 | 报废原因 arm_screason |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmftunit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fid_entryid |  | fid,fentryid |
| 2 | pk_t_arm_scrapreportentry |  | fentryid |
