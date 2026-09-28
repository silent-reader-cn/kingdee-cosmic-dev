# 凭证号同步日志-gl_syncnumvoucher_log

## 凭证号同步日志-主表 t_gl_syncnumvoucher_log

- **表名称：** 凭证号同步日志-主表
- **表名：** t_gl_syncnumvoucher_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftypeid | 凭证类型 | int8 | 64 |  | √ | 0 | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |
| 3 | fadjustdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 4 | fmainvouchernum | 主账簿凭证号 | varchar | 80 |  | √ | ' ' | 主账簿凭证号 |
| 5 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 6 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 7 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 8 | fdestvouchernum | 现凭证号 | varchar | 80 |  | √ | ' ' | 现凭证号 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fsrcvouchernum | 原凭证号 | varchar | 80 |  | √ | ' ' | 原凭证号 |
| 12 | fadjusterid | 调整人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_syncnumvoucher_log |  | forgid,fbooktypeid |
| 2 | pk_t_gl_syncnumvoucher_log |  | fid |
