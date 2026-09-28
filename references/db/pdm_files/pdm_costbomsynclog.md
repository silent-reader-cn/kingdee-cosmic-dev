# 成本同步日志查询-pdm_costbomsynclog

## 成本同步日志查询-主表 t_pdm_costbomsynclog

- **表名称：** 成本同步日志查询-主表
- **表名：** t_pdm_costbomsynclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmoduler | 功能模块 | varchar | 50 |  | √ | ' ' | 功能模块,枚举: pdm_mftbom :BOM维护 pdm_eco :工程变更单 pdm_route :工艺路线维护 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | freason | 失败原因 | text | 0 |  |  | null | 失败原因 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 12 | fstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 0 :执行成功 1 :执行失败 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | freason_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 21 | fbillno | 单据编码 | text | 0 |  |  | null | 单据编码 |
| 22 | fcombofield | fcombofield | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_costbomsynclog |  | fid |
| 2 | idx_t_pdm_costbomsynclog_master |  | fmasterid |
| 3 | idx_t_pdm_costbomsynclog_createorg |  | fcreateorgid |

---

## 成本同步日志查询-使用范围表 t_pdm_costbomsynclog_u

- **表名称：** 成本同步日志查询-使用范围表
- **表名：** t_pdm_costbomsynclog_u

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
| 1 | idx_t_pdm_costbomsynclog_u_uo |  | fuseorgid |
| 2 | pk_t_pdm_costbomsynclog_u |  | fdataid,fuseorgid |

---

## 成本同步日志查询-使用范围位图表 t_pdm_costbomsynclog_m

- **表名称：** 成本同步日志查询-使用范围位图表
- **表名：** t_pdm_costbomsynclog_m

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
| 1 | pk_t_pdm_costbomsynclog_m |  | forgid |

---

## 成本同步日志查询-多语言表 t_pdm_costbomsynclog_l

- **表名称：** 成本同步日志查询-多语言表
- **表名：** t_pdm_costbomsynclog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 128 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 32 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 32 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pdm_costbomsynclog_l |  | fpkid |
| 2 | idx_t_pdm_costbomsynclog_l |  | fid,flocaleid |
