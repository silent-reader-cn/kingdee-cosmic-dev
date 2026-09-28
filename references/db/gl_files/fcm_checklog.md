# 结账检查执行日志-fcm_checklog

## 结账检查执行日志-主表 t_fcm_checklog

- **表名称：** 结账检查执行日志-主表
- **表名：** t_fcm_checklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 30 |  | √ | ' ' |  |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcheckitemcode | 检查项编码 | varchar | 30 |  | √ | ' ' | 检查项编码 |
| 7 | forgid | 业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fresult | 执行 | varchar | 30 |  | √ | ' ' | 执行,枚举: 1 :成功 0 :失败 2 :执行异常 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fcheckitemname | 检查项名称 | varchar | 500 |  | √ | ' ' | 检查项名称 |
| 11 | fcheckitemid | 检查项ID | int8 | 64 |  | √ | 0 | 检查项ID |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fbizappid | 应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 14 | fexecutionperiod | 执行期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 15 | fexecutiontraceid | TraceId | varchar | 60 |  | √ | ' ' | TraceId |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fexecutortime | fexecutortime | timestamp | 0 |  |  | null |  |
| 18 | fsubbiztypeid | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 19 | ffailcause | 失败原因 | varchar | 50 |  | √ | ' ' | 失败原因 |
| 20 | fsuggesttype | 控制级别 | bpchar | 1 |  | √ | ' ' | 控制级别,枚举: 1 :警告 2 :不通过 |
| 21 | fbillno | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcm_checklog |  | fid |
| 2 | idx_fcm_checklog_name |  | fbillno |
| 3 | idx_fcm_checklog_orgbizcreate |  | forgid,fbizappid,fcreatetime |
