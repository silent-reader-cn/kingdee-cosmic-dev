# 对账类型-frm_amount_type

## 对账类型-主表 t_ai_amounttype

- **表名称：** 对账类型-主表
- **表名：** t_ai_amounttype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 4 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 5 | fbizapp | 业务系统 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_amounttype |  | forgid,fbizapp |
| 2 | t_ai_amounttype_pkey |  | fid |

---

## 金额类别-多语言表 t_ai_amounttypeentry_l

- **表名称：** 金额类别-多语言表
- **表名：** t_ai_amounttypeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_amounttypeentry_l_pkey |  | fpkid |
| 2 | idx_ai_amounttypeentry_l |  | fentryid,flocaleid |

---

## 对账类型-多语言表 t_ai_amounttype_l

- **表名称：** 对账类型-多语言表
- **表名：** t_ai_amounttype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_amounttype_l |  | fid,flocaleid |
| 2 | t_ai_amounttype_l_pkey |  | fpkid |

---

## 金额类别-子表 t_ai_amounttypeentry

- **表名称：** 金额类别-子表
- **表名：** t_ai_amounttypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 4 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 5 | fbizapp | fbizapp | varchar | 36 |  | √ | ' ' |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 8 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_amounttypeentry_pkey |  | fentryid |
| 2 | idx_ai_amounttypeentry |  | fid |
