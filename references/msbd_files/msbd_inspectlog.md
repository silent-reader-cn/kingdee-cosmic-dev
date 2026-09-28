# 数据巡检日志-msbd_inspectlog

## 检查详情-子表 t_msbd_inspectlogentry

- **表名称：** 检查详情-子表
- **表名：** t_msbd_inspectlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectdetail | 巡检详情 | varchar | 2000 |  |  | null | 巡检详情 |
| 3 | fexcpstacktrace | 异常堆栈信息 | varchar | 512 |  |  | null | 异常堆栈信息 |
| 4 | ffixeddatadetail_tag | 修复数据详情_详情 | text | 0 |  |  | null | 修复数据详情_详情 |
| 5 | fexcpstacktrace_tag | 异常堆栈信息_详情 | text | 0 |  |  | null | 异常堆栈信息_详情 |
| 6 | fentrystatus | 检查结果 | varchar | 5 |  | √ | ' ' | 检查结果,枚举: A :警告 B :失败 C :异常 D :成功 E :部分修复 F :已修复 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fruningstatus | 运行状态 | varchar | 5 |  | √ | ' ' | 运行状态,枚举: A :未开始 B :运行中 C :已完成 D :已终止 |
| 9 | fdescription | 描述 | varchar | 512 |  |  | null | 描述 |
| 10 | fruningprocess | 运行进度 | varchar | 5 |  | √ | ' ' | 运行进度,枚举: A :0%（处理插件） B :10%（处理插件） C :20%（处理插件） D :30%（处理插件） E :40%（处理插件） F :50%（处理插件） G :60%（处理插件） H :70%（处理插件） I :80%（处理插件） J :90%（处理插件） K :100%（处理插件） L :0%（校验条件） M :10%（校验条件） N :20%（校验条件） O :30%（校验条件） P :40%（校验条件） Q :50%（校验条件） R :60%（校验条件） S :70%（校验条件） T :80%（校验条件） U :90%（校验条件） V :100%（校验条件） W :100% X :0% |
| 11 | ffixeddatadetail | 修复数据详情 | varchar | 512 |  |  | null | 修复数据详情 |
| 12 | finspectunitid | 数据巡检模型编码 | int8 | 64 |  | √ | 0 | 数据巡检模型 msbd_inspectunit |
| 13 | fisfixed | 是否修复 | bpchar | 1 |  | √ | '0' | 是否修复 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msbd_inspectlogentry |  | fentryid |
| 2 | idx_msbd_inspectlogentry |  | fid |

---

## 数据巡检日志-主表 t_msbd_inspectlog

- **表名称：** 数据巡检日志-主表
- **表名：** t_msbd_inspectlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexetime | 巡检时间 | timestamp | 0 |  |  | null | 巡检时间 |
| 3 | fexeuserid | 执行用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | finspectplanid | 数据巡检计划 | int8 | 64 |  | √ | 0 | 数据巡检计划 msbd_inspectplan |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finspectjobid | 数据巡检任务 | int8 | 64 |  | √ | 0 | 数据巡检任务 msbd_inspectjob |
| 7 | fendtime | 巡检完成时间 | timestamp | 0 |  |  | null | 巡检完成时间 |
| 8 | fexestatus | 执行状态 | varchar | 5 |  | √ | ' ' | 执行状态,枚举: A :进行中 B :已完成 |
| 9 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectlog_fnumber |  | finspectjobid |
| 2 | pk_t_msbd_inspectlog |  | fid |

---

## 异常数据列表-子表 t_msbd_inspectlogentry_e

- **表名称：** 异常数据列表-子表
- **表名：** t_msbd_inspectlogentry_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fobjtypeid | 对象类型 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 2 | fobjid | 对象ID | int8 | 64 |  | √ | 0 | 对象ID |
| 3 | fextralinfo | 其他信息 | varchar | 500 |  | √ | ' ' | 其他信息 |
| 4 | fobjentryid | 对象分录ID | int8 | 64 |  | √ | 0 | 对象分录ID |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fbizuniquesympol | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 9 | fobjdes | 对象描述 | varchar | 500 |  | √ | ' ' | 对象描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msbd_inspectlogentry_e |  | fentryid |
| 2 | pk_t_msbd_inspectlogentry_e |  | fdetailid |
