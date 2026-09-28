# 第三方应用拆分表-xkopenthird_appsplit

## 第三方应用拆分表-主表 t_open_3rdapps_g

- **表名称：** 第三方应用拆分表-主表
- **表名：** t_open_3rdapps_g

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | appSecret | varchar | 255 |  | √ | ' ' | appSecret |
| 3 | fappkey | appId | varchar | 50 |  | √ | ' ' | appId |
| 4 | fgatewayappid | fgatewayappid | varchar | 50 |  | √ | ' ' |  |
| 5 | facgw_identity | x-acgw-identity | varchar | 255 |  | √ | ' ' | x-acgw-identity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_3rdapps_g |  | fid |
| 2 | idx_t_open_3rdapps_g |  | fappkey |
