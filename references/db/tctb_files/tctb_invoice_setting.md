# 新增发票参数-tctb_invoice_setting

## 新增发票参数-主表 t_tctb_invoice_setting

- **表名称：** 新增发票参数-主表
- **表名：** t_tctb_invoice_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsecret | 秘钥 | varchar | 100 |  | √ | ' ' | 秘钥 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :保存 B :启用 C :禁用 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fclientid | 客户ID | varchar | 100 |  | √ | ' ' | 客户ID |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fpassword | 密码 | varchar | 100 |  | √ | ' ' | 密码 |
| 9 | forg | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fpassword_enp | fpassword_enp | text | 0 |  |  | null |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | furl | URL链接 | varchar | 100 |  | √ | ' ' | URL链接 |
| 14 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctb_invoice_setting_pkey |  | fid |
| 2 | idx_tctb_invoice_setting |  | fbillno |
