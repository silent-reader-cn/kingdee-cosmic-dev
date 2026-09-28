# 数据检查项-sca_datacheckitem

## 数据检查项-多语言表 t_sca_datacheckitem_l

- **表名称：** 数据检查项-多语言表
- **表名：** t_sca_datacheckitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 6 | ftips | 提示语 | varchar | 255 |  | √ | ' ' | 提示语 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_datacheckitem_l_pkey |  | fpkid |
| 2 | idx_sca_datacheckitem_l |  | fname |

---

## 数据检查项-主表 t_sca_datacheckitem

- **表名称：** 数据检查项-主表
- **表名：** t_sca_datacheckitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fplugin | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 3 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 4 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: aca :实际成本 sca :标准成本 |
| 5 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_datacheckitem |  | fnumber,fappnum |
| 2 | t_sca_datacheckitem_pkey |  | fid |
