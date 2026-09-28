# 单据映射-dhc_billmapping

## 单据映射-多语言表 t_dhc_billmapping_l

- **表名称：** 单据映射-多语言表
- **表名：** t_dhc_billmapping_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 3 | fmappingname | 映射字段名 | varchar | 300 |  | √ | ' ' | 映射字段名 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 6 | fbillname | fbillname | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_dhc_billmapping_l_pkey |  | fpkid |
| 2 | idx_dhc_map_locale_id |  | fid,flocaleid |

---

## 单据映射-主表 t_dhc_billmapping

- **表名称：** 单据映射-主表
- **表名：** t_dhc_billmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 36 |  | √ | ' ' |  |
| 3 | fmappingname | fmappingname | varchar | 300 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | ftag | 表头字段标志位 | bpchar | 1 |  | √ | ' ' | 表头字段标志位,枚举: 1 :是 0 :否 |
| 6 | fmappingnumber | 映射字段编码 | varchar | 300 |  | √ | ' ' | 映射字段编码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fbill | 接入单据 | int8 | 64 |  | √ | 0 | 接入单据 dhc_billaccessed |
| 9 | fbillname | 接入单据名称 | varchar | 36 |  | √ | ' ' | 接入单据名称 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbillnumber | 接入单据编码 | varchar | 36 |  | √ | ' ' | 接入单据编码 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | '1' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcusattribute | 自定义属性 | bpchar | 1 |  | √ | ' ' | 自定义属性,枚举: D :系统默认 C :自定义 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 16 | fsequence | 展示顺序 | int8 | 64 |  | √ | 0 | 展示顺序 |
| 17 | fmappingtype | 映射方式 | bpchar | 1 |  | √ | ' ' | 映射方式,枚举: A :映射 B :无需映射 C :主题配置 D :映射及值对应 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 字段编码 | varchar | 36 |  | √ | ' ' | 字段编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_billmapping_config |  | fbillnumber,fnumber |
| 2 | t_dhc_billmapping_pkey |  | fid |
