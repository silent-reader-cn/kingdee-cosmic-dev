# 接口异常监控-task_exceptionrecord

## 接口异常监控-主表 t_tk_excprecord

- **表名称：** 接口异常监控-主表
- **表名：** t_tk_excprecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fretrytime | 最后处理时间 | timestamp | 0 |  |  | null | 最后处理时间 |
| 3 | fapplorg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | frequestparam | 请求参数 | varchar | 210 |  | √ | ' ' | 请求参数 |
| 5 | frequestparam_tag | 请求参数_详情 | text | 0 |  |  | null | 请求参数_详情 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fiscompensate | 是否需要补偿 | bpchar | 1 |  | √ | '0' | 是否需要补偿 |
| 8 | fnotifymember | 通知成员 | varchar | 200 |  | √ | ' ' | 通知成员 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fisnotified | 是否已发通知 | int8 | 64 |  | √ | 0 | 是否已发通知 |
| 11 | fnotifytype | 通知类型 | varchar | 100 |  | √ | ' ' | 通知类型 |
| 12 | finftype | 接口类型 | varchar | 20 |  | √ | ' ' | 接口类型 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fcompensatestatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: 0 :失败 1 :成功 2 :标过 3 :停止 |
| 16 | ffailuretime | 异常创建时间 | timestamp | 0 |  |  | null | 异常创建时间 |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 21 | fbilltypename | 单据类型名称 | varchar | 50 |  | √ | ' ' | 单据类型名称 |
| 22 | fapplicant | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | ffailurereason_tag | 异常原因_详情 | text | 0 |  |  | null | 异常原因_详情 |
| 24 | fretrycounts | 重试次数 | int8 | 64 |  | √ | 0 | 重试次数 |
| 25 | fdealtype | 处理方式 | varchar | 10 |  | √ | ' ' | 处理方式 |
| 26 | fexceptiontype | 异常类型 | varchar | 25 |  | √ | ' ' | 异常类型 |
| 27 | fbillid | 单据id | varchar | 100 |  | √ | ' ' | 单据id |
| 28 | ffailurereason | 异常原因 | varchar | 210 |  | √ | ' ' | 异常原因 |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fbilltype | 单据类型 | varchar | 100 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_exceprecord_fbillno |  | fbillno |
| 2 | idx_ssc_exprecord_fstatus |  | fcompensatestatus |
| 3 | idx_ssc_exprecord_fiscompen |  | fiscompensate |
| 4 | t_tk_excprecord_pkey |  | fid |
