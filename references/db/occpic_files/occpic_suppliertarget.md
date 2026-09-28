# 采购政策目标-occpic_suppliertarget

## 关联子实体-子表 t_occpic_starget_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occpic_starget_lk

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
| 1 | pk_occpic_starget_lk |  | fpkid |
| 2 | idx_occpic_starget_lk_fk |  | fid |

---

## 采购政策目标-关联追踪表 t_occpic_starget_tc

- **表名称：** 采购政策目标-关联追踪表
- **表名：** t_occpic_starget_tc

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
| 1 | pk_occpic_starget_tc |  | fid |
| 2 | idx_occpic_starget_tc_tbill |  | ftbillid |
| 3 | idx_occpic_starget_tc_tid |  | ftid |

---

## 采购政策目标-反写记录表 t_occpic_starget_wb

- **表名称：** 采购政策目标-反写记录表
- **表名：** t_occpic_starget_wb

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
| 1 | idx_occpic_starget_wb_fk |  | fid |
| 2 | pk_occpic_starget_wb |  | fentryid |

---

## 返利标准-子表 t_occpic_starget_ife

- **表名称：** 返利标准-子表
- **表名：** t_occpic_starget_ife

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
| 10 | fgroup | 组号 | int4 | 32 |  | √ | 0 | 组号 |
| 11 | fitemmaxamount | <金额最大值 | numeric | 23 | 10 | √ | 0 | <金额最大值 |
| 12 | fitemfixedamount | 固定金额 | numeric | 23 | 10 | √ | 0 | 固定金额 |
| 13 | fitemmaxachive | <达成率最大值 | numeric | 23 | 10 | √ | 0 | <达成率最大值 |
| 14 | fitemblqty | 基线数量 | numeric | 23 | 10 | √ | 0 | 基线数量 |
| 15 | fconditongroupid | 条件组 | int8 | 64 |  | √ | 0 | [条件组 ocdbd_conditongroup](../occpic_files/ocdbd_conditongroup.md) |
| 16 | fitemminachive | ≥达成率最小值 | numeric | 23 | 10 | √ | 0 | ≥达成率最小值 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fitemarebatepercent | 预提返点率% | numeric | 23 | 10 | √ | 0 | 预提返点率% |
| 19 | fitemafixedamount | 预提固定金额 | numeric | 23 | 10 | √ | 0 | 预提固定金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_starget_ife |  | fentryid |
| 2 | idx_occpic_stargetife_fid |  | fid |

---

## 采购政策目标-主表 t_occpic_starget

- **表名称：** 采购政策目标-主表
- **表名：** t_occpic_starget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablecaltime | 启用计算时间 | timestamp | 0 |  |  | null | 启用计算时间 |
| 3 | faccrualformulaid | 预提计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 4 | fnrebateclassid | 返利类别 | int8 | 64 |  | √ | 0 | [返利类别 msrcs_rebateclass](../msrcs_files/msrcs_rebateclass.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fpushtype | 政策生成目标控制 | bpchar | 1 |  | √ | 'A' | 政策生成目标控制,枚举: A :审核自动生成全部 B :自动生成到上一结算周期 C :手工指定结算周期生成 |
| 9 | fgroupkey | 分组依据 | int8 | 64 |  | √ | 0 | 分组依据 |
| 10 | fcustomdaterange | 手动下推格式化有效期 | varchar | 2000 |  | √ | ' ' | 手动下推格式化有效期 |
| 11 | fpresettle | 是否预结算 | bpchar | 1 |  | √ | '0' | 是否预结算 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 目标名称 | varchar | 80 |  | √ | ' ' | 目标名称 |
| 15 | fsettperiod | 结算周期 | bpchar | 1 |  | √ | ' ' | 结算周期,枚举: C :按周 B :按月 E :按季度 A :按年 D :全生命周期 |
| 16 | fnladdertypeid | 返利判断标准 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :已失效 |
| 18 | fcalculatestatus | 计算状态 | bpchar | 1 |  | √ | 'A' | 计算状态,枚举: A :未开始计算 B :需要计算 C :计算结束 D :手工结束 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | funitid | 政策考核计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 22 | fdescription | 政策说明 | varchar | 255 |  | √ | ' ' | 政策说明 |
| 23 | fstarttime | 政策有效期.开始 | timestamp | 0 |  |  | null | 政策有效期.开始 |
| 24 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 25 | fpolicyid | 采购返利政策 | int8 | 64 |  | √ | 0 | 采购返利政策 occpic_supplierpolicy |
| 26 | fbalanceorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fsupplierclassid | 供应商分类 | int8 | 64 |  | √ | 0 | [供应商分类 bd_suppliergroup](../basedata_files/bd_suppliergroup.md) |
| 28 | fnrebatetypeid | 返利计算公式 | int8 | 64 |  | √ | 0 | [返利计算公式 msrcs_rebateformula](../msrcs_files/msrcs_rebateformula.md) |
| 29 | fendtime | 政策有效期.结束 | timestamp | 0 |  |  | null | 政策有效期.结束 |
| 30 | fcurrencyid | 考核币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fkpiid | 政策类型 | int8 | 64 |  | √ | 0 | [政策类型 ocdbd_kpi](../occpic_files/ocdbd_kpi.md) |
| 33 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occpic_starget |  | fid |
| 2 | idx_occpic_starget_noname |  | fbillno,fname |
| 3 | idx_occpic_starget_pid |  | fpolicyid |
