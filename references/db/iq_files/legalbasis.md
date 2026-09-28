# 法规依据-legalbasis

## 法规依据-多语言表 t_iq_legal_basis_l

- **表名称：** 法规依据-多语言表
- **表名：** t_iq_legal_basis_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 适用板块 | varchar | 50 |  | √ | ' ' | 适用板块 |
| 3 | fruletype | 规则类别 | varchar | 50 |  | √ | ' ' | 规则类别 |
| 4 | flawname | 法规名称 | varchar | 200 |  | √ | ' ' | 法规名称 |
| 5 | fchapterno | 章节号 | varchar | 200 |  | √ | ' ' | 章节号 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iq_legal_basis_l |  | fid |
| 2 | pk_iq_legal_basis_l |  | fpkid |

---

## 法规依据-主表 t_iq_legal_basis

- **表名称：** 法规依据-主表
- **表名：** t_iq_legal_basis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 适用板块 | varchar | 50 |  | √ | ' ' | 适用板块 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fruletype | 规则类别 | varchar | 50 |  | √ | ' ' | 规则类别 |
| 6 | fchapterno | 章节号 | varchar | 200 |  | √ | ' ' | 章节号 |
| 7 | fhyperlink | 法规名称超链接 | varchar | 200 |  | √ | ' ' | 法规名称超链接 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | flawname | 法规名称 | varchar | 200 |  | √ | ' ' | 法规名称 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iq_legal_basis_name |  | fname |
| 2 | pk_iq_legal_basis |  | fid |
| 3 | idx_iq_legal_basis_number |  | fnumber |
