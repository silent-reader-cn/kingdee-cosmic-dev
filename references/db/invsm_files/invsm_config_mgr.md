# 参数配置管理-invsm_config_mgr

## 参数配置管理-主表 t_invsm_config_mgr

- **表名称：** 参数配置管理-主表
- **表名：** t_invsm_config_mgr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 3 | fconfigkey | 参数key | varchar | 50 |  | √ | ' ' | 参数key |
| 4 | fconfigvalue | 配置值 | varchar | 50 |  | √ | ' ' | 配置值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invsm_config_mgr |  | fconfigkey |
| 2 | pk_invsm_config_mgr |  | fid |
