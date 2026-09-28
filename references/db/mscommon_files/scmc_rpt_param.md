# 报表参数-scmc_rpt_param

## 报表参数-主表 t_scmc_rpt_globalparam

- **表名称：** 报表参数-主表
- **表名：** t_scmc_rpt_globalparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fquerylimit | 查询记录上限 | int4 | 32 |  | √ | 0 | 查询记录上限 |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | frequestlimit | 请求上限 | int4 | 32 |  | √ | 0 | 请求上限 |
| 5 | fenablelog | 是否启用分析日志 | bpchar | 1 |  | √ | '0' | 是否启用分析日志 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fexportlimit | 导出记录上限 | int4 | 32 |  | √ | 0 | 导出记录上限 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_scmc_rpt_param_fno |  | fnumber |
| 2 | pk_t_scmc_rpt_globalparam |  | fid |
