# 影响对象变更操作-plm_rm_change_effectopt

## 影响对象变更操作-主表 t_plm_rm_change_effectopt

- **表名称：** 影响对象变更操作-主表
- **表名：** t_plm_rm_change_effectopt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 变更操作 | varchar | 255 |  | √ | ' ' | 变更操作 |
| 3 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rm_change_effectopt |  | fid |
| 2 | idx_plm_rm_change_effectopt_m0 |  | fnumber |

---

## 影响对象变更操作-多语言表 t_plm_rm_change_effectopt_l

- **表名称：** 影响对象变更操作-多语言表
- **表名：** t_plm_rm_change_effectopt_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 变更操作 | varchar | 399 |  | √ | ' ' | 变更操作 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_change_effopt_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rm_change_effectopt_l |  | fpkid |
