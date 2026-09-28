# 变动费率规则-ocmem_rollraterule

## 渠道类型-多选基础资料表 t_ocmem_rr_chltype

- **表名称：** 渠道类型-多选基础资料表
- **表名：** t_ocmem_rr_chltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 渠道类型 ocdbd_channel_type |
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

## 叠加单据体-子表 t_ocmem_rollsupentry

- **表名称：** 叠加单据体-子表
- **表名：** t_ocmem_rollsupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldformuladesc | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 3 | ffieldformula | 计算公式 | text | 0 |  |  | null | 计算公式 |
| 4 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 5 | fallocationrate | 分配比例% | numeric | 23 | 10 | √ | 0 | 分配比例% |
| 6 | ffeeuseorgrange | 费用组织范围条件 | bpchar | 1 |  | √ | ' ' | 费用组织范围条件,枚举: A :预算数据源对应部门 B :指定的上级部门 C :指定的非上级部门 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fratesetting | 费率设置方案 | bpchar | 1 |  | √ | 'A' | 费率设置方案,枚举: A :按商品 B :按商品分类 |
| 5 | fchannelrange | 适用渠道范围 | bpchar | 1 |  | √ | 'A' | 适用渠道范围,枚举: A :全类型适用 B :指定适用类型 C :指定渠道 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fcomments | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 8 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 9 | fruletype | 费率规则 | bpchar | 1 |  | √ | 'A' | 费率规则,枚举: A :金额比例 B :单位费用金额 |
| 10 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 12 | ftotalsalerate | 费率值 | numeric | 23 | 10 | √ | 0 | 费率值 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fchangestatus | 变更状态 | bpchar | 1 |  | √ | 'B' | 变更状态,枚举: A :变更中 B :正常 C :已变更 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fuserange | 方案适用范围 | bpchar | 1 |  | √ | 'A' | 方案适用范围,枚举: A :全组织适用 B :指定适用组织 |
| 19 | fchangetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fchangeuser | 变更用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fversion | 版本号 | int4 | 32 |  | √ | 1 | 版本号 |

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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
| 3 | fchannelid | 渠道名称 | int8 | 64 |  | √ | 0 | 渠道 ocdbd_channel |
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

## 使用组织分录-子表 t_ocmem_ratechgrecord

- **表名称：** 使用组织分录-子表
- **表名：** t_ocmem_ratechgrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangetime | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fchangeuser | 变更用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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

## 使用组织分录-子表 t_ocmem_rr_orgdetail

- **表名称：** 使用组织分录-子表
- **表名：** t_ocmem_rr_orgdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织名称 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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

---

## 单据体-子表 t_ocmem_rollrateentry

- **表名称：** 单据体-子表
- **表名：** t_ocmem_rollrateentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 4 | fallocationrate | 分配比例% | numeric | 23 | 10 | √ | 0 | 分配比例% |
| 5 | forgpatternid | 组织形态 | int8 | 64 |  | √ | 0 | 组织形态 bos_org_pattern |
| 6 | ffeeuseorgrange | 费用组织范围条件 | bpchar | 1 |  | √ | ' ' | 费用组织范围条件,枚举: A :预算数据源对应部门 B :指定的上级部门 C :指定的非上级部门 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rollrateentry |  | fentryid |
| 2 | idx_ocmem_rollrateentry_fid |  | fid |
