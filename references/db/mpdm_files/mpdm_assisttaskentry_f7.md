# 辅助任务分录F7-mpdm_assisttaskentry_f7

## 辅助任务分录F7-多语言表 t_mpdm_assisttaskentry_l

- **表名称：** 辅助任务分录F7-多语言表
- **表名：** t_mpdm_assisttaskentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftaskdesc | 任务说明 | varchar | 2000 |  | √ | ' ' | 任务说明 |
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
| 1 | idx_mpdm_assisttaskentry_l_id |  | fentryid,flocaleid |
| 2 | pk_mpdm_assisttaskentry_l |  | fpkid |

---

## 设备-多选基础资料表 t_mpdm_assisttask_eqp

- **表名称：** 设备-多选基础资料表
- **表名：** t_mpdm_assisttask_eqp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [设备 sfc_equipment](../mpdm_files/sfc_equipment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_assisttask_eqp |  | fpkid |
| 2 | idx_mpdm_task_eqp_fidbdid |  | fentryid,fbasedataid |

---

## 辅助任务分录F7-主表 t_mpdm_assisttaskentry

- **表名称：** 辅助任务分录F7-主表
- **表名：** t_mpdm_assisttaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 单据编号 | int8 | 64 |  | √ | 0 | [辅助任务F7 mpdm_assisttask_f7](../mpdm_files/mpdm_assisttask_f7.md) |
| 2 | fmanualtime | 实际人工工时 | numeric | 23 | 10 | √ | 0 | 实际人工工时 |
| 3 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [辅助任务类型 mpdm_assisttasktype](../mpdm_files/mpdm_assisttasktype.md) |
| 5 | fexecuteorgid | 执行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fplanmanualtime | 计划人工工时 | numeric | 23 | 10 | √ | 0 | 计划人工工时 |
| 9 | flinkreportqty | 关联汇报数量 | numeric | 23 | 10 | √ | 0 | 关联汇报数量 |
| 10 | fbegintime | 实际开工时间 | timestamp | 0 |  |  | null | 实际开工时间 |
| 11 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 12 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 13 | fexecutedepartid | 执行车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fplanmachinetime | 计划机器工时 | numeric | 23 | 10 | √ | 0 | 计划机器工时 |
| 15 | fworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 16 | fprotimeunitid | 工时单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: A :计划 B :下达 C :开工 D :完工 E :关闭 |
| 18 | ftransmittime | ftransmittime | timestamp | 0 |  |  | null |  |
| 19 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 20 | fqty | 物料数量 | numeric | 23 | 10 | √ | 0 | 物料数量 |
| 21 | ftaskdesc | 任务说明 | varchar | 2000 |  | √ | ' ' | 任务说明 |
| 22 | fnormprocessid | 标准工序 | int8 | 64 |  | √ | 0 | [标准工序 mpdm_normprocess](../mpdm_files/mpdm_normprocess.md) |
| 23 | fclosebeforestatus | 关闭前状态 | bpchar | 1 |  | √ | ' ' | 关闭前状态,枚举: A :计划 B :下达 C :开工 D :完工 E :关闭 |
| 24 | funitid | 物料单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | flinkmanualtime | 关联实际人工工时 | numeric | 23 | 10 | √ | 0 | 关联实际人工工时 |
| 26 | fplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 27 | fproduceteamid | 团队 | int8 | 64 |  | √ | 0 | [制造团队 mpdm_mftteam](../mpdm_files/mpdm_mftteam.md) |
| 28 | flinkmachinetime | 关联实际机器工时 | numeric | 23 | 10 | √ | 0 | 关联实际机器工时 |
| 29 | fplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 30 | fmachinetime | 实际机器工时 | numeric | 23 | 10 | √ | 0 | 实际机器工时 |
| 31 | fendtime | 实际完工时间 | timestamp | 0 |  |  | null | 实际完工时间 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_assisttaskentry_fid |  | fid |
| 2 | pk_mpdm_assisttaskentry |  | fentryid |
