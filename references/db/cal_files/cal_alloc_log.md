# 费用分摊日志-cal_alloc_log

## 费用分摊日志-主表 t_cal_alloclog

- **表名称：** 费用分摊日志-主表
- **表名：** t_cal_alloclog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fresultno | 分摊记录编码 | varchar | 50 |  | √ | ' ' | 分摊记录编码 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foperdetail | 操作详情 | varchar | 300 |  | √ | ' ' | 操作详情 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | forg | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsendbillid | 应付单id | int8 | 64 |  | √ | 0 | 应付单id |
| 11 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | ftype | 分摊类型 | bpchar | 1 |  | √ | ' ' | 分摊类型,枚举: 1 :采购费用分摊 2 :销售费用分摊 |
| 13 | foperstatus | 分摊状态 | bpchar | 1 |  | √ | ' ' | 分摊状态,枚举: 0 :处理中 1 :成功 2 :失败 3 :部分成功 4 :部分失败（处理中） |
| 14 | fsendbillno | 应付单编码 | varchar | 50 |  | √ | ' ' | 应付单编码 |
| 15 | fopertime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 16 | foperdetail_tag | 操作详情_详情 | text | 0 |  |  | null | 操作详情_详情 |
| 17 | fopertype | 分摊方式 | bpchar | 1 |  | √ | ' ' | 分摊方式,枚举: 1 :手动分摊 2 :自动分摊 3 :差额分摊 4 :手动反分摊 5 :自动反分摊 6 :关联分摊 |
| 18 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fresultid | 分摊记录id | int8 | 64 |  | √ | 0 | 分摊记录id |
| 21 | fbilltype | 应付单类型 | varchar | 50 |  | √ | ' ' | 应付单类型,枚举: ap_busbill :暂估应付单 ap_finapbill :财务应付单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_alloclog |  | fsendbillid,foperstatus |
| 2 | pk_t_cal_alloclog |  | fid |
