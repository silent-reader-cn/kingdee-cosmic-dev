# webservice配置-er_config_webservice

## 单据体-子表 t_er_configentry

- **表名称：** 单据体-子表
- **表名：** t_er_configentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkey | key | varchar | 50 |  | √ | ' ' | key |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fval | val | varchar | 50 |  | √ | ' ' | val |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_configentry_pkey |  | fentryid |
| 2 | idx_er_cofien_fid |  | fid |

---

## webservice配置-主表 t_er_config

- **表名称：** webservice配置-主表
- **表名：** t_er_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusername | userName | varchar | 50 |  | √ | ' ' | userName |
| 3 | fdbtype | dbType | varchar | 50 |  | √ | ' ' | dbType |
| 4 | fdcname | dcName | varchar | 50 |  | √ | ' ' | dcName |
| 5 | fip_port | ip_port | varchar | 50 |  | √ | ' ' | ip_port |
| 6 | flanguage | language | varchar | 50 |  | √ | ' ' | language |
| 7 | fslnname | slnName | varchar | 50 |  | √ | ' ' | slnName |
| 8 | fpassword | password | varchar | 50 |  | √ | ' ' | password |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_config_pkey |  | fid |
| 2 | idx_er_config_fusername |  | fusername |
