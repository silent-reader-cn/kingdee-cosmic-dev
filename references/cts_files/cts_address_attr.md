# 控件属性替代-cts_address_attr

## 控件属性替代-主表 t_cts_addrpropalias

- **表名称：** 控件属性替代-主表
- **表名：** t_cts_addrpropalias

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ftype | 类别 | varchar | 50 |  | √ | ' ' | 类别 |
| 4 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 5 | fcolumnname | 属性 | varchar | 36 |  | √ | ' ' | 属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_addrpropalias |  | fid |
| 2 | idx_cts_addrpropalias |  | ftype |

---

## 控件属性替代-多语言表 t_cts_addrpropalias_l

- **表名称：** 控件属性替代-多语言表
- **表名：** t_cts_addrpropalias_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cts_addrpropalias_l |  | fpkid |
| 2 | idx_cts_addrpropalias_l |  | fid,flocaleid |
