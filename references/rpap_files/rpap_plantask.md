# 调度计划-rpap_plantask

## 调度计划-主表 t_rpap_plantask

- **表名称：** 调度计划-主表
- **表名：** t_rpap_plantask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhour | 间隔（小时） | varchar | 10 |  | √ | ' ' | 间隔（小时）,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 24 :24 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | feffectiveendtime | 有效时间(止) | timestamp | 0 |  |  | null | 有效时间(止) |
| 5 | fisdelete | 是否已经删除 | varchar | 10 |  | √ | '0' | 是否已经删除,枚举: 已删除 :1 未删除 :0 |
| 6 | frobot | 机器人 | int8 | 64 |  | √ | 0 | 机器人 rpap_robot |
| 7 | fweek | 周 | varchar | 50 |  | √ | ' ' | 周,枚举: 1 :周一 2 :周二 3 :周三 4 :周四 5 :周五 6 :周六 7 :周日 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fdescription_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 11 | fmonth | 月 | varchar | 30 |  | √ | ' ' | 月,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 |
| 12 | fexcutenum | 已执行总次数 | int8 | 64 |  | √ | 0 | 已执行总次数 |
| 13 | feffectivestarttime | 有效时间(始) | timestamp | 0 |  |  | null | 有效时间(始) |
| 14 | fday | 日 | varchar | 100 |  | √ | ' ' | 日,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 13 :13 14 :14 15 :15 16 :16 17 :17 18 :18 19 :19 20 :20 21 :21 22 :22 23 :23 24 :24 25 :25 26 :26 27 :27 28 :28 29 :29 30 :30 31 :31 |
| 15 | fmin | 间隔（分钟） | varchar | 10 |  | √ | ' ' | 间隔（分钟）,枚举: 5 :5 10 :10 15 :15 30 :30 45 :45 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fexecutetimedesc | 执行时间（页面描述） | varchar | 255 |  | √ | ' ' | 执行时间（页面描述） |
| 19 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fexecutetime | 执行时间 | int4 | 32 |  | √ | 0 | 执行时间 |
| 22 | fplanname | 调度计划名称 | varchar | 100 |  | √ | ' ' | 调度计划名称 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | fexecutestarttime | 执行时间（始） | int4 | 32 |  | √ | 0 | 执行时间（始） |
| 26 | fexecuteendtime | 执行时间（止） | int4 | 32 |  | √ | 0 | 执行时间（止） |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :停用 1 :启用 |
| 28 | flastexcutetime | 上次执行时间 | timestamp | 0 |  |  | null | 上次执行时间 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | frepeatcycle | 执行频率 | varchar | 10 |  | √ | ' ' | 执行频率,枚举: 1 :分钟 2 :小时 3 :天 4 :周 5 :月 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rpap_plantask |  | fid |
| 2 | idx_t_rpap_plantask_orgid |  | forgid |

---

## 单据体-子表 t_rpap_plantask_process

- **表名称：** 单据体-子表
- **表名：** t_rpap_plantask_process

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fprocess | 流程 | int8 | 64 |  | √ | 0 | 流程 rpap_process |
| 5 | farguments | 参数 | text | 0 |  |  | null | 参数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plantask_process_p |  | fprocess |
| 2 | pk_t_rpap_plantask_process |  | fentryid |
