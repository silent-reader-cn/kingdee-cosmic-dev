# 余额规则逻辑字段-bal_logic_col

## 余额规则逻辑字段-多语言表 t_bal_logic_col_l

- **表名称：** 余额规则逻辑字段-多语言表
- **表名：** t_bal_logic_col_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_lg_col_l_lid |  | fid,flocaleid |
| 2 | pk_bal_logic_col_l |  | fpkid |

---

## 余额规则逻辑字段-主表 t_bal_logic_col

- **表名称：** 余额规则逻辑字段-主表
- **表名：** t_bal_logic_col

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fname | 名称 | varchar | 30 |  | √ | ' ' | 名称 |
| 3 | fsysinit | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | '0' | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_logic_col |  | fid |
| 2 | idx_bal_lg_col_no |  | fno |
