# 成本主体类别-cal_bd_costaccounttype

## 成本主体类别-多语言表 t_cal_costaccounttype_l

- **表名称：** 成本主体类别-多语言表
- **表名：** t_cal_costaccounttype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costaccounttype_l_pkey |  | fpkid |
| 2 | idx_cal_catype_l_fid |  | fid,flocaleid |

---

## 成本主体类别-主表 t_cal_costaccounttype

- **表名称：** 成本主体类别-主表
- **表名：** t_cal_costaccounttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fisprev | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fisingroup | 跨成本主体成组 | bpchar | 1 |  | √ | '0' | 跨成本主体成组 |
| 5 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 6 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_costaccounttype_pkey |  | fid |
| 2 | idx_cal_catype_fnumber |  | fnumber |
