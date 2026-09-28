# 转换规则版本-botp_convertrulever

## 转换规则版本-多语言表 t_botp_convertrulever_l

- **表名称：** 转换规则版本-多语言表
- **表名：** t_botp_convertrulever_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 版本名称 | varchar | 255 |  | √ | ' ' | 版本名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_convertrulever_l |  | fid,flocaleid |
| 2 | pk_t_botp_convertrulever_l |  | fpkid |

---

## 转换规则版本-主表 t_botp_convertrulever

- **表名称：** 转换规则版本-主表
- **表名：** t_botp_convertrulever

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 版本名称 | varchar | 255 |  | √ | ' ' | 版本名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fconvertrule | 转换规则 | varchar | 36 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | flatest | 是否最新版本 | bpchar | 1 |  | √ | '0' | 是否最新版本,枚举: 0 :否 1 :是 |
| 12 | fnumber | 版本编码 | varchar | 36 |  | √ | ' ' | 版本编码 |
| 13 | fdata | 转换规则json | text | 0 |  |  | null | 转换规则json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_convertrulever_n |  | fnumber |
| 2 | pk_t_botp_convertrulever |  | fid |
