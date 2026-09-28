# 组卷方案配置-eafc_autovolume_scheme

## 组卷方案配置-主表 tk_eafc_autovolume_sche

- **表名称：** 组卷方案配置-主表
- **表名：** tk_eafc_autovolume_sche

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | fname | varchar | 50 |  |  | null |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 8 | fk_eafc_is_pack_box_vol | 按卷自动预装盒 | bpchar | 1 |  | √ | '0' | 按卷自动预装盒 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 8 :按分配组织 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fk_eafc_is_auto_pack_vol | 在线接收自动组卷 | bpchar | 1 |  | √ | '0' | 在线接收自动组卷 |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 是否启用 | varchar | 50 |  | √ | ' ' | 是否启用,枚举: 0 :否 1 :是 |
| 19 | fk_eafc_useorg | 所属组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 21 | fk_eafc_business_type | 适用分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_eafc_autovolume_sche_master |  | fmasterid |
| 2 | idx_tk_eafc_autovolume_sche_createorg |  | fcreateorgid |
| 3 | pk__tk_eafc_autovolume_sche |  | fid |

---

## 明细维度单据体-子表 tk_eafc_autovolsc_ruson_e

- **表名称：** 明细维度单据体-子表
- **表名：** tk_eafc_autovolsc_ruson_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fk_eafc_auto_combo | 下拉列表 | varchar | 50 |  | √ | ' ' | 下拉列表,枚举: |
| 2 | fk_eafc_auto_date | 日期 | timestamp | 0 |  |  | null | 日期 |
| 3 | fk_eafc_arch_field_det | 维度内容 | varchar | 50 |  | √ | ' ' | 维度内容 |
| 4 | fk_eafc_auto_use_field | 使用字段 | varchar | 50 |  | √ | ' ' | 使用字段 |
| 5 | fk_eafc_auto_text | 文本 | varchar | 50 |  | √ | ' ' | 文本 |
| 6 | fk_eafc_auto_decimal | 小数 | numeric | 23 | 10 |  | null | 小数 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fk_eafc_auto_yeardate | 日期(年度) | timestamp | 0 |  |  | null | 日期(年度) |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fk_eafc_auto_int | 整数 | int4 | 32 |  | √ | 0 | 整数 |
| 12 | fk_eafc_auto_datetime | 长日期 | timestamp | 0 |  |  | null | 长日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__tk_eafc_autovolsc_ruson_e |  | fdetailid |

---

## 组卷方案配置-使用范围表 tk_eafc_autovolume_sche_u

- **表名称：** 组卷方案配置-使用范围表
- **表名：** tk_eafc_autovolume_sche_u

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
| 1 | idx_tk_eafc_autovolume_sche_u_uo |  | fuseorgid |
| 2 | tk_eafc_autovolume_sche_u_pkey |  | fdataid,fuseorgid |

---

## 排序单据体-子表 tk_eafc_autovolsche_soent

- **表名称：** 排序单据体-子表
- **表名：** tk_eafc_autovolsche_soent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_eafc_so_field | 卷内字段 | varchar | 50 |  | √ | ' ' | 卷内字段,枚举: |
| 3 | fk_eafc_so_priority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: 1 :1 2 :2 3 :3 4 :4 |
| 4 | fk_eafc_so_sort_rule | 排序规则 | varchar | 50 |  | √ | ' ' | 排序规则,枚举: asc :升序 desc :降序 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__tk_eafc_autovolsche_soent |  | fentryid |

---

## 组卷方案配置-多语言表 tk_eafc_autovolume_sche_l

- **表名称：** 组卷方案配置-多语言表
- **表名：** tk_eafc_autovolume_sche_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | pk__tk_eafc_autovolume_sche_l |  | fpkid |

---

## 单据体-子表 tk_eafc_autovolsche_ruent

- **表名称：** 单据体-子表
- **表名：** tk_eafc_autovolsche_ruent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_set_manual_rule | 设为手工规则 | bpchar | 1 |  | √ | '0' | 设为手工规则 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fk_eafc_arch_field | 维度内容 | varchar | 50 |  | √ | ' ' | 维度内容,枚举: |
| 5 | fk_set_control_rule | 设为自动规则 | bpchar | 1 |  | √ | '1' | 设为自动规则 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fk_eafc_arch_detail | 自动条件明细值 | varchar | 1000 |  | √ | ' ' | 自动条件明细值 |
| 8 | fk_eafc_arch_condition | 自动规则条件 | varchar | 50 |  | √ | ' ' | 自动规则条件,枚举: 1 :任一 2 :等于 3 :不等于 |
| 9 | fk_eafc_arch_type | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型,枚举: 1 :业务 2 :档案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__tk_eafc_autovolsche_ruent |  | fentryid |

---

## 分配组织单据体-子表 tk_eafc_autovolsche_org

- **表名称：** 分配组织单据体-子表
- **表名：** tk_eafc_autovolsche_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fk_arc_org | 归档组织 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_eafc_autovolsche_org_fk |  | fentryid |
