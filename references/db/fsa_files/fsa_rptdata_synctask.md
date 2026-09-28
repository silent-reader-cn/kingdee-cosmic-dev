# 任务列表-fsa_rptdata_synctask

## 任务列表-主表 t_fsa_rptdatasynctask

- **表名称：** 任务列表-主表
- **表名：** t_fsa_rptdatasynctask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fstaticstatus_info | 工作任务的状态信息 | varchar | 255 |  | √ | ' ' | 工作任务的状态信息 |
| 4 | fstatus | 状态 | varchar | 2 |  | √ | ' ' | 状态,枚举: 0 :新增 1 :进行中 2 :成功完成 9 :失败 10 :手动中断 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ftasktype | 任务类型 | varchar | 3 |  | √ | ' ' | 任务类型,枚举: 0 :从总账报表同步数据的任务 1 :单报表指标更新计算 2 :跨报表指标更新计算 20 :从合并报表多维数据库同步数据的任务 98 :创建数据表任务 99 :删除数据表任务 100 :删除(或标记)数据表中数据记录的任务 101 :回滚删除(或标记)数据表中数据记录的任务 21 :从合并报表多维数据库同步数据的任务组 22 :导入离线数据任务 23 :单维度缺失层级补齐任务 |
| 7 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 8 | frptdatasyncparam | 同步参数名称 | int8 | 64 |  | √ | 0 | 同步参数设置 fsa_syncparam |
| 9 | fexecutiontime | 执行时长 | varchar | 50 |  | √ | ' ' | 执行时长 |
| 10 | fstaticstatus_info_tag | 工作任务的状态信息_详情 | text | 0 |  |  | null | 工作任务的状态信息_详情 |
| 11 | fversion | 取数版本 | varchar | 50 |  | √ | ' ' | 取数版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_rptdatasynctask |  | fid |
| 2 | idx_fsa_rptdatasynctask_1 |  | frptdatasyncparam,fstatus |
