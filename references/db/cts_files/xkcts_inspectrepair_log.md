# 巡检任务修复日志-xkcts_inspectrepair_log

## 巡检任务修复日志-主表 t_xkinsp_repair_log

- **表名称：** 巡检任务修复日志-主表
- **表名：** t_xkinsp_repair_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fparametername | 巡检维度 | varchar | 300 |  | √ | ' ' | 巡检维度 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | frepairstatus | 操作结果 | varchar | 10 |  | √ | ' ' | 操作结果,枚举: 1 :成功 2 :失败 |
| 8 | fitemid | 检查项 | int8 | 64 |  | √ | 0 | [巡检检查项 xkcts_inspectitem](../cts_files/xkcts_inspectitem.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | frepairtype | 操作 | varchar | 10 |  | √ | ' ' | 操作,枚举: 1 :自动 2 :手动 |
| 11 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 任务批次编号 | varchar | 30 |  | √ | ' ' | 任务批次编号 |
| 13 | frepairmsg | 结果说明 | varchar | 200 |  | √ | ' ' | 结果说明 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_repair_log |  | fid |
| 2 | idx_repair_log_creat |  | fcreatetime |
| 3 | idx_repair_log_item |  | fitemid |

---

## 巡检任务修复日志-多语言表 t_xkinsp_repair_log_l

- **表名称：** 巡检任务修复日志-多语言表
- **表名：** t_xkinsp_repair_log_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | frepairmsg | 结果说明 | varchar | 200 |  | √ | ' ' | 结果说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinsp_repair_log_l |  | fpkid |
| 2 | idx_xkinsp_repair_log_l |  | fid,flocaleid |
