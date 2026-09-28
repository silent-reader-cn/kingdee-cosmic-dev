# 安全库存计算日志-invp_safestock_callog

## 安全库存计算日志-主表 t_invp_safestock_callog

- **表名称：** 安全库存计算日志-主表
- **表名：** t_invp_safestock_callog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ferrormsg | 错误信息 | varchar | 2000 |  | √ | ' ' | 错误信息 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fschemeid | 安全库存统计方案 | int8 | 64 |  | √ | 0 | 安全库存统计方案 invp_safestock_scheme |
| 5 | flevelidmsg_tag | 水位信息_详情 | text | 0 |  |  | null | 水位信息_详情 |
| 6 | fmsgusertime | 耗时/ms | int8 | 64 |  | √ | 0 | 耗时/ms |
| 7 | fsubtaskend | 子任务结束时间 | timestamp | 0 |  |  | null | 子任务结束时间 |
| 8 | fsubtaskno | 子任务号 | varchar | 50 |  | √ | ' ' | 子任务号 |
| 9 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :已创建 B :成功 C :失败 D :重试中 |
| 10 | fsubtaskcount | 子任务执行水位数量 | int8 | 64 |  | √ | 0 | 子任务执行水位数量 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | flevelidmsg | 水位信息 | varchar | 2000 |  | √ | ' ' | 水位信息 |
| 13 | fmastertaskno | 主任务号 | varchar | 50 |  | √ | ' ' | 主任务号 |
| 14 | fmsgstart | 子任务开始时间 | timestamp | 0 |  |  | null | 子任务开始时间 |
| 15 | ferrormsg_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_invp_safestock_taskno |  | fmastertaskno,fsubtaskno |
| 2 | pk_t_invp_safestock_callog |  | fid |
