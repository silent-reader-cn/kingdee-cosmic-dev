# 第三方Web服务器-third_web_server

## 认证参数-子表 t_bas_3rd_web_server_para

- **表名称：** 认证参数-子表
- **表名：** t_bas_3rd_web_server_para

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam_value2 | 加密参数值 | varchar | 2000 |  | √ | ' ' | 加密参数值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparam_name | 参数名 | varchar | 30 |  | √ | ' ' | 参数名 |
| 5 | fparam_value | 明文参数值 | varchar | 2000 |  | √ | ' ' | 明文参数值 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_3rd_web_server_para_fk |  | fid |
| 2 | pk_bas_3rd_web_server_para |  | fentryid |

---

## 第三方Web服务器-主表 t_bas_3rd_web_server

- **表名称：** 第三方Web服务器-主表
- **表名：** t_bas_3rd_web_server

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fconnect_timeout | 连接超时（毫秒） | int4 | 32 |  | √ | 0 | 连接超时（毫秒） |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | furl | URL前缀 | varchar | 300 |  | √ | ' ' | URL前缀 |
| 8 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 9 | fmax_tps | 流量控制（次/秒） | int4 | 32 |  | √ | 0 | 流量控制（次/秒） |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_3rd_web_server |  | fid |
| 2 | idx_3rd_web_server_n |  | fnumber |

---

## 第三方Web服务器-多语言表 t_bas_3rd_web_server_l

- **表名称：** 第三方Web服务器-多语言表
- **表名：** t_bas_3rd_web_server_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_3rd_web_server_l_0 |  | fid,flocaleid |
| 2 | pk_bas_3rd_web_server_l |  | fpkid |
