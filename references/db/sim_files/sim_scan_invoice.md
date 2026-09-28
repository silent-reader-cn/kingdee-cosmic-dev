# 扫码开票-sim_scan_invoice

## 扫码开票-主表 t_sim_scan_invoice

- **表名称：** 扫码开票-主表
- **表名：** t_sim_scan_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbuyertaxno | 购方税号 | varchar | 30 |  | √ | ' ' | 购方税号 |
| 3 | fremark | 客户留言 | varchar | 255 |  | √ | ' ' | 客户留言 |
| 4 | faddress | 开票地址 | varchar | 255 |  | √ | ' ' | 开票地址 |
| 5 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 6 | fbank | 开户银行 | varchar | 255 |  | √ | ' ' | 开户银行 |
| 7 | fbankaccount | 银行账号 | varchar | 30 |  | √ | ' ' | 银行账号 |
| 8 | fbuyerphone | 手机号码 | varchar | 20 |  | √ | ' ' | 手机号码 |
| 9 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fstatus | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :未使用 1 :已使用 |
| 11 | finvoicephone | 开票电话 | varchar | 20 |  | √ | ' ' | 开票电话 |
| 12 | fbuyerproperty | 购方类型 | varchar | 50 |  | √ | ' ' | 购方类型,枚举: 0 :企业 1 :个人 |
| 13 | finvoicetype | 发票种类 | varchar | 50 |  | √ | ' ' | 发票种类,枚举: 026 :电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :纸质专用发票 |
| 14 | fwxid | 微信ID | varchar | 50 |  | √ | ' ' | 微信ID |
| 15 | fbuyername | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 16 | fbuyeremail | 邮箱地址 | varchar | 200 |  | √ | ' ' | 邮箱地址 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_scan_invoice |  | forg |
| 2 | pk_sim_scan_invoice |  | fid |
