# 贸易术语-gtm_tradeterm

## 贸易术语-使用范围表 t_gtm_tradeterm_u

- **表名称：** 贸易术语-使用范围表
- **表名：** t_gtm_tradeterm_u

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
| 1 | pk_t_gtm_tradeterm_u |  | fdataid,fuseorgid |
| 2 | idx_t_gtm_tradeterm_u_uo |  | fuseorgid |

---

## 费用项目-多语言表 t_gtm_expenseitem_l

- **表名称：** 费用项目-多语言表
- **表名：** t_gtm_expenseitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | fexpenseitemdesc | 费用说明 | varchar | 399 |  | √ | ' ' | 费用说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_expenseitem_l |  | fpkid |
| 2 | idx_gtm_expenseitem_l_0 |  | fentryid,flocaleid |

---

## 贸易术语-多语言表 t_gtm_tradeterm_l

- **表名称：** 贸易术语-多语言表
- **表名：** t_gtm_tradeterm_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 770 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 术语说明 | varchar | 770 |  | √ | ' ' | 术语说明 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_tradeterm_l |  | fpkid |
| 2 | idx_gtm_tradeterm_l |  | fid,flocaleid |

---

## 贸易术语-主表 t_gtm_tradeterm

- **表名称：** 贸易术语-主表
- **表名：** t_gtm_tradeterm

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapproverid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [贸易术语分组 gtm_tradetermgroup](../gtm_files/gtm_tradetermgroup.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fintercormsver | 解释通则版本 | varchar | 50 |  | √ | ' ' | 解释通则版本,枚举: 1 :国际贸易术语解释通则 2000 2 :国际贸易术语解释通则 2010 3 :国际贸易术语解释通则 2020 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fapprovedate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 16 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcomment | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 20 | fenglishname | 英文名称 | varchar | 100 |  | √ | ' ' | 英文名称 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fdescription | 术语说明 | varchar | 512 |  | √ | ' ' | 术语说明 |
| 24 | fislogistics | 启用运输 | bpchar | 1 |  | √ | '0' | 启用运输 |
| 25 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 26 | fisintransit | 启用在途 | bpchar | 1 |  | √ | '0' | 启用在途 |
| 27 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 29 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gtm_tradeterm_master |  | fmasterid |
| 2 | idx_gtm_tradeterm |  | fnumber |
| 3 | idx_t_gtm_tradeterm_createorg |  | fcreateorgid |
| 4 | pk_gtm_tradeterm |  | fid |

---

## 费用项目-子表 t_gtm_expenseitem

- **表名称：** 费用项目-子表
- **表名：** t_gtm_expenseitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fexpenseitemdesc | 费用说明 | varchar | 255 |  | √ | ' ' | 费用说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtm_expenseitem |  | fentryid |
| 2 | idx_gtm_expenseitem_fk |  | fid |
