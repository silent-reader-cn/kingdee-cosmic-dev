# 存储方案-plm_plmdc_storage_scheme

## 组织-子表 t_plmdc_electron_org

- **表名称：** 组织-子表
- **表名：** t_plmdc_electron_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_electron_org_fk |  | fid |
| 2 | pk_t_plmdc_electron_org |  | fentryid |

---

## 存储方案-多语言表 t_plmdc_storage_scheme_l

- **表名称：** 存储方案-多语言表
- **表名：** t_plmdc_storage_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmdc_storage_scheme_l_0 |  | fid,flocaleid |
| 2 | pk_plmdc_storage_scheme_l |  | fpkid |

---

## 存储方案-使用范围表 t_plmdc_storage_scheme_u

- **表名称：** 存储方案-使用范围表
- **表名：** t_plmdc_storage_scheme_u

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
| 1 | pk_t_plmdc_storage_scheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_plmdc_storage_scheme_u_uo |  | fuseorgid |

---

## 存储方案-主表 t_plmdc_storage_scheme

- **表名称：** 存储方案-主表
- **表名：** t_plmdc_storage_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | fappsecret | varchar | 50 |  | √ | ' ' |  |
| 3 | fservernumber | fservernumber | varchar | 50 |  | √ | ' ' |  |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmainwarehouse | 是否主仓 | varchar | 50 |  | √ | ' ' | 是否主仓,枚举: 1 :是 0 :否 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fstoragetype | 存储方式 | varchar | 50 |  | √ | ' ' | 存储方式,枚举: A :仅云端存储 B :仅本地存储 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | flocalserver | 服务器名称 | int8 | 64 |  | √ | 0 | [服务器配置 plm_plmdc_fs_cfg](../plmdc_files/plm_plmdc_fs_cfg.md) |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int4 | 32 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fstoragedoclist | 存储文档类型列表 | varchar | 255 |  | √ | ' ' | 存储文档类型列表 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fappkey | fappkey | varchar | 50 |  | √ | ' ' |  |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fstart | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 23 | fcloudserver | 服务器名称 | int8 | 64 |  | √ | 0 | [服务器配置 plm_plmdc_fs_cfg](../plmdc_files/plm_plmdc_fs_cfg.md) |
| 24 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fstoragedoclist_tag | 存储文档类型列表_详情 | text | 0 |  |  | null | 存储文档类型列表_详情 |
| 26 | fserveraddress | fserveraddress | varchar | 50 |  | √ | ' ' |  |
| 27 | fservernumber1 | fservernumber1 | varchar | 50 |  | √ | ' ' |  |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 30 | fserverport | fserverport | varchar | 50 |  | √ | ' ' |  |
| 31 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plmdc_storage_scheme_master |  | fmasterid |
| 2 | idx_t_plmdc_storage_scheme_createorg |  | fcreateorgid |
| 3 | idx_plmdc_storage_scheme_no |  | fnumber |
| 4 | pk_plmdc_storage_scheme |  | fid |
