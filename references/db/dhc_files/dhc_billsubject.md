# 单据主题-dhc_billsubject

## 单据主题-多语言表 t_dhc_billsubject_l

- **表名称：** 单据主题-多语言表
- **表名：** t_dhc_billsubject_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_dhc_billsubject_l_pkey |  | fpkid |
| 2 | idx_dhc_billsubject_l_id |  | fid |

---

## 单据体-子表 t_dhc_subjectentry

- **表名称：** 单据体-子表
- **表名：** t_dhc_subjectentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fposttext | 后置文本 | varchar | 100 |  | √ | ' ' | 后置文本 |
| 3 | frulefieldid | 单据字段 | varchar | 100 |  | √ | ' ' | 单据字段 |
| 4 | fmark | 单据标示 | varchar | 100 |  | √ | ' ' | 单据标示 |
| 5 | fpretext | 前置文本 | varchar | 100 |  | √ | ' ' | 前置文本 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_subjectentry_id |  | fid |
| 2 | t_dhc_subjectentry_pkey |  | fentryid |

---

## 单据主题-主表 t_dhc_billsubject

- **表名称：** 单据主题-主表
- **表名：** t_dhc_billsubject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 170 |  | √ | ' ' | 备注 |
| 3 | fbillnumber | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 11 | fbillname | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dhc_billsubject_billnumber |  | fbillnumber |
| 2 | t_dhc_billsubject_pkey |  | fid |
