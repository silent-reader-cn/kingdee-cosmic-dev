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
| 2 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | 费用活动方案 ocmem_activityplan_f7 |
| 3 | fnrebateclassid | 返利类别 | int8 | 64 |  | √ | 0 | 返利类别 msrcs_rebateclass |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fbnfcustomerid | 返利客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fpushtype | 政策生成目标控制 | bpchar | 1 |  | √ | 'A' | 政策生成目标控制,枚举: A :审核自动生成全部 B :自动生成到上一结算周期 C :手工指定结算周期生成 |
| 9 | fcustomdaterange | 手动下推格式化有效期 | varchar | 2000 |  | √ | ' ' | 手动下推格式化有效期 |
| 10 | fpresettle | 是否预结算 | bpchar | 1 |  | √ | '0' | 是否预结算 |
| 11 | fbaselineamount | 基线金额 | numeric | 23 | 10 | √ | 0 | 基线金额 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fname | 目标名称 | varchar | 255 |  | √ | ' ' | 目标名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsettperiod | 结算周期 | bpchar | 1 |  | √ | ' ' | 结算周期,枚举: C :按周 B :按月 E :按季度 A :按年 D :全生命周期 |
| 16 | fbaselineqty | 基线数量 | numeric | 23 | 10 | √ | 0 | 基线数量 |
| 17 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | 返利计算公式库 msrcs_rebateformula |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已失效 |
| 19 | fcalculatestatus | 计算状态 | bpchar | 1 |  | √ | 'A' | 计算状态,枚举: A :未开始计算 B :需要计算 C :计算结束 D :手工结束 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fbnfchannelclassid | 渠道分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 23 | fdescription | 政策说明 | varchar | 255 |  | √ | ' ' | 政策说明 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fpolicyid | 返利政策 | int8 | 64 |  | √ | 0 | 返利政策F7 ocdbd_rebatepolicyf7 |
| 26 | fstarttime | 目标有效期.开始 | timestamp | 0 |  |  | null | 目标有效期.开始 |
| 27 | fcalscopetype | 政策设置方式 | bpchar | 1 |  | √ | ' ' | 政策设置方式,枚举: A :一个政策只定义一组条件政策 B :一个政策可定义多组条件政策 |
| 28 | fbnfchannelid | 返利渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 29 | fbalanceorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fcalbilltypeid | 考核业务数据类型 | int8 | 64 |  | √ | 0 | 业务数据类型 ocdbd_bizdatatype |
| 31 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | 返利计算公式库 msrcs_rebateformula |
| 32 | fendtime | 目标有效期.结束 | timestamp | 0 |  |  | null | 目标有效期.结束 |
| 33 | fcurrencyid | 考核币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fbnfcustomerclassid | 客户分类 | int8 | 64 |  | √ | 0 | 客户分类 bd_customergroup |
| 36 | fkpiid | 政策类型 | int8 | 64 |  | √ | 0 | 政策类型 ocdbd_kpi |

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
| 2 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 4 | fmaterialclassid | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |

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
| 2 | fitemictpercent | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 3 | fitemmaxqty | <数量最大值 | numeric | 23 | 10 | √ | 0 | <数量最大值 |
| 4 | fitemrebateamount | 单位返利金额 | numeric | 23 | 10 | √ | 0 | 单位返利金额 |
| 5 | fitemblamount | 基线金额 | numeric | 23 | 10 | √ | 0 | 基线金额 |
| 6 | fitemminqty | ≥数量最小值 | numeric | 23 | 10 | √ | 0 | ≥数量最小值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fitemminamount | ≥金额最小值 | numeric | 23 | 10 | √ | 0 | ≥金额最小值 |
| 9 | fgroup | 组号 | int4 | 32 |  | √ | 0 | 组号 |
| 10 | fitemmaxamount | <金额最大值 | numeric | 23 | 10 | √ | 0 | <金额最大值 |
| 11 | fitemfixedamount | 固定金额 | numeric | 23 | 10 | √ | 0 | 固定金额 |
| 12 | fitemmaxachive | <达成率最大值 | numeric | 23 | 10 | √ | 0 | <达成率最大值 |
| 13 | fitemblqty | 基线数量 | numeric | 23 | 10 | √ | 0 | 基线数量 |
| 14 | fconditongroupid | 条件组 | int8 | 64 |  | √ | 0 | 条件组 ocdbd_conditongroup |
| 15 | fitemminachive | ≥达成率最小值 | numeric | 23 | 10 | √ | 0 | ≥达成率最小值 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

## 返利标准-子表 t_occpic_rbtgt_form_dt

- **表名称：** 返利标准-子表
- **表名：** t_occpic_rbtgt_form_dt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaxqty | <数量最大值 | numeric | 23 | 10 | √ | 0 | <数量最大值 |
| 3 | fminachive | ≥达成率最小值 | numeric | 23 | 10 | √ | 0 | ≥达成率最小值 |
| 4 | fictpercent | 返点率% | numeric | 23 | 10 | √ | 0 | 返点率% |
| 5 | fmaxamount | <金额最大值 | numeric | 23 | 10 | √ | 0 | <金额最大值 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffixedamount | 固定金额 | numeric | 23 | 10 | √ | 0 | 固定金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fminamount | ≥金额最小值 | numeric | 23 | 10 | √ | 0 | ≥金额最小值 |
| 10 | fminqty | ≥数量最小值 | numeric | 23 | 10 | √ | 0 | ≥数量最小值 |
| 11 | fmaxachive | <达成率最大值 | numeric | 23 | 10 | √ | 0 | <达成率最大值 |
| 12 | frebateamount | 单位返利金额 | numeric | 23 | 10 | √ | 0 | 单位返利金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occpic_rbtgtformdt_fid |  | fid |
| 2 | pk_occpic_rbtgt_form_dt |  | fentryid |
