# 归档范围设置-eafc_category_edit

## 归档范围设置-主表 tk_eafc_category_mana_ent

- **表名称：** 归档范围设置-主表
- **表名：** tk_eafc_category_mana_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 父单据内码 | int8 | 64 |  | √ | null | 父单据内码 |
| 2 | fk_eafc_cata_show | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 3 | fk_eafc_category_descri | 分类描述 | varchar | 50 |  | √ | ' ' | 分类描述 |
| 4 | fk_fpy_check_business | fk_fpy_check_business | bpchar | 1 |  | √ | '0' |  |
| 5 | fk_eafc_manager_dime | fk_eafc_manager_dime | varchar | 50 |  | √ | ' ' |  |
| 6 | fk_eafc_is_alone_box | 是否启用纸档管理 | bpchar | 1 |  | √ | '0' | 是否启用纸档管理 |
| 7 | fk_eafc_open_log | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 8 | fk_eafc_catalogue | 所属目录号 | varchar | 50 |  | √ | ' ' | 所属目录号 |
| 9 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 10 | fk_eafc_usestatus | fk_eafc_usestatus | varchar | 50 |  | √ | ' ' |  |
| 11 | fk_eafc_updatetime | fk_eafc_updatetime | timestamp | 0 |  |  | null |  |
| 12 | fk_eafc_category_code | 类别代码 | varchar | 50 |  | √ | ' ' | 类别代码 |
| 13 | fk_eafc_file_digit | 组件位制(档号) | varchar | 50 |  | √ | ' ' | 组件位制(档号),枚举: 5 :万位 6 :十万位 7 :百万位 8 :千万位 9 :亿位 |
| 14 | fk_eafc_is_manager | 是否启用管理方式 | varchar | 50 |  | √ | ' ' | 是否启用管理方式,枚举: 1 :是 2 :否 |
| 15 | fk_eafc_category_level | fk_eafc_category_level | varchar | 50 |  | √ | ' ' |  |
| 16 | fparententryid | 父节点内码 | int8 | 64 |  | √ | 0 | 父节点内码 |
| 17 | fk_eafc_category_type | 类别层级 | varchar | 50 |  | √ | ' ' | 类别层级,枚举: eafc_archive_type :门类(一级类别） eafc_category :类别(二级类别) eafc_business_type :类型(三级类别) |
| 18 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 19 | fk_eafc_isseparate | 允许独立归档 | bpchar | 1 |  | √ | '0' | 允许独立归档 |
| 20 | feafc_dimension | 自动生成维度 | varchar | 50 |  | √ | '0' | 自动生成维度,枚举: 0 :按批次归档 |
| 21 | fk_eafc_aggregation_level | 聚合层次组 | varchar | 50 |  | √ | ' ' | 聚合层次组,枚举: 1 :案卷 2 :文件 |
| 22 | fk_eafc_paper_manage_mode | 实物管理模式 | varchar | 50 |  | √ | ' ' | 实物管理模式,枚举: 1 :按卷装盒模式 2 :按件装盒模式 |
| 23 | feafc_archived_generate | 保管清册生成方式 | varchar | 50 |  | √ | '0' | 保管清册生成方式,枚举: 0 :自动 1 :手动 2 :不生成 |
| 24 | fk_eafc_volume_digit | 案卷位制(档号) | varchar | 50 |  | √ | ' ' | 案卷位制(档号),枚举: 4 :千位 5 :万位 6 :十万位 7 :百万位 |
| 25 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 26 | fk_eafc_createtime_str | fk_eafc_createtime_str | varchar | 50 |  | √ | ' ' |  |
| 27 | fk_eafc_cycle | 归档周期 | varchar | 50 |  | √ | ' ' | 归档周期,枚举: 1 :一个月 2 :一季度 3 :半年 4 :年 |
| 28 | fk_eafc_category | 分类 | int8 | 64 |  |  | null | 档案类型（一级） eafc_archive_type |
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
