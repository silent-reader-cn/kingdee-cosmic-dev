# 调度部署记录-sch_deployinfo

## 调度部署记录-主表 t_sch_deployinfo

- **表名称：** 调度部署记录-主表
- **表名：** t_sch_deployinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexporttime | 数据包导出时间 | timestamp | 0 |  |  | null | 数据包导出时间 |
| 3 | ffilename | 文件名 | varchar | 255 |  | √ | ' ' | 文件名 |
| 4 | fpath | 文件部署路径 | varchar | 50 |  | √ | ' ' | 文件部署路径 |
| 5 | fschid | 计划id | varchar | 36 |  | √ | ' ' | 计划id |
| 6 | fexectime | 执行时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 执行时间 |
| 7 | fversion | 版本 | varchar | 10 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sch_deployinfo |  | fid |
| 2 | idx_sch_deployinfo_schid |  | fschid |
| 3 | idx_sch_deployinfo_filename |  | ffilename |
