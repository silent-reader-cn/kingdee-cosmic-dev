# 成本工艺路线同步日志-cad_syncrouter_log

## 成本工艺路线同步日志-主表 t_cad_syncrouter_log

- **表名称：** 成本工艺路线同步日志-主表
- **表名：** t_cad_syncrouter_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsynctime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 3 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fproductrouterid | 制造工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 5 | fmsg | 失败原因 | varchar | 2000 |  | √ | ' ' | 失败原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_syncrouter_log |  | fid |
| 2 | idx_cad_syncrouter_log |  | fproductrouterid |
