# API配置-idi_api_config

## API配置-多语言表 t_idi_api_config_l

- **表名称：** API配置-多语言表
- **表名：** t_idi_api_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_api_config_l |  | fpkid |
| 2 | idx_idi_api_config_l_fid |  | fid |

---

## 参数信息-子表 t_idi_api_param_config

- **表名称：** 参数信息-子表
- **表名：** t_idi_api_param_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamname | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fparamtype | 参数值 | varchar | 50 |  | √ | ' ' | 参数值 |
| 5 | fparamdesc | 参数说明 | varchar | 255 |  |  | null | 参数说明 |
| 6 | fparamid | fparamid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fparamid | fparamid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_api_param_config_fid |  | fid |
| 2 | pk_t_idi_api_param_config |  | fparamid |

---

## API配置-主表 t_idi_api_config

- **表名称：** API配置-主表
- **表名：** t_idi_api_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fclientid | client_id | varchar | 64 |  | √ | ' ' | client_id |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fclientsecret | client_secret | varchar | 128 |  | √ | ' ' | client_secret |
| 7 | fhttpmethod | 请求方式 | varchar | 30 |  | √ | ' ' | 请求方式,枚举: GET :GET POST :POST |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | furl | url | varchar | 1024 |  | √ | ' ' | url |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_api_config_number |  | fnumber |
| 2 | pk_t_idi_api_config |  | fid |
