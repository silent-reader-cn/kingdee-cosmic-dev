# 税金缴纳/退还-gtcp_taxpay_refund_bill

## 税金缴纳/退还-主表 t_gtcp_taxpay_refund_bill

- **表名称：** 税金缴纳/退还-主表
- **表名：** t_gtcp_taxpay_refund_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaxestype | 税金类别 | varchar | 50 |  | √ | ' ' | 税金类别,枚举: pay :缴税 refund :退税 |
| 3 | fpayrefunddate | 缴/退税时间 | timestamp | 0 |  |  | null | 缴/退税时间 |
| 4 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 5 | forg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 9 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 10 | fdatasouce | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :计税底稿 2 :手工登记 |
| 11 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 12 | fbillno | 税金编号 | varchar | 100 |  | √ | ' ' | 税金编号 |
| 13 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 14 | fdraftid | 底稿id | int8 | 64 |  | √ | 0 | 申报底稿列表 gtcp_normal_draft_list |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fpayrefstatus | 缴/退税状态 | varchar | 50 |  | √ | ' ' | 缴/退税状态,枚举: nopay :未缴税 pay :已缴税 noneedpay :无需缴税 norefund :未退税 refund :已退税 noneedrefund :无需退税 |
| 19 | fdraftnumber | 底稿编号 | varchar | 200 |  | √ | ' ' | 底稿编号 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 22 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 23 | fcoin | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fpaymentenddate | 缴款截止日 | timestamp | 0 |  |  | null | 缴款截止日 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtcp_taxpay_refund_bill |  | fid |
| 2 | idx_gtcp_taxpayrb_org |  | forg,ftaxsystem,ftaxtype,ftaxareagroup |
