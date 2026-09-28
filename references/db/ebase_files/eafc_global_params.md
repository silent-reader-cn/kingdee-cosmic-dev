# 全局配置参数-eafc_global_params

## 全局配置参数-主表 tk_eafc_global_oarams

- **表名称：** 全局配置参数-主表
- **表名：** tk_eafc_global_oarams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_configvalue | 配置值 | varchar | 500 |  | √ | ' ' | 配置值 |
| 3 | fk_eafc_remark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 4 | fk_eafc_configkey | 参数key | varchar | 50 |  | √ | ' ' | 参数key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_global_oarams |  | fid |
