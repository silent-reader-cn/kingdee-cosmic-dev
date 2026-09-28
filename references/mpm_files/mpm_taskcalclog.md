# 项目任务计算日志-mpm_taskcalclog

## 项目任务计算日志-主表 t_mpm_taskcalclog

- **表名称：** 项目任务计算日志-主表
- **表名：** t_mpm_taskcalclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fdeviationrate | 偏差率 | numeric | 23 | 10 | √ | 0 | 偏差率 |
| 5 | fprocess | 完成率 | numeric | 23 | 10 | √ | 0 | 完成率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_taskcalclog |  | fcreatetime,fprojectid |
| 2 | pk_mpm_taskcalclog |  | fid |
