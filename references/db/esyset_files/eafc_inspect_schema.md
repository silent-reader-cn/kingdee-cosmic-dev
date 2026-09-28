# 四性检测配置-eafc_inspect_schema

## 四性检测配置-使用范围表 tk_eafc_inspect_schema_u

- **表名称：** 四性检测配置-使用范围表
- **表名：** tk_eafc_inspect_schema_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | tk_eafc_inspect_schema_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_tk_eafc_inspect_schema_u_uo |  | fuseorgid |

---

## 四性检测配置-主表 tk_eafc_inspect_schema

- **表名称：** 四性检测配置-主表
- **表名：** tk_eafc_inspect_schema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_book_type | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fk_eafc_usable_config_tag | 可用性检测配置详情_详情 | text | 0 |  |  | null | 可用性检测配置详情_详情 |
| 8 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 11 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 12 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 13 | fk_eafc_priority_level | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 |
| 14 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fname | fname | varchar | 50 |  |  | null |  |
| 18 | fk_fpy_nosign | fk_fpy_nosign | bpchar | 1 |  | √ | '0' |  |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fk_eafc_detection_process | 检测环节 | varchar | 50 |  | √ | ' ' | 检测环节,枚举: 1 :接收环节 2 :归档环节 |
| 21 | fk_eafc_usable_config | 可用性检测配置详情 | varchar | 255 |  | √ | ' ' | 可用性检测配置详情 |
| 22 | fk_eafc_integrity_config_tag | 完整性检测配置详情_详情 | text | 0 |  |  | null | 完整性检测配置详情_详情 |
| 23 | fk_eafc_real_config | 真实性检测配置详情 | varchar | 255 |  | √ | ' ' | 真实性检测配置详情 |
| 24 | fk_eafc_safe_config | 安全性检测配置详情 | varchar | 255 |  | √ | ' ' | 安全性检测配置详情 |
| 25 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | fk_eafc_detection_type | 检测类型 | varchar | 50 |  | √ | ' ' | 检测类型,枚举: 1 :真实性 2 :完整性 3 :可用性 4 :安全性 |
| 27 | fk_eafc_real_config_tag | 真实性检测配置详情_详情 | text | 0 |  |  | null | 真实性检测配置详情_详情 |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fk_eafc_useorg | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fk_eafc_integrity_config | 完整性检测配置详情 | varchar | 255 |  | √ | ' ' | 完整性检测配置详情 |
| 31 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 32 | fk_eafc_desc | 方案描述 | varchar | 500 |  | √ | ' ' | 方案描述 |
| 33 | fk_eafc_safe_config_tag | 安全性检测配置详情_详情 | text | 0 |  |  | null | 安全性检测配置详情_详情 |
| 34 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_schema |  | fid |
| 2 | idx_tk_eafc_inspect_schema_master |  | fmasterid |
| 3 | idx_tk_eafc_inspect_schema_createorg |  | fcreateorgid |

---

## 四性检测配置-多语言表 tk_eafc_inspect_schema_l

- **表名称：** 四性检测配置-多语言表
- **表名：** tk_eafc_inspect_schema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_inspect_schema_l |  | fpkid |
