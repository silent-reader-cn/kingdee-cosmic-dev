# 供应组织分配运算-mds_dpsplanexec

## 供应组织分配运算-主表 t_mds_dpsplanexec

- **表名称：** 供应组织分配运算-主表
- **表名：** t_mds_dpsplanexec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | frepeat | 重复运算 | bpchar | 1 |  | √ | '0' | 重复运算 |
| 5 | fcalculatepro | 计算进度 | int8 | 64 |  | √ | 0 | 计算进度 |
| 6 | fpredtime | 预约时间 | int8 | 64 |  | √ | 0 | 预约时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdpssiteschemeid | 供应组织分配方案 | int8 | 64 |  | √ | 0 | [供应组织分配方案定义 mds_siteschemedef](../mds_files/mds_siteschemedef.md) |
| 9 | frunningtype | 运行时间类型 | varchar | 50 |  | √ | ' ' | 运行时间类型,枚举: |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fplanid | 计划号 | varchar | 50 |  | √ | ' ' | 计划号 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :计划 C :关闭 |
| 13 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | fsummin | 计算总时长（秒） | int8 | 64 |  | √ | 0 | 计算总时长（秒） |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fdaysofmon | 月 | varchar | 100 |  | √ | ' ' | 月 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fprocesscount | 进度总数 | int8 | 64 |  | √ | 0 | 进度总数 |
| 21 | fdaysofweek | 周 | varchar | 50 |  | √ | ' ' | 周 |
| 22 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fjobid | 作业号 | varchar | 50 |  | √ | ' ' | 作业号 |
| 26 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | frepeattype | 时间重复类型 | varchar | 50 |  | √ | ' ' | 时间重复类型,枚举: |
| 28 | fstartdate | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 29 | fenable | 计算状态 | varchar | 50 |  | √ | ' ' | 计算状态,枚举: A :待运算 B :运算中 C :完成 D :异常 E :终止 |
| 30 | fnumber | 计算请求ID | varchar | 30 |  | √ | ' ' | 计算请求ID |
| 31 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_dpsplanexec |  | fid |
| 2 | idx_t_mds_dpsplanexec_master |  | fmasterid |
| 3 | idx_y_mds_dpsplanexec |  | forgid |
| 4 | idx_t_mds_dpsplanexec_createorg |  | fcreateorgid |

---

## 日志明细-子表 t_mds_dpstreelogeentry

- **表名称：** 日志明细-子表
- **表名：** t_mds_dpstreelogeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrytreedetailmsg | 详细信息 | varchar | 1000 |  | √ | ' ' | 详细信息 |
| 3 | fentrytreename | 步骤名称 | varchar | 500 |  | √ | ' ' | 步骤名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentrytreeoperatmin | 运行时间（秒） | numeric | 23 | 10 | √ | 0.0000000000 | 运行时间（秒） |
| 8 | fentrytreeseq | 步骤 | int8 | 64 |  | √ | 0 | 步骤 |
| 9 | fentrytreeresult | 运行结果 | varchar | 50 |  | √ | ' ' | 运行结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_dpstreelogeent |  | fid |
| 2 | pk_t_mds_dpstreelogeent |  | fentryid |

---

## 供应组织分配运算-使用范围表 t_mds_dpsplanexec_u

- **表名称：** 供应组织分配运算-使用范围表
- **表名：** t_mds_dpsplanexec_u

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
| 1 | idx_t_mds_dpsplanexec_u_uo |  | fuseorgid |
| 2 | pk_t_mds_dpsplanexec_u |  | fdataid,fuseorgid |

---

## 供应组织分配运算-多语言表 t_mds_dpsplanexec_l

- **表名称：** 供应组织分配运算-多语言表
- **表名：** t_mds_dpsplanexec_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_dpsplanexec_l |  | fpkid |
| 2 | idx_y_mds_dpsplanexec_l |  | fid,flocaleid |

---

## 供应组织分配运算-使用范围位图表 t_mds_dpsplanexec_m

- **表名称：** 供应组织分配运算-使用范围位图表
- **表名：** t_mds_dpsplanexec_m

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
| 1 | pk_t_mds_dpsplanexec_m |  | forgid |
