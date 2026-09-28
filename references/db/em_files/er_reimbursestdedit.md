# 报销标准-er_reimbursestdedit

## 标准明细-子表 t_er_reimbursestdentry

- **表名称：** 标准明细-子表
- **表名：** t_er_reimbursestdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frank | frank | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftriparea | 出差地域 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 6 | faccountable | faccountable | bpchar | 1 |  | √ | '0' |  |
| 7 | fstandardamount | 标准金额（0代表实报实销） | numeric | 28 | 10 | √ | 0.0000000000 | 标准金额（0代表实报实销） |
| 8 | faircraftcabin | 舱位 | varchar | 30 |  | √ | ' ' | 舱位,枚举: 1 :公务舱 2 :经济舱 3 :实报实销 |
| 9 | fseat | 座位 | varchar | 30 |  | √ | ' ' | 座位,枚举: 1 :一等座/软卧 2 :二等座/软卧 3 :二等座/硬卧 4 :实报实销 |
| 10 | fposition | 职位 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 11 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 12 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 13 | fberth | 铺位 | varchar | 30 |  | √ | ' ' | 铺位,枚举: 1 :卧铺 2 :实报实销 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_reimbursestdentry_pkey |  | fentryid |
| 2 | idx_er_rs_fseq |  | fid,fseq |

---

## 报销标准-主表 t_er_reimbursestd

- **表名称：** 报销标准-主表
- **表名：** t_er_reimbursestd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fcomment | 备注 | varchar | 255 |  |  | null | 备注 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcontrolmethod | 控制方法 | varchar | 25 |  | √ | ' ' | 控制方法,枚举: 0 :按年控制 1 :按季控制 2 :按月控制 3 :按天控制 4 :按人次控制 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fcontrolmode | 控制方式 | varchar | 25 |  | √ | ' ' | 控制方式,枚举: 0 :无控制 1 :严格控制 2 :提示且填写超标说明 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | fstatus | 数据状态 | varchar | 25 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 22 | fnormalsort | 标准分类 | varchar | 25 |  | √ | ' ' | 标准分类,枚举: 0 :职位 1 :职位+出差地域 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_rs_fnumber |  | fnumber |
| 2 | idx_t_er_reimbursestd_master |  | fmasterid |
| 3 | t_er_reimbursestd_pkey |  | fid |
| 4 | idx_t_er_reimbursestd_createorg |  | fcreateorgid |

---

## 报销标准-使用范围位图表 t_er_reimbursestd_m

- **表名称：** 报销标准-使用范围位图表
- **表名：** t_er_reimbursestd_m

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
| 1 | pk_t_er_reimbursestd_m |  | forgid |

---

## 报销标准-多语言表 t_er_reimbursestd_l

- **表名称：** 报销标准-多语言表
- **表名：** t_er_reimbursestd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_rbsl_fid |  | fid,flocaleid |
| 2 | t_er_reimbursestd_l_pkey |  | fpkid |

---

## 报销标准-使用范围表 t_er_reimbursestd_u

- **表名称：** 报销标准-使用范围表
- **表名：** t_er_reimbursestd_u

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
| 1 | t_er_reimbursestd_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_er_reimbursestd_u_uo |  | fuseorgid |
