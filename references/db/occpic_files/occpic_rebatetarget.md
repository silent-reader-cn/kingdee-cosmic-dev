# 政策目标-occpic_rebatetarget

## 关联子实体-子表 t_occpic_rebatetarget_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_rebatetarget_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rebatetarget_lk_fk |  | fid |
| 2 | pk_occpic_rebatetarget_lk |  | fpkid |

---

## 政策目标-主表 t_occpic_rebatetarget

- **表名称：** 政策目标-主表
- **表名：** t_occpic_rebatetarget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablecaltime | 启用计算时间 | timestamp | 0 |  |  | null | 启用计算时间 |
| 3 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | [费用活动方案 ocmem_activityplan_f7](../ocmem_files/ocmem_activityplan_f7.md) |
| 4 | faccrualformulaid | 预提计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 5 | fnrebateclassid | 返利类别 | int8 | 64 |  | √ | 0 | [返利类别 msrcs_rebateclass](../msrcs_files/msrcs_rebateclass.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbnfcustomerid | 返利客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fpushtype | 政策生成目标控制 | bpchar | 1 |  | √ | 'A' | 政策生成目标控制,枚举: A :审核自动生成全部 B :自动生成到上一结算周期 C :手工指定结算周期生成 |
| 11 | fgroupkey | 分组依据 | int8 | 64 |  | √ | 0 | 分组依据 |
| 12 | fcustomdaterange | 手动下推格式化有效期 | varchar | 2000 |  | √ | ' ' | 手动下推格式化有效期 |
| 13 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 14 | fpresettle | 是否预结算 | bpchar | 1 |  | √ | '0' | 是否预结算 |
| 15 | fbaselineamount | 基线金额 | numeric | 23 | 10 | √ | 0 | 基线金额 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fname | 目标名称 | varchar | 255 |  | √ | ' ' | 目标名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsettperiod | 结算周期 | bpchar | 1 |  | √ | ' ' | 结算周期,枚举: C :按周 B :按月 E :按季度 A :按年 D :全生命周期 |
| 20 | fbaselineqty | 基线数量 | numeric | 23 | 10 | √ | 0 | 基线数量 |
| 21 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已失效 |
| 23 | fcalculatestatus | 计算状态 | bpchar | 1 |  | √ | 'A' | 计算状态,枚举: A :未开始计算 B :需要计算 C :计算结束 D :手工结束 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 26 | fbnfchannelclassid | 渠道分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 27 | fdescription | 政策说明 | varchar | 255 |  | √ | ' ' | 政策说明 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fpolicyid | 返利政策 | int8 | 64 |  | √ | 0 | [返利政策F7 ocdbd_rebatepolicyf7](../occpic_files/ocdbd_rebatepolicyf7.md) |
| 30 | fstarttime | 目标有效期.开始 | timestamp | 0 |  |  | null | 目标有效期.开始 |
| 31 | fcalscopetype | 政策设置方式 | bpchar | 1 |  | √ | ' ' | 政策设置方式,枚举: A :一个政策只定义一组条件政策 B :一个政策可定义多组条件政策 |
| 32 | fbnfchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 33 | fbalanceorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fcalbilltypeid | 考核业务数据类型 | int8 | 64 |  | √ | 0 | [业务数据类型 ocdbd_bizdatatype](../occpic_files/ocdbd_bizdatatype.md) |
| 35 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 36 | fendtime | 目标有效期.结束 | timestamp | 0 |  |  | null | 目标有效期.结束 |
| 37 | fcurrencyid | 考核币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fbnfcustomerclassid | 客户分类 | int8 | 64 |  | √ | 0 | [客户分类 bd_customergroup](../basedata_files/bd_customergroup.md) |
| 40 | fkpiid | 政策类型 | int8 | 64 |  | √ | 0 | [政策类型 ocdbd_kpi](../occpic_files/ocdbd_kpi.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_rebatetarget |  | fid |
| 2 | idx_occpic_rbtgt_chl |  | fbnfchannelid |
| 3 | idx_occpic_rbtgt_efftime |  | fstarttime,fendtime |
| 4 | idx_occpic_rbtgt_policy |  | fpolicyid |
| 5 | idx_occpic_rbtgt_bno |  | fbillno |

---

## 政策目标-关联追踪表 t_occpic_rebatetarget_tc

- **表名称：** 政策目标-关联追踪表
- **表名：** t_occpic_rebatetarget_tc

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
| 1 | idx_occpic_rebatetarget_tc_tid |  | ftid |
| 2 | pk_occpic_rebatetarget_tc |  | fid |
| 3 | idx_occpic_rebatetarget_tc_tbill |  | ftbillid |

---

## 分组返利标准-子表 t_occpic_rbtgt_itemfomul

- **表名称：** 分组返利标准-子表
- **表名：** t_occpic_rbtgt_itemfomul

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
| 1 | pk_occpic_rbtgt_itemfomul |  | fentryid |
| 2 | idx_occpic_rbtgtitemfomul_fid |  | fid |

---

## 政策目标-反写记录表 t_occpic_rebatetarget_wb

- **表名称：** 政策目标-反写记录表
- **表名：** t_occpic_rebatetarget_wb

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
| 1 | pk_occpic_rebatetarget_wb |  | fentryid |
| 2 | idx_occpic_rebatetarget_wb_fk |  | fid |

---

## 返利商品-子表 t_occpic_rbtgt_itemclass

- **表名称：** 返利商品-子表
- **表名：** t_occpic_rbtgt_itemclass

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
| 1 | pk_occpic_rbtgt_itemclass |  | fentryid |
| 2 | idx_occpic_rbtgtitemclass_fid |  | fid |

---

## 返利标准-子表 t_occpic_rbtgt_form_dt

- **表名称：** 返利标准-子表
- **表名：** t_occpic_rbtgt_form_dt

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
| 1 | idx_occpic_rbtgtformdt_fid |  | fid |
| 2 | pk_occpic_rbtgt_form_dt |  | fentryid |
