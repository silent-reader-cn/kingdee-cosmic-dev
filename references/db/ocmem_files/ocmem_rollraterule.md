# 变动费率规则-ocmem_rollraterule

## 渠道类型-多选基础资料表 t_ocmem_rr_chltype

- **表名称：** 渠道类型-多选基础资料表
- **表名：** t_ocmem_rr_chltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [渠道类型 ocdbd_channel_type](../ocdbd_files/ocdbd_channel_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rr_chltype |  | fpkid |
| 2 | idx_ocmem_rr_chltype_id |  | fid,fbasedataid |

---

## 使用组织分录-子表 t_ocmem_ratechgrecord

- **表名称：** 使用组织分录-子表
- **表名：** t_ocmem_ratechgrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangetime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fchangeuser | 变更用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fversion | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |
| 7 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | ' ' | 变更状态,枚举: A :变更中 B :正常 C :已变更 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_ratechgrecord |  | fentryid |
| 2 | idx_ocmem_ratechgrecord_fid |  | fid |

---

## 单据体-子表 t_ocmem_rollrateentry

- **表名称：** 单据体-子表
- **表名：** t_ocmem_rollrateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 4 | fallocationrate | 分配比例% | numeric | 23 | 10 | √ | 0 | 分配比例% |
| 5 | forgpatternid | 组织形态 | int8 | 64 |  | √ | 0 | [组织形态 bos_org_pattern](../base_files/bos_org_pattern.md) |
| 6 | ffeeuseorgrange | 费用组织范围条件 | bpchar | 1 |  | √ | ' ' | 费用组织范围条件,枚举: A :预算数据源对应部门 B :指定的上级部门 C :指定的非上级部门 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fnormalenddate | 生效结束日期 | timestamp | 0 |  |  | null | 生效结束日期 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fnormalstartdate | 生效开始日期 | timestamp | 0 |  |  | null | 生效开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_rollrateentry_fid |  | fid |
| 2 | pk_ocmem_rollrateentry |  | fentryid |

---

## 叠加单据体-子表 t_ocmem_rollsupentry

- **表名称：** 叠加单据体-子表
- **表名：** t_ocmem_rollsupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsupenddate | 生效结束日期 | timestamp | 0 |  |  | null | 生效结束日期 |
| 3 | ffieldformuladesc | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 4 | ffieldformula | 计算公式 | text | 0 |  |  | null | 计算公式 |
| 5 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 6 | fallocationrate | 分配比例% | numeric | 23 | 10 | √ | 0 | 分配比例% |
| 7 | ffeeuseorgrange | 费用组织范围条件 | bpchar | 1 |  | √ | ' ' | 费用组织范围条件,枚举: A :预算数据源对应部门 B :指定的上级部门 C :指定的非上级部门 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fsupstartdate | 生效开始日期 | timestamp | 0 |  |  | null | 生效开始日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rollsupentry |  | fentryid |
| 2 | idx_ocmem_rollsupentry_fid |  | fid |

---

## 变动费率规则-主表 t_ocmem_rollraterule

- **表名称：** 变动费率规则-主表
- **表名：** t_ocmem_rollraterule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatafilter | 数据筛选条件 | text | 0 |  |  | null | 数据筛选条件 |
| 3 | ffilterscheme | 自定义过滤条件 | text | 0 |  |  | null | 自定义过滤条件 |
| 4 | fcomments | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 5 | fruletype | 费率规则 | bpchar | 1 |  | √ | 'A' | 费率规则,枚举: A :金额比例 B :单位费用金额 |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcaltype | 适用周期范围 | bpchar | 1 |  | √ | 'A' | 适用周期范围,枚举: A :全周期 B :指定营销周期 |
| 8 | ftotalsalerate | 费率值 | numeric | 23 | 10 | √ | 0 | 费率值 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'B' | 变更状态,枚举: A :变更中 B :正常 C :已变更 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fuserange | 方案适用范围 | bpchar | 1 |  | √ | 'A' | 方案适用范围,枚举: A :全组织适用 B :指定适用组织 |
| 15 | fbudgetyearid | 预算年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 16 | fbillentity | 计算数据源 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fversion | 版本号 | int4 | 32 |  | √ | 1 | 版本号 |
| 18 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fratesetting | 费率设置方案 | bpchar | 1 |  | √ | 'A' | 费率设置方案,枚举: A :按商品 B :按商品分类 |
| 21 | fchannelrange | 适用渠道范围 | bpchar | 1 |  | √ | 'A' | 适用渠道范围,枚举: A :全类型适用 B :指定适用类型 C :指定渠道 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fstarteffectdate | 生效开始日期 | timestamp | 0 |  |  | null | 生效开始日期 |
| 24 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | [商品分类 mdr_item_class](../gmc_files/mdr_item_class.md) |
| 25 | fitemid | 商品 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 26 | fendeffectdate | 生效结束日期 | timestamp | 0 |  |  | null | 生效结束日期 |
| 27 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fchangeuser | 变更用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rollraterule |  | fid |
| 2 | idx_ocmem_rollraterule_num |  | fnumber |

---

## 指定行政组织-多选基础资料表 t_ocmem_rollsupfeeorgs

- **表名称：** 指定行政组织-多选基础资料表
- **表名：** t_ocmem_rollsupfeeorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rollsupfeeorgs |  | fpkid |
| 2 | idx_ocmem_rollsupfeeorgs |  | fentryid,fbasedataid |

---

## 指定行政组织-多选基础资料表 t_ocmem_rollrulefeeorgs

- **表名称：** 指定行政组织-多选基础资料表
- **表名：** t_ocmem_rollrulefeeorgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 2 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rollrulefeeorgs |  | fpkid |
| 2 | idx_ocmem_rollrulefeeorgs |  | fentryid,fbasedataid |

---

## 变动费率规则-多语言表 t_ocmem_rollraterule_l

- **表名称：** 变动费率规则-多语言表
- **表名：** t_ocmem_rollraterule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rollraterule_l |  | fpkid |
| 2 | idx_ocmem_rollraterulel_flid |  | fid,flocaleid |

---

## 适用渠道分录-子表 t_ocmem_rr_chldetail

- **表名称：** 适用渠道分录-子表
- **表名：** t_ocmem_rr_chldetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fchannelid | 渠道名称 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_rr_chldt_id |  | fid |
| 2 | pk_ocmem_rr_chldetail |  | fentryid |

---

## 使用组织分录-子表 t_ocmem_rr_orgdetail

- **表名称：** 使用组织分录-子表
- **表名：** t_ocmem_rr_orgdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织名称 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rr_orgdetail |  | fentryid |
| 2 | idx_ocmem_rr_orgdt_id |  | fid |
