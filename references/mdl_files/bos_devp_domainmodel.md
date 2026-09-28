# 元模型-bos_devp_domainmodel

## 元模型-多语言表 t_dm_domaintype_l

- **表名称：** 元模型-多语言表
- **表名：** t_dm_domaintype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dm_domaintype_l |  | fid,flocaleid |
| 2 | pk_t_dm_domaintype_l |  | fpkid |

---

## 元模型-主表 t_dm_domaintype

- **表名称：** 元模型-主表
- **表名：** t_dm_domaintype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxml | 详情 | varchar | 255 |  | √ | ' ' | 详情 |
| 3 | fparent | 父元模型 | varchar | 50 |  | √ | ' ' | 父元模型 |
| 4 | fextend | 是否扩展 | bpchar | 1 |  | √ | '0' | 是否扩展 |
| 5 | fissys | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 6 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 7 | fparentnumber | 父元模型代码 | varchar | 50 |  | √ | ' ' | 父元模型代码 |
| 8 | fxml_tag | 详情_详情 | text | 0 |  |  | null | 详情_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_dm_domaintype |  | fnumber |
| 2 | pk_t_dm_domaintype |  | fid |
