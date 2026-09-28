# 任务日志-fsa_rptdata_synclog

## 任务日志-主表 t_fsa_rptdatasynclog

- **表名称：** 任务日志-主表
- **表名：** t_fsa_rptdatasynclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finstance | 运行同步操作的实例ID | varchar | 100 |  | √ | ' ' | 运行同步操作的实例ID |
| 3 | fmsg_tag | 日志信息_详情 | text | 0 |  |  | null | 日志信息_详情 |
| 4 | fcreatetime | 日志创建时间 | timestamp | 0 |  |  | null | 日志创建时间 |
| 5 | ftasktype | 任务类型 | varchar | 3 |  | √ | ' ' | 任务类型,枚举: 0 :从总账报表同步数据的任务 1 :单报表指标更新计算 2 :跨报表指标更新计算 20 :从合并报表多维数据库同步数据的任务 98 :创建数据表任务 99 :删除数据表任务 100 :删除(或标记)数据表中数据记录的任务 101 :回滚删除(或标记)数据表中数据记录的任务 21 :从合并报表多维数据库同步数据的任务组 22 :导入离线数据任务 23 :单维度缺失层级补齐任务 |
| 6 | fdatasrctype | 数据集合的目标数据来源类型 | varchar | 50 |  | √ | ' ' | 数据集合的目标数据来源类型,枚举: 0 :自定义 bcmParamSource :星瀚合并报表 2 :星瀚预算 3 :星瀚总账 fileParamSource :导入离线数据 |
| 7 | fmsg | 日志信息 | varchar | 510 |  |  | null | 日志信息 |
| 8 | ftaskoperatetoken | 任务操作所使用的Token | int8 | 64 |  | √ | 0 | 任务操作所使用的Token |
| 9 | fdatasyncparam | 数据同步参数 | int8 | 64 |  | √ | 0 | [同步参数设置 fsa_syncparam](../fsa_files/fsa_syncparam.md) |
| 10 | fstatus | 同步状态： | varchar | 2 |  | √ | '0' | 同步状态：,枚举: 0 :未开始 1 :进行中 2 :成功完成 9 :失败 10 :手动终止 |
| 11 | fupdatetime | 日志更新时间 | timestamp | 0 |  |  | null | 日志更新时间 |
| 12 | fparamdetail_tag | 数据同步参数自定义明细_详情 | text | 0 |  |  | null | 数据同步参数自定义明细_详情 |
| 13 | fdatasynctask | 所属的同步任务ID | int8 | 64 |  | √ | 0 | 所属的同步任务ID |
| 14 | fdatacollection | 数据集合 | int8 | 64 |  | √ | 0 | [数据集合 fsa_data_collection](../fsa_files/fsa_data_collection.md) |
| 15 | fparamdetail | 数据同步参数自定义明细 | varchar | 510 |  |  | null | 数据同步参数自定义明细 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptdatasynclog |  | fid |
