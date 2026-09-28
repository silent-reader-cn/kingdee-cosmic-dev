# 余额模型参数-bal_config

## 余额模型参数-主表 t_bal_cfg

- **表名称：** 余额模型参数-主表
- **表名：** t_bal_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | feg_check_spcount | 检查快照数量 | bpchar | 1 |  | √ | '1' | 检查快照数量 |
| 3 | fcl_invalid_min | 判定事务ID超时的安全时间/min | int4 | 32 |  | √ | 0 | 判定事务ID超时的安全时间/min |
| 4 | fnt_bill_bs | 消息中单据ID的批量数 | int4 | 32 |  | √ | 0 | 消息中单据ID的批量数 |
| 5 | fnt_allasync_min | 待更新单据发布间隔时间/min | int4 | 32 |  | √ | 0 | 待更新单据发布间隔时间/min |
| 6 | fcr_data_bs | 巡检重算数据的批量数 | int4 | 32 |  | √ | 0 | 巡检重算数据的批量数 |
| 7 | fbal | 余额表 | varchar | 36 |  | √ | ' ' | 余额表 bal_balanceinfo |
| 8 | fcl_checktx_bs | 判断事务ID是否失效的批量数 | int4 | 32 |  | √ | 0 | 判断事务ID是否失效的批量数 |
| 9 | fnt_delay_ms | 通知延迟时间/ms | int4 | 32 |  | √ | 0 | 通知延迟时间/ms |
| 10 | feg_addbal_bs | 分析余额的批量数 | int4 | 32 |  | √ | 0 | 分析余额的批量数 |
| 11 | fnt_updating_op | 加急处理更新中事务 | bpchar | 1 |  | √ | '1' | 加急处理更新中事务 |
| 12 | fnt_threadmode | 更新中事务单线程模式 | bpchar | 1 |  | √ | '0' | 更新中事务单线程模式 |
| 13 | fcl_pubtx_bs | 消息中失效事务ID的批量数 | int4 | 32 |  | √ | 0 | 消息中失效事务ID的批量数 |
| 14 | fmv_tpdata_bs | 转移快照的批量数 | int4 | 32 |  | √ | 0 | 转移快照的批量数 |
| 15 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fmv_merge_sql | 合并SQL更新 | bpchar | 1 |  | √ | '1' | 合并SQL更新 |
| 17 | fnt_tx_bs | 消息中事务ID的批量数 | int4 | 32 |  | √ | 0 | 消息中事务ID的批量数 |
| 18 | fcl_safe_min | 判定节点死亡的安全时间/min | int4 | 32 |  | √ | 0 | 判定节点死亡的安全时间/min |
| 19 | fnt_async_op | 加急处理待更新单据 | bpchar | 1 |  | √ | '1' | 加急处理待更新单据 |
| 20 | fmv_keycol_bs | 合并更新keycol批量数 | int4 | 32 |  | √ | 0 | 合并更新keycol批量数 |
| 21 | fnt_tx_limit | 更新中事务消费单节点并行度 | int4 | 32 |  | √ | 0 | 更新中事务消费单节点并行度 |
| 22 | feg_dist_entryid | 历史快照去重 | bpchar | 1 |  | √ | '0' | 历史快照去重 |
| 23 | feg_ignore_cover | 数值全为0忽略覆盖数据 | bpchar | 1 |  | √ | '0' | 数值全为0忽略覆盖数据 |
| 24 | fmodifier | 修改人 | int8 | 64 |  | √ | '0' | 人员 bos_user |
| 25 | feg_addsp_bs | INSERT快照的批量数 | int4 | 32 |  | √ | 0 | INSERT快照的批量数 |
| 26 | fmv_updateper_bs | 更新期间余额的批量数 | int4 | 32 |  | √ | 0 | 更新期间余额的批量数 |
| 27 | fmv_maxquery_bs | 合并查询快照上限 | int4 | 32 |  | √ | 0 | 合并查询快照上限 |
| 28 | fmv_updatereal_bs | 更新即时余额的批量数 | int4 | 32 |  | √ | 0 | 更新即时余额的批量数 |
| 29 | fnt_reupdate_limit | 待更新单据消费单节点并行度 | int4 | 32 |  | √ | 0 | 待更新单据消费单节点并行度 |
| 30 | fnt_partasync_min | 更新中事务发布间隔时间/min | int4 | 32 |  | √ | 0 | 更新中事务发布间隔时间/min |
| 31 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_cfg |  | fid |
