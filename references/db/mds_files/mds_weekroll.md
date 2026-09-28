# 周滚动设置-mds_weekroll

## 运算日志-子表 t_mds_weekrolllog

- **表名称：** 运算日志-子表
- **表名：** t_mds_weekrolllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocessdata | 处理数据量 | int8 | 64 |  | √ | 0 | 处理数据量 |
| 3 | fdetailmsg | 详细信息 | varchar | 1000 |  | √ | ' ' | 详细信息 |
| 4 | foperatmin | 运行时间（秒） | numeric | 23 | 10 | √ | 0.0000000000 | 运行时间（秒） |
| 5 | fstepseq | 步骤顺序 | varchar | 50 |  | √ | ' ' | 步骤顺序 |
| 6 | fstepname | 步骤名称 | varchar | 50 |  | √ | ' ' | 步骤名称 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fresult | 运行结果 | varchar | 100 |  | √ | ' ' | 运行结果 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_weekrolllog |  | fid |
| 2 | pk_t_mds_weekrolllog |  | fentryid |

---

## 周滚动设置-主表 t_mds_weekroll

- **表名称：** 周滚动设置-主表
- **表名：** t_mds_weekroll

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstime | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fcalculatepro | 计算进度 | numeric | 23 | 10 | √ | 0.0000000000 | 计算进度 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fplanid | 任务号 | varchar | 50 |  | √ | ' ' | 任务号 |
| 8 | fstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :计划 C :终止 D :关闭 |
| 9 | faccstatus | 任务状态 | varchar | 5 |  | √ | ' ' | 任务状态,枚举: A :暂存 B :计划 C :终止 D :关闭 |
| 10 | fsummin | 计算总时长（秒） | numeric | 23 | 10 | √ | 0.0000000000 | 计算总时长（秒） |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fsetval | 设置数据 | varchar | 2000 |  | √ | ' ' | 设置数据 |
| 16 | fetime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fjobid | 作业号 | varchar | 50 |  | √ | ' ' | 作业号 |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fexecstatus | 执行状态 | varchar | 5 |  | √ | ' ' | 执行状态,枚举: A :未开始 B :错误 C :终止 D :完成 E :执行中 |
| 23 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_weekroll |  | fnumber |
| 2 | idx_t_mds_weekroll_master |  | fmasterid |
| 3 | idx_t_mds_weekroll_createorg |  | fcreateorgid |
| 4 | pk_t_mds_weekroll |  | fid |

---

## 周滚动设置-使用范围表 t_mds_weekroll_u

- **表名称：** 周滚动设置-使用范围表
- **表名：** t_mds_weekroll_u

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
| 1 | idx_t_mds_weekroll_u_uo |  | fuseorgid |
| 2 | pk_t_mds_weekroll_u |  | fdataid,fuseorgid |

---

## 周滚动设置-多语言表 t_mds_weekroll_l

- **表名称：** 周滚动设置-多语言表
- **表名：** t_mds_weekroll_l

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
| 1 | idx_mds_weekroll_l |  | fid,flocaleid |
| 2 | pk_t_mds_weekroll_l |  | fpkid |

---

## 周滚动设置-使用范围位图表 t_mds_weekroll_m

- **表名称：** 周滚动设置-使用范围位图表
- **表名：** t_mds_weekroll_m

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
| 1 | pk_t_mds_weekroll_m |  | forgid |

---

## 供方单据体-子表 t_mds_weekrollentb

- **表名称：** 供方单据体-子表
- **表名：** t_mds_weekrollentb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifier | fentrymodifier | int8 | 64 |  | √ | 0 |  |
| 3 | fverid | 周滚动版本 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 4 | fentrycreatedate | fentrycreatedate | timestamp | 0 |  |  | null |  |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentrycreator | fentrycreator | int8 | 64 |  | √ | 0 |  |
| 8 | fentrymodifydate | fentrymodifydate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_weekrollentb |  | fid |
| 2 | pk_t_mds_weekrollentb |  | fentryid |

---

## 需方单据体-子表 t_mds_weekrollenta

- **表名称：** 需方单据体-子表
- **表名：** t_mds_weekrollenta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifier | fentrymodifier | int8 | 64 |  | √ | 0 |  |
| 3 | fentrycreatedate | fentrycreatedate | timestamp | 0 |  |  | null |  |
| 4 | fsetid | 发货取数 | int8 | 64 |  | √ | 0 | 数据源配置 mrp_resource_dataconf_rgt |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentrycreator | fentrycreator | int8 | 64 |  | √ | 0 |  |
| 8 | fentrymodifydate | fentrymodifydate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_weekrollenta |  | fentryid |
| 2 | idx_mds_weekrollenta |  | fid |
