# 全宗管理-eafc_general_archive_base

## 全宗管理-主表 tk_eafc_general_archive_b

- **表名称：** 全宗管理-主表
- **表名：** tk_eafc_general_archive_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | fname | varchar | 50 |  |  | null |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fk_eafc_booktype | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 11 | fk_eafc_superior_org | 上级业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fk_eafc_enterprise_tax | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |
| 13 | fenable | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 14 | fnumber | 全宗号 | varchar | 30 |  | √ | ' ' | 全宗号 |
| 15 | fk_eafc_desc | 全宗描述 | varchar | 50 |  | √ | ' ' | 全宗描述 |
| 16 | fk_eafc_effective_time | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_general_archive_b |  | fid |

---

## 全宗管理-多语言表 tk_eafc_general_archive_b_l

- **表名称：** 全宗管理-多语言表
- **表名：** tk_eafc_general_archive_b_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 全宗名称 | varchar | 50 |  | √ | ' ' | 全宗名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_general_archive_b_l |  | fpkid |
