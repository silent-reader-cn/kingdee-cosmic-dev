# 促销政策-ocdpm_promotepolicy

## 促销规则分录-分表 t_ocdpm_pp_rule_x

- **表名称：** 促销规则分录-分表
- **表名：** t_ocdpm_pp_rule_x

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fispropricecycle | 促销单价-是否循环计算 | bpchar | 1 |  | √ | '0' | 促销单价-是否循环计算 |
| 3 | fdiscounttate | 折扣率(%) | numeric | 23 | 10 | √ | 0 | 折扣率(%) |
| 4 | fthatgiftassqty | 指定品赠送-辅助数量 | numeric | 23 | 10 | √ | 0 | 指定品赠送-辅助数量 |
| 5 | fladderminamount | 阶梯最小金额(>=) | numeric | 23 | 10 | √ | 0 | 阶梯最小金额(>=) |
| 6 | fthatgiftexcprice | 指定品赠送-换购单价 | numeric | 23 | 10 | √ | 0 | 指定品赠送-换购单价 |
| 7 | fpricedisctamt | 单价折扣额（含税） | numeric | 23 | 10 | √ | 0 | 单价折扣额（含税） |
| 8 | fbuyqty | 购买条件数量 | numeric | 23 | 10 | √ | 0 | 购买条件数量 |
| 9 | fisperpricecycle | 单价折扣额-是否循环计算 | bpchar | 1 |  | √ | '0' | 单价折扣额-是否循环计算 |
| 10 | fthatgiftqty | 指定品赠送-数量 | numeric | 23 | 10 | √ | 0 | 指定品赠送-数量 |
| 11 | fminlimitassqty | 最小起买辅助数量 | numeric | 23 | 10 | √ | 0 | 最小起买辅助数量 |
| 12 | fbuyamount | 购买条件金额（含税） | numeric | 23 | 10 | √ | 0 | 购买条件金额（含税） |
| 13 | fthisgiftqty | 本品赠送-数量 | numeric | 23 | 10 | √ | 0 | 本品赠送-数量 |
| 14 | fisthatcycleaccount | 指定品赠送-是否循环计算 | bpchar | 1 |  | √ | '0' | 指定品赠送-是否循环计算 |
| 15 | fminlimitqty | 最小起买数量 | numeric | 23 | 10 | √ | 0 | 最小起买数量 |
| 16 | fladdermaxassqty | 阶梯最大辅助数量(<) | numeric | 23 | 10 | √ | 0 | 阶梯最大辅助数量(<) |
| 17 | fladdermaxamount | 阶梯最大金额(<) | numeric | 23 | 10 | √ | 0 | 阶梯最大金额(<) |
| 18 | fminbuypiece | 最小起买份数 | numeric | 23 | 10 | √ | 0 | 最小起买份数 |
| 19 | ffixeddisctamount | 整单折扣额（含税） | numeric | 23 | 10 | √ | 0 | 整单折扣额（含税） |
| 20 | ftypebetgroup | 指定品赠送-赠品组间执行方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 21 | fladderminassqty | 阶梯最小辅助数量(>=) | numeric | 23 | 10 | √ | 0 | 阶梯最小辅助数量(>=) |
| 22 | fladderminbase | 阶梯最小份数(>=) | numeric | 23 | 10 | √ | 0 | 阶梯最小份数(>=) |
| 23 | fbasebuyqty | 基本单位购买数量 | numeric | 23 | 10 | √ | 0 | 基本单位购买数量 |
| 24 | fiscycleaccount | 本品赠送-是否循环计算 | bpchar | 1 |  | √ | '0' | 本品赠送-是否循环计算 |
| 25 | ftypeingroup | 指定品赠送-赠品组内执行方式 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 26 | fbasegiftqty | 基本单位赠送数量 | numeric | 23 | 10 | √ | 0 | 基本单位赠送数量 |
| 27 | fthisgiftassqty | 本品赠送-辅助数量 | numeric | 23 | 10 | √ | 0 | 本品赠送-辅助数量 |
| 28 | fprocondition | 促销条件 | bpchar | 1 |  | √ | ' ' | 促销条件,枚举: B :按金额 A :按数量 |
| 29 | fminlimitamount | 最小起买金额 | numeric | 23 | 10 | √ | 0 | 最小起买金额 |
| 30 | fbuyassqty | 购买条件辅助数量 | numeric | 23 | 10 | √ | 0 | 购买条件辅助数量 |
| 31 | fisfixeddisctcycle | 整单折扣额-是否循环计算 | bpchar | 1 |  | √ | '0' | 整单折扣额-是否循环计算 |
| 32 | fprounitprice | 促销单价 | numeric | 23 | 10 | √ | 0 | 促销单价 |
| 33 | fladdermaxbase | 阶梯最大份数(<) | numeric | 23 | 10 | √ | 0 | 阶梯最大份数(<) |
| 34 | fladdermaxqty | 阶梯最大数量(<) | numeric | 23 | 10 | √ | 0 | 阶梯最大数量(<) |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 36 | fladderminqty | 阶梯最小数量(>=) | numeric | 23 | 10 | √ | 0 | 阶梯最小数量(>=) |
| 37 | fbuymutiple | 指定产品购买条件份数 | numeric | 23 | 10 | √ | 0 | 指定产品购买条件份数 |
| 38 | ftotaldiscount | 整单折扣率(%) | numeric | 23 | 10 | √ | 0 | 整单折扣率(%) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_pp_rule_x |  | fentryid |
| 2 | idx_ocdpm_pprulex_fid |  | fid |

---

## 订货范围单据体-子表 t_ocdpm_pp_order

- **表名称：** 订货范围单据体-子表
- **表名：** t_ocdpm_pp_order

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderchannelid | 订货渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 3 | fchannelclassid | 渠道分类 | int8 | 64 |  | √ | 0 | 渠道分类 ocdbd_channel_class |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcustomerclassid | 客户分类 | int8 | 64 |  | √ | 0 | 客户分类 bd_customergroup |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_pp_order_fid |  | fid |
| 2 | pk_ocdpm_pp_order |  | fentryid |

---

## 促销策略-多选基础资料表 t_ocdpm_pp_policys

- **表名称：** 促销策略-多选基础资料表
- **表名：** t_ocdpm_pp_policys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 渠道促销策略 ocdpm_promotionstrategy |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_pp_policys_fbid |  | fentryid,fbasedataid |
| 2 | pk_ocdpm_pp_policys |  | fpkid |

---

## 促销政策-主表 t_ocdpm_promotepolicy

- **表名称：** 促销政策-主表
- **表名：** t_ocdpm_promotepolicy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | fname | 促销政策名称 | varchar | 80 |  | √ | ' ' | 促销政策名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :失效 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fdescribe | 促销政策规则描述 | varchar | 1000 |  | √ | ' ' | 促销政策规则描述 |
| 8 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fpriority | 促销政策优先级 | numeric | 23 | 10 | √ | 0 | 促销政策优先级 |
| 10 | factivityplanid | 活动方案 | int8 | 64 |  | √ | 0 | 费用活动方案 ocmem_activityplan_f7 |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | finvaliduserid | 失效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | feffectivedate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 16 | finvalidtime | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 17 | fpromotetypeid | 促销类型 | int8 | 64 |  | √ | 0 | 渠道促销类型 ocdpm_promotiontype |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillno | 促销政策编号 | varchar | 80 |  | √ | ' ' | 促销政策编号 |
| 20 | fexpirationdate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_promotepolicy |  | fid |
| 2 | idx_ocdpm_promotepolicy_no |  | fbillno |

---

## 促销规则分录-子表 t_ocdpm_pp_rule

- **表名称：** 促销规则分录-子表
- **表名：** t_ocdpm_pp_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fassunit | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fenablelimit | 启用限量 | bpchar | 1 |  | √ | '0' | 启用限量 |
| 5 | fladdernoid | 阶梯号 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 6 | frowtype | 行类型 | bpchar | 1 |  | √ | 'A' | 行类型,枚举: A :主产品行 B :赠品行 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 8 | fitemclassid | 商品分类编码 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 9 | fmaterialgroupid | 物料组编码 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 10 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fprostarttime | 促销组开始日期 | timestamp | 0 |  |  | null | 促销组开始日期 |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | flimittypeid | 限量方式 | int8 | 64 |  | √ | 0 | 限量方式 ocdpm_limittype |
| 14 | fjoinlimit | 已关联限量 | bpchar | 1 |  | √ | '0' | 已关联限量 |
| 15 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 16 | flimitqty | 限量数量 | numeric | 23 | 10 | √ | 0 | 限量数量 |
| 17 | fprogroupnoid | 促销组号 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 18 | fpggroupnoid | 主产品组/赠品组号 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 19 | fbaseunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fprioritydetailid | 促销组优先级 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 23 | fproendtime | 促销组结束日期 | timestamp | 0 |  |  | null | 促销组结束日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdpm_pprule_fid |  | fid |
| 2 | pk_ocdpm_pp_rule |  | fentryid |

---

## 销售主体单据体-子表 t_ocdpm_pp_sale

- **表名称：** 销售主体单据体-子表
- **表名：** t_ocdpm_pp_sale

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 4 | fsaleorgid | 销售组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsalechannelid | 销售渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 7 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_pp_sale |  | fentryid |
| 2 | idx_ocdpm_ppsale_fid |  | fid |

---

## 例外商品分录-子表 t_ocdpm_pp_excdetail

- **表名称：** 例外商品分录-子表
- **表名：** t_ocdpm_pp_excdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexceptionmaterialid | 例外物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fexceptionauxpty | 例外辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fexceptionitemid | 例外商品编码 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fexceptionunitid | 例外计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdpm_pp_excdetail |  | fentryid |
| 2 | idx_ocdpm_ppexcdetail_fid |  | fid |
