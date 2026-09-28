# 模拟报价取价来源类型-sm_simquotpricesrctype

## 模拟报价取价来源类型-多语言表 t_sm_simquotpricesrctype_l

- **表名称：** 模拟报价取价来源类型-多语言表
- **表名：** t_sm_simquotpricesrctype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | pk_sm_simquotpricesrctype_l |  | fpkid |
| 2 | idx_sm_simquotprcsrctype_l |  | fid |

---

## 模拟报价取价来源类型-主表 t_sm_simquotpricesrctype

- **表名称：** 模拟报价取价来源类型-主表
- **表名：** t_sm_simquotpricesrctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fissys | 是否系统预置 | bpchar | 1 |  | √ | ' ' | 是否系统预置 |
| 4 | fclassname | 实现类 | varchar | 255 |  | √ | ' ' | 实现类 |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sm_simquotpricesrctype |  | fid |
| 2 | idx_sm_simquotpricesrctype |  | fnumber |
