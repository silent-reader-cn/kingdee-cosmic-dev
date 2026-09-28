# 性能审计日志-bos_performancelog

## 性能审计日志-主表 t_sys_performancelog

- **表名称：** 性能审计日志-主表
- **表名：** t_sys_performancelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbugcode | bug号 | varchar | 50 |  | √ | ' ' | bug号 |
| 3 | fcreaterfield | 点击人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ferrormsg | 推送失败信息 | varchar | 50 |  | √ | ' ' | 推送失败信息 |
| 5 | fhassended | 已录 | bpchar | 1 |  | √ | '0' | 已录 |
| 6 | fcheckboxfield | 性能异常 | bpchar | 1 |  | √ | '0' | 性能异常 |
| 7 | fcreatedatefield | 点击时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 点击时间 |
| 8 | fmethodkey | 操作标识 | varchar | 150 |  | √ | ' ' | 操作标识 |
| 9 | fformid | 表单id | varchar | 50 |  | √ | ' ' | 表单id |
| 10 | fappid | 应用id | varchar | 50 |  | √ | ' ' | 应用id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sys_performancelog |  | fid |
