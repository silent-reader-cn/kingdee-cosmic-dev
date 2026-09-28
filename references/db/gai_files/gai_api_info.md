# API基础信息-gai_api_info

## API基础信息-主表 t_gai_api_info

- **表名称：** API基础信息-主表
- **表名：** t_gai_api_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | API名称 | varchar | 200 |  | √ | ' ' | API名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | fuseorg | int8 | 64 |  | √ | 0 |  |
| 7 | fapinumber | fapinumber | varchar | 50 |  |  | ' ' |  |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | fctrlstrategy | varchar | 50 |  |  | ' ' |  |
| 12 | fstatus | 数据状态 | varchar | 50 |  |  | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fapiname | fapiname | varchar | 100 |  |  | ' ' |  |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fapipath | API路径 | varchar | 200 |  |  | ' ' | API路径 |
| 17 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 18 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 19 | fenable | 使用状态 | varchar | 50 |  |  | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fbussinessorg | fbussinessorg | int8 | 64 |  | √ | 0 |  |
| 21 | fnumber | API编码 | varchar | 30 |  |  | ' ' | API编码 |
| 22 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_api_info |  | fid |

---

## API基础信息-多语言表 t_gai_api_info_l

- **表名称：** API基础信息-多语言表
- **表名：** t_gai_api_info_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | API名称 | varchar | 200 |  | √ | ' ' | API名称 |
| 3 | frepo_name | frepo_name | varchar | 200 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gai_api_info_l |  | fpkid |
