# 工作量批量新增-fa_workload_batch

## 工作量批量新增-多语言表 t_fa_workload_l

- **表名称：** 工作量批量新增-多语言表
- **表名：** t_fa_workload_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 工作量批量新增-使用范围表 t_fa_workload_u

- **表名称：** 工作量批量新增-使用范围表
- **表名：** t_fa_workload_u

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
| 1 | idx_t_fa_workload_u_uo |  | fuseorgid |
| 2 | pk_t_fa_workload_u |  | fdataid,fuseorgid |

---

## 工作量批量新增-主表 t_fa_workload

- **表名称：** 工作量批量新增-主表
- **表名：** t_fa_workload

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fperiodid | fperiodid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | frealcardid | frealcardid | int8 | 64 |  | √ | 0 |  |
| 11 | fassetbookid | fassetbookid | int8 | 64 |  | √ | 0 |  |
| 12 | fpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 xkbd_policy |
| 13 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 19 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 20 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 21 | fdepreuseid | fdepreuseid | int8 | 64 |  | √ | 0 |  |
| 22 | fworkload | fworkload | numeric | 19 | 6 | √ | 0.000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_workload_pkey |  | fid |
| 2 | idx_fa_workload |  | forgid |
| 3 | idx_t_fa_workload_createorg |  | fcreateorgid |
