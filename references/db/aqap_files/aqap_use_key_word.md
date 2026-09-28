# 付款用途关键字-aqap_use_key_word

## 付款用途关键字-主表 t_aqap_use_key_word

- **表名称：** 付款用途关键字-主表
- **表名：** t_aqap_use_key_word

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 4 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 5 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 6 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :系统默认 1 :用户自定义 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fuse_key_word | 用途关键字 | varchar | 50 |  | √ | ' ' | 用途关键字 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_use_key_word_pkey |  | fid |

---

## 付款用途关键字-多语言表 t_aqap_use_key_word_l

- **表名称：** 付款用途关键字-多语言表
- **表名：** t_aqap_use_key_word_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_use_key_word_l_pkey |  | fpkid |
