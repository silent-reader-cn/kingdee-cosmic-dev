# 结束初始化（废弃）-ipop_initendinitial

## 结束初始化（废弃）-主表 t_ipop_initendinitial

- **表名称：** 结束初始化（废弃）-主表
- **表名：** t_ipop_initendinitial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappnumber | 应用简码 | varchar | 50 |  | √ | ' ' | 应用简码 |
| 3 | fformid | 实体标识 | varchar | 50 |  | √ | ' ' | 实体标识 |
| 4 | fformname | 资料名称 | varchar | 255 |  | √ | ' ' | 资料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_initendinitial |  | fid |
| 2 | idx_ipop_initendinitial_id |  | fformid |

---

## 结束初始化（废弃）-多语言表 t_ipop_initendinitial_l

- **表名称：** 结束初始化（废弃）-多语言表
- **表名：** t_ipop_initendinitial_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fformname | 资料名称 | varchar | 255 |  | √ | ' ' | 资料名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_initendinitial_l |  | fpkid |
| 2 | idx_ipop_initendinitial_l |  | fid,flocaleid |
