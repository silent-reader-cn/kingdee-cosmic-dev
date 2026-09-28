# 数据反馈单-occba_checkaccountback

## 关联单据分录-子表 t_occba_checkacctbacke

- **表名称：** 关联单据分录-子表
- **表名：** t_occba_checkacctbacke

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 摘要 | varchar | 30 |  | √ | ' ' | 摘要,枚举: im_saloutbill :收到商品金额 cas_recbill :采购付款金额 occba_moneyincome :采购付款金额 occba_channelbalance :期初余额 sum :小计 |
| 3 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 4 | fpaymentamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 5 | fsrcbillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpayableamount | 应收金额 | numeric | 23 | 10 | √ | 0 | 应收金额 |
| 8 | fsrcbilltype | 单据类型 | varchar | 80 |  | √ | ' ' | 单据类型 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_checkacctbacke_bid |  | fsrcbillid |
| 2 | idx_occba_checkacctbacke_bno |  | fsrcbillno |
| 3 | pk_occba_checkacctbacke |  | fentryid |
| 4 | idx_occba_checkacctbacke_id |  | fid |

---

## 数据反馈单-主表 t_occba_checkacctback

- **表名称：** 数据反馈单-主表
- **表名：** t_occba_checkacctback

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcomment | 问题描述 | varchar | 2000 |  | √ | ' ' | 问题描述 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | foperatorid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | foperatetime | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbizdate | 反馈日期 | timestamp | 0 |  |  | null | 反馈日期 |
| 13 | fbackstatus | 处理状态 | bpchar | 1 |  | √ | 'A' | 处理状态,枚举: A :待处理 B :已处理 |
| 14 | fopinion | 处理意见 | varchar | 2000 |  | √ | ' ' | 处理意见 |
| 15 | fchannelid | 反馈渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_checkacctback_bno |  | fbillno |
| 2 | idx_occba_checkacctback_orgid |  | forgid |
| 3 | pk_occba_checkacctback |  | fid |
| 4 | idx_occba_checkacctback_chanid |  | fchannelid |
