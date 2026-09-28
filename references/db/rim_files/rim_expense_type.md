# 手动添加单据类型-rim_expense_type

## 手动添加单据类型-主表 t_rim_expense_type

- **表名称：** 手动添加单据类型-主表
- **表名：** t_rim_expense_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 单据类型名称 | varchar | 100 |  | √ | ' ' | 单据类型名称 |
| 3 | foperate_scanner | 扫描仪 | varchar | 10 |  | √ | ' ' | 扫描仪,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | foperate_san_gun | 扫码枪 | varchar | 10 |  | √ | ' ' | 扫码枪,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 6 | foperate_excel_import | EXCEL导入 | varchar | 10 |  | √ | '1' | EXCEL导入,枚举: 0 :不支持 1 :支持 |
| 7 | fcreatetime | 添加时间 | timestamp | 0 |  |  | null | 添加时间 |
| 8 | foperate_attach_qrcode | 手机上传 | varchar | 10 |  | √ | ' ' | 手机上传,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 9 | foperate_att_qrcode_type | 手机上传二维码类型 | varchar | 10 |  | √ | ' ' | 手机上传二维码类型,枚举: cloudhub :云之家 weixin :微信 |
| 10 | foperate_qrcode_type | 手机上传二维码类型 | varchar | 10 |  | √ | ' ' | 手机上传二维码类型,枚举: cloudhub :云之家 weixin :微信 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | foperate_attach_upload | 附件上传 | varchar | 10 |  | √ | ' ' | 附件上传,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 13 | foperate_attach_scanner | 扫描仪录入 | varchar | 10 |  | √ | ' ' | 扫描仪录入,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 14 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | foperate_qrcode | 手机上传 | varchar | 10 |  | √ | ' ' | 手机上传,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 16 | fcreatorid | 添加人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | foperate_person_invoice | 个人收票 | varchar | 10 |  | √ | ' ' | 个人收票,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 18 | foperate_enter | 手工录入 | varchar | 10 |  | √ | ' ' | 手工录入,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 19 | foperate_upload | 发票上传 | varchar | 10 |  | √ | ' ' | 发票上传,枚举: 0 :不展示 2 :按权限 1 :展示 |
| 20 | fnumber | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 21 | foperate_company_invoice | 企业收票 | varchar | 10 |  | √ | ' ' | 企业收票,枚举: 0 :不展示 2 :按权限 1 :展示 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rim_expense_type |  | fid |
| 2 | idx_rim_expense_type |  | fnumber |
