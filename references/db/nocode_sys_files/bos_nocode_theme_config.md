# 个人主题配置-bos_nocode_theme_config

## 个人主题配置-主表 t_nocode_theme_config

- **表名称：** 个人主题配置-主表
- **表名：** t_nocode_theme_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfig | 主题配置 | text | 0 |  |  | null | 主题配置 |
| 3 | fuid | 用户id | int8 | 64 |  | √ | 0 | 用户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_theme_config |  | fid |
| 2 | idx_nc_theme_uid |  | fuid |
