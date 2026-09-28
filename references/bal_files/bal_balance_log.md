# 余额更新日志-bal_balance_log

## 余额更新日志-主表 t_bal_balancelog

- **表名称：** 余额更新日志-主表
- **表名：** t_bal_balancelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceid | TraceId | varchar | 50 |  | √ | ' ' | TraceId |
| 3 | ftype | 更新类型 | bpchar | 1 |  | √ | ' ' | 更新类型,枚举: 1 :正常更新 0 :异常回滚 2 :异步任务 |
| 4 | fbillids_tag | 更新的单据ID_详情 | text | 0 |  |  | null | 更新的单据ID_详情 |
| 5 | fheadmsg | 错误日志 | varchar | 2000 |  | √ | ' ' | 错误日志 |
| 6 | fstart | 服务开始时间 | timestamp | 0 |  |  | null | 服务开始时间 |
| 7 | fop | 操作 | varchar | 20 |  | √ | ' ' | 操作 |
| 8 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fbillids | 更新的单据ID | varchar | 2000 |  | √ | ' ' | 更新的单据ID |
| 10 | fresult | 服务执行结果 | bpchar | 1 |  | √ | ' ' | 服务执行结果,枚举: 1 :成功 0 :失败 |
| 11 | fusetime | 服务耗时/ms | int8 | 64 |  | √ | 0 | 服务耗时/ms |
| 12 | fbillname | 实体对象 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bal_log_st |  | fstart |
| 2 | pk_bal_balancelog |  | fid |
| 3 | idx_bal_log_bn |  | fbillname |

---

## 日志详情-子表 t_bal_balancelogentry

- **表名称：** 日志详情-子表
- **表名：** t_bal_balancelogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspdatacount | 生成快照行数 | int4 | 32 |  | √ | 0 | 生成快照行数 |
| 3 | fdbrute | 更新库 | varchar | 10 |  | √ | ' ' | 更新库 |
| 4 | fruleusetime | 规则耗时/ms | int8 | 64 |  | √ | 0 | 规则耗时/ms |
| 5 | fruleresult | 规则执行结果 | bpchar | 1 |  | √ | ' ' | 规则执行结果,枚举: 1 :成功 0 :失败 2 :未更新 3 :重试成功 4 :重试失败 5 :未重试 |
| 6 | fupdatetype | 更新方式 | bpchar | 1 |  | √ | ' ' | 更新方式,枚举: A :同步 B :部分异步 C :完全异步 |
| 7 | fruleno | 规则编码 | varchar | 30 |  | √ | ' ' | 余额更新规则列表 bal_balanceupdaterule |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | frulemsg | 错误日志 | varchar | 2000 |  | √ | ' ' | 错误日志 |
| 10 | fruleplugintime | 业务插件耗时/ms | int4 | 32 |  | √ | 0 | 业务插件耗时/ms |
| 11 | frulestart | 规则执行时间 | timestamp | 0 |  |  | null | 规则执行时间 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_balancelogentry |  | fentryid |
| 2 | idx_bal_log_e_fbno |  | fruleno |
| 3 | idx_bal_log_e_fid |  | fid |
