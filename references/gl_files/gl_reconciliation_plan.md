# 集团交易对账方案-gl_reconciliation_plan

## 集团交易对账方案-主表 t_gl_acccheck

- **表名称：** 集团交易对账方案-主表
- **表名：** t_gl_acccheck

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcurrency | 对账币别 | varchar | 30 |  | √ | ' ' | 对账币别,枚举: |
| 9 | fcurrencytext | 对账币别 | varchar | 30 |  | √ | ' ' | 对账币别 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '0' | 控制策略,枚举: |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | '0' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | foppositecourseid | 对方科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcourseid | 本方科目表 | int8 | 64 |  | √ | 0 | 科目表 bd_accounttable |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 23 | fcombofield | 对账类型 | varchar | 30 |  | √ | ' ' | 对账类型,枚举: A :科目对账 B :现金流量对账 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gl_acccheck_master |  | fmasterid |
| 2 | pk_t_gl_acccheck |  | fid |
| 3 | idx_t_gl_acccheck_createorg |  | fcreateorgid |
| 4 | idx_gl_acccheck_index |  | fuseorg |

---

## 集团交易对账方案-使用范围表 t_gl_acccheck_u

- **表名称：** 集团交易对账方案-使用范围表
- **表名：** t_gl_acccheck_u

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
| 1 | idx_t_gl_acccheck_u_uo |  | fuseorgid |
| 2 | pk_t_gl_acccheck_u |  | fdataid,fuseorgid |

---

## 集团交易对账方案-使用范围位图表 t_gl_acccheck_m

- **表名称：** 集团交易对账方案-使用范围位图表
- **表名：** t_gl_acccheck_m

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
| 1 | pk_t_gl_acccheck_m |  | forgid |

---

## 集团交易对账方案-多语言表 t_gl_acccheck_l

- **表名称：** 集团交易对账方案-多语言表
- **表名：** t_gl_acccheck_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_acccheck_l |  | fid,flocaleid |
| 2 | pk_t_gl_acccheck_l |  | fpkid |

---

## 单据体-子表 t_gl_acccheckentry

- **表名称：** 单据体-子表
- **表名：** t_gl_acccheckentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountdimensionbxid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 3 | faccesstypes | 取数类型 | varchar | 30 |  | √ | ' ' | 取数类型,枚举: 4 :本期发生额 5 :本年累计发生额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fcoursesid | 本方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 6 | faccountdimensionbkid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 7 | foppositecashflowid | 对方现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 8 | fcashflowid | 本方现金流量项目 | int8 | 64 |  | √ | 0 | 现金流量项目 gl_cashflowitem |
| 9 | foppositecoursesid | 对方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 10 | faccountdimensiondkid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 11 | faccesstype | 取数类型 | varchar | 30 |  | √ | ' ' | 取数类型,枚举: 1 :期初余额 2 :本期发生额 3 :期末余额 |
| 12 | faccountdimensiondxid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gl_acccheckentry |  | fentryid |
| 2 | idx_gl_acccheckentry_fid |  | fid |
