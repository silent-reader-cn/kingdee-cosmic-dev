# 税务组织信息-bastax_taxorg

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

## 税务组织信息-主表 t_bastax_taxorg

- **表名称：** 税务组织信息-主表
- **表名：** t_bastax_taxorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fistaxpayer | 纳税主体 | bpchar | 1 |  | √ | ' ' | 纳税主体 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | funifiedsocialcode | 统一社会信用代码 | varchar | 100 |  | √ | ' ' | 统一社会信用代码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 使用状态(单据头) | varchar | 50 |  | √ | ' ' | 使用状态(单据头),枚举: 0 :禁用 1 :可用 |
| 9 | flicensestatus | 许可状态 | varchar | 50 |  | √ | ' ' | 许可状态,枚举: A :未授权 B :已授权 C :已注销 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ftaxpayer | 纳税人名称 | varchar | 255 |  | √ | ' ' | 纳税人名称 |
| 12 | fcmborgtype | 来源职能类型 | int8 | 64 |  | √ | 0 | 组织职能类型 bos_org_biz |
| 13 | ftaxpayerdetail | 纳税主体信息 | varchar | 50 |  | √ | ' ' | 纳税主体信息 |
| 14 | fisvirtual | 虚体 | bpchar | 1 |  | √ | ' ' | 虚体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bastax_taxorg |  | fid |
| 2 | idx_bastax_taxorg |  | forgid |
| 3 | idx_bastax_taxno |  | funifiedsocialcode |

---

## 单据体-子表 t_bastax_taxorg_entity

- **表名称：** 单据体-子表
- **表名：** t_bastax_taxorg_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 3 | fistaxpayer | 纳税主体 | bpchar | 1 |  | √ | '0' | 纳税主体 |
| 4 | ftaxpayer | 纳税人名称 | varchar | 255 |  | √ | ' ' | 纳税人名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
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
