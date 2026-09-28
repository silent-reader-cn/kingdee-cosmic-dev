# 签名供应商-ca_config_provider

## 签名供应商-多语言表 t_bd_signconfig_l

- **表名称：** 签名供应商-多语言表
- **表名：** t_bd_signconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprovidername | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_signconfig_l_id |  | fid,flocaleid |
| 2 | t_bd_signconfig_l_pkey |  | fpkid |

---

## 签名供应商-主表 t_bd_signconfig

- **表名称：** 签名供应商-主表
- **表名：** t_bd_signconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfig | 签名配置 | varchar | 255 |  | √ | ' ' | 签名配置 |
| 3 | fconfig_tag | 签名配置_详情 | text | 0 |  |  | null | 签名配置_详情 |
| 4 | fprovidername | fprovidername | varchar | 100 |  | √ | ' ' |  |
| 5 | fprovider | 供应商 | varchar | 6 |  | √ | ' ' | 供应商,枚举: 0 :天威诚信 1 :CFCA 2 :信安世纪 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_signconfig_provider |  | fprovider |
| 2 | t_bd_signconfig_pkey |  | fid |
