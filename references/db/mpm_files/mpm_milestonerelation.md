# 里程碑关联任务-mpm_milestonerelation

## 里程碑关联任务-主表 t_mpm_milestonerel

- **表名称：** 里程碑关联任务-主表
- **表名：** t_mpm_milestonerel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frelsubprojectid | 关联子项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | frelsubmilestoneid | 关联子项目里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 5 | fmilestoneid | 项目里程碑 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_milestonerel |  | fid |
| 2 | idx_mpm_milestonerel_ms |  | fmilestoneid |
| 3 | idx_mpm_milestonerel_prj |  | fprojectid |
| 4 | idx_mpm_milestonerel_rms |  | frelsubmilestoneid |
| 5 | idx_mpm_milestonerel_rprj |  | frelsubprojectid |
