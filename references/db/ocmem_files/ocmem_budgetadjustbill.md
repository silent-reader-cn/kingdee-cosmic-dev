# 预算调整单-ocmem_budgetadjustbill

## 调整明细-子表 t_ocmem_bcadjustentry

- **表名称：** 调整明细-子表
- **表名：** t_ocmem_bcadjustentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetbalanceid | 预算编码 | int8 | 64 |  | √ | 0 | 预算余额表 ocdbd_budgetbalance |
| 3 | forgid | 预算承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fregionid | 所属大区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | foldamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 8 | fitemid | 预算产品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 9 | fadjustamount | 调整金额 | numeric | 23 | 10 | √ | 0 | 调整金额 |
| 10 | fnewamount | 调整后可用余额 | numeric | 23 | 10 | √ | 0 | 调整后可用余额 |
| 11 | fprovinceid | 所属省区 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 13 | fyear | fyear | timestamp | 0 |  |  | null |  |
| 14 | fchannelid | 渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_bcadjustentry |  | fentryid |
| 2 | idx_ocmem_bcadjustentry_bbid |  | fbudgetbalanceid |
| 3 | idx_ocmem_bcadjustentry_fid |  | fid |

---

## 预算调整单-关联追踪表 t_ocmem_bcadjustbill_tc

- **表名称：** 预算调整单-关联追踪表
- **表名：** t_ocmem_bcadjustbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_bcadjustbill_tc_tid |  | ftid |
| 2 | idx_ocmem_bcadjustbill_tc_tbill |  | ftbillid |
| 3 | pk_ocmem_bcadjustbill_tc |  | fid |

---

## 关联子实体-子表 t_ocmem_bcadjustentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ocmem_bcadjustentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_bcadjustentry_lk |  | fpkid |
| 2 | idx_ocmem_bcadjustentry_lk_fk |  | fentryid |

---

## 预算调整单-主表 t_ocmem_bcadjustbill

- **表名称：** 预算调整单-主表
- **表名：** t_ocmem_bcadjustbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 预算公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbudgetorgid | 预算编制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbudgetmonthid | 预算月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fadjusttype | 调整类型 | bpchar | 1 |  | √ | ' ' | 调整类型,枚举: A :总额不变 B :总额增减 |
| 13 | fbizdate | 调整日期 | timestamp | 0 |  |  | null | 调整日期 |
| 14 | fbillsource | 单据来源 | bpchar | 1 |  | √ | 'A' | 单据来源,枚举: A :手工创建 B :预算滚动 C :费率变更 |
| 15 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 16 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 17 | fmonthid | fmonthid | int8 | 64 |  | √ | 0 |  |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fdimension | 预算周期维度 | bpchar | 1 |  | √ | 'A' | 预算周期维度,枚举: A :按年 B :按月 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_bcadjustbill_no |  | fbillno |
| 2 | pk_ocmem_bcadjustbill |  | fid |

---

## 预算调整单-反写记录表 t_ocmem_bcadjustbill_wb

- **表名称：** 预算调整单-反写记录表
- **表名：** t_ocmem_bcadjustbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_bcadjustbill_wb_fk |  | fid |
| 2 | pk_ocmem_bcadjustbill_wb |  | fentryid |

---

## 调整明细-分表 t_ocmem_bcadjustentry_c

- **表名称：** 调整明细-分表
- **表名：** t_ocmem_bcadjustentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpoolitemclassid | 关联数据源计算商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 3 | fpoolchannelid | 关联数据源渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 4 | fcalallocationrate | 计算分配比例% | numeric | 23 | 10 | √ | 0 | 计算分配比例% |
| 5 | fcalamount | 关联计算金额 | numeric | 23 | 10 | √ | 0 | 关联计算金额 |
| 6 | fruletype | 关联费率规则 | bpchar | 1 |  | √ | ' ' | 关联费率规则,枚举: A :金额比例 B :单位费用金额 |
| 7 | ftotalsalerate | 关联计算费率值 | numeric | 23 | 10 | √ | 0 | 关联计算费率值 |
| 8 | fpoolentryid | 关联数据源分录id | int8 | 64 |  | √ | 0 | 关联数据源分录id |
| 9 | frollruleid | 关联变动费率规则 | int8 | 64 |  | √ | 0 | 变动费率规则 ocmem_rollraterule |
| 10 | fcalunitid | 关联计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | frollruleentryid | 关联规则分录id | int8 | 64 |  | √ | 0 | 关联规则分录id |
| 12 | fcalqty | 关联计算数量 | numeric | 23 | 10 | √ | 0 | 关联计算数量 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | fruleitemid | 关联规则商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 15 | fruleitemclassid | 关联规则商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 16 | fversion | 关联版本号 | int4 | 32 |  | √ | 0 | 关联版本号 |
| 17 | fpoolitemid | 关联数据源商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_bcadjustentry_c_fid |  | fid |
| 2 | pk_ocmem_bcadjustentry_c |  | fentryid |
