# 需求计划运算-mds_planexec

## 需求计划运算-多语言表 t_mds_planexec_l

- **表名称：** 需求计划运算-多语言表
- **表名：** t_mds_planexec_l

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
| 1 | pk_t_mds_planexec_l |  | fpkid |

---

## 需求计划运算-使用范围位图表 t_mds_planexec_m

- **表名称：** 需求计划运算-使用范围位图表
- **表名：** t_mds_planexec_m

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
| 1 | pk_t_mds_planexec_m |  | forgid |

---

## 需求计划运算-使用范围表 t_mds_planexec_u

- **表名称：** 需求计划运算-使用范围表
- **表名：** t_mds_planexec_u

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
| 1 | idx_t_mds_planexec_u_uo |  | fuseorgid |
| 2 | pk_t_mds_planexec_u |  | fdataid,fuseorgid |

---

## 需求计划运算-主表 t_mds_planexec

- **表名称：** 需求计划运算-主表
- **表名：** t_mds_planexec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frplancalid | 需求计划方案 | int8 | 64 |  | √ | 0 | [需求计划方案F7 mds_rplancalf7](../mds_files/mds_rplancalf7.md) |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | frepeat | 重复运算 | bpchar | 1 |  | √ | '0' | 重复运算 |
| 6 | fcalculatepro | 计算进度 | numeric | 23 | 10 | √ | 0.0000000000 | 计算进度 |
| 7 | fpredtime | 预约时间 | int8 | 64 |  | √ | 0 | 预约时间 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | frunningtype | 运行时间类型 | varchar | 30 |  | √ | ' ' | 运行时间类型,枚举: |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fplanid | 计划号 | varchar | 50 |  | √ | ' ' | 计划号 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :计划 C :关闭 |
| 13 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | fsummin | 计算总时长（秒） | numeric | 23 | 10 | √ | 0.0000000000 | 计算总时长（秒） |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fdaysofmon | 月 | varchar | 100 |  | √ | ' ' | 月 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fdaysofweek | 周 | varchar | 50 |  | √ | ' ' | 周 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fjobid | 作业号 | varchar | 50 |  | √ | ' ' | 作业号 |
| 25 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | frepeattype | 时间重复类型 | varchar | 30 |  | √ | ' ' | 时间重复类型,枚举: |
| 27 | fstartdate | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 28 | fenable | 计算状态 | varchar | 30 |  | √ | ' ' | 计算状态,枚举: A :待运算 B :运算中 C :完成 D :错误 E :终止 |
| 29 | fnumber | 计算请求ID | varchar | 80 |  | √ | ' ' | 计算请求ID |
| 30 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_planexec_master |  | fmasterid |
| 2 | pk_t_mds_planexec |  | fid |
| 3 | idx_t_mds_planexec_createorg |  | fcreateorgid |

---

## 运算日志-子表 t_mds_execlogeentry

- **表名称：** 运算日志-子表
- **表名：** t_mds_execlogeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessdata | 处理数据量 | int8 | 64 |  | √ | 0 | 处理数据量 |
| 3 | fdetailmsg | 详细信息 | varchar | 255 |  | √ | ' ' | 详细信息 |
| 4 | foperatmin | 运行时间（秒） | numeric | 23 | 10 | √ | 0.0000000000 | 运行时间（秒） |
| 5 | fstepseq | 步骤顺序 | varchar | 50 |  | √ | ' ' | 步骤顺序 |
| 6 | fstepname | 步骤名称 | varchar | 255 |  | √ | ' ' | 步骤名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fresult | 运行结果 | varchar | 200 |  | √ | ' ' | 运行结果 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_execlogeentry |  | fentryid |
