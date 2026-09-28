# 凭证模板扩展字段-ai_vchtpl_extfield

## 凭证模板扩展字段-主表 t_ai_vchtpl_extfield

- **表名称：** 凭证模板扩展字段-主表
- **表名：** t_ai_vchtpl_extfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvchfieldname | 凭证字段名 | varchar | 50 |  | √ | ' ' | 凭证字段名 |
| 3 | ftplfieldkey | 凭证模板字段编码 | varchar | 30 |  | √ | ' ' | 凭证模板字段编码 |
| 4 | ftplfieldname | 凭证模板字段名称 | varchar | 255 |  | √ | ' ' | 凭证模板字段名称 |
| 5 | ftplfieldsort | 模板字段类型 | varchar | 30 |  | √ | ' ' | 模板字段类型,枚举: Head :单据头 Entry :单据分录 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_vchtpl_extfield |  | fid |
| 2 | idx_ai_vchtpl_extfield |  | fvchfieldname |

---

## 凭证模板扩展字段-多语言表 t_ai_vchtpl_extfield_l

- **表名称：** 凭证模板扩展字段-多语言表
- **表名：** t_ai_vchtpl_extfield_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftplfieldname | 凭证模板字段名称 | varchar | 255 |  | √ | ' ' | 凭证模板字段名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_vchtpl_extfield_l |  | fid,flocaleid |
| 2 | pk_t_ai_vchtpl_extfield_l |  | fpkid |
