# 防重服务日志-fcs_repeatctrllog

## 防重服务日志-主表 t_fcs_repeatctrllog

- **表名称：** 防重服务日志-主表
- **表名：** t_fcs_repeatctrllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdestbilltype | 目标单类型 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcosttime | 耗时(ms) | int4 | 32 |  | √ | 0 | 耗时(ms) |
| 5 | ftraceid | traceid | varchar | 60 |  | √ | ' ' | traceid |
| 6 | fsourcebilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fexception_tag | 异常信息_详情 | text | 0 |  |  | ' ' | 异常信息_详情 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | frepeatsetid | 防重设置 | int8 | 64 |  | √ | 0 | 支付防重 fcs_checkctrl |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fdestbillid | 目标单ID | int8 | 64 |  | √ | 0 | 目标单ID |
| 15 | fcheckresult | 校验结果 | varchar | 30 |  | √ | ' ' | 校验结果,枚举: repeat :重推 excess :超额 |
| 16 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 17 | fexception | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 18 | flogtype | 日志分类 | varchar | 80 |  | √ | ' ' | 日志分类,枚举: payaccess :支付准入 accessrecord :链路存储 repeatctrl :支付防重 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fcs_repeatctrllog |  | fid |
| 2 | idx_t_fcs_repeatctrllog_srcid |  | fsourcebillid |
| 3 | idx_t_fcs_repeatctrllog_type |  | fcreatetime,flogtype |
