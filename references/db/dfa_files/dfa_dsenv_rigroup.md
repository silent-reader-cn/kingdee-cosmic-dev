# 取数环境报表项目分组映射-dfa_dsenv_rigroup

## 取数环境报表项目分组映射-主表 t_dfa_dsenv_rigroup

- **表名称：** 取数环境报表项目分组映射-主表
- **表名：** t_dfa_dsenv_rigroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fitemgroupname | 报表项目分组名称 | varchar | 255 |  | √ | ' ' | 报表项目分组名称 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fdatasrcenv | 取数环境 | int8 | 64 |  | √ | 0 | [取数环境 dfa_datasource_env](../dfa_files/dfa_datasource_env.md) |
| 4 | fdatasourcetype | 数据源类型 | varchar | 50 |  | √ | ' ' | 数据源类型 |
| 5 | fitemgroupcode | 报表项目分组编码 | varchar | 255 |  | √ | ' ' | 报表项目分组编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_dsenv_rigroup_m0 |  | fitemgroupcode |
| 2 | pk_dfa_dsenv_rigroup |  | fid |
