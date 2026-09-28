# 数据标签-privacy_transdatatag

## 数据标签-多语言表 t_privacy_transdatatag_l

- **表名称：** 数据标签-多语言表
- **表名：** t_privacy_transdatatag_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标签名称 | varchar | 255 |  | √ | ' ' | 标签名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_privacy_transtag_l_fid |  | fid,flocaleid |
| 2 | pk_t_privacy_transdatatag_l |  | fpkid |

---

## 数据标签-主表 t_privacy_transdatatag

- **表名称：** 数据标签-主表
- **表名：** t_privacy_transdatatag

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 标签名称 | varchar | 255 |  | √ | ' ' | 标签名称 |
| 3 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 7 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdatacategory | 数据类别 | varchar | 10 |  | √ | ' ' | 数据类别,枚举: 0 :个人数据 1 :经营数据 2 :技术数据 |
| 10 | fdesenruleid | 脱敏规则 | varchar | 36 |  | √ | ' ' | [脱敏规则 privacy_desen_rules](../privacy_files/privacy_desen_rules.md) |
| 11 | fnumber | 标签编码 | varchar | 50 |  | √ | ' ' | 标签编码 |
| 12 | fdatalevel | 数据级别 | varchar | 10 |  | √ | ' ' | 数据级别,枚举: 0 :敏感个人数据 1 :一般个人数据 2 :关键商业数据 3 :关键技术数据 4 :国家关键数据 5 :普通数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_privacy_transtag_num |  | fnumber |
| 2 | pk_t_privacy_transdatatag |  | fid |
