# 余额模型参数-bal_config

## 余额模型参数-主表 t_bal_cfg

- **表名称：** 余额模型参数-主表
- **表名：** t_bal_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | '0' | id |
| 2 | fac_auto_repair | 转移前自动修复 | bpchar | 1 |  | √ | '1' | 转移前自动修复 |
| 3 | feg_check_spcount | 检查快照数量 | bpchar | 1 |  | √ | '1' | 检查快照数量 |
| 4 | fcl_invalid_min | 判定事务ID超时的安全时间/min | int4 | 32 |  | √ | 0 | 判定事务ID超时的安全时间/min |
| 5 | fnt_bill_bs | 消息中单据ID的批量数 | int4 | 32 |  | √ | 0 | 消息中单据ID的批量数 |
| 6 | fnt_allasync_min | 待更新单据发布间隔时间/min | int4 | 32 |  | √ | 0 | 待更新单据发布间隔时间/min |
| 7 | fcr_data_bs | 巡检重算数据的批量数 | int4 | 32 |  | √ | 0 | 巡检重算数据的批量数 |
| 8 | fbal | 余额表 | varchar | 36 |  | √ | ' ' | [余额表 bal_balanceinfo](../bal_files/bal_balanceinfo.md) |
| 9 | fcl_checktx_bs | 判断事务ID是否失效的批量数 | int4 | 32 |  | √ | 0 | 判断事务ID是否失效的批量数 |
| 10 | fnt_delay_ms | 通知延迟时间/ms | int4 | 32 |  | √ | 0 | 通知延迟时间/ms |
| 11 | feg_addbal_bs | 分析余额的批量数 | int4 | 32 |  | √ | 0 | 分析余额的批量数 |
| 12 | fnt_updating_op | 加急处理更新中事务 | bpchar | 1 |  | √ | '1' | 加急处理更新中事务 |
| 13 | fnt_threadmode | 更新中事务单线程模式 | bpchar | 1 |  | √ | '0' | 更新中事务单线程模式 |
| 14 | fcl_pubtx_bs | 消息中失效事务ID的批量数 | int4 | 32 |  | √ | 0 | 消息中失效事务ID的批量数 |
| 15 | fmv_tpdata_bs | 转移快照的批量数 | int4 | 32 |  | √ | 0 | 转移快照的批量数 |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fmv_merge_sql | 合并SQL更新 | bpchar | 1 |  | √ | '1' | 合并SQL更新 |
| 18 | fac_limit_day | 允许转移几天前的数据 | int4 | 32 |  | √ | 0 | 允许转移几天前的数据 |
| 19 | fnt_tx_bs | 消息中事务ID的批量数 | int4 | 32 |  | √ | 0 | 消息中事务ID的批量数 |
| 20 | fcl_safe_min | 判定节点死亡的安全时间/min | int4 | 32 |  | √ | 0 | 判定节点死亡的安全时间/min |
| 21 | fnt_async_op | 加急处理待更新单据 | bpchar | 1 |  | √ | '1' | 加急处理待更新单据 |
| 22 | fmv_keycol_bs | 合并更新keycol批量数 | int4 | 32 |  | √ | 0 | 合并更新keycol批量数 |
| 23 | fnt_tx_limit | 更新中事务消费单节点并行度 | int4 | 32 |  | √ | 0 | 更新中事务消费单节点并行度 |
| 24 | feg_dist_entryid | 历史快照去重 | bpchar | 1 |  | √ | '0' | 历史快照去重 |
| 25 | feg_ignore_cover | 数值全为0忽略覆盖数据 | bpchar | 1 |  | √ | '0' | 数值全为0忽略覆盖数据 |
| 26 | fac_record_bs | 即时余额记录转移的批量数 | int8 | 64 |  | √ | 0 | 即时余额记录转移的批量数 |
| 27 | fmodifier | 修改人 | int8 | 64 |  | √ | '0' | [人员 bos_user](../base_files/bos_user.md) |
| 28 | feg_addsp_bs | INSERT快照的批量数 | int4 | 32 |  | √ | 0 | INSERT快照的批量数 |
| 29 | fmv_updateper_bs | 更新期间余额的批量数 | int4 | 32 |  | √ | 0 | 更新期间余额的批量数 |
| 30 | fmv_maxquery_bs | 合并查询快照上限 | int4 | 32 |  | √ | 0 | 合并查询快照上限 |
| 31 | fmv_updatereal_bs | 更新即时余额的批量数 | int4 | 32 |  | √ | 0 | 更新即时余额的批量数 |
| 32 | fnt_reupdate_limit | 待更新单据消费单节点并行度 | int4 | 32 |  | √ | 0 | 待更新单据消费单节点并行度 |
| 33 | fnt_partasync_min | 更新中事务发布间隔时间/min | int4 | 32 |  | √ | 0 | 更新中事务发布间隔时间/min |
| 34 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bal_cfg |  | fid |
