# 状态变更记录-task_statechange

## 状态变更记录-主表 t_tk_statechange

- **表名称：** 状态变更记录-主表
- **表名：** t_tk_statechange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | foperatorid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fjobid | 任务 | int8 | 64 |  | √ | 0 | 任务 |
| 6 | fnewjobstate | 新任务状态 | varchar | 10 |  | √ | ' ' | 新任务状态,枚举: 11 :待上传影像 12 :待分配 22 :待手工分配 10 :分配异常 8 :回收 13 :待审核 0 :暂挂 2 :退回重扫 7 :影像重传 3 :审核通过 4 :审核不通过 14 :待质检 15 :待整改 16 :待复核 17 :质检暂挂 18 :整改暂挂 19 :复核暂挂 21 :质检完成 20 :取消 1 :正常（弃用） 5 :废弃（弃用） 6 :打回（弃用） 9 :去重（弃用） |
| 7 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 8 | foldjobstate | 原任务状态 | varchar | 10 |  | √ | ' ' | 原任务状态,枚举: 11 :待上传影像 12 :待分配 22 :待手工分配 10 :分配异常 13 :待审核 0 :暂挂 2 :退回重扫 7 :影像重传 3 :审核通过 4 :审核不通过 8 :回收 14 :待质检 15 :待整改 16 :待复核 17 :质检暂挂 18 :整改暂挂 19 :复核暂挂 21 :质检完成 20 :取消 1 :正常（弃用） 5 :废弃（弃用） 6 :打回（弃用） 9 :去重（弃用） |
| 9 | fmessages | 处理意见 | varchar | 2000 |  | √ | ' ' | 处理意见 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fmessagestate | 消息状态 | varchar | 10 |  | √ | ' ' | 消息状态,枚举: 0 :未读 1 :已读 |
| 15 | finnermsg | 内部说明 | varchar | 2000 |  |  | ' ' | 内部说明 |
| 16 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | foperationnum | 操作数 | int8 | 64 |  | √ | 0 | 操作数 |
| 20 | foperation | 处理操作 | varchar | 10 |  | √ | ' ' | 处理操作,枚举: 1 :审批通过 2 :审批不通过 3 :暂挂 4 :取消暂挂 5 :退回重扫 6 :分配人员 7 :重分配人员 8 :自动分配人员 9 :废弃 10 :打回 11 :创建任务 12 :更新节点处理人 13 :强制取消分配 14 :主动获取任务 15 :重新参与分配 16 :影像重传 17 :已整改 18 :合格 19 :不合格 20 :取消退回重扫 21 :跳转流程 22 :修改优先级 |
| 21 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 22 | fdecision | 决策项 | int8 | 64 |  | √ | 0 | 决策项 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_statechange_pkey |  | fid |
| 2 | index_ssc_statechange |  | fnumber |
| 3 | idx_ssc_sttchg_fjbid_chgtm |  | fjobid,fchangetime |

---

## 状态变更记录-多语言表 t_tk_statechange_l

- **表名称：** 状态变更记录-多语言表
- **表名：** t_tk_statechange_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_statechange_l_pkey |  | fpkid |
| 2 | index_ssc_statechange_l |  | fid,flocaleid |
