# 凭证中间表-pa_dsvoucherdata

## 凭证中间表-主表 t_pa_dsvoucherdata

- **表名称：** 凭证中间表-主表
- **表名：** t_pa_dsvoucherdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fextid | 来源ID | varchar | 64 |  | √ | ' ' | 来源ID |
| 3 | ftext10 | ##文本10 | varchar | 100 |  | √ | ' ' | ##文本10 |
| 4 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |
| 5 | fusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态 fa_usestatus |
| 6 | fflexauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 7 | faccount | faccount | int8 | 64 |  | √ | 0 |  |
| 8 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 9 | fdecimal4 | ##小数4 | numeric | 23 | 10 | √ | 0 | ##小数4 |
| 10 | fdecimal3 | ##小数3 | numeric | 23 | 10 | √ | 0 | ##小数3 |
| 11 | fdecimal6 | ##小数6 | numeric | 23 | 10 | √ | 0 | ##小数6 |
| 12 | fdecimal5 | ##小数5 | numeric | 23 | 10 | √ | 0 | ##小数5 |
| 13 | fdecimal8 | ##小数8 | numeric | 23 | 10 | √ | 0 | ##小数8 |
| 14 | fdecimal7 | ##小数7 | numeric | 23 | 10 | √ | 0 | ##小数7 |
| 15 | fdecimal9 | ##小数9 | numeric | 23 | 10 | √ | 0 | ##小数9 |
| 16 | fdecimal2 | 本期贷方 | numeric | 23 | 10 | √ | 0 | 本期贷方 |
| 17 | fdecimal1 | 本期借方 | numeric | 23 | 10 | √ | 0 | 本期借方 |
| 18 | ftext3 | ##文本3 | varchar | 100 |  | √ | ' ' | ##文本3 |
| 19 | ftext4 | ##文本4 | varchar | 100 |  | √ | ' ' | ##文本4 |
| 20 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 21 | freceivablesid | 应收款项性质 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 22 | ftext5 | ##文本5 | varchar | 100 |  | √ | ' ' | ##文本5 |
| 23 | ftext6 | ##文本6 | varchar | 100 |  | √ | ' ' | ##文本6 |
| 24 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 25 | ftext7 | ##文本7 | varchar | 100 |  | √ | ' ' | ##文本7 |
| 26 | ftext8 | ##文本8 | varchar | 100 |  | √ | ' ' | ##文本8 |
| 27 | ftext9 | ##文本9 | varchar | 100 |  | √ | ' ' | ##文本9 |
| 28 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 29 | ftripexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | 差旅项目 er_tripexpenseitem |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | fdecimal10 | ##小数10 | numeric | 23 | 10 | √ | 0 | ##小数10 |
| 32 | flotid | 批号 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 33 | fperiod | fperiod | int8 | 64 |  | √ | 0 |  |
| 34 | fborrowerid | 借款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 36 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 37 | fassistantdata1 | ##辅助资料1 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 38 | freceivingbilltypeid | 收款类型 | int8 | 64 |  | √ | 0 | 收款用途 cas_receivingbilltype |
| 39 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 40 | fpayablesid | 应付款项性质 | int8 | 64 |  | √ | 0 | 应付款项性质 ap_payproperty |
| 41 | fproject2id | 项目2 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 42 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | 配置号 bd_configuredcode |
| 43 | faccountbanksid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 44 | fexpenseitemeditid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 45 | fassistantdata12 | ##辅助资料12 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 46 | fassistantdata11 | ##辅助资料11 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 47 | fassistantdata10 | ##辅助资料10 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 48 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | 库存事务 im_invscheme |
| 49 | fassistantdata16 | ##辅助资料16 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 50 | fassistantdata15 | ##辅助资料15 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 51 | fassistantdata14 | ##辅助资料14 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 52 | fassistantdata13 | ##辅助资料13 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 53 | fassistantdata7 | ##辅助资料7 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 54 | fassistantdata6 | ##辅助资料6 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 55 | fassistantdata19 | ##辅助资料19 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 56 | fassistantdata9 | ##辅助资料9 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 57 | fassistantdata18 | ##辅助资料18 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 58 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 59 | fassistantdata8 | ##辅助资料8 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 60 | fassistantdata17 | ##辅助资料17 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 61 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 62 | fassistantdata3 | ##辅助资料3 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 63 | fassistantdata2 | ##辅助资料2 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 64 | fbatchid | 批次 | varchar | 64 |  | √ | ' ' | 批次 |
| 65 | fassistantdata5 | ##辅助资料5 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 66 | ftext1 | 发票类型 | varchar | 100 |  | √ | ' ' | 发票类型 |
| 67 | fassetcategoryid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 68 | fassistantdata4 | ##辅助资料4 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 69 | ftext2 | ##文本2 | varchar | 100 |  | √ | ' ' | ##文本2 |
| 70 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 71 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 72 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 73 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | 资金用途 cas_fundflowitem |
| 74 | fpayeeid | 收款人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 75 | fvouchertypeid | 凭证类型 | int8 | 64 |  | √ | 0 | 凭证字 gl_vouchertype |
| 76 | fassistantdata20 | ##辅助资料20 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 77 | fuseorgid | 使用部门 | int8 | 64 |  | √ | 0 | 行政组织（部门） bos_adminorg |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | uk_pa_dsvoucherdata |  | fextid |
| 2 | pk_t_pa_dsvoucherdata |  | fid |
| 3 | idx_pa_org_period |  | forg,fperiod |
