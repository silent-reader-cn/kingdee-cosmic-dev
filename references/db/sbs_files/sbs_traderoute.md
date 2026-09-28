# 贸易路线-sbs_traderoute

## 贸易路线-多语言表 t_sbs_traderoute_l

- **表名称：** 贸易路线-多语言表
- **表名：** t_sbs_traderoute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_traderoute_l |  | fid,flocaleid |
| 2 | pk_sbs_traderoute_l |  | fpkid |

---

## 中间贸易组织-子表 t_sbs_tradeorg

- **表名称：** 中间贸易组织-子表
- **表名：** t_sbs_tradeorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_tradeorg |  | fentryid |
| 2 | idx_sbs_tradeorg |  | fid |

---

## 贸易路径概览-子表 t_sbs_traderouteentry

- **表名称：** 贸易路径概览-子表
- **表名：** t_sbs_traderouteentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstep | 步骤 | int4 | 32 |  | √ | 0 | 步骤 |
| 3 | ffixedprice | 固定价格 | numeric | 23 | 10 | √ | 0 | 固定价格 |
| 4 | fbillform | 单据名称 | varchar | 50 |  | √ | ' ' | 单据名称,枚举: sm_salorder :销售订单 pm_purorderbill :采购订单 |
| 5 | faddamount | 加减价格 | numeric | 23 | 10 | √ | 0 | 加减价格 |
| 6 | fpricesource | 价格来源 | varchar | 50 |  | √ | ' ' | 价格来源,枚举: 0 :价目表 1 :前序单据 2 :固定价格 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fasrate | 加减比率% | numeric | 23 | 10 | √ | 0 | 加减比率% |
| 11 | ftaxsource | 税率来源 | varchar | 50 |  | √ | ' ' | 税率来源,枚举: 0 :固定 1 :来源前序订单 |
| 12 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | finternalcstype | 内部客户/供应商类型 | varchar | 50 |  | √ | ' ' | 内部客户/供应商类型,枚举: bd_customer :客户 bd_supplier :供应商 |
| 15 | finternalcsid | 内部客户/供应商 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | ftransdays | 运输天数 | int4 | 32 |  | √ | 0 | 运输天数 |
| 17 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_traderouteentry |  | fentryid |
| 2 | idx_sbs_traderouteentry |  | fid |

---

## 贸易路线-主表 t_sbs_traderoute

- **表名称：** 贸易路线-主表
- **表名：** t_sbs_traderoute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftargetorgid | 目标业务组织 | int8 | 64 |  |  | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fautogeninvbill | 关联库存单据自动创建 | bpchar | 1 |  | √ | '1' | 关联库存单据自动创建 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | ftargetinvbillstatus | 目标库存单据状态 | varchar | 50 |  | √ | ' ' | 目标库存单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | ftargetbilltypeid | 目标单据类型 | int8 | 64 |  |  | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | ftargetorderstatus | 目标订单单据状态 | varchar | 50 |  | √ | ' ' | 目标订单单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsrcbill | 源头单据 | varchar | 50 |  | √ | ' ' | 源头单据,枚举: sm_salorder :销售订单 pm_purorderbill :采购订单 |
| 13 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fexternalsc | 外部供应商/客户 | bpchar | 1 |  | √ | '0' | 外部供应商/客户 |
| 16 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fsrcorgid | 源头业务组织 | int8 | 64 |  |  | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fcreatorid | 创建人 | int8 | 64 |  |  | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 20 | ftargetbill | 目标单据 | varchar | 50 |  | √ | ' ' | 目标单据,枚举: sm_salorder :销售订单 pm_purorderbill :采购订单 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fsrcbilltypeid | 源头单据类型 | int8 | 64 |  |  | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_traderoute |  | fnumber |
| 2 | pk_sbs_traderoute |  | fid |
