# 数据处理结果-pbd_schandleresult

## 数据处理结果-主表 t_pur_scdataresult

- **表名称：** 数据处理结果-主表
- **表名：** t_pur_scdataresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 耗时（秒） | int8 | 64 |  | √ | 0 | 耗时（秒） |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsourcebilltype | 源单业务操作类型 | varchar | 50 |  | √ | ' ' | 源单业务操作类型 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcontext | 运行上下文 | varchar | 2000 |  | √ | ' ' | 运行上下文 |
| 8 | fprogress | 进度（%） | int8 | 64 |  | √ | 0 | 进度（%） |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsourcebillid | 源单id | varchar | 30 |  | √ | ' ' | 源单id |
| 14 | ftaskid | 执行任务 | int8 | 64 |  | √ | 0 | [数据处理配置 pbd_srmdatasetting](../pbd_files/pbd_srmdatasetting.md) |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_scdataset_fbillid |  | fsourcebillid,fsourcebilltype,fcreatetime |
| 2 | pk_pur_scdataresult |  | fid |

---

## 执行结果分录-子表 t_pur_handleresultentry

- **表名称：** 执行结果分录-子表
- **表名：** t_pur_handleresultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ferrinfo | 错误详情 | varchar | 2000 |  | √ | ' ' | 错误详情 |
| 3 | fsubtime | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 4 | fdetail | 执行详情 | varchar | 2000 |  | √ | ' ' | 执行详情 |
| 5 | fsubstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 5 :跳过 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftaskid | 任务明细 | int8 | 64 |  | √ | 0 | [数据处理任务节点 pbd_scdatatask](../pbd_files/pbd_scdatatask.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsubstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pur_handleresultentry |  | fentryid |
| 2 | idx_pur_handleresultentry_fid |  | fid,fseq |
