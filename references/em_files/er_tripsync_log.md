# 商旅集成日志(旧)-er_tripsync_log

## 商旅集成日志(旧)-主表 t_er_tripsynclog

- **表名称：** 商旅集成日志(旧)-主表
- **表名：** t_er_tripsynclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceid | 请求traceId | varchar | 300 |  | √ | ' ' | 请求traceId |
| 3 | fmessage | 日志内容 | text | 0 |  |  | null | 日志内容 |
| 4 | frequestdata | 请求数据 | text | 0 |  |  | null | 请求数据 |
| 5 | ffunction | 功能 | varchar | 300 |  | √ | ' ' | 功能,枚举: orgInvoke :组织 userInvoke :人员 tripReqBillInvoke :出差申请单 loginInvoke :登录 orderInvoke :订单 checkingInvoke :结算单 invoiceSendInvoke :发票开具 invoiceReceiveInvoke :发票接收 tripCityInvoke :城市更新 tripCarRegulationInvoke :出差用车制度 imageInvoke :影像信息 dailyVehicleBillInvoke :用车申请单 mealApplicationBillInvoke :用餐申请单 tripTokenInvoke :token |
| 6 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :成功 B :失败 |
| 7 | frequesturl | 请求URL | varchar | 300 |  |  | null | 请求URL |
| 8 | frequestdata_tag | 请求数据_详情 | text | 0 |  |  | null | 请求数据_详情 |
| 9 | fserver | 服务商 | varchar | 80 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 |
| 10 | fsynctime | 集成时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 集成时间 |
| 11 | fresponsedata | 响应数据 | text | 0 |  |  | null | 响应数据 |
| 12 | fresponsedata_tag | 响应数据_详情 | text | 0 |  |  | null | 响应数据_详情 |
| 13 | fbillid | 业务单据id | varchar | 300 |  |  | null | 业务单据id |
| 14 | fmessage_tag | 日志内容_详情 | text | 0 |  |  | null | 日志内容_详情 |
| 15 | fbillno | 业务单据编号 | varchar | 300 |  |  | '1970-01-01 00:00:00' | 业务单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tripsynclog_fserver |  | fserver |
| 2 | idx_tripsynclog_billid |  | fbillid,fserver,fstatus |
| 3 | t_er_tripsynclog_pkey |  | fid |
