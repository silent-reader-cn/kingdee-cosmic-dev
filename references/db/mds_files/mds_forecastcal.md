# 预测计划运算-mds_forecastcal

## 运算日志-子表 t_mds_forecastcallog

- **表名称：** 运算日志-子表
- **表名：** t_mds_forecastcallog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdetailmsg | 详细信息 | varchar | 1000 |  | √ | ' ' | 详细信息 |
| 3 | foperatmin | 运行时间（秒） | varchar | 50 |  | √ | ' ' | 运行时间（秒） |
| 4 | fstepseq | 步骤顺序 | varchar | 50 |  | √ | ' ' | 步骤顺序 |
| 5 | fstepname | 步骤名称 | varchar | 255 |  | √ | ' ' | 步骤名称 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fresult | 运行结果 | varchar | 50 |  | √ | ' ' | 运行结果 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_forecastcallog |  | fentryid |
| 2 | idx_mds_forecastcallog |  | fid |

---

## 预测计划运算-使用范围表 t_mds_forecastcal_u

- **表名称：** 预测计划运算-使用范围表
- **表名：** t_mds_forecastcal_u

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
| 1 | pk_t_mds_forecastcal_u |  | fdataid,fuseorgid |
| 2 | idx_t_mds_forecastcal_u_uo |  | fuseorgid |

---

## 预测计划运算-多语言表 t_mds_forecastcal_l

- **表名称：** 预测计划运算-多语言表
- **表名：** t_mds_forecastcal_l

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
| 1 | pk_t_mds_forecastcal_l |  | fpkid |
| 2 | idx_mds_forecastcal_l |  | fid,flocaleid |

---

## 预测计划运算-使用范围位图表 t_mds_forecastcal_m

- **表名称：** 预测计划运算-使用范围位图表
- **表名：** t_mds_forecastcal_m

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
| 1 | pk_t_mds_forecastcal_m |  | forgid |

---

## 预测计划运算-主表 t_mds_forecastcal

- **表名称：** 预测计划运算-主表
- **表名：** t_mds_forecastcal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpredversion | 目标预测版本 | int8 | 64 |  | √ | 0 | 版本定义 mds_vrds |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | frepeat | 重复运算 | bpchar | 1 |  | √ | '0' | 重复运算 |
| 5 | fcalculatepro | 计算进度 | numeric | 23 | 8 | √ | 0.00000000 | 计算进度 |
| 6 | fpredtime | 预约时间 | int8 | 64 |  | √ | 0 | 预约时间 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | frunningtype | 运行时间类型 | varchar | 50 |  | √ | ' ' | 运行时间类型,枚举: 0 :立即运算 1 :预约时间运算 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fplanid | 计划号 | varchar | 50 |  | √ | ' ' | 计划号 |
| 11 | fstatus | 状态 | varchar | 5 |  | √ | ' ' | 状态,枚举: A :暂存 B :计划 C :关闭 |
| 12 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | fsummin | 计算总时长（秒） | numeric | 23 | 8 | √ | 0.00000000 | 计算总时长（秒） |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fdaysofmon | 月 | varchar | 100 |  | √ | ' ' | 月 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | ffcalplanid | 预测计划方案 | int8 | 64 |  | √ | 0 | 预测计算方案定义F7 mds_forecastcalplanf7 |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fdaysofweek | 周 | varchar | 50 |  | √ | ' ' | 周 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fcalstatus | 计算状态 | varchar | 50 |  | √ | ' ' | 计算状态,枚举: A :待运算 B :运算中 C :完成 D :错误 E :终止 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fjobid | 作业号 | varchar | 50 |  | √ | ' ' | 作业号 |
| 26 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :自由分配 5 :全局共享 7 :私有 1 :逐级分配 6 :管控范围内共享 |
| 27 | frepeattype | 时间重复类型 | varchar | 50 |  | √ | ' ' | 时间重复类型,枚举: 0 :周 1 :月 |
| 28 | fstartdate | 启动时间 | timestamp | 0 |  |  | null | 启动时间 |
| 29 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 计算请求ID | varchar | 80 |  | √ | ' ' | 计算请求ID |
| 31 | flosedate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 32 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_forecastcal |  | fid |
| 2 | idx_t_mds_forecastcal_master |  | fmasterid |
| 3 | idx_mds_forecastcal |  | fnumber |
| 4 | idx_t_mds_forecastcal_createorg |  | fcreateorgid |
