# 加密参数配置-tsate_secret_config

## 加密参数配置-主表 t_tsate_secret_config

- **表名称：** 加密参数配置-主表
- **表名：** t_tsate_secret_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsecretvalue | secret_value | varchar | 255 |  | √ | ' ' | secret_value |
| 3 | fsecretkey | secretkey | varchar | 255 |  | √ | ' ' | secretkey |
| 4 | fsecretkey_tag | fsecretkey_tag | text | 0 |  |  | null |  |
| 5 | fsecretvalue_tag | secret_value_详情 | text | 0 |  |  | null | secret_value_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_secret_selkey |  | fsecretkey |
| 2 | pk_tsate_secret_config |  | fid |
