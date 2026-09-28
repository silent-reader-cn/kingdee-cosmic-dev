# 业务类型-aqap_business_type

## 业务类型-多语言表 t_aqap_business_type_l

- **表名称：** 业务类型-多语言表
- **表名：** t_aqap_business_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 业务名称 | varchar | 255 |  | √ | ' ' | 业务名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_business_type_l_pkey |  | fpkid |
| 2 | idx_aqap_business_type_l_0 |  | fid,flocaleid |

---

## 业务类型-主表 t_aqap_business_type

- **表名称：** 业务类型-主表
- **表名：** t_aqap_business_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 8 | fnumber | 业务类型 | varchar | 80 |  | √ | ' ' | 业务类型 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_business_type_pkey |  | fid |
