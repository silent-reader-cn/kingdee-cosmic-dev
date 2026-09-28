# 人员同步至云平台失败日志-bos_user_syntoyptfaillog

## 人员同步至云平台失败日志-主表 t_lic_usersynfaillog

- **表名称：** 人员同步至云平台失败日志-主表
- **表名：** t_lic_usersynfaillog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftype | 同步方式 | varchar | 30 |  | √ | '1' | 同步方式,枚举: 1 :定时任务 2 :手动重试 |
| 3 | fcreatetime | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 4 | fopuserid | 执行者 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fuserid | 被同步人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | freason | 原因 | varchar | 255 |  | √ | ' ' | 原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_lic_user_fuserid |  | fuserid |
| 2 | t_lic_usersynfaillog_pkey |  | fid |
