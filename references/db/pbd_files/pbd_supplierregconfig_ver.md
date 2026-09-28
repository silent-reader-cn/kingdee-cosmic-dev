# 注册资料模板配置版本记录-pbd_supplierregconfig_ver

## 页签配置分录-子表 t_pbd_suppageconfig_tab

- **表名称：** 页签配置分录-子表
- **表名：** t_pbd_suppageconfig_tab

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftabname | 页签名称 | varchar | 255 |  | √ | ' ' | 页签名称 |
| 3 | ftabid | 页签控件id | varchar | 100 |  | √ | ' ' | 页签控件id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftabenable | 启用 | bpchar | 1 |  | √ | '1' | 启用 |
| 7 | ftabno | 页签标识 | varchar | 50 |  | √ | ' ' | 页签标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_suppageconfig_tab_fid |  | fid |
| 2 | pk_pbd_suppageconfig_tab |  | fentryid |

---

## 字段配置分录-子表 t_pbd_suppageconfig_field

- **表名称：** 字段配置分录-子表
- **表名：** t_pbd_suppageconfig_field

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flock | 锁定 | bpchar | 1 |  | √ | '0' | 锁定 |
| 2 | ffieldvisiblestatus | 字段可见状态 | varchar | 100 |  | √ | ' ' | 字段可见状态 |
| 3 | ffieldlockstatus | 字段锁定状态 | varchar | 100 |  | √ | ' ' | 字段锁定状态 |
| 4 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 5 | fvisible | 显示 | bpchar | 1 |  | √ | '0' | 显示 |
| 6 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 7 | ffieldno | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 11 | ffieldid | 字段控件id | varchar | 100 |  | √ | ' ' | 字段控件id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_suppageconfig_field |  | fdetailid |
| 2 | idx_pbd_pageconfig_feid_seq |  | fentryid,fseq |

---

## 注册资料模板配置版本记录-主表 t_pbd_supplierpageconfig

- **表名称：** 注册资料模板配置版本记录-主表
- **表名：** t_pbd_supplierpageconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcconfigid | 源调查表配置id | varchar | 80 |  | √ | ' ' | 源调查表配置id |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 10 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 11 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 12 | fversion | 版本号 | varchar | 50 |  | √ | '1' | 版本号 |
| 13 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 19 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 20 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: adm_supplierreg :注册 adm_questions :调查问卷 |
| 21 | fsyspreset | fsyspreset | bpchar | 1 |  | √ | '0' |  |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fversionstatus | 版本状态 | bpchar | 1 |  | √ | 'A' | 版本状态,枚举: A :当前版本 B :历史版本 |
| 24 | fnumber | 模板编码 | varchar | 80 |  | √ | ' ' | 模板编码 |
| 25 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 26 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_supplierpageconfig |  | fid |
| 2 | idx_pbd_suppageconfig_fnum |  | fnumber |
| 3 | idx_t_pbd_supplierpageconfig_createorg |  | fcreateorgid |
| 4 | idx_t_pbd_supplierpageconfig_master |  | fmasterid |

---

## 关联子实体-子表 t_pbd_suppageconfig_ver_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pbd_suppageconfig_ver_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_suppageconfig_ver_lk |  | fpkid |
| 2 | idx_pbd_suppageconfig_ver_lk_fk |  | fid |

---

## 注册资料模板配置版本记录-多语言表 t_pbd_supplierpageconfig_l

- **表名称：** 注册资料模板配置版本记录-多语言表
- **表名：** t_pbd_supplierpageconfig_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_suppageconfig_l_fidlid |  | fid,flocaleid |
| 2 | pk_pbd_supplierpageconfig_l |  | fpkid |

---

## 注册资料模板配置版本记录-使用范围表 t_pbd_supplierpageconfig_u

- **表名称：** 注册资料模板配置版本记录-使用范围表
- **表名：** t_pbd_supplierpageconfig_u

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
| 1 | idx_t_pbd_supplierpageconfig_u_uo |  | fuseorgid |
| 2 | pk_t_pbd_supplierpageconfig_u |  | fdataid,fuseorgid |

---

## 附件模板分录-子表 t_pbd_questionconfigatt

- **表名称：** 附件模板分录-子表
- **表名：** t_pbd_questionconfigatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmustprovide | 必须提供 | bpchar | 1 |  | √ | '0' | 必须提供 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fqualificationtypeid | 资质类型 | int8 | 64 |  | √ | 0 | [资质类型维护 bd_qualification_type](../basedata_files/bd_qualification_type.md) |
| 6 | fattdescribe | 附件描述 | varchar | 255 |  | √ | ' ' | 附件描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_questionconfigatt_fid |  | fid |
| 2 | pk_pbd_questionconfigatt |  | fentryid |

---

## 附件模板上传-附件表 t_pbd_questionattach

- **表名称：** 附件模板上传-附件表
- **表名：** t_pbd_questionattach

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [附件字段实体 bd_attachment](../frame_files/bd_attachment.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_questionattach |  | fpkid |
| 2 | idx_pbd_questionattach_fbdid |  | fbasedataid |
