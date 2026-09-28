# 智能执行方案操作参数-gl_intellexecparam

## 单据体-子表 t_gl_intellexecparamentry

- **表名称：** 单据体-子表
- **表名：** t_gl_intellexecparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam | 参数编码 | varchar | 100 |  | √ | ' ' | 参数编码 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fparamtype | 参数类型 | varchar | 30 |  | √ | ' ' | 参数类型,枚举: text :文本 boolean :布尔 int :整形 combo :下拉框 |
| 5 | frequire | 必填 | bpchar | 1 |  | √ | '0' | 必填 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparamval | 参数默认值 | varchar | 100 |  |  | ' ' | 参数默认值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_operparamentry_id |  | fid |
| 2 | t_gl_intellexecparamentry_pkey |  | fentryid |

---

## 单据体-多语言表 t_gl_intellexecparamentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_gl_intellexecparamentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparamname | 参数名称 | varchar | 255 |  | √ | ' ' | 参数名称 |
| 2 | fparamdesc | 参数描述 | varchar | 1000 |  | √ | ' ' | 参数描述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fcomboval | 有效值范围 | varchar | 1000 |  | √ | ' ' | 有效值范围 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_operparameid |  | fentryid,flocaleid |
| 2 | t_gl_intellexecparamentry_l_pkey |  | fpkid |

---

## 智能执行方案操作参数-多语言表 t_gl_intellexecparam_l

- **表名称：** 智能执行方案操作参数-多语言表
- **表名：** t_gl_intellexecparam_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 400 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_param_mul |  | fid,flocaleid |
| 2 | t_gl_intellexecparam_l_pkey |  | fpkid |

---

## 智能执行方案操作参数-主表 t_gl_intellexecparam

- **表名称：** 智能执行方案操作参数-主表
- **表名：** t_gl_intellexecparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbussiness | 业务类型 | varchar | 80 |  | √ | ' ' | 业务类型,枚举: |
| 3 | fbizapp | 业务应用 | varchar | 18 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 4 | foper | 执行操作 | varchar | 80 |  | √ | ' ' | 执行操作,枚举: |
| 5 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_intellexecparam_pkey |  | fid |
| 2 | idx_param_number |  | fnumber |
