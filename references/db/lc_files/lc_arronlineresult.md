# 到单记录查询-lc_arronlineresult

## 到单记录查询-主表 t_lc_arronlineresult

- **表名称：** 到单记录查询-主表
- **表名：** t_lc_arronlineresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdocs_tag | 单据集合_详情 | text | 0 |  |  | null | 单据集合_详情 |
| 3 | fwayno | 提（运）单号 | varchar | 50 |  | √ | ' ' | 提（运）单号 |
| 4 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcreditno | 信用证号 | varchar | 50 |  | √ | ' ' | 信用证号 |
| 6 | frdate2 | 二次到单日期 | varchar | 50 |  | √ | ' ' | 二次到单日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcredittype | 信用证类型 | varchar | 50 |  | √ | ' ' | 信用证类型 |
| 9 | fremitamount | 索汇总金额 | numeric | 23 | 10 | √ | 0 | 索汇总金额 |
| 10 | fcreditcurrency | 信用证币种 | varchar | 50 |  | √ | ' ' | 信用证币种 |
| 11 | ffbankcnapscode | 来单银行编号 | varchar | 50 |  | √ | ' ' | 来单银行编号 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fbatchno | 影像批次号 | varchar | 150 |  | √ | ' ' | 影像批次号 |
| 15 | ffilelist_tag | 文件列表_详情 | text | 0 |  |  | null | 文件列表_详情 |
| 16 | flcbillno | 到单单据编号 | varchar | 50 |  | √ | ' ' | 到单单据编号 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | ffdate | 来单日期 | varchar | 50 |  | √ | ' ' | 来单日期 |
| 19 | ffilelistres | 文件列表返回报文 | varchar | 255 |  | √ | ' ' | 文件列表返回报文 |
| 20 | fstartdate | 起算日期 | varchar | 50 |  | √ | ' ' | 起算日期 |
| 21 | ftenor | 付款期限天数 | varchar | 50 |  | √ | ' ' | 付款期限天数 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | ffilestatus | 文件下载状态 | varchar | 50 |  | √ | ' ' | 文件下载状态,枚举: A :下载中 B :下载完成 C :下载失败 |
| 24 | ffbankname | 来单银行名称 | varchar | 255 |  | √ | ' ' | 来单银行名称 |
| 25 | freceivedflag | 到单标识 | varchar | 50 |  | √ | ' ' | 到单标识 |
| 26 | fbilldisdesc_tag | 单据不符点描述_详情 | text | 0 |  |  | null | 单据不符点描述_详情 |
| 27 | fdraftno | 发票号 | varchar | 50 |  | √ | ' ' | 发票号 |
| 28 | famount | 单据金额 | numeric | 23 | 10 | √ | 0 | 单据金额 |
| 29 | fbillinfo | 单据信息 | varchar | 150 |  | √ | ' ' | 单据信息 |
| 30 | freceivedno | 到单编号 | varchar | 50 |  | √ | ' ' | 到单编号 |
| 31 | fstatus | 交易状态 | varchar | 50 |  | √ | ' ' | 交易状态 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fbillcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | ffilelistres_tag | 文件列表返回报文_详情 | text | 0 |  |  | null | 文件列表返回报文_详情 |
| 35 | fprsbankcharge | 交单行费用 | numeric | 23 | 10 | √ | 0 | 交单行费用 |
| 36 | fpayeeaccname | 收款人名称 | varchar | 255 |  | √ | ' ' | 收款人名称 |
| 37 | fbanktype | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 38 | fbanknameaddr | 收款行名称及地址 | varchar | 255 |  | √ | ' ' | 收款行名称及地址 |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fbilldisdesc | 单据不符点描述 | varchar | 255 |  | √ | ' ' | 单据不符点描述 |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fcurrency | 单据币种 | varchar | 50 |  | √ | ' ' | 单据币种 |
| 43 | fopendate | 开证日期 | varchar | 50 |  | √ | ' ' | 开证日期 |
| 44 | fisregister | 登记 | bpchar | 1 |  | √ | '0' | 登记 |
| 45 | fcontractamount | 合同金额 | numeric | 23 | 10 | √ | 0 | 合同金额 |
| 46 | fcontractno | 合同号 | varchar | 50 |  | √ | ' ' | 合同号 |
| 47 | fdocs | 单据集合 | varchar | 255 |  | √ | ' ' | 单据集合 |
| 48 | fduedate | 付款到期日 | varchar | 50 |  | √ | ' ' | 付款到期日 |
| 49 | facptstatus | 承付状态 | varchar | 50 |  | √ | ' ' | 承付状态,枚举: 1 :未承付 2 :已承兑未付款 3 :承兑失败 4 :已付款 5 :付款失败 |
| 50 | fbizdate | 到单日期 | timestamp | 0 |  |  | null | 到单日期 |
| 51 | ffilelist | 文件列表 | varchar | 255 |  | √ | ' ' | 文件列表 |
| 52 | frdate | 到单日期 | varchar | 50 |  | √ | ' ' | 到单日期 |
| 53 | fexplain | 期限描述 | varchar | 255 |  | √ | ' ' | 期限描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_arronlineresult_org |  | forgid |
| 2 | pk_t_lc_arronlineresult |  | fid |
