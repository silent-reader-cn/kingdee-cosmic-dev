# 归档范围设置-eafc_category_manager

## 归档范围设置-主表 tk_eafc_category_manager

- **表名称：** 归档范围设置-主表
- **表名：** tk_eafc_category_manager

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fk_eafc_useorg | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_category_manager |  | fid |
| 2 | idx_tk_eafc_category_manager_createorg |  | fcreateorgid |
| 3 | idx_tk_eafc_category_manager_master |  | fmasterid |

---

## 树形单据体-子表 tk_eafc_category_mana_ent

- **表名称：** 树形单据体-子表
- **表名：** tk_eafc_category_mana_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_cata_show | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 3 | fk_eafc_category_descri | 类别号描述 | varchar | 50 |  | √ | ' ' | 类别号描述 |
| 4 | fk_fpy_check_business | 自定义分类 | bpchar | 1 |  | √ | '0' | 自定义分类 |
| 5 | fk_eafc_manager_dime | 管理维度 | varchar | 50 |  | √ | ' ' | 管理维度,枚举: 1 :全局共享 |
| 6 | fk_eafc_is_alone_box | 是否启用纸档管理 | bpchar | 1 |  | √ | '0' | 是否启用纸档管理 |
| 7 | fk_eafc_open_log | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 8 | fk_eafc_catalogue | 所属目录 | varchar | 50 |  | √ | ' ' | 所属目录 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fk_eafc_usestatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :在用 2 :未用 |
| 11 | fk_eafc_updatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 12 | fk_eafc_category_code | 类别代码 | varchar | 50 |  | √ | ' ' | 类别代码 |
| 13 | fk_eafc_file_digit | 组件位制 | varchar | 50 |  | √ | ' ' | 组件位制,枚举: 5 :万位 6 :十万位 7 :百万位 8 :千万位 9 :亿位 |
| 14 | fk_eafc_is_manager | 是否启用管理方式 | varchar | 50 |  | √ | ' ' | 是否启用管理方式,枚举: 1 :是 2 :否 |
| 15 | fk_eafc_category_level | 分类级别 | varchar | 50 |  | √ | ' ' | 分类级别,枚举: 1 :一级类别 2 :二级类别 3 :三级类别 |
| 16 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 17 | fk_eafc_category_type | 类别层级 | varchar | 50 |  | √ | ' ' | 类别层级,枚举: eafc_archive_type :一级类别 eafc_category :二级类别 eafc_business_type :三级类别 |
| 18 | fk_eafc_storage_period | 保管年限 | varchar | 50 |  | √ | ' ' | 保管年限,枚举: 1 :10年 2 :30年 3 :永久 |
| 19 | fk_eafc_isseparate | 允许独立归档 | bpchar | 1 |  | √ | '0' | 允许独立归档 |
| 20 | feafc_dimension | feafc_dimension | varchar | 50 |  | √ | '0' |  |
| 21 | fk_eafc_aggregation_level | 聚合层次 | varchar | 50 |  | √ | ' ' | 聚合层次,枚举: 1 :案卷 2 :文件 |
| 22 | fk_eafc_paper_manage_mode | 实物管理模式 | varchar | 50 |  | √ | ' ' | 实物管理模式,枚举: 1 :按卷装盒模式 2 :按件装盒模式 |
| 23 | feafc_archived_generate | 保管清册生成方式 | varchar | 50 |  | √ | '0' | 保管清册生成方式,枚举: 0 :自动 1 :手动 2 :不生成 |
| 24 | fk_eafc_volume_digit | 案卷位制 | varchar | 50 |  | √ | ' ' | 案卷位制,枚举: 4 :千位 5 :万位 6 :十万位 7 :百万位 |
| 25 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 26 | fk_eafc_createtime_str | 创建时间 | varchar | 50 |  | √ | ' ' | 创建时间 |
| 27 | fk_eafc_cycle | 周期 | varchar | 50 |  | √ | ' ' | 周期,枚举: 1 :一个月 2 :一季度 3 :半年 4 :年 |
| 28 | fk_eafc_category | 类别 | int8 | 64 |  |  | null | 档案类型（一级） eafc_archive_type |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_category_mana_ent_fk |  | fid |
| 2 | pk__eafc_category_mana_ent |  | fentryid |

---

## 归档范围设置-使用范围表 tk_eafc_category_manager_u

- **表名称：** 归档范围设置-使用范围表
- **表名：** tk_eafc_category_manager_u

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
| 1 | pk_eafc_category_manager_u |  | fdataid,fuseorgid |

---

## 归档范围设置-多语言表 tk_eafc_category_manager_l

- **表名称：** 归档范围设置-多语言表
- **表名：** tk_eafc_category_manager_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_category_manager_l |  | fpkid |
