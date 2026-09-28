# 会计要素表-bd_element_table

## 会计要素表-主表 t_bd_accountelement

- **表名称：** 会计要素表-主表
- **表名：** t_bd_accountelement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 3 | fissyspreset | 预置数据 | bpchar | 1 |  | √ | '0' | 预置数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_accountelement |  | fid |
| 2 | idx_accountelement_fnumber |  | fnumber |

---

## 会计要素表-多语言表 t_bd_accountelement_l

- **表名称：** 会计要素表-多语言表
- **表名：** t_bd_accountelement_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_accountelement_l |  | fpkid |
| 2 | idx_accountelement_l_loc |  | fid,flocaleid |
