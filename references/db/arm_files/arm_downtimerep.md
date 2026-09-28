# 停机时长汇报-arm_downtimerep

## 停机时长汇报-主表 t_arm_downtimerep

- **表名称：** 停机时长汇报-主表
- **表名：** t_arm_downtimerep

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 5 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 C :已审核 B :已提交 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fpersonnel | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fworkshop | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fbiztime | 业务日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 业务日期 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fteamsgroup | 班组 | int8 | 64 |  | √ | 0 | [班组 mpdm_classgroup](../mpdm_files/mpdm_classgroup.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arm_downtimerep_m0 |  | fbillno |
| 2 | pk_arm_downtimerep |  | fid |

---

## 单据体-子表 t_arm_downtimerepentity

- **表名称：** 单据体-子表
- **表名：** t_arm_downtimerepentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fdownreason | 停机原因 | int8 | 64 |  | √ | 0 | [原因代码 arm_screason](../arm_files/arm_screason.md) |
| 4 | fdowntime | 停机时长 | numeric | 23 | 10 | √ | 0 | 停机时长 |
| 5 | ftimeunitrep | 时间单位 | varchar | 50 |  | √ | ' ' | 时间单位,枚举: hour :小时 minute :分钟 second :秒 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_arm_downtimerepentity |  | fentryid |
| 2 | idx_arm_downtimerepentity_fk |  | fid |
