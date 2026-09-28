# 账簿类型管理-eafc_book_manager

## 账簿类型管理-主表 tk_eafc_book_manager

- **表名称：** 账簿类型管理-主表
- **表名：** tk_eafc_book_manager

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_eafc_book_type | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 7 | fk_eafc_tax_no | 企业税号 | varchar | 50 |  | √ | ' ' | 企业税号 |
| 8 | fk_eafc_book_no | 账簿编码 | varchar | 30 |  | √ | ' ' | 账簿编码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fk_eafc_enable | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :可用 |
| 13 | fk_eafc_createtime | 接收时间 | timestamp | 0 |  |  | null | 接收时间 |
| 14 | fk_eafc_general_code | 全宗号 | varchar | 50 |  | √ | ' ' | 全宗号 |
| 15 | fk_eafc_remark | 备注 | varchar | 514 |  | √ | ' ' | 备注 |
| 16 | fk_eafc_general_desc | 全宗号描述 | varchar | 50 |  | √ | ' ' | 全宗号描述 |
| 17 | fk_eafc_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_book_manager |  | fid |

---

## 账簿类型管理-多语言表 tk_eafc_book_manager_l

- **表名称：** 账簿类型管理-多语言表
- **表名：** tk_eafc_book_manager_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
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
| 1 | idx_eafc_book_manager_l_fk |  | fid |
| 2 | pk_eafc_book_manager_l |  | fpkid |
