# 数据巡检任务-msbd_inspectjob

## 数据巡检任务-多语言表 t_msbd_inspectjob_l

- **表名称：** 数据巡检任务-多语言表
- **表名：** t_msbd_inspectjob_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_inspectjob_l |  | fpkid |
| 2 | idx_msbd_inspectjob_l_fid |  | fid,flocaleid |
| 3 | idx_msbd_inspectjob_l_fname |  | fname,fid |

---

## 数据巡检项目-子表 t_msbd_inspectjobentry

- **表名称：** 数据巡检项目-子表
- **表名：** t_msbd_inspectjobentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectunitid | 数据巡检模型编码 | int8 | 64 |  | √ | 0 | [数据巡检模型 msbd_inspectunit](../msbd_files/msbd_inspectunit.md) |
| 3 | fdmfunitenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fwarnlevel | 告警级别 | varchar | 5 |  | √ | ' ' | 告警级别,枚举: A :警告 B :错误 |
| 6 | fcanupdate | 允许修改 | bpchar | 1 |  | √ | '0' | 允许修改 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectjobentry |  | fid |
| 2 | pk_t_msbd_inspectjobentry |  | fentryid |

---

## 数据巡检任务-主表 t_msbd_inspectjob

- **表名称：** 数据巡检任务-主表
- **表名：** t_msbd_inspectjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frunorder | 执行顺序 | varchar | 5 |  | √ | ' ' | 执行顺序,枚举: 0 :串行 |
| 3 | fbatchmaxnum | 每个巡检模型最大执行批量 | int8 | 64 |  | √ | 0 | 每个巡检模型最大执行批量 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 6 | fmaxparallelnum | 最多线程数（个） | int8 | 64 |  | √ | 0 | 最多线程数（个） |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmaxinspectnum | 最大巡检数量 | int8 | 64 |  | √ | 0 | 最大巡检数量 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fstrategy | 执行策略 | varchar | 5 |  | √ | ' ' | 执行策略,枚举: 1 :等待前一任务执行完毕 |
| 12 | fdescription | fdescription | varchar | 512 |  |  | null |  |
| 13 | frunmode | 执行模式 | varchar | 5 |  | √ | ' ' | 执行模式,枚举: 0 :单机执行 1 :广播分片 |
| 14 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 17 | frunconcurrent | 巡检模型并行执行 | bpchar | 1 |  | √ | '0' | 巡检模型并行执行 |
| 18 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | ftimeout | 最长可执行时间（分） | int8 | 64 |  | √ | 0 | 最长可执行时间（分） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_inspectjob |  | fid |
| 2 | idx_msbd_inspectjob_fnumber |  | fnumber |
