# 收入账票核销记录查询-tcvat_wfrecord

## 单据体-子表 t_tcvat_wfrecord_detail

- **表名称：** 单据体-子表
- **表名：** t_tcvat_wfrecord_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbackwfop | 操作 | varchar | 50 |  | √ | ' ' | 操作 |
| 3 | fassbchxje | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 4 | ftaxrate | 税率 | varchar | 50 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.15 :15% 0.16 :16% 0.17 :17% |
| 5 | fzpcy | 账票差异 | varchar | 50 |  | √ | ' ' | 账票差异,枚举: bqsrbqkp :本期收入，本期开票 bqsrwqkp :本期收入，往期开票 wqsrbqkp :往期收入，本期开票 yjcy :永久差异 |
| 6 | fbillqty | 数量-主 | numeric | 23 | 10 | √ | 0 | 数量-主 |
| 7 | finvoicestatus | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 7 :作废中 |
| 8 | fassbillid | 单据ID-辅 | int8 | 64 |  | √ | 0 | 单据ID-辅 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fgoodsname | 商品名称 | varchar | 300 |  | √ | ' ' | 商品名称 |
| 11 | fassbillqty | 数量-辅 | numeric | 23 | 10 | √ | 0 | 数量-辅 |
| 12 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 13 | fassbillno | 单据编号-辅 | varchar | 50 |  | √ | ' ' | 单据编号-辅 |
| 14 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 15 | fassbilltype | 单据类型-辅 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fbuyername | 购方名称 | varchar | 150 |  | √ | ' ' | 购方名称 |
| 17 | fmainwfinfo_tag | 核销详情-主_详情 | text | 0 |  |  | null | 核销详情-主_详情 |
| 18 | fkjpzh | 会计凭证号 | varchar | 50 |  | √ | ' ' | 会计凭证号 |
| 19 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 20 | fbillno | 科目编码 | varchar | 50 |  | √ | ' ' | 科目编码 |
| 21 | fqty | 核销数量-主 | numeric | 23 | 10 | √ | 0 | 核销数量-主 |
| 22 | fassbillentryid | 单据分录ID-辅 | int8 | 64 |  | √ | 0 | 单据分录ID-辅 |
| 23 | fje | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 24 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 25 | fassunit | 计量单位-辅 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fpzhh | 凭证行号 | varchar | 50 |  | √ | ' ' | 凭证行号 |
| 27 | fverifymatch | 核销匹配 | varchar | 150 |  | √ | ' ' | 核销匹配 |
| 28 | fmainwfinfo | 核销详情-主 | varchar | 255 |  | √ | ' ' | 核销详情-主 |
| 29 | fasswfinfo_tag | 核销详情-辅_详情 | text | 0 |  |  | null | 核销详情-辅_详情 |
| 30 | fbchxje | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 31 | fpzjzdate | 凭证记账日期 | timestamp | 0 |  |  | null | 凭证记账日期 |
| 32 | faccperiod | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间,枚举: 01 :01 02 :02 03 :03 04 :04 05 :05 06 :06 07 :07 08 :08 09 :09 10 :10 11 :11 12 :12 |
| 33 | fbillentryid | 单据分录ID-主 | int8 | 64 |  | √ | 0 | 单据分录ID-主 |
| 34 | finvoicetype | 发票种类 | varchar | 50 |  | √ | ' ' | 发票种类,枚举: 026 :增值税电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :增值税专用发票 025 :增值税普通发票（卷票） 10xdp :全电发票（普通发票） 08xdp :全电发票（增值税专用发票） |
| 35 | finvoiceamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 36 | fassqty | 核销数量-辅 | numeric | 23 | 10 | √ | 0 | 核销数量-辅 |
| 37 | fbillid | 单据ID-主 | int8 | 64 |  | √ | 0 | 单据ID-主 |
| 38 | fbalanceid | 科目名称 | varchar | 36 |  | √ | ' ' | [科目 tdm_account](../tdm_files/tdm_account.md) |
| 39 | fasswfinfo | 核销详情-辅 | varchar | 255 |  | √ | ' ' | 核销详情-辅 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fbilltype | 单据类型-主 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 42 | funit | 计量单位-主 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fsummary | 摘要 | varchar | 2000 |  | √ | ' ' | 摘要 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_wfrecord_detail |  | fentryid |
| 2 | idx_tcvat_wfrecord_detail_fk |  | fid |

---

## 收入账票核销记录查询-主表 t_tcvat_wfrecord

- **表名称：** 收入账票核销记录查询-主表
- **表名：** t_tcvat_wfrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 核销批号 | varchar | 50 |  | √ | ' ' | 核销批号 |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcreatorid | 核销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 8 | fheadwfinfo | 核销详情 | varchar | 255 |  | √ | ' ' | 核销详情 |
| 9 | fwfnumber | 核销编码 | varchar | 30 |  | √ | ' ' | 核销编码 |
| 10 | fheadwfinfo_tag | 核销详情_详情 | text | 0 |  |  | null | 核销详情_详情 |
| 11 | fwriteofftypeid | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_wfrecord |  | ftaxorg,fwriteofftypeid |
| 2 | pk_tcvat_wfrecord |  | fid |
