# 变动费率变更-ocmem_rollrulechange

## 变动费率变更-主表 t_ocmem_rulechange

- **表名称：** 变动费率变更-主表
- **表名：** t_ocmem_rulechange

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | feffectiveuser | 生效人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fchangestatus | 生效状态 | bpchar | 1 |  | √ | 'A' | 生效状态,枚举: A :草案 B :已生效 C :已完成 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fneedsyn | 需要同步变更已发生的费用 | bpchar | 1 |  | √ | '0' | 需要同步变更已发生的费用 |
| 10 | fendrolldate | 已发生费用时间范围.结束 | timestamp | 0 |  |  | null | 已发生费用时间范围.结束 |
| 11 | fissyn | 已同步变更已发生的费用 | bpchar | 1 |  | √ | '0' | 已同步变更已发生的费用 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 14 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 15 | fstartrolldate | 已发生费用时间范围.开始 | timestamp | 0 |  |  | null | 已发生费用时间范围.开始 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rulechange |  | fid |
| 2 | idx_ocmem_rulechange_billno |  | fbillno |

---

## 保存前关联费用规则-多选基础资料表 t_ocmem_rc_mulraterules

- **表名称：** 保存前关联费用规则-多选基础资料表
- **表名：** t_ocmem_rc_mulraterules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 变动费率规则 ocmem_rollraterule |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_rc_mulraterules |  | fpkid |
| 2 | idx_ocmem_rc_mulraterules_fid |  | fid |

---

## 费率变更明细-子表 t_ocmem_changeentry

- **表名称：** 费率变更明细-子表
- **表名：** t_ocmem_changeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fratesetting | 费率设置方案 | bpchar | 1 |  | √ | ' ' | 费率设置方案,枚举: A :按商品 B :按商品分类 |
| 3 | fnewtotalsalerate | 新费率值 | numeric | 23 | 10 | √ | 0 | 新费率值 |
| 4 | foldtotalsalerate | 原费率值 | numeric | 23 | 10 | √ | 0 | 原费率值 |
| 5 | fuserange | 方案适用范围 | bpchar | 1 |  | √ | ' ' | 方案适用范围,枚举: A :全组织适用 B :指定适用组织 |
| 6 | fitemclassid | 商品分类 | int8 | 64 |  | √ | 0 | 商品分类 mdr_item_class |
| 7 | fruletype | 费率规则 | bpchar | 1 |  | √ | ' ' | 费率规则,枚举: A :金额比例 B :单位费用金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fitemid | 商品 | int8 | 64 |  | √ | 0 | 商品信息 ocdbd_iteminfo |
| 11 | fversion | 原版本号 | int4 | 32 |  | √ | 0 | 原版本号 |
| 12 | fraterule | 规则编码 | int8 | 64 |  | √ | 0 | 变动费率规则 ocmem_rollraterule |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocmem_changeentry_fid |  | fid |
| 2 | pk_ocmem_changeentry |  | fentryid |

---

## 变更明细关联费用类型-子表 t_ocmem_changechilentry

- **表名称：** 变更明细关联费用类型-子表
- **表名：** t_ocmem_changechilentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | 营销费用类型 ocdbd_expensetype |
| 2 | fnewallocationrate | 新分配比例% | numeric | 23 | 10 | √ | 0 | 新分配比例% |
| 3 | flinkentryid | 关联分录id | int8 | 64 |  | √ | 0 | 关联分录id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 6 | foldallocationrate | 原分配比例% | numeric | 23 | 10 | √ | 0 | 原分配比例% |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fisaddnew | 是否变更新增 | bpchar | 1 |  | √ | '0' | 是否变更新增 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocmem_changechilentry |  | fdetailid |
| 2 | idx_ocmem_changechilentry_eid |  | fentryid |
