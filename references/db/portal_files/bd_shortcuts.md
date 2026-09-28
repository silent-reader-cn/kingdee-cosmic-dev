# 快捷键基础资料-bd_shortcuts

## 快捷键基础资料-主表 t_bas_shortcuts

- **表名称：** 快捷键基础资料-主表
- **表名：** t_bas_shortcuts

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopinstructions | 操作说明 | varchar | 256 |  | √ | ' ' | 操作说明 |
| 3 | fkeycode | 键码 | varchar | 255 |  | √ | ' ' | 键码 |
| 4 | fdefaultkeycode | 默认快捷键键码 | varchar | 50 |  | √ | ' ' | 默认快捷键键码 |
| 5 | fmulilang_type | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 6 | fmodifier | 修改人 | varchar | 50 |  | √ | ' ' | 人员 bos_user |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建日期 |
| 8 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 9 | fdefaultshortcut | 默认快捷键 | varchar | 50 |  | √ | ' ' | 默认快捷键 |
| 10 | foperationtype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 11 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 12 | fshortcut | 快捷键 | varchar | 50 |  | √ | ' ' | 快捷键 |
| 13 | fissystem | 是否系统预设 | varchar | 10 |  | √ | ' ' | 是否系统预设 |
| 14 | foperationnum | 操作编码 | varchar | 50 |  | √ | ' ' | 操作编码 |
| 15 | fmulilang_des | 操作说明 | varchar | 256 |  | √ | ' ' | 操作说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_shortcuts |  | foperationnum |
| 2 | pk_t_bas_shortcuts |  | fid |

---

## 快捷键基础资料-多语言表 t_bas_shortcuts_l

- **表名称：** 快捷键基础资料-多语言表
- **表名：** t_bas_shortcuts_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmulilang_type | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fmulilang_des | 操作说明 | varchar | 256 |  | √ | ' ' | 操作说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bas_shortcuts_l |  | fpkid |
| 2 | idx_bas_shortcuts_l_0 |  | fid,flocaleid |
