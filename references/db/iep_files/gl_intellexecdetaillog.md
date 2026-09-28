# 智能方案详细日志-gl_intellexecdetaillog

## 智能方案详细日志-主表 t_gl_intellschemalog

- **表名称：** 智能方案详细日志-主表
- **表名：** t_gl_intellschemalog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetorgid | 目标公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 4 | fsourceorgid | 源公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbussiness | 业务单据 | varchar | 50 |  | √ | ' ' | 业务单据 |
| 6 | ftargetbillnumber | 目标单据编码 | varchar | 100 |  |  | ' ' | 目标单据编码 |
| 7 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | foper | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fsrcbillid | 来源单据内码 | int8 | 64 |  | √ | 0 | 来源单据内码 |
| 11 | fexecnumber | 执行次数 | int4 | 32 |  | √ | 0 | 执行次数 |
| 12 | flastexectime | 最后执行时间 | timestamp | 0 |  |  | null | 最后执行时间 |
| 13 | fopersumlogid | 操作汇总日志id | int8 | 64 |  | √ | 0 | 操作汇总日志id |
| 14 | fbizappid | 业务应用 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 15 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 1 :进行中 2 :成功 3 :失败 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fintelschemaid | 执行方案 | int8 | 64 |  | √ | 0 | [智能执行方案 gl_intellexecschema](../iep_files/gl_intellexecschema.md) |
| 18 | fdate | fdate | int8 | 64 |  | √ | 0 |  |
| 19 | ftargetbooksid | ftargetbooksid | int8 | 64 |  | √ | 0 |  |
| 20 | fexecdetail | 描述 | text | 0 |  |  | null | 描述 |
| 21 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_intellschemalog_operid |  | fopersumlogid |
| 2 | idx_gl_intellschemalog |  | fcreatetime |
| 3 | t_gl_intellschemalog_pkey |  | fid |
| 4 | idx_gl_intellschemalog_date |  | fdate |
| 5 | idx_gl_intellschemalog_fid |  | fintelschemaid |
| 6 | idx_gl_intellschemalog_secnum |  | fsrcbillid,fsrcbillnumber |
