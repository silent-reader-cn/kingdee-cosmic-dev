# 集成日志-ocdbd_integrationlog

## 集成日志-主表 t_ocdbd_integrationlog

- **表名称：** 集成日志-主表
- **表名：** t_ocdbd_integrationlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsynmessage | 同步异常信息 | text | 0 |  |  | null | 同步异常信息 |
| 3 | fiscflowid | 服务流程 | int8 | 64 |  | √ | 0 | [服务流程 isc_service_flow](../iscb_files/isc_service_flow.md) |
| 4 | fsourceentryid | 源单分录行id | int8 | 64 |  | √ | 0 | 源单分录行id |
| 5 | fisctriggeid | 启动方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 6 | fsyntime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 7 | fsynuser | 同步用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fiscuccess | 同步是否成功 | bpchar | 1 |  | √ | ' ' | 同步是否成功 |
| 9 | ftargetbillid | 目标单id | int8 | 64 |  | √ | 0 | 目标单id |
| 10 | fsourcebill | 源单 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 11 | fbillpkid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 12 | fsynop | 操作 | varchar | 10 |  | √ | ' ' | 操作,枚举: save :保存 submit :提交 audit :审核 unsubmit :撤销 unaudit :反审核 entryclose :行关闭 entryunclose :行反关闭 delete :删除 |
| 13 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_integrationlog |  | fbillpkid |
| 2 | pk_ocdbd_integrationlog |  | fid |
