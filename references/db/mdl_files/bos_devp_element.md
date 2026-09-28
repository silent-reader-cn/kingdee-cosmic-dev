# 元素-bos_devp_element

## 元素-多语言表 t_dm_elementtype_l

- **表名称：** 元素-多语言表
- **表名：** t_dm_elementtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodeltypename | 元模型类型名称 | varchar | 50 |  | √ | ' ' | 元模型类型名称 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcategoryname | 所属分组名称 | varchar | 50 |  | √ | ' ' | 所属分组名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fapplynumbername | 所属元模型名称 | varchar | 680 |  |  | null | 所属元模型名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dm_elementtype_l |  | fid,flocaleid |
| 2 | pk_t_dm_elementtype_l |  | fpkid |

---

## 单据体-多语言表 t_dm_elementtypeentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_dm_elementtypeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpropertyname | 名称 | varchar | 106 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_elementtypeentry_l |  | fpkid |
| 2 | idx_dm_elementtypeentry_l |  | fentryid,flocaleid |

---

## 元素-主表 t_dm_elementtype

- **表名称：** 元素-主表
- **表名：** t_dm_elementtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxml | xml | varchar | 255 |  | √ | ' ' | xml |
| 3 | fcategory | 所属分组 | varchar | 50 |  | √ | ' ' | 所属分组,枚举: |
| 4 | fcategoryxml | 分组xml | varchar | 255 |  | √ | ' ' | 分组xml |
| 5 | fmodeltype | 所属元模型 | varchar | 50 |  | √ | ' ' | 所属元模型,枚举: |
| 6 | fisv | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 7 | fcategoryxml_tag | 分组xml_详情 | text | 0 |  |  | null | 分组xml_详情 |
| 8 | fpackagename | 所属包名 | varchar | 400 |  | √ | ' ' | 所属包名 |
| 9 | fxml_tag | xml_详情 | text | 0 |  |  | null | xml_详情 |
| 10 | fissys | 扩展 | bpchar | 1 |  | √ | '0' | 扩展 |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 12 | fapplynumber | 所属元模型 | varchar | 500 |  | √ | ' ' | 所属元模型,枚举: |
| 13 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_elementtype |  | fid |
| 2 | idx_t_dm_elementtype |  | fnumber |

---

## 单据体-子表 t_dm_elementtypeentry

- **表名称：** 单据体-子表
- **表名：** t_dm_elementtypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 3 | fexpand | 继承 | bpchar | 1 |  | √ | '0' | 继承 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fpropertynumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dm_elementtypeentry |  | fentryid |
| 2 | idx_dm_elementtypeentry |  | fid,fseq |
