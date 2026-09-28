# 发票回推日志-invsm_callback_log

## 发票回推日志-主表 t_invsm_callback_log

- **表名称：** 发票回推日志-主表
- **表名：** t_invsm_callback_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbusinesssystemcode | 业务系统编码 | varchar | 32 |  | √ | ' ' | 业务系统编码 |
| 3 | finvoicestatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 |
| 4 | fcallbacktype | 回调类型 | varchar | 30 |  | √ | ' ' | 回调类型,枚举: invoice :发票 bill :单据 3 :发票失败回调 4 :单据失败回调 5 :全部回调 |
| 5 | fcallbackcontent | fcallbackcontent | varchar | 255 |  | √ | ' ' |  |
| 6 | fbusinesstype | 业务类型(回调动作) | varchar | 50 |  | √ | ' ' | 业务类型(回调动作),枚举: INVOICE.OPEN :正常开票 INVOICE.CANCEL :发票作废 INVOICE.RED :发票红冲 |
| 7 | forg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcallbackcontents_tag | 回调内容_详情 | text | 0 |  |  | null | 回调内容_详情 |
| 9 | fbusinessfid | 业务主键 | int8 | 64 |  | √ | 0 | 业务主键 |
| 10 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 11 | fcallbackurl | 回调地址 | varchar | 250 |  | √ | ' ' | 回调地址 |
| 12 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 13 | fcallbackbillno | 回调单据编号 | varchar | 50 |  | √ | ' ' | 回调单据编号 |
| 14 | fcallbackresult | 回调结果 | varchar | 20 |  | √ | ' ' | 回调结果 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fcallbackmessage | 回调信息 | varchar | 200 |  | √ | ' ' | 回调信息 |
| 17 | fcallbackcontent_tag | fcallbackcontent_tag | text | 0 |  |  | null |  |
| 18 | fcallback_status | fcallback_status | varchar | 50 |  | √ | ' ' |  |
| 19 | fcallbackcontents | 回调内容 | varchar | 255 |  | √ | ' ' | 回调内容 |
| 20 | fcallbackstatus | 回调状态 | varchar | 50 |  | √ | ' ' | 回调状态,枚举: 0 :成功 1 :失败 2 :待回调 |
| 21 | fretrytimes | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 22 | finvoicetype | 发票种类 | varchar | 50 |  | √ | ' ' | 发票种类,枚举: 026 :电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :纸质专用发票 08xdp :全电发票（增值税专用发票） 10xdp :全电发票（普通发票） |
| 23 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 24 | fissuetype | 开票类型 | varchar | 50 |  | √ | ' ' | 开票类型,枚举: 0 :蓝票 1 :红票 |
| 25 | ftargetsystem | 目标系统 | varchar | 50 |  | √ | 'systemsource' | 目标系统,枚举: originalbill :开票申请单 systemsource :业务系统 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invsm_callback_log |  | fbusinesssystemcode |
| 2 | pk_invsm_callback_log |  | fid |
