# 弹性域-bos_flex

## 弹性域-主表 t_bas_flex

- **表名称：** 弹性域-主表
- **表名：** t_bas_flex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fseparator | fseparator | varchar | 10 |  | √ | ' ' |  |
| 3 | fdisplayproperty | 显示属性 | bpchar | 1 |  | √ | '2' | 显示属性,枚举: 1 :编码 2 :名称 3 :编码+名称 |
| 4 | ftable | ftable | varchar | 25 |  | √ | ' ' |  |
| 5 | fdisplayformat | fdisplayformat | int8 | 64 |  | √ | 0 |  |
| 6 | fnumber | 编码 | varchar | 10 |  | √ | ' ' | 编码 |
| 7 | fformid | 弹性域表单 | varchar | 36 |  | √ | ' ' | 弹性域表单 |
| 8 | fbasedataservice | fbasedataservice | varchar | 200 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_flex_pkey |  | fid |
| 2 | idx_bas_flex_fnumber |  | fnumber |

---

## 弹性域-多语言表 t_bas_flex_l

- **表名称：** 弹性域-多语言表
- **表名：** t_bas_flex_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 200 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bas_flex_l_fid |  | fid,flocaleid |
| 2 | t_bas_flex_l_pkey |  | fpkid |
