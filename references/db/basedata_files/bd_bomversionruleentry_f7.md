# BOM版本规则分录F7-bd_bomversionruleentry_f7

## BOM版本规则分录F7-多语言表 t_bd_bomversionruleentry_l

- **表名称：** BOM版本规则分录F7-多语言表
- **表名：** t_bd_bomversionruleentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fversion | 版本 | varchar | 100 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_bomversionruleentry_l_pkey |  | fpkid |
| 2 | idx_bd_bomversionruleentry_l |  | fentryid,flocaleid |

---

## BOM版本规则分录F7-主表 t_bd_bomversionruleentry

- **表名称：** BOM版本规则分录F7-主表
- **表名：** t_bd_bomversionruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |
| 2 | fseq | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_bomversionruleentry_pkey |  | fentryid |
| 2 | idx_bd_bomversionruleentry |  | fid,fseq |
