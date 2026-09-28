# 适用条件属性值-bos_crappcondprovalue

## 适用条件属性值-主表 t_cr_appcondprovalue

- **表名称：** 适用条件属性值-主表
- **表名：** t_cr_appcondprovalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fvalue | 属性值 | varchar | 80 |  | √ | ' ' | 属性值 |
| 3 | fappcondproid | 适用条件属性 | varchar | 36 |  | √ | ' ' | 适用条件属性 bos_coderuleappcondpro |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cr_appcondprovalue_pkey |  | fid |
| 2 | idx_t_cr_appcpvalue_condpro |  | fappcondproid |

---

## 适用条件属性值-多语言表 t_cr_appcondprovalue_l

- **表名称：** 适用条件属性值-多语言表
- **表名：** t_cr_appcondprovalue_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_appcondprovalue_l_fid |  | fid,flocaleid |
| 2 | t_cr_appcondprovalue_l_pkey |  | fpkid |
