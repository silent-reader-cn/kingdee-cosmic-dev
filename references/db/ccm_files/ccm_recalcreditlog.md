# 信用重算过程日志-ccm_recalcreditlog

## 信用重算过程日志-主表 t_ccm_recalproclog

- **表名称：** 信用重算过程日志-主表
- **表名：** t_ccm_recalproclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 操作内容 | varchar | 2000 |  | √ | ' ' | 操作内容 |
| 3 | fprogressrate | 进度 | int4 | 32 |  | √ | 0 | 进度 |
| 4 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 5 | fsessionid | 线程ID | varchar | 100 |  | √ | ' ' | 线程ID |
| 6 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ccm_recalproclog |  | fid |
| 2 | idx_ccm_recalproclog |  | fcreatetime |
