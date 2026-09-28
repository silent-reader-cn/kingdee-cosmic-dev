# 参数设置-tctb_param_setting

## 参数设置-主表 t_tctb_param_setting

- **表名称：** 参数设置-主表
- **表名：** t_tctb_param_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | value | varchar | 100 |  | √ | ' ' | value |
| 3 | fkey | key | varchar | 100 |  | √ | ' ' | key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_param_setting |  | fkey |
| 2 | t_tctb_param_setting_pkey |  | fid |
