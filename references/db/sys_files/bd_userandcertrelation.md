# 证书用户关系-bd_userandcertrelation

## 证书用户关系-主表 t_bd_userandcertrelation

- **表名称：** 证书用户关系-主表
- **表名：** t_bd_userandcertrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcertid | 证书主键 | int8 | 64 |  | √ | 0 | 证书主键 |
| 3 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_userandcertrelation_pkey |  | fid |
| 2 | idx_bd_certuser_rel_certid |  | fcertid |
| 3 | idx_bd_certuser_rel_userid |  | fuserid |
