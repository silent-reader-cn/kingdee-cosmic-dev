# 比价记录-mal_compareprice

## 比价分录-子表 t_mal_comparepriceentry

- **表名称：** 比价分录-子表
- **表名：** t_mal_comparepriceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fladderprice | 阶梯价格 | numeric | 23 | 10 | √ | 0 | 阶梯价格 |
| 4 | fgoodsid | 商品信息 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | faddqty | 加入数量 | numeric | 23 | 10 | √ | 0 | 加入数量 |
| 8 | fprice | 结算价 | numeric | 23 | 10 | √ | 0 | 结算价 |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fcompareresult | 对比结果 | bpchar | 1 |  | √ | ' ' | 对比结果,枚举: 0 :最高价 1 :最低价 |
| 11 | fisadd | 是否选中 | bpchar | 1 |  | √ | '0' | 是否选中 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_comparepriceentry |  | fentryid |
| 2 | idx_mal_compareentry_fid_fseq |  | fid,fseq |

---

## 比价记录-主表 t_mal_compareprice

- **表名称：** 比价记录-主表
- **表名：** t_mal_compareprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 比价人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcomparedetailshot | 比价详情快照 | varchar | 255 |  |  | ' ' | 比价详情快照 |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 比价日期 | timestamp | 0 |  |  | null | 比价日期 |
| 7 | forgid | 比价组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fcomparedetailshot_tag | 比价详情快照_详情 | text | 0 |  |  | null | 比价详情快照_详情 |
| 10 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_comprice_fcreatorid |  | forgid,fcreatorid |
| 2 | pk_t_mal_compareprice |  | fid |
| 3 | idx_mal_comprice_fcreatetime |  | fcreatetime |
