# 关联关系认定表-theme_rdetermination_bill

## 关联关系认定表-主表 t_theme_rdetermination

- **表名称：** 关联关系认定表-主表
- **表名：** t_theme_rdetermination

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | frtransacttype | frtransacttype | int8 | 64 |  | √ | 0 |  |
| 8 | fipoorgid | IPO主体 | int8 | 64 |  | √ | 0 | [IPO编制组织 ipo_org](../ipobase_files/ipo_org.md) |
| 9 | frtransacttypeld | 关联关系类型 | int8 | 64 |  | √ | 0 | [关联关系类型 theme_rtransact_type](../ipobase_files/theme_rtransact_type.md) |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | ftransactioncontent | 关联交易内容 | int8 | 64 |  | √ | 0 | [关联交易内容 theme_transaction_content](../ipobase_files/theme_transaction_content.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '7' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fcontacttype | 内容类型 | varchar | 50 |  | √ | ' ' | 内容类型,枚举: 0 :客户 1 :员工 2 :供应商 3 :行政组织 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 18 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 19 | fisaffiliate | 是否关联方 | bpchar | 1 |  | √ | '1' | 是否关联方 |
| 20 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 21 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 23 | fbillno | fbillno | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_theme_rdetermination |  | fid |
| 2 | idx_t_theme_rdetermination_createorg |  | fcreateorgid |
| 3 | idx_t_theme_rdetermination_master |  | fmasterid |
| 4 | idx_rdetermination_name |  | fname |

---

## 关联关系认定表-多语言表 t_theme_rdetermination_l

- **表名称：** 关联关系认定表-多语言表
- **表名：** t_theme_rdetermination_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rdetermination_lname |  | flocaleid,fname |
| 2 | pk_theme_rdetermination_l |  | fpkid |

---

## 关联关系认定表-使用范围表 t_theme_rdetermination_u

- **表名称：** 关联关系认定表-使用范围表
- **表名：** t_theme_rdetermination_u

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
| 1 | idx_t_theme_rdetermination_u_uo |  | fuseorgid |
| 2 | pk_t_theme_rdetermination_u |  | fdataid,fuseorgid |
