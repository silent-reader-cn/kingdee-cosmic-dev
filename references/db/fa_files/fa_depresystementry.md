# 折旧体系分录-fa_depresystementry

## 折旧体系分录-多语言表 t_fa_depresystementry_l

- **表名称：** 折旧体系分录-多语言表
- **表名：** t_fa_depresystementry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_depsysent_l_fid |  | fid |
| 2 | t_fa_depresystementry_l_pkey |  | fpkid |

---

## 折旧体系分录-主表 t_fa_depresystementry

- **表名称：** 折旧体系分录-主表
- **表名：** t_fa_depresystementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  |  | ' ' |  |
| 3 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 4 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 5 | fdeprecurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fassetpolicy | 资产政策 | int8 | 64 |  | √ | 0 | 折旧政策 fa_assetpolicy |
| 8 | fdepreuseid | 折旧用途 | int8 | 64 |  | √ | 0 | 折旧用途 fa_depreuse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depresystementry_pkey |  | fentryid |
| 2 | idx_fa_depsysent_fid |  | fid |
