# 供应链报表参数-scmc_report_params

## 供应链报表参数-主表 t_scmc_report_params

- **表名称：** 供应链报表参数-主表
- **表名：** t_scmc_report_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 参数值 | varchar | 100 |  | √ | ' ' | 参数值 |
| 3 | fkey | 参数标识 | varchar | 100 |  | √ | ' ' | 参数标识 |
| 4 | fsysid | 所属系统 | varchar | 50 |  | √ | ' ' | 所属系统,枚举: all :供应链公共 pm :采购 conm :合同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scmc_report_params |  | fid |
| 2 | idx_scmc_report_params |  | fkey |
