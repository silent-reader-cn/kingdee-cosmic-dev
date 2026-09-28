# 营销活动计划-ocmem_activityscheme

## 营销活动计划-多语言表 t_ocmem_activityscheme_l

- **表名称：** 营销活动计划-多语言表
- **表名：** t_ocmem_activityscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fbillname | 活动计划名称 | varchar | 250 |  | √ | ' ' | 活动计划名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_actscheme_l_flid |  | fid,flocaleid |
| 2 | pk_ocmem_activityscheme_l |  | fpkid |

---

## 返利规则分录-子表 t_ocmem_actschemerebate

- **表名称：** 返利规则分录-子表
- **表名：** t_ocmem_actschemerebate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpresaleamt | 预计销售金额 | numeric | 23 | 10 | √ | 0 | 预计销售金额 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fprerebateamt | 预计返利金额 | numeric | 23 | 10 | √ | 0 | 预计返利金额 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fitembrand | 品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 7 | frebatecondition | 返利条件 | varchar | 2000 |  | √ | ' ' | 返利条件 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fitemgroup | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 11 | frebatepresaleqty | 预计销售数量 | numeric | 23 | 10 | √ | 0 | 预计销售数量 |
| 12 | fitem | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 13 | frebatescheme | 返利方案 | bpchar | 1 |  | √ | 'A' | 返利方案,枚举: A :单位返利 B :返点返利 O :其他 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | frebatestrategy | 返利策略 | varchar | 2000 |  | √ | ' ' | 返利策略 |
| 16 | fitemunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_actschemerebate_fk |  | fid |
| 2 | pk_ocmem_actschemerebate |  | fentryid |

---

## 费用明细分录-子表 t_ocmem_actschemefee

- **表名称：** 费用明细分录-子表
- **表名：** t_ocmem_actschemefee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffeeamt | 费用金额 | numeric | 23 | 10 | √ | 0 | 费用金额 |
| 3 | fremark | 使用说明 | varchar | 500 |  | √ | ' ' | 使用说明 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fpaydeptid | 承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdeptrate | 部门承担占比(%) | numeric | 23 | 2 | √ | 0 | 部门承担占比(%) |
| 8 | fcompanyrate | 公司占比(%) | numeric | 23 | 2 | √ | 0 | 公司占比(%) |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcompanyfeeamt | 公司承担总额 | numeric | 23 | 10 | √ | 0 | 公司承担总额 |
| 11 | ffeeexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fdeptamt | 部门承担金额 | numeric | 23 | 10 | √ | 0 | 部门承担金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_actschemefee |  | fentryid |
| 2 | idx_ocmem_actschemefee_fk |  | fid |

---

## 量化效果指标分录-多语言表 t_ocmem_actschemereidv_l

- **表名称：** 量化效果指标分录-多语言表
- **表名：** t_ocmem_actschemereidv_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | findicatorname | 指标名称 | varchar | 80 |  | √ | ' ' | 指标名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_actschemereidv_flid |  | fentryid,flocaleid |
| 2 | pk_ocmem_actschemereidv_l |  | fpkid |

---

## 量化效果指标分录-子表 t_ocmem_actschemereidv

- **表名称：** 量化效果指标分录-子表
- **表名：** t_ocmem_actschemereidv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | findicatorname | 指标名称 | varchar | 80 |  | √ | ' ' | 指标名称 |
| 4 | fweight | 权重 | numeric | 23 | 2 | √ | 0 | 权重 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdatasource | 数据来源 | bpchar | 1 |  | √ | 'A' | 数据来源,枚举: A :销售系统 B :CRM系统 C :FSA系统 D :财务系统 E :供应链系统 O :其他系统 |
| 8 | ftargetvalue | 目标值 | numeric | 23 | 2 | √ | 0 | 目标值 |
| 9 | findicatortype | 指标类型 | bpchar | 1 |  | √ | 'A' | 指标类型,枚举: A :财务指标 B :客户指标 C :经营指标 O :其他 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_actschemereidv_fk |  | fid |
| 2 | pk_ocmem_actschemereidv |  | fentryid |

---

## 营销活动计划-主表 t_ocmem_activityscheme

- **表名称：** 营销活动计划-主表
- **表名：** t_ocmem_activityscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftotalfeeamt | 预计总费用 | numeric | 23 | 10 | √ | 0 | 预计总费用 |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fplanorgid | 策划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 主办公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbegindate | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fpriority | 活动优先级 | bpchar | 1 |  | √ | '1' | 活动优先级,枚举: 0 :高 1 :中 2 :低 |
| 10 | fplandeptid | 策划部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fplanstatus | 活动计划状态 | bpchar | 1 |  | √ | 'A' | 活动计划状态,枚举: A :策划中 B :审批中 C :已审批 D :执行中 E :已结案 F :已终止 |
| 13 | fbillname | 活动计划名称 | varchar | 250 |  | √ | ' ' | 活动计划名称 |
| 14 | fplandescribe | 计划描述 | varchar | 2000 |  | √ | ' ' | 计划描述 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | factschemetypeid | 活动计划类型 | int8 | 64 |  | √ | 0 | [活动计划类型 ocmem_activityschemetype](../ocmem_files/ocmem_activityschemetype.md) |
| 19 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fbillno | 活动计划编码 | varchar | 80 |  | √ | ' ' | 活动计划编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | ftargetdescribe | 目标描述 | varchar | 2000 |  | √ | ' ' | 目标描述 |
| 23 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_activityscheme |  | fid |
| 2 | idx_ocmem_actscheme_billno |  | fbillno |

---

## 活动场景-多选基础资料表 t_ocmem_actschemescene

- **表名称：** 活动场景-多选基础资料表
- **表名：** t_ocmem_actschemescene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [活动场景 ocdbd_activityscene](../ocmem_files/ocdbd_activityscene.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_actschemescene_fk |  | fid |
| 2 | pk_ocmem_actschemescene |  | fpkid |

---

## 客户范围分录-子表 t_ocmem_actschemecust

- **表名称：** 客户范围分录-子表
- **表名：** t_ocmem_actschemecust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fchannelgradeid | 客户等级 | int8 | 64 |  | √ | 0 | [渠道等级 ocdbd_channel_grade](../ocdbd_files/ocdbd_channel_grade.md) |
| 5 | fchannelclassid | 客户分类 | int8 | 64 |  | √ | 0 | [渠道分类 ocdbd_channel_class](../ocdbd_files/ocdbd_channel_class.md) |
| 6 | fchannelremark | 客户行备注 | varchar | 255 |  | √ | ' ' | 客户行备注 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fchannelid | 客户编码 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_actschemecust_fk |  | fid |
| 2 | pk_ocmem_actschemecust |  | fentryid |

---

## 产品范围分录-子表 t_ocmem_actschemeprod

- **表名称：** 产品范围分录-子表
- **表名：** t_ocmem_actschemeprod

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fplanitembrandid | 品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 4 | fplanitemgroupid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fprodremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fitemid | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_actschemeprod |  | fentryid |
| 2 | idx_ocmem_actschemeprod_fk |  | fid |

---

## 促销规则分录-子表 t_ocmem_actschemeprom

- **表名称：** 促销规则分录-子表
- **表名：** t_ocmem_actschemeprom

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpresaleamt | 预计销售金额 | numeric | 23 | 10 | √ | 0 | 预计销售金额 |
| 3 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fpromotionscheme | 促销方案 | bpchar | 1 |  | √ | 'A' | 促销方案,枚举: A :满减 B :买赠 C :降价 O :其他 |
| 6 | fplanitembrand | 品牌 | int8 | 64 |  | √ | 0 | [商品品牌 mdr_item_brand](../gmc_files/mdr_item_brand.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fplanitem | 商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 9 | fprice | 正常价格 | numeric | 23 | 10 | √ | 0 | 正常价格 |
| 10 | fpromcondition | 促销条件 | varchar | 2000 |  | √ | ' ' | 促销条件 |
| 11 | fpromotionstrategy | 促销策略 | varchar | 2000 |  | √ | ' ' | 促销策略 |
| 12 | fplanitemgroup | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fpresaleqty | 预计销售数量 | numeric | 23 | 10 | √ | 0 | 预计销售数量 |
| 15 | fpromotionamt | 促销让利金额 | numeric | 23 | 10 | √ | 0 | 促销让利金额 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fpromotionprice | 促销价格 | numeric | 23 | 10 | √ | 0 | 促销价格 |
| 18 | fitemunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_actschemeprom |  | fentryid |
| 2 | idx_ocmem_actschemeprom_fk |  | fid |

---

## 非量化效果指标分录-子表 t_ocmem_nonactschemereidv

- **表名称：** 非量化效果指标分录-子表
- **表名：** t_ocmem_nonactschemereidv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnonindivatorname | 指标名称 | varchar | 150 |  | √ | ' ' | 指标名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fnonindivatordescribe | 指标描述 | varchar | 2000 |  | √ | ' ' | 指标描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_nonactschemereidv |  | fentryid |
| 2 | idx_ocmem_nonactschemereidv_fk |  | fid |
