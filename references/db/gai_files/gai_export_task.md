# 数据导出任务-gai_export_task

## 数据导出任务-主表 t_gai_export_task

- **表名称：** 数据导出任务-主表
- **表名：** t_gai_export_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexporttime | 导出时间 | timestamp | 0 |  |  | null | 导出时间 |
| 3 | floginfo | 导出信息 | varchar | 255 |  | √ | ' ' | 导出信息 |
| 4 | floginfo_tag | 导出信息_详情 | text | 0 |  |  | null | 导出信息_详情 |
| 5 | fuser | 导出人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fexportfile | 导出文件 | varchar | 255 |  | √ | ' ' | 导出文件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gai_export_task |  | fid |
