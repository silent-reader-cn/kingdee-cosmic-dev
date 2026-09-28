# 合并方案-xkcr_scopetype

## 合并方案-主表 t_xkcr_scopetype

- **表名称：** 合并方案-主表
- **表名：** t_xkcr_scopetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fconsolidationmode | 权益核算 | bpchar | 1 |  | √ | ' ' | 权益核算,枚举: 0 :统一在控股组织核算 1 :按股权关系核算 |
| 5 | facctsysid | 核算体系 | int8 | 64 |  | √ | 0 | 核算体系 xkbd_accountingsys |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fchangereason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | facctcalendarid | 会计日历 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | facctpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 13 | fislastedversion | 是否最新版本 | bpchar | 1 |  | √ | ' ' | 是否最新版本 |
| 14 | fbasecurrencyid | 主币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 15 | fversiongroupid | 版本id | int8 | 64 |  | √ | 0 | 版本id |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 21 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 22 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fversion | 变更版本 | int8 | 64 |  | √ | 0 | 变更版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_scopetype |  | fid |
| 2 | idx_xkcr_scopetype_vgid |  | fversiongroupid |

---

## 合并范围-子表 t_xkcr_scopehis

- **表名称：** 合并范围-子表
- **表名：** t_xkcr_scopehis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscopeparent | 父级范围 | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |
| 3 | fpid | fpid | int8 | 64 |  | √ | 0 | pid |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fscope | 范围 | int8 | 64 |  | √ | 0 | 合并范围 xkcr_scope |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_scopehis |  | fentryid |
| 2 | idx_xkcr_scopehis_fid |  | fid |

---

## 组织结构-子表 t_xkcr_company

- **表名称：** 组织结构-子表
- **表名：** t_xkcr_company

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcompany | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fisctrcompany | 是否控股 | bpchar | 1 |  | √ | ' ' | 是否控股,枚举: 1 :是 0 :否 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_company |  | fdetailid |
| 2 | idx_xkcr_company_fentryid |  | fentryid |

---

## 合并方案-多语言表 t_xkcr_scopetype_l

- **表名称：** 合并方案-多语言表
- **表名：** t_xkcr_scopetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fchangereason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_scopetype_l_fid |  | fid,flocaleid |
| 2 | pk_xkcr_scopetype_l |  | fpkid |
