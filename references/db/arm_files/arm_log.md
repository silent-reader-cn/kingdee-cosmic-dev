# 生产线排程日志-arm_log

## 生产线排程日志-主表 t_arm_log

- **表名称：** 生产线排程日志-主表
- **表名：** t_arm_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fstartdatetime | 开始时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 开始时间 |
| 5 | fenddatetime | 结束时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 结束时间 |
| 6 | forgid | 销售组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbillid | 源单据编号 | int8 | 64 |  | √ | 0 | 销售计划协议 amccsa_custschdorder |
| 8 | flineno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 9 | fbillno | 日志编号 | varchar | 30 |  | √ | ' ' | 日志编号 |
| 10 | fbilltype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: 0 :自动排程 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_log |  | fid |
| 2 | idx_t_arm_log_bill |  | fbilltype,fbillid,flineno |

---

## 单据体-子表 t_arm_logentry

- **表名称：** 单据体-子表
- **表名：** t_arm_logentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetail | 详细信息 | varchar | 500 |  | √ | ' ' | 详细信息 |
| 3 | fstepno | 步骤序号 | int8 | 64 |  | √ | 0 | 步骤序号 |
| 4 | fstepname | 步骤名称 | varchar | 500 |  | √ | ' ' | 步骤名称 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | flogtime | 记录时间 | int8 | 64 |  | √ | 0 | 记录时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_log_fid |  | fid |
| 2 | pk_t_arm_logentry |  | fentryid |
