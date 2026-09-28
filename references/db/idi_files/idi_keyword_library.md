# 敏感词库-idi_keyword_library

## 敏感词库-多语言表 t_idi_keyword_library_l

- **表名称：** 敏感词库-多语言表
- **表名：** t_idi_keyword_library_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaledesc | 词库描述 | varchar | 400 |  | √ | ' ' | 词库描述 |
| 3 | fname | 词库名称 | varchar | 1000 |  | √ | ' ' | 词库名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_keyword_library_l |  | fpkid |
| 2 | idx_idi_key_lib_l_fid |  | fid |

---

## 敏感词库-主表 t_idi_keyword_library

- **表名称：** 敏感词库-主表
- **表名：** t_idi_keyword_library

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 词库名称 | varchar | 255 |  | √ | ' ' | 词库名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 6 | fwhitelist | 白名单 | varchar | 1000 |  | √ | ' ' | 白名单 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fkeyword | 敏感词 | varchar | 1000 |  | √ | ' ' | 敏感词 |
| 9 | flocaledesc | 词库描述 | varchar | 100 |  | √ | ' ' | 词库描述 |
| 10 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 词库编号 | varchar | 30 |  | √ | ' ' | 词库编号 |
| 15 | fdesc | 词库描述 | varchar | 100 |  | √ | ' ' | 词库描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_keyword_library |  | fid |
| 2 | idx_idi_key_lib_num |  | fnumber |
