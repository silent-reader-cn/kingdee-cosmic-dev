# WeLink-cts_welink

## WeLink-主表 t_bas_welink

- **表名称：** WeLink-主表
- **表名：** t_bas_welink

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | 应用秘钥 | varchar | 150 |  | √ | ' ' | 应用秘钥 |
| 3 | fappname | 应用名称 | varchar | 150 |  | √ | ' ' | 应用名称 |
| 4 | fappid | 应用ID | varchar | 150 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_welink |  | fid |
| 2 | idx_welink_fappid |  | fappid |
