# 密集架设置-eafc_shelf_config

## 密集架设置-主表 tk_eafc_shelf_config

- **表名称：** 密集架设置-主表
- **表名：** tk_eafc_shelf_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_shelf_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :可用 2 :禁用 0 :已满 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_eafc_box_total | 总容量（盒） | int8 | 64 |  |  | null | 总容量（盒） |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fk_eafc_shelf_name | 密集架名称 | varchar | 50 |  | √ | ' ' | 密集架名称 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_eafc_box_idle | 剩余空间（盒） | int8 | 64 |  |  | null | 剩余空间（盒） |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fk_eafc_integerfield | 已上架（盒） | int8 | 64 |  |  | null | 已上架（盒） |
| 14 | fk_eafc_area_fid | 所属区域 | int8 | 64 |  |  | null | 所属区域 |
| 15 | fbillno | 密集架编号 | varchar | 30 |  | √ | ' ' | 密集架编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_shelf_config |  | fid |

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
