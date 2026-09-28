# 返利政策-occpic_rebatepolicy

## 返利标准-子表 t_occpic_rp_formula

- **表名称：** 返利标准-子表
- **表名：** t_occpic_rp_formula

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fafixedamount | 预提固定金额 | numeric | 23 | 10 | √ | 0 | 预提固定金额 |
| 3 | fminachive | ≥达成率最小值 | numeric | 23 | 10 | √ | 0 | ≥达成率最小值 |
| 4 | fmaxamount | <金额最大值 | numeric | 23 | 10 | √ | 0 | <金额最大值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | farebateamount | 预提单位返利金额 | numeric | 23 | 10 | √ | 0 | 预提单位返利金额 |
| 7 | fminamount | ≥金额最小值 | numeric | 23 | 10 | √ | 0 | ≥金额最小值 |
| 8 | frebateamount | 单位返利金额 | numeric | 23 | 10 | √ | 0 | 单位返利金额 |
| 9 | faictpercent | 预提返点率% | numeric | 23 | 10 | √ | 0 | 预提返点率% |
| 10 | fmaxqty | <数量最大值 | numeric | 23 | 10 | √ | 0 | <数量最大值 |
| 11 | fictpercent | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 12 | ffixedamount | 固定金额 | numeric | 23 | 10 | √ | 0 | 固定金额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fminqty | ≥数量最小值 | numeric | 23 | 10 | √ | 0 | ≥数量最小值 |
| 15 | fmaxachive | <达成率最大值 | numeric | 23 | 10 | √ | 0 | <达成率最大值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_rp_formula |  | fentryid |
| 2 | idx_occpic_rpformula_fid |  | fid |

---

## 返利商品-子表 t_occpic_rp_itemclass

- **表名称：** 返利商品-子表
- **表名：** t_occpic_rp_itemclass

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 4 | fmaterialclassid | 物料分类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_rp_itemclass |  | fentryid |
| 2 | idx_occpic_rpitemclass_fid |  | fid |

---

## 返利政策-主表 t_occpic_rebatepolicy

- **表名称：** 返利政策-主表
- **表名：** t_occpic_rebatepolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 3 | faccrualformulaid | 预提计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 4 | fnrebateclassid | 返利类别 | int8 | 64 |  | √ | 0 | [返利类别 msrcs_rebateclass](../msrcs_files/msrcs_rebateclass.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fpushtype | 政策生成目标控制 | bpchar | 1 |  | √ | 'A' | 政策生成目标控制,枚举: A :审核自动生成全部 B :自动生成到上一结算周期 C :手工指定结算周期生成 |
| 9 | fcustomdaterange | 手动下推格式化有效期 | varchar | 2000 |  | √ | ' ' | 手动下推格式化有效期 |
| 10 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 11 | fbaselineamount | 基线金额 | numeric | 23 | 10 | √ | 0 | 基线金额 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 政策名称 | varchar | 80 |  | √ | ' ' | 政策名称 |
| 15 | fsettperiod | 结算周期 | bpchar | 1 |  | √ | ' ' | 结算周期,枚举: C :按周 B :按月 E :按季度 A :按年 D :全生命周期 |
| 16 | fbaselineqty | 基线数量 | numeric | 23 | 10 | √ | 0 | 基线数量 |
| 17 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已失效 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fdescription | 政策说明 | varchar | 255 |  | √ | ' ' | 政策说明 |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fstarttime | 政策有效期.开始 | timestamp | 0 |  |  | null | 政策有效期.开始 |
| 24 | fcalscopetype | 政策设置方式 | bpchar | 1 |  | √ | ' ' | 政策设置方式,枚举: A :一个政策只定义一组条件政策 B :一个政策可定义多组条件政策 |
| 25 | fbalanceorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fcalbilltypeid | 考核业务数据类型 | int8 | 64 |  | √ | 0 | [业务数据类型 ocdbd_bizdatatype](../occpic_files/ocdbd_bizdatatype.md) |
| 27 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 28 | fendtime | 政策有效期.结束 | timestamp | 0 |  |  | null | 政策有效期.结束 |
| 29 | fcurrencyid | 政策考核币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fkpiid | 政策类型 | int8 | 64 |  | √ | 0 | [政策类型 ocdbd_kpi](../occpic_files/ocdbd_kpi.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatepolicy_bno |  | fbillno |
| 2 | pk_occpic_rebatepolicy |  | fid |

---

## 返利对象-子表 t_occpic_rp_bnfcust

- **表名称：** 返利对象-子表
- **表名：** t_occpic_rp_bnfcust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fblqty | 基线数量 | numeric | 23 | 10 | √ | 0 | 基线数量 |
| 3 | fchannelclassid | 渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcustomerclassid | 客户分类 | int8 | 64 |  | √ | 0 | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 6 | fblamount | 基线金额 | numeric | 23 | 10 | √ | 0 | 基线金额 |
| 7 | fchannelid | 渠道编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fcustomerid | 客户编码 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rpbnfcust_fid |  | fid |
| 2 | pk_occpic_rp_bnfcust |  | fentryid |

---

## 分组返利标准-子表 t_occpic_rp_itemfomul

- **表名称：** 分组返利标准-子表
- **表名：** t_occpic_rp_itemfomul

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitemarebateamount | 预提单位返利金额 | numeric | 23 | 10 | √ | 0 | 预提单位返利金额 |
| 3 | fitemictpercent | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 4 | fitemmaxqty | <数量最大值 | numeric | 23 | 10 | √ | 0 | <数量最大值 |
| 5 | fitemrebateamount | 单位返利金额 | numeric | 23 | 10 | √ | 0 | 单位返利金额 |
| 6 | fitemblamount | 基线金额 | numeric | 23 | 10 | √ | 0 | 基线金额 |
| 7 | fitemminqty | ≥数量最小值 | numeric | 23 | 10 | √ | 0 | ≥数量最小值 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fitemminamount | ≥金额最小值 | numeric | 23 | 10 | √ | 0 | ≥金额最小值 |
| 10 | fitemaictpercent | 预提返点率% | numeric | 23 | 10 | √ | 0 | 预提返点率% |
| 11 | fgroup | 组号 | int4 | 32 |  | √ | 0 | 组号 |
| 12 | fitemmaxamount | <金额最大值 | numeric | 23 | 10 | √ | 0 | <金额最大值 |
| 13 | fitemfixedamount | 固定金额 | numeric | 23 | 10 | √ | 0 | 固定金额 |
| 14 | fitemmaxachive | <达成率最大值 | numeric | 23 | 10 | √ | 0 | <达成率最大值 |
| 15 | fitemblqty | 基线数量 | numeric | 23 | 10 | √ | 0 | 基线数量 |
| 16 | fconditongroupid | 条件组 | int8 | 64 |  | √ | 0 | [条件组 ocdbd_conditongroup](../occpic_files/ocdbd_conditongroup.md) |
| 17 | fitemminachive | ≥达成率最小值 | numeric | 23 | 10 | √ | 0 | ≥达成率最小值 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fitemafixedamount | 预提固定金额 | numeric | 23 | 10 | √ | 0 | 预提固定金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_rp_itemfomul |  | fentryid |
| 2 | idx_occpic_rpitemfomul_fid |  | fid |
