# 用户消息通知接收状态-fatvs_userinformstatus

## 用户消息通知接收状态-主表 t_fatvs_userinformstatus

- **表名称：** 用户消息通知接收状态-主表
- **表名：** t_fatvs_userinformstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdailyinform | 每日接收日报通知 | bpchar | 1 |  | √ | '1' | 每日接收日报通知 |
| 3 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 4 | femployeeid | 数字员工ID | int8 | 64 |  | √ | 0 | 数字员工ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fatvs_userinfo |  | fuserid,femployeeid |
| 2 | pk_t_fatvs_userinformstatus |  | fid |
