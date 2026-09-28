# 任务扩展参数表-task_ext_param

## 任务扩展参数表-主表 t_tk_taskextparam

- **表名称：** 任务扩展参数表-主表
- **表名：** t_tk_taskextparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fextparam | 扩展参数 | text | 0 |  |  | null | 扩展参数 |
| 5 | fisstoreindb | 单据数据是否存表 | bpchar | 1 |  | √ | '1' | 单据数据是否存表 |
| 6 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 7 | fextparam_tag | 扩展参数_详情 | text | 0 |  |  | null | 扩展参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_extparam_tkid |  | ftaskid |
| 2 | t_tk_taskextparam_pkey |  | fid |
