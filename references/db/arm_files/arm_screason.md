# 原因代码-arm_screason

## 原因代码-主表 t_arm_screason

- **表名称：** 原因代码-主表
- **表名：** t_arm_screason

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 原因说明 | varchar | 510 |  |  | null | 原因说明 |
| 3 | ftype | 原因代码类型 | bpchar | 1 |  | √ | ' ' | 原因代码类型,枚举: 0 :报废原因 1 :停机原因 |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fnumber | 原因 | varchar | 50 |  | √ | ' ' | 原因 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_screason_no |  | fnumber |
| 2 | pk_t_arm_screason |  | fid |

---

## 原因代码-多语言表 t_arm_screason_l

- **表名称：** 原因代码-多语言表
- **表名：** t_arm_screason_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 原因说明 | varchar | 510 |  |  | null | 原因说明 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_screason_fid |  | fid |
| 2 | pk_t_arm_screason_l |  | fpkid |
