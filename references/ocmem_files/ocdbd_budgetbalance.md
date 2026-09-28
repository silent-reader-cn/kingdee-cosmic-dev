# 预算余额表-ocdbd_budgetbalance

## 预算余额表-主表 t_ocmem_budgetbalance

- **表名称：** 预算余额表-主表
- **表名：** t_ocmem_budgetbalance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 行政组织（部门） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fitemclassid | 预算产品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 7 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 8 | famount | 期初金额 | numeric | 23 | 10 | √ | 0 | 期初金额 |
| 9 | fitemid | 预算产品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 等级 | int4 | 32 |  | √ | 0 | 等级 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | favailableamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 16 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 17 | fusedamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 18 | fbudgetyearid | 年度 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_period |
| 19 | fmonthid | 月份 | int8 | 64 |  | √ | 0 | 营销周期 ocdbd_assess_entity |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fchannelid | 预算渠道 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
| 23 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fkeycol | keycol | varchar | 80 |  | √ | ' ' | keycol |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_budgetbalance |  | fid |
| 2 | idx_ocmem_budgetbalance_no |  | fnumber |

---

## 预算余额表-多语言表 t_ocmem_budgetbalance_l

- **表名称：** 预算余额表-多语言表
- **表名：** t_ocmem_budgetbalance_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | ffullname | ffullname | varchar | 80 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_budgetbalance_l |  | fpkid |
| 2 | idx_ocmem_budgetbalance_flid |  | fid,flocaleid |
