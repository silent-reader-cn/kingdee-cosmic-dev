# 字段控制设置-er_bill_setting

## 单据体-多语言表 t_er_bill_setting_entry_l

- **表名称：** 单据体-多语言表
- **表名：** t_er_bill_setting_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdiyname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_billsetting_fid |  | fentryid |
| 2 | pk_t_er_bill_setting_entry_l |  | fpkid |

---

## 字段控制设置-主表 t_er_bill_setting

- **表名称：** 字段控制设置-主表
- **表名：** t_er_bill_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 单据类型 | int8 | 64 |  | √ | 0 | 单据设置 er_setting_group |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fispreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 25 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | ffastreimburse | 向导式发起 | bpchar | 1 |  | √ | '0' | 向导式发起 |
| 13 | fpicturefield | 图标url | varchar | 255 |  | √ | ' ' | 图标url |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fname | 名称 | varchar | 255 |  |  | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fformtitle | 表单标题 | varchar | 50 |  | √ | ' ' | 表单标题 |
| 20 | freimbursetype | 报账类型 | varchar | 50 |  | √ | ' ' | 报账类型,枚举: |
| 21 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | 业务事项 er_standard_type |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 25 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_billset_group |  | fgroupid |
| 2 | idx_t_er_bill_setting_master |  | fmasterid |
| 3 | idx_t_er_bill_setting_createorg |  | fcreateorgid |
| 4 | pk_t_er_bill_setting |  | fid |

---

## 单据体-子表 t_er_bill_setting_entry

- **表名称：** 单据体-子表
- **表名：** t_er_bill_setting_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flock | 锁定 | bpchar | 1 |  |  | '0' | 锁定 |
| 3 | flockconditionjson_tag | 锁定条件json_详情 | text | 0 |  |  | ' ' | 锁定条件json_详情 |
| 4 | ffieldname | 字段 | varchar | 50 |  |  | ' ' | 字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdiyname | 显示名称 | varchar | 50 |  |  | ' ' | 显示名称 |
| 7 | flockconditionexpr_tag | 锁定条件解析式_详情 | text | 0 |  |  | ' ' | 锁定条件解析式_详情 |
| 8 | ffieldnumber | 字段标识 | varchar | 50 |  |  | ' ' | 字段标识 |
| 9 | flockcondition | 锁定条件 | varchar | 1024 |  |  | ' ' | 锁定条件 |
| 10 | fmustinput | 必录 | bpchar | 1 |  |  | '0' | 必录 |
| 11 | flockconditionexpr | 锁定条件解析式 | varchar | 255 |  | √ | ' ' | 锁定条件解析式 |
| 12 | ffieldtype | 类型 | varchar | 10 |  |  | ' ' | 类型,枚举: field :字段 entry :单据体 |
| 13 | fhidden | 可见 | bpchar | 1 |  |  | '0' | 可见 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | flockconditionjson | 锁定条件json | varchar | 255 |  | √ | ' ' | 锁定条件json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_settingentry_fid |  | fid |
| 2 | pk_t_er_bill_setting_entry |  | fentryid |

---

## 字段控制设置-多语言表 t_er_bill_setting_l

- **表名称：** 字段控制设置-多语言表
- **表名：** t_er_bill_setting_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fformtitle | 表单标题 | varchar | 100 |  | √ | ' ' | 表单标题 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_bill_setting_l |  | fpkid |
| 2 | idx_setting_l_fid |  | fid |

---

## 字段控制设置-使用范围表 t_er_bill_setting_u

- **表名称：** 字段控制设置-使用范围表
- **表名：** t_er_bill_setting_u

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
| 1 | idx_t_er_bill_setting_u_uo |  | fuseorgid |
| 2 | pk_t_er_bill_setting_u |  | fdataid,fuseorgid |
