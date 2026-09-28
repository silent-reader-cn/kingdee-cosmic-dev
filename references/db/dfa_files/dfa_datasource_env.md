# 取数环境-dfa_datasource_env

## 取数环境-主表 t_dfa_datasource_env

- **表名称：** 取数环境-主表
- **表名：** t_dfa_datasource_env

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 取数环境名称 | varchar | 255 |  | √ | ' ' | 取数环境名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fconnectinfojson_tag | 连接信息大文本_详情 | text | 0 |  |  | null | 连接信息大文本_详情 |
| 6 | fsrctype | 环境选项 | varchar | 50 |  | √ | ' ' | 环境选项,枚举: 0 :星空旗舰版 1 :星空企业版 2 :星瀚 |
| 7 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fenvtype | 取数环境类型 | varchar | 50 |  | √ | ' ' | 取数环境类型,枚举: 0 :金蝶云 |
| 13 | fconnectinfojson | 连接信息大文本 | varchar | 2000 |  | √ | ' ' | 连接信息大文本 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 取数环境编码 | varchar | 255 |  | √ | ' ' | 取数环境编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_datasource_env_m0 |  | fmasterid |
| 2 | pk_dfa_datasource_env |  | fid |

---

## 取数环境-多语言表 t_dfa_datasource_env_l

- **表名称：** 取数环境-多语言表
- **表名：** t_dfa_datasource_env_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 取数环境名称 | varchar | 1024 |  | √ | ' ' | 取数环境名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_datasource_env_l_0 |  | fid,flocaleid |
| 2 | pk_dfa_datasource_env_l |  | fpkid |
