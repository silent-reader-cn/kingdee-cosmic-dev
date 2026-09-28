# 扫码开票设置（原默认开票项）-bdm_scaninvoice_setting

## 扫码开票设置（原默认开票项）-主表 t_bdm_scaninvoice_setting

- **表名称：** 扫码开票设置（原默认开票项）-主表
- **表名：** t_bdm_scaninvoice_setting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 联系电话 | varchar | 50 |  | √ | ' ' | 联系电话 |
| 3 | faddress | 自取地址 | varchar | 230 |  | √ | ' ' | 自取地址 |
| 4 | fscantype | 扫码开票类型 | varchar | 4 |  | √ | ' ' | 扫码开票类型,枚举: 0 :扫码提交抬头 1 :扫码开票 |
| 5 | fdrawer | 开票人 | varchar | 50 |  | √ | ' ' | 开票人 |
| 6 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率,枚举: 0 :0% 0.015 :1.5% 0.01 :1% 0.02 :2% 0.03 :3% 0.04 :4% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 7 | fqrcodevalidity | 二维码有效期 | varchar | 50 |  | √ | ' ' | 二维码有效期 |
| 8 | feqinfono | 设备编号 | varchar | 50 |  | √ | ' ' | 设备编号 |
| 9 | fprice | 单价（取这个值） | numeric | 23 | 10 | √ | 0.0000000000 | 单价（取这个值） |
| 10 | finvoicetype | 发票种类 | varchar | 50 |  | √ | ' ' | 发票种类,枚举: 004 :纸质增值税专用发票 007 :增值税普通发票（纸票） 026 :增值税电子普通发票 028 :增值税电子专用发票 |
| 11 | fgoodscode | 商品编码 | varchar | 50 |  | √ | ' ' | 商品编码 |
| 12 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 13 | fsystemcode | 业务系统编码 | varchar | 50 |  | √ | ' ' | 业务系统编码 |
| 14 | feqinfotaxno | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 15 | fdefaultgoods | 默认开票项 | bpchar | 1 |  | √ | ' ' | 默认开票项 |
| 16 | fnumber | key值 | varchar | 50 |  | √ | ' ' | key值 |
| 17 | fupdatedate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdm_scaninvoice_setting |  | fid |
| 2 | idx_bdm_scaninvoice_setting |  | feqinfotaxno |
