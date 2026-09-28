# 收入账票比对结果单-tcvat_acc_inv_comp

## 本期开票，本期确认收入-子表 t_tcvat_acc_invcomp_ent

- **表名称：** 本期开票，本期确认收入-子表
- **表名：** t_tcvat_acc_invcomp_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fje | 凭证金额 | numeric | 23 | 10 | √ | 0 | 凭证金额 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 4 | fpzhh | 凭证行号 | varchar | 50 |  | √ | ' ' | 凭证行号 |
| 5 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 6 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 7 | finvoicestatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 7 :作废中 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpzjzdate | 凭证记账日期 | timestamp | 0 |  |  | null | 凭证记账日期 |
| 10 | faccperiod | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 11 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |
| 12 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :增值税专用发票 025 :增值税普通发票（卷票） 10xdp :全电发票（普通发票） 08xdp :全电发票（增值税专用发票） |
| 13 | fcurwfdata | 本期核销金额 | numeric | 23 | 10 | √ | 0 | 本期核销金额 |
| 14 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 15 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 16 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 17 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 18 | fbalanceid | 科目名称 | varchar | 36 |  | √ | ' ' | [科目 tdm_account](../tdm_files/tdm_account.md) |
| 19 | fwfdate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 20 | fbuyername | 购方名称 | varchar | 50 |  | √ | ' ' | 购方名称 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fkjpzh | 会计凭证号 | varchar | 50 |  | √ | ' ' | 会计凭证号 |
| 23 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 24 | fbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_acc_invcomp_ent |  | fentryid |
| 2 | idx_tcvat_acc_invcomp_ent_fk |  | fid |

---

## 收入账票比对结果单-主表 t_tcvat_acc_inv_comp

- **表名称：** 收入账票比对结果单-主表
- **表名：** t_tcvat_acc_inv_comp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbqkpwqqramtsum | 本期开票，往期确认金额合计 | numeric | 23 | 10 | √ | 0 | 本期开票，往期确认金额合计 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fbqwkpbqqramtsum | 本期未开票，本期确认金额合计 | numeric | 23 | 10 | √ | 0 | 本期未开票，本期确认金额合计 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fwfstartdate | 核销期间.开始 | timestamp | 0 |  |  | null | 核销期间.开始 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |
| 12 | fenddate | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 13 | fwfenddate | 核销期间.结束 | timestamp | 0 |  |  | null | 核销期间.结束 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fstartdate | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |
| 16 | fwqkpbqqramtsum | 往期开票，本期确认金额合计 | numeric | 23 | 10 | √ | 0 | 往期开票，本期确认金额合计 |
| 17 | fbqkpbqqramtsum | 本期开票，本期确认金额合计 | numeric | 23 | 10 | √ | 0 | 本期开票，本期确认金额合计 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbqkpbqwqramtsum | 本期开票，本期未确认金额合计 | numeric | 23 | 10 | √ | 0 | 本期开票，本期未确认金额合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_acc_inv_comp |  | fid |
| 2 | idx_t_tcvat_acc_inv_comp |  | forgid,fwriteofftypeid,fstartdate,fenddate |

---

## 往期开票，本期确认收入-子表 t_tcvat_acc_invcomp_ent1

- **表名称：** 往期开票，本期确认收入-子表
- **表名：** t_tcvat_acc_invcomp_ent1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fje | 凭证金额 | numeric | 23 | 10 | √ | 0 | 凭证金额 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 4 | fpzhh | 凭证行号 | varchar | 50 |  | √ | ' ' | 凭证行号 |
| 5 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 6 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 7 | finvoicestatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 7 :作废中 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpzjzdate | 凭证记账日期 | timestamp | 0 |  |  | null | 凭证记账日期 |
| 10 | faccperiod | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 11 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :增值税专用发票 025 :增值税普通发票（卷票） 10xdp :全电发票（普通发票） 08xdp :全电发票（增值税专用发票） |
| 12 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 13 | fcurwfdata | 本期核销金额 | numeric | 23 | 10 | √ | 0 | 本期核销金额 |
| 14 | fbalance | 科目名称 | varchar | 36 |  | √ | ' ' | [科目 tdm_account](../tdm_files/tdm_account.md) |
| 15 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 16 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 17 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 18 | fwfdate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 19 | fbuyername | 购方名称 | varchar | 50 |  | √ | ' ' | 购方名称 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fkjpzh | 会计凭证号 | varchar | 50 |  | √ | ' ' | 会计凭证号 |
| 22 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 23 | fwriteofftype | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |
| 24 | fbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_acc_invcomp_ent1 |  | fentryid |
| 2 | idx_tcvat_acc_invcomp_ent1_fk |  | fid |

---

## 本期开票，往期确认收入-子表 t_tcvat_acc_invcomp_ent2

- **表名称：** 本期开票，往期确认收入-子表
- **表名：** t_tcvat_acc_invcomp_ent2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fje | 凭证金额 | numeric | 23 | 10 | √ | 0 | 凭证金额 |
| 3 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 4 | fpzhh | 凭证行号 | varchar | 50 |  | √ | ' ' | 凭证行号 |
| 5 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 6 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 7 | finvoicestatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 7 :作废中 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpzjzdate | 凭证记账日期 | timestamp | 0 |  |  | null | 凭证记账日期 |
| 10 | faccperiod | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 11 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :增值税专用发票 025 :增值税普通发票（卷票） 10xdp :全电发票（普通发票） 08xdp :全电发票（增值税专用发票） |
| 12 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 13 | fcurwfdata | 本期核销金额 | numeric | 23 | 10 | √ | 0 | 本期核销金额 |
| 14 | fbalance | 科目名称 | varchar | 36 |  | √ | ' ' | [科目 tdm_account](../tdm_files/tdm_account.md) |
| 15 | finvoiceamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 16 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 17 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 18 | fwfdate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 19 | fbuyername | 购方名称 | varchar | 50 |  | √ | ' ' | 购方名称 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fkjpzh | 会计凭证号 | varchar | 50 |  | √ | ' ' | 会计凭证号 |
| 22 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 23 | fwriteofftype | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |
| 24 | fbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_acc_invcomp_ent2 |  | fentryid |
| 2 | idx_tcvat_acc_invcomp_ent2_fk |  | fid |

---

## 本期未开票，本期确认收入-子表 t_tcvat_acc_invcomp_ent3

- **表名称：** 本期未开票，本期确认收入-子表
- **表名：** t_tcvat_acc_invcomp_ent3

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fje | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | fpzhh | 凭证行号 | varchar | 50 |  | √ | ' ' | 凭证行号 |
| 4 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 5 | fbalance | 科目名称 | varchar | 36 |  | √ | ' ' | [科目 tdm_account](../tdm_files/tdm_account.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fpzjzdate | 凭证记账日期 | timestamp | 0 |  |  | null | 凭证记账日期 |
| 8 | fnowriteoff | 未核销金额 | numeric | 23 | 10 | √ | 0 | 未核销金额 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fkjpzh | 会计凭证号 | varchar | 50 |  | √ | ' ' | 会计凭证号 |
| 11 | fbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_acc_invcomp_ent3_fk |  | fid |
| 2 | pk_tcvat_acc_invcomp_ent3 |  | fentryid |

---

## 本期开票，本期未确认收入-子表 t_tcvat_acc_invcomp_ent4

- **表名称：** 本期开票，本期未确认收入-子表
- **表名：** t_tcvat_acc_invcomp_ent4

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 4 | finvoicestatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 7 :作废中 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnowriteofftax | 未核销税额 | numeric | 23 | 10 | √ | 0 | 未核销税额 |
| 7 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 026 :增值税电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :增值税专用发票 025 :增值税普通发票（卷票） 10xdp :全电发票（普通发票） 08xdp :全电发票（增值税专用发票） |
| 8 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 9 | finvoiceamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 10 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 11 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 12 | fbuyername | 购方名称 | varchar | 50 |  | √ | ' ' | 购方名称 |
| 13 | fnowriteoff | 未核销金额 | numeric | 23 | 10 | √ | 0 | 未核销金额 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_acc_invcomp_ent4 |  | fentryid |
| 2 | idx_tcvat_acc_invcomp_ent4_fk |  | fid |
