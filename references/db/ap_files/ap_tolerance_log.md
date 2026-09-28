# 容差日志-ap_tolerance_log

## 容差日志-主表 t_ap_tolerance_log

- **表名称：** 容差日志-主表
- **表名：** t_ap_tolerance_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontrolparty | 管控方 | varchar | 50 |  | √ | ' ' | 管控方 |
| 3 | foppositeparty | 对比方 | varchar | 50 |  | √ | ' ' | 对比方 |
| 4 | flowerlimit | 下限 | varchar | 50 |  | √ | ' ' | 下限 |
| 5 | foppositeobject | 对比对象 | varchar | 50 |  | √ | ' ' | 对比对象 |
| 6 | ftolerancelimit | 容差限制 | varchar | 50 |  | √ | ' ' | 容差限制 |
| 7 | foperationtime | 长日期 | timestamp | 0 |  |  | null | 长日期 |
| 8 | fstrategyname | 容差策略名称 | varchar | 50 |  | √ | ' ' | 容差策略名称 |
| 9 | fupperlimit | 上限 | varchar | 50 |  | √ | ' ' | 上限 |
| 10 | fcontrolobject | 管控对象 | varchar | 50 |  | √ | ' ' | 管控对象 |
| 11 | fsource | 容差方案来源 | varchar | 50 |  | √ | ' ' | 容差方案来源 |
| 12 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_tol_log_operatime |  | foperationtime |
| 2 | pk_t_ap_tolerance_log |  | fid |
