# 归档组织映射基础资料-fpy_syset_orgmapp

## 归档组织映射基础资料-主表 tk_fpy_syset_orgmapp_ent

- **表名称：** 归档组织映射基础资料-主表
- **表名：** tk_fpy_syset_orgmapp_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_fpy_mappingtype | 映射方式 | varchar | 50 |  | √ | ' ' | 映射方式,枚举: number :编码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_fpy_taraccountid | 组织机构问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fk_fpy_srcorgname | 来源单据名称 | varchar | 50 |  | √ | ' ' | 来源单据名称 |
| 9 | fk_fpy_tarorgid | 归档组织编码 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 10 | fk_fpy_srcaccountnum | 来源组织机构问题 | varchar | 50 |  | √ | ' ' | 来源组织机构问题 |
| 11 | fmodifierfield | fmodifierfield | int8 | 64 |  |  | null |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 15 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 来源组织编码 | varchar | 30 |  | √ | ' ' | 来源组织编码 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_syset_orgmapp_ent |  | fentryid |

---

## 归档组织映射基础资料-多语言表 tk_fpy_syset_orgmapp_ent_l

- **表名称：** 归档组织映射基础资料-多语言表
- **表名：** tk_fpy_syset_orgmapp_ent_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_syset_orgmapp_ent_l |  | fpkid |
