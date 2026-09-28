# 收票主体-er_invoice_entity

## 收票主体-主表 t_er_invoiceentity

- **表名称：** 收票主体-主表
- **表名：** t_er_invoiceentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvoicereceiveraddress | 发票接收人地址 | varchar | 255 |  | √ | ' ' | 发票接收人地址 |
| 3 | foutuniqueid | 外部唯一ID | varchar | 50 |  | √ | ' ' | 外部唯一ID |
| 4 | finvoicereceiver | 发票接收人 | varchar | 255 |  | √ | ' ' | 发票接收人 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fpurchasermobile | 购方电话 | varchar | 30 |  | √ | ' ' | 购方电话 |
| 9 | finvoicereceivermobile | 发票接收人电话 | varchar | 25 |  | √ | ' ' | 发票接收人电话 |
| 10 | fpurchaseraddress | 购方地址 | varchar | 255 |  | √ | ' ' | 购方地址 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态 |
| 13 | fpurchasertaxnumber | 纳税人识别号 | varchar | 30 |  | √ | ' ' | 纳税人识别号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | finvoiceentityno | 收票主体编码 | varchar | 100 |  | √ | ' ' | 收票主体编码 |
| 16 | finvoicereceivermail | 发票接收人邮箱 | varchar | 50 |  | √ | ' ' | 发票接收人邮箱 |
| 17 | fpurchaseraccountbank | 购方开户行 | varchar | 50 |  | √ | ' ' | 购方开户行 |
| 18 | finvoicetitle | 发票抬头 | varchar | 255 |  | √ | ' ' | 发票抬头 |
| 19 | fpurchaseraccountno | 购方开户行账号 | varchar | 100 |  | √ | ' ' | 购方开户行账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_invoiceentity |  | fid |
| 2 | idx_er_finvoiceentityno |  | finvoiceentityno |
