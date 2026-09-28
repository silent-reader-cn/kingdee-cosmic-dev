# 税务组织信息分录-bastax_taxorg_entry

## 适用税种-多选基础资料表 t_bastax_taxorg_applytax

- **表名称：** 适用税种-多选基础资料表
- **表名：** t_bastax_taxorg_applytax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_taxorg_applytax |  | fpkid |
| 2 | idx_bastax_taxorg_applytax_fk |  | fentryid |

---

## 税收辖区-多选基础资料表 t_bastax_taxorg_area

- **表名称：** 税收辖区-多选基础资料表
- **表名：** t_bastax_taxorg_area

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxorg_area_fk |  | fentryid |
| 2 | pk_bastax_taxorg_area |  | fpkid |

---

## 税务组织信息分录-主表 t_bastax_taxorg_entity

- **表名称：** 税务组织信息分录-主表
- **表名：** t_bastax_taxorg_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 税务组织 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |
| 2 | fstatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 3 | fistaxpayer | 纳税主体 | bpchar | 1 |  | √ | '0' | 纳税主体 |
| 4 | ftaxpayer | 纳税人名称 | varchar | 255 |  | √ | ' ' | 纳税人名称 |
| 5 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 6 | ftaxpayerdetail | 纳税主体信息 | varchar | 50 |  | √ | ' ' | 纳税主体信息 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 9 | funifiedsocialcode | 税号 | varchar | 100 |  | √ | ' ' | 税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bastax_taxorg_entity_fk |  | fid |
| 2 | pk_bastax_taxorg_entity |  | fentryid |
