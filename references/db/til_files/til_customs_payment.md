# 海关专用缴款书单据-til_customs_payment

## 海关专用缴款书单据-主表 t_tdm_customs_payment

- **表名称：** 海关专用缴款书单据-主表
- **表名：** t_tdm_customs_payment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fctype | 税种类别 | varchar | 30 |  | √ | ' ' | 税种类别,枚举: zzs :增值税 gs :关税 xfs :消费税 |
| 3 | fgetoffice | 收入机关 | varchar | 50 |  | √ | ' ' | 收入机关 |
| 4 | fdeclarenum | 报关单编号 | varchar | 50 |  | √ | ' ' | 报关单编号 |
| 5 | fyxdkskje | 有效抵扣税款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 有效抵扣税款金额 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsigndate | 填发日期 | timestamp | 0 |  |  | null | 填发日期 |
| 8 | fcometermstatus | 进项状态 | varchar | 30 |  | √ | ' ' | 进项状态,枚举: not :未勾选 yes :勾选不抵扣 yesverify :勾选认证 |
| 9 | fsourcesystem | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcertstatus | fcertstatus | varchar | 50 |  | √ | ' ' |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fselectresult | fselectresult | varchar | 50 |  | √ | ' ' |  |
| 14 | fpaylimittime | 缴款期限 | timestamp | 0 |  |  | null | 缴款期限 |
| 15 | ftranstoolnum | 运输工具号 | varchar | 50 |  | √ | ' ' | 运输工具号 |
| 16 | fdealgoodsnum | 提/装货单号 | varchar | 50 |  | √ | ' ' | 提/装货单号 |
| 17 | fapplyunitnum | 申请单位编号 | varchar | 50 |  | √ | ' ' | 申请单位编号 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | funitname | 缴款单位名称 | varchar | 80 |  | √ | ' ' | 缴款单位名称 |
| 24 | funitnumber | 缴款单位账号 | varchar | 50 |  | √ | ' ' | 缴款单位账号 |
| 25 | fspecialtaxcode | 专用缴款书号码 | varchar | 200 |  | √ | ' ' | 专用缴款书号码 |
| 26 | fperiod | 所属税期 | timestamp | 0 |  |  | null | 所属税期 |
| 27 | fselectstatus | fselectstatus | varchar | 50 |  | √ | ' ' |  |
| 28 | fcontractnum | 合同批文号 | varchar | 50 |  | √ | ' ' | 合同批文号 |
| 29 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: income :模板引入 synchro :系统同步 |
| 30 | ftaxtotal | 税款金额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 税款金额合计 |
| 31 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | ' ' | 生成凭证 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | funitbank | 缴款单位开户银行 | varchar | 58 |  | √ | ' ' | 缴款单位开户银行 |
| 34 | fverifystatus | 稽核结果 | varchar | 30 |  | √ | ' ' | 稽核结果,枚举: ing :稽核中 true :相符 false :不符 lack :缺联 repeat :重号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_customs_payment |  | forgid |
| 2 | pk_tdm_customs_payment |  | fid |

---

## 海关专用缴款书子表明细-子表 t_tdm_customs_pay_item

- **表名称：** 海关专用缴款书子表明细-子表
- **表名：** t_tdm_customs_pay_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxtate | 税率% | numeric | 23 | 10 | √ | 0.0000000000 | 税率% |
| 3 | ftaxnumber | 税号 | varchar | 50 |  | √ | ' ' | 税号 |
| 4 | fgoodsname | 货物名称 | varchar | 50 |  | √ | ' ' | 货物名称 |
| 5 | ffinishtaxprice | 完税价格 | numeric | 23 | 10 | √ | 0.0000000000 | 完税价格 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftaxmoney | 税款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税款金额 |
| 8 | fnumber | 数量 | int8 | 64 |  | √ | 0 | 数量 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_customs_pay_item_fk |  | fid |
| 2 | pk_tdm_customs_pay_item |  | fentryid |
