# 层节设置(基础资料)-eafc_floor_config_base

## 层节设置(基础资料)-多语言表 tk_eafc_floor_config_base_l

- **表名称：** 层节设置(基础资料)-多语言表
- **表名：** tk_eafc_floor_config_base_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_floor_config_base_l |  | fpkid |

---

## 层节设置(基础资料)-主表 tk_eafc_floor_config_base

- **表名称：** 层节设置(基础资料)-主表
- **表名：** tk_eafc_floor_config_base

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 50 |  |  | null |  |
| 4 | fk_eafc_box_total | 总容量 | int8 | 64 |  |  | null | 总容量 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fk_eafc_box_used | 已上架 | int8 | 64 |  |  | null | 已上架 |
| 9 | fk_eafc_box_idle | 剩余空间 | int8 | 64 |  |  | null | 剩余空间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fk_eafc_shelf_fid | 所属密集架 | int8 | 64 |  |  | null | 所属密集架 |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 2 :禁用 1 :可用 0 :已满 |
| 14 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_floor_config_base_no |  | fnumber |
| 2 | pk__eafc_floor_config_base |  | fid |

---

## 单据体-子表 tk_eafc_box_config

- **表名称：** 单据体-子表
- **表名：** tk_eafc_box_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_archive_num_no | 档号 | varchar | 50 |  | √ | ' ' | 档号 |
| 3 | fk_eafc_box_no | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 4 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_file_sign | 题名 | varchar | 50 |  | √ | ' ' | 题名 |
| 7 | fk_eafc_box_fid | 档案盒id | varchar | 50 |  | √ | ' ' | 档案盒id |
| 8 | fk_eafc_desc | 备注说明 | varchar | 200 |  | √ | ' ' | 备注说明 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 10 | fk_eafc_business_type | 类别 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_box_config |  | fentryid |
