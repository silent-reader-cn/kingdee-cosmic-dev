# 共享MQ失败统计-task_mq_faile

## 共享MQ失败统计-主表 t_tk_mqfail

- **表名称：** 共享MQ失败统计-主表
- **表名：** t_tk_mqfail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmqparam_tag | 共享MQ参数_详情 | text | 0 |  |  | null | 共享MQ参数_详情 |
| 3 | fmqregion | MQ领域 | varchar | 30 |  | √ | ' ' | MQ领域,枚举: ssc :共享中心 bos :影像系统 |
| 4 | fmqqueue | MQ队列 | varchar | 100 |  | √ | ' ' | MQ队列,枚举: kd.ssc.task.eas.ssc_attachment :附件获取MQ kd.bos.imageplatform.service.image :影像系统同步EAS |
| 5 | fmqexceptionmsg | 异常信息 | varchar | 300 |  | √ | ' ' | 异常信息 |
| 6 | fmqexceptionstack_tag | 异常堆栈_详情 | text | 0 |  |  | null | 异常堆栈_详情 |
| 7 | fmqparam | 共享MQ参数 | varchar | 300 |  | √ | ' ' | 共享MQ参数 |
| 8 | fmqexceptiontime | 异常时间 | timestamp | 0 |  |  | null | 异常时间 |
| 9 | fmqexceptionstack | 异常堆栈 | varchar | 300 |  | √ | ' ' | 异常堆栈 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_mqfail_pkey |  | fid |
| 2 | index_tk_mqfail_mqqueue |  | fmqqueue |
| 3 | index_tk_mqfail_region |  | fmqregion |
