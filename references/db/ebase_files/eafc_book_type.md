# 机构问题-eafc_book_type

## 归档组织-子表 tk_eafc_allocate_org

- **表名称：** 归档组织-子表
- **表名：** tk_eafc_allocate_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_main_org | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fk_eafc_arcorg | 归档组织编码 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_allocate_org |  | fentryid |

---

## 机构问题-主表 tk_eafc_book_type

- **表名称：** 机构问题-主表
- **表名：** tk_eafc_book_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_book_desc | 账簿性质 | varchar | 50 |  | √ | ' ' | 账簿性质,枚举: 主账簿 :主账簿 管理账簿 :管理账簿 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 650 |  | √ | ' ' |  |
| 5 | fk_eafc_resource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :自动绑定 3 :初始化 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_eafc_book_type | 机构问题类型 | varchar | 50 |  | √ | ' ' | 机构问题类型,枚举: 1 :账簿类型 2 :账簿 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fk_eafc_institution_num | 机构编码 | varchar | 650 |  | √ | ' ' | 机构编码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | fk_eafc_creator | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fk_eafc_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fnumber | 机构问题编码 | varchar | 650 |  | √ | ' ' | 机构问题编码 |
| 17 | fk_eafc_remark | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 18 | fk_eafc_unique_code | 机构问题代码 | varchar | 650 |  | √ | ' ' | 机构问题代码 |
| 19 | fk_eafc_arcorg | fk_eafc_arcorg | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_book_type |  | fid |

---

## 机构问题-多语言表 tk_eafc_book_type_l

- **表名称：** 机构问题-多语言表
- **表名：** tk_eafc_book_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 机构问题名称 | varchar | 50 |  | √ | ' ' | 机构问题名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_book_type_l |  | fpkid |
| 2 | idx_eafc_book_type_l_fk |  | fid |
