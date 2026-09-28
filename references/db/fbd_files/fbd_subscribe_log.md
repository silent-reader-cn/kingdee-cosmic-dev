# 订阅消费清单-fbd_subscribe_log

## 订阅消费清单-主表 t_fbd_subscribe_log

- **表名称：** 订阅消费清单-主表
- **表名：** t_fbd_subscribe_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fdatasourceid | 业务对象 | varchar | 50 |  | √ | ' ' | 单据主实体 bos_billmainentity |
| 8 | fbiztime | 消费时间 | timestamp | 0 |  |  | null | 消费时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsubscriberid | 订阅方案编码 | int8 | 64 |  | √ | 0 | 订阅方案 fbd_subscribe |
| 12 | frecuserid | 消息接收人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fbd_subscribe_log_num |  | fbillno |
| 2 | idx_t_fbd_subscribe_log_biz |  | fdatasourceid,fbillid |
| 3 | pk_t_fbd_subscribe_log |  | fid |
