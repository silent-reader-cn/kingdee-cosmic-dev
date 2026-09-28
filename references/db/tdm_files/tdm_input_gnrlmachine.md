# 通用机打发票-tdm_input_gnrlmachine

## 通用机打发票-主表 t_tdm_input_gnrlmachine

- **表名称：** 通用机打发票-主表
- **表名：** t_tdm_input_gnrlmachine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdrawer | 开票人 | varchar | 16 |  | √ | ' ' | 开票人 |
| 3 | fcheckcode | 校验码 | varchar | 64 |  | √ | ' ' | 校验码 |
| 4 | fpayee | 收款人 | varchar | 16 |  | √ | ' ' | 收款人 |
| 5 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 6 | fexit | 出口 | varchar | 40 |  | √ | ' ' | 出口 |
| 7 | fplace | 发票所在地 | varchar | 40 |  | √ | ' ' | 发票所在地 |
| 8 | fticketcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 9 | forg | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 13 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 14 | finvoicecode | 发票代码 | varchar | 64 |  | √ | ' ' | 发票代码 |
| 15 | freviewer | 复核人 | varchar | 16 |  | √ | ' ' | 复核人 |
| 16 | fbuyername | 购方名称 | varchar | 200 |  | √ | ' ' | 购方名称 |
| 17 | finvoiceno | 发票号码 | varchar | 64 |  | √ | ' ' | 发票号码 |
| 18 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 19 | fsalertaxno | 销方税号 | varchar | 40 |  | √ | ' ' | 销方税号 |
| 20 | fbuyertaxno | 购方税号 | varchar | 70 |  | √ | ' ' | 购方税号 |
| 21 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 22 | ftime | 过路过桥发票时间 格式：时分秒 | varchar | 20 |  | √ | ' ' | 过路过桥发票时间 格式：时分秒 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 28 | fentrance | 入口 | varchar | 40 |  | √ | ' ' | 入口 |
| 29 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 7 :通用机打发票 17 :过路过桥费 |
| 30 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 31 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_input_gnrlmachine |  | forg,finvoicecode,finvoiceno |
| 2 | t_tdm_input_gnrlmachine_pkey |  | fid |
