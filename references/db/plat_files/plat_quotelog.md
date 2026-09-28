# 取价日志-plat_quotelog

## 取价日志-主表 t_plat_quotelog

- **表名称：** 取价日志-主表
- **表名：** t_plat_quotelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fquotestarttime | 取价开始时间 | timestamp | 0 |  |  | null | 取价开始时间 |
| 3 | fquoteendtime | 取价结束时间 | timestamp | 0 |  |  | null | 取价结束时间 |
| 4 | fquotesrcno | 取价来源单据编号 | varchar | 80 |  | √ | ' ' | 取价来源单据编号 |
| 5 | flogjson | 日志明细文本 | varchar | 512 |  |  | null | 日志明细文本 |
| 6 | flogresult | 取价结果简要描述 | varchar | 100 |  |  | ' ' | 取价结果简要描述 |
| 7 | fquotebillseq | 取价行号 | int8 | 64 |  | √ | 0 | 取价行号 |
| 8 | fquotebillid | 取价单据id | int8 | 64 |  | √ | 0 | 取价单据id |
| 9 | flogkey | 日志key | varchar | 50 |  | √ | ' ' | 日志key |
| 10 | flogjson_tag | 日志明细文本_详情 | text | 0 |  |  | null | 日志明细文本_详情 |
| 11 | fquotebillentryid | 取价单据分录id | int8 | 64 |  | √ | 0 | 取价单据分录id |
| 12 | fquotesrcseq | 价格来源行号 | int8 | 64 |  | √ | 0 | 价格来源行号 |
| 13 | fquoteorgid | 取价组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fquotebill | 取价单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 15 | flogtype | 日志类型 | varchar | 5 |  | √ | ' ' | 日志类型,枚举: norm :正常 exp :异常 |
| 16 | fquoteuserid | 取价员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fquotesrcbill | 取价来源单据 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plat_quotelog |  | fid |
| 2 | idx_plat_quotelog |  | fquoteorgid,fquotebill,fquotestarttime |
