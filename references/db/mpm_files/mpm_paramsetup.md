# 项目管理参数配置-mpm_paramsetup

## 项目管理参数配置-主表 t_mpm_paramset

- **表名称：** 项目管理参数配置-主表
- **表名：** t_mpm_paramset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 200 |  |  | ' ' | 名称 |
| 3 | fparam | 参数 | varchar | 200 |  |  | ' ' | 参数 |
| 4 | fnumber | 编码 | varchar | 50 |  |  | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_paramset |  | fid |
| 2 | idx_mpm_paramset_number |  | fnumber |
