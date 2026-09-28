# 执照-fmm_license

## 执照-主表 t_fmm_license

- **表名称：** 执照-主表
- **表名：** t_fmm_license

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | femployeeid | 员工工号 | int8 | 64 |  | √ | 0 | 企业人力资源池 pmbd_enterprise_hm_res_po |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | flicensetypeid | 执照类型 | int8 | 64 |  | √ | 0 | 执照类型 fmm_license_type |
| 8 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpermanent | 永久有效 | bpchar | 1 |  | √ | '0' | 永久有效 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fexpiredate | 有效截止日期 | timestamp | 0 |  |  | null | 有效截止日期 |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fissuedate | 发照日期 | timestamp | 0 |  |  | null | 发照日期 |
| 20 | fissuer | 签发人 | varchar | 50 |  | √ | ' ' | 签发人 |
| 21 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fissueauthority | 发证机关 | varchar | 50 |  | √ | ' ' | 发证机关 |
| 23 | fqrcode | 二维码号 | varchar | 255 |  | √ | ' ' | 二维码号 |
| 24 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fauthtypeid | 类别 | int8 | 64 |  | √ | 0 | 授权类别 fmm_authorizecategory |
| 26 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 27 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fenglishlevelid | 英语等级 | int8 | 64 |  | √ | 0 | 英语等级 fmm_english_level |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_license_createorg |  | fcreateorgid |
| 2 | idx_t_fmm_license_master |  | fmasterid |
| 3 | pk_fmm_license |  | fid |
| 4 | idx_fmm_licese_fnumber |  | fnumber |
| 5 | idx_fmm_licese_fcreatetime |  | fcreatetime |

---

## 签署机型-子表 t_fmm_signedentry

- **表名称：** 签署机型-子表
- **表名：** t_fmm_signedentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsignedauthority | 签署机关 | varchar | 50 |  | √ | ' ' | 签署机关 |
| 3 | fenginemodelid | 发动机型号 | int8 | 64 |  | √ | 0 | 发动机型号 mpdm_enginetype |
| 4 | fmodelid | 机型 | int8 | 64 |  | √ | 0 | 检修设备型号 mpdm_over_device_number |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 7 | fsignremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsigneddate | 签署日期 | timestamp | 0 |  |  | null | 签署日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_signedentry |  | fentryid |
| 2 | idx_fmm_signry_fid |  | fid |
| 3 | idx_fmm_signry_fseq |  | fseq |

---

## 执照-使用范围表 t_fmm_license_u

- **表名称：** 执照-使用范围表
- **表名：** t_fmm_license_u

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
| 1 | pk_t_fmm_license_u |  | fdataid,fuseorgid |
| 2 | idx_t_fmm_license_u_uo |  | fuseorgid |

---

## 执照-使用范围位图表 t_fmm_license_m

- **表名称：** 执照-使用范围位图表
- **表名：** t_fmm_license_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fmm_license_m |  | forgid |

---

## 执照-多语言表 t_fmm_license_l

- **表名称：** 执照-多语言表
- **表名：** t_fmm_license_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_license_l |  | fpkid |
| 2 | idx_fmm_licesel_fid |  | fid,flocaleid |

---

## 颁发记录-子表 t_fmm_issueentry

- **表名称：** 颁发记录-子表
- **表名：** t_fmm_issueentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fissueday | 颁发日期 | timestamp | 0 |  |  | null | 颁发日期 |
| 3 | fissueby | 颁发人 | varchar | 50 |  | √ | ' ' | 颁发人 |
| 4 | faddtypeid | 增加类别 | int8 | 64 |  | √ | 0 | 授权类别 fmm_authorizecategory |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_issury_fid |  | fid |
| 2 | idx_fmm_issury_fseq |  | fseq |
| 3 | pk_fmm_issueentry |  | fentryid |
