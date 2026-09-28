# 核销后台参数-msmod_wf_dbparam

## 核销后台参数-主表 t_msmod_wf_dbparam

- **表名称：** 核销后台参数-主表
- **表名：** t_msmod_wf_dbparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 取值 | varchar | 50 |  | √ | ' ' | 取值 |
| 3 | fkey | 标识 | varchar | 50 |  | √ | ' ' | 标识 |
| 4 | fwriteofftype | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msmod_wf_dbparam |  | fid |
| 2 | idx_t_msmod_wf_dbparam_fkey |  | fkey |
