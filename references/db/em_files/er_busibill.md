# 消费支付明细-er_busibill

## 消费支付明细-主表 t_er_busibill

- **表名称：** 消费支付明细-主表
- **表名：** t_er_busibill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbusitype | 交易类型 | varchar | 50 |  | √ | ' ' | 交易类型,枚举: 00 :一般消费 01 :预借现金 12 :预借现金退货 20 :一般消费退货 60 :还款及费用 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fuser | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fdept | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcurrency | 交易币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fcompany | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | faccout | 银行账户 | varchar | 50 |  | √ | ' ' | 银行账户 |
| 13 | fbusiname | 商户名称 | varchar | 50 |  | √ | ' ' | 商户名称 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fserver | 服务商 | int8 | 64 |  | √ | 0 | 服务商设置 er_biz_info |
| 16 | fbusiamount | 交易金额 | numeric | 23 | 10 | √ | 0 | 交易金额 |
| 17 | fhappenddate | 账单期间 | timestamp | 0 |  |  | null | 账单期间 |
| 18 | fbusidate | fbusidate | timestamp | 0 |  |  | null |  |
| 19 | fcardnumber | 银行卡号 | varchar | 50 |  | √ | ' ' | 银行卡号 |
| 20 | fbillno | 消费编码 | varchar | 50 |  | √ | ' ' | 消费编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fbillperiod | 账单日 | timestamp | 0 |  |  | null | 账单日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_busibill |  | fid |
| 2 | idx_busi_user |  | fuser |
| 3 | idx_busi_company |  | fcompany,fdept |
| 4 | idx_busi_ac |  | faccout,fcardnumber |
| 5 | idx_busi_server |  | fserver |
