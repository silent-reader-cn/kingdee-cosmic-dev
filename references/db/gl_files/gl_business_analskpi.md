# 财务指标-gl_business_analskpi

## 财务指标-多语言表 t_gl_analskpi_l

- **表名称：** 财务指标-多语言表
- **表名：** t_gl_analskpi_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmuliexpression | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_analskpi_l_pkey |  | fpkid |
| 2 | idx_gl_analskpi_l |  | fid,flocaleid |

---

## 财务指标-使用范围位图表 t_gl_analskpi_m

- **表名称：** 财务指标-使用范围位图表
- **表名：** t_gl_analskpi_m

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
| 1 | pk_t_gl_analskpi_m |  | forgid |

---

## 财务指标-使用范围表 t_gl_analskpi_u

- **表名称：** 财务指标-使用范围表
- **表名：** t_gl_analskpi_u

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
| 1 | idx_t_gl_analskpi_u_uo |  | fuseorgid |
| 2 | t_gl_analskpi_u_pkey |  | fdataid,fuseorgid |

---

## 财务指标-主表 t_gl_analskpi

- **表名称：** 财务指标-主表
- **表名：** t_gl_analskpi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdesp | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fmuliexpression | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 11 | ftradestandard | 行业标准值 | numeric | 19 | 6 | √ | 0.000000 | 行业标准值 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | freporttype | 报表类型 | varchar | 50 |  | √ | ' ' | 报表类型,枚举: balancesheet :资产负债表 income :利润表 taxshow :企业纳税表 cashflow :现金流量表 |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 18 | fexpression | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: |
| 21 | fkpitype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 1 :系统预置 2 :自定义 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 24 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_gl_analskpi_master |  | fmasterid |
| 2 | idx_gl_analskpi |  | fnumber |
| 3 | t_gl_analskpi_pkey |  | fid |
| 4 | idx_t_gl_analskpi_createorg |  | fcreateorgid |
