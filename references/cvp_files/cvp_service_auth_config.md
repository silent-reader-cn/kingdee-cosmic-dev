# 视觉识别服务配置-cvp_service_auth_config

## 视觉识别服务配置-主表 t_cvp_service_auth_config

- **表名称：** 视觉识别服务配置-主表
- **表名：** t_cvp_service_auth_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpubliccipher | 公钥 | varchar | 1000 |  | √ | ' ' | 公钥 |
| 3 | fclientid | 客户端ID | varchar | 100 |  | √ | ' ' | 客户端ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_service_auth_conf |  | fclientid |
| 2 | pk_t_cvp_service_auth_config |  | fid |
