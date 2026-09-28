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
| 4 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 5 | fusestatusid | 使用状态 | int8 | 64 |  | √ | 0 | [使用状态 fa_usestatus](../fa_files/fa_usestatus.md) |
| 6 | fflexauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
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
| 20 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 21 | freceivablesid | 应收款项性质 | int8 | 64 |  | √ | 0 | [应付款项性质 ap_payproperty](../ap_files/ap_payproperty.md) |
| 22 | ftext5 | ##文本5 | varchar | 100 |  | √ | ' ' | ##文本5 |
| 23 | ftext6 | ##文本6 | varchar | 100 |  | √ | ' ' | ##文本6 |
| 24 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | ftext7 | ##文本7 | varchar | 100 |  | √ | ' ' | ##文本7 |
| 26 | ftext8 | ##文本8 | varchar | 100 |  | √ | ' ' | ##文本8 |
| 27 | ftext9 | ##文本9 | varchar | 100 |  | √ | ' ' | ##文本9 |
| 28 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | ftripexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | [差旅项目 er_tripexpenseitem](../em_files/er_tripexpenseitem.md) |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 31 | fdecimal10 | ##小数10 | numeric | 23 | 10 | √ | 0 | ##小数10 |
| 32 | flotid | 批号 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 33 | fperiod | fperiod | int8 | 64 |  | √ | 0 |  |
| 34 | fborrowerid | 借款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 36 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 37 | fassistantdata1 | ##辅助资料1 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 38 | freceivingbilltypeid | 收款类型 | int8 | 64 |  | √ | 0 | [收款用途 cas_receivingbilltype](../cas_files/cas_receivingbilltype.md) |
| 39 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 40 | fpayablesid | 应付款项性质 | int8 | 64 |  | √ | 0 | [应付款项性质 ap_payproperty](../ap_files/ap_payproperty.md) |
| 41 | fproject2id | 项目2 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 42 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 43 | faccountbanksid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 44 | fexpenseitemeditid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 45 | fassistantdata12 | ##辅助资料12 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 46 | fassistantdata11 | ##辅助资料11 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 47 | fassistantdata10 | ##辅助资料10 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 48 | finvschemeid | 库存事务 | int8 | 64 |  | √ | 0 | [库存事务 im_invscheme](../im_files/im_invscheme.md) |
| 49 | fassistantdata16 | ##辅助资料16 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 50 | fassistantdata15 | ##辅助资料15 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 51 | fassistantdata14 | ##辅助资料14 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 52 | fassistantdata13 | ##辅助资料13 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 53 | fassistantdata7 | ##辅助资料7 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 54 | fassistantdata6 | ##辅助资料6 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 55 | fassistantdata19 | ##辅助资料19 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 56 | fassistantdata9 | ##辅助资料9 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 57 | fassistantdata18 | ##辅助资料18 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 58 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 59 | fassistantdata8 | ##辅助资料8 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 60 | fassistantdata17 | ##辅助资料17 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 61 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fassistantdata3 | ##辅助资料3 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 63 | fassistantdata2 | ##辅助资料2 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 64 | fbatchid | 批次 | varchar | 64 |  | √ | ' ' | 批次 |
| 65 | fassistantdata5 | ##辅助资料5 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 66 | ftext1 | 发票类型 | varchar | 100 |  | √ | ' ' | 发票类型 |
| 67 | fassetcategoryid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 68 | fassistantdata4 | ##辅助资料4 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 69 | ftext2 | ##文本2 | varchar | 100 |  | √ | ' ' | ##文本2 |
| 70 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 71 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 72 | fcurrency | fcurrency | int8 | 64 |  | √ | 0 |  |
| 73 | ffundflowitemid | 资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 74 | fpayeeid | 收款人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 75 | fvouchertypeid | 凭证类型 | int8 | 64 |  | √ | 0 | [凭证字 gl_vouchertype](../gl_files/gl_vouchertype.md) |
| 76 | fassistantdata20 | ##辅助资料20 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 77 | fuseorgid | 使用部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |

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
