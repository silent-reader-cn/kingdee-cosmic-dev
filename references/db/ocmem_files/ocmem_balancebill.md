# 费用预算单-ocmem_balancebill

## 单据体-子表 t_ocmem_budgetbillentry

- **表名称：** 单据体-子表
- **表名：** t_ocmem_budgetbillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 预算承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 5 | fitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 8 | famount | 预算金额 | numeric | 23 | 10 | √ | 0 | 预算金额 |
| 9 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fitemid | 预算产品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_budgetbillentry_fid |  | fid |
| 2 | pk_ocmem_budgetbillentry |  | fentryid |

---

## 费用预算单-主表 t_ocmem_budgetbill

- **表名称：** 费用预算单-主表
- **表名：** t_ocmem_budgetbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 预算公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftotalamount | 预算总金额 | numeric | 23 | 10 | √ | 0 | 预算总金额 |
| 7 | fbudgetorgid | 预算编制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbudgetmonthid | 预算月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 9 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 14 | fbudgetdescription | 预算说明 | varchar | 255 |  | √ | ' ' | 预算说明 |
| 15 | fbudgetname | 预算名称 | varchar | 510 |  | √ | ' ' | 预算名称 |
| 16 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fdimension | 预算周期维度 | bpchar | 1 |  | √ | 'A' | 预算周期维度,枚举: A :按年 B :按月 |
| 20 | fbudgetdescription_tag | 预算说明_详情 | text | 0 |  |  | null | 预算说明_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_budgetbill |  | fid |
| 2 | idx_ocmem_budgetbill_no |  | fbillno |
