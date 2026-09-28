# 盘亏盘盈单-fa_invdiffer

## 盘亏盘盈单-关联追踪表 t_fa_invdiffer_tc

- **表名称：** 盘亏盘盈单-关联追踪表
- **表名：** t_fa_invdiffer_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_invdiffer_tc_tid |  | ftid |
| 2 | pk_fa_invdiffer_tc |  | fid |
| 3 | idx_fa_invdiffer_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_fa_invdiffer_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_invdiffer_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_invdiffer_lk |  | fpkid |
| 2 | idx_fa_invdiffer_lk_fk |  | fid |

---

## 盘点差异分录-子表 t_fa_invdiffererentry

- **表名称：** 盘点差异分录-子表
- **表名：** t_fa_invdiffererentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbookquantity | 账面数量 | numeric | 23 | 10 | √ | 0.0000000000 | 账面数量 |
| 3 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fname | 资产名称 | varchar | 50 |  | √ | ' ' | 资产名称 |
| 5 | finventorytaskid | 盘点任务 | int8 | 64 |  | √ | 0 | [我的盘点任务 fa_inventory_task](../fa_files/fa_inventory_task.md) |
| 6 | finventorytime | 盘点日期(弃用) | timestamp | 0 |  |  | null | 盘点日期(弃用) |
| 7 | finventoryquantity | 盘点数量 | numeric | 23 | 10 | √ | 0.0000000000 | 盘点数量 |
| 8 | fassetqtyleft | 可生成数量 | numeric | 23 | 10 | √ | 0.0000000000 | 可生成数量 |
| 9 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fdifferquantity | 差异数量 | numeric | 23 | 10 | √ | 0.0000000000 | 差异数量 |
| 12 | frealcardid | 实物卡片 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 13 | fbarcode | 条形码 | varchar | 50 |  | √ | ' ' | 条形码 |
| 14 | finventorydifferstatus | 盘点差异状态 | bpchar | 1 |  | √ | ' ' | 盘点差异状态,枚举: 1 :盘盈从0到1 2 :盘盈从1到N 3 :盘亏 0 :无变化 |
| 15 | fchangemodeid | 增减方式 | int8 | 64 |  | √ | 0 | [增减方式 fa_changemode](../fa_files/fa_changemode.md) |
| 16 | fassetunitid | 资产组织（弃用） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 18 | fheadusedeptid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | finventoryway | 盘点方式(弃用) | bpchar | 1 |  | √ | ' ' | 盘点方式(弃用),枚举: A :人人盘点 B :手工盘点 C :API导入 D :人人PC盘点 |
| 20 | fdifferamount | 差异金额(弃用) | numeric | 19 | 6 | √ | 0.000000 | 差异金额(弃用) |
| 21 | finventorydiffer | 盘点差异 | bpchar | 1 |  | √ | ' ' | 盘点差异,枚举: A :盘盈 B :盘亏 C :无差异 |
| 22 | finventoryrecordid | 盘点记录 | int8 | 64 |  | √ | 0 | [盘点记录基础资料 fa_inventory_record_base](../fa_files/fa_inventory_record_base.md) |
| 23 | fnumber | 资产编码 | varchar | 80 |  | √ | ' ' | 资产编码 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_invdiffererentry |  | fid |
| 2 | pk_t_fa_invdiffererentry |  | fentryid |

---

## 盘亏盘盈单-主表 t_fa_invdiffer

- **表名称：** 盘亏盘盈单-主表
- **表名：** t_fa_invdiffer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecordgroupbillno | 资产盘点表 | varchar | 30 |  | √ | ' ' | 资产盘点表 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 状态 | bpchar | 1 |  | √ | 'A' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finventschemeid | 盘点方案 | int8 | 64 |  | √ | 0 | [盘点方案 fa_inventscheme_new](../fa_files/fa_inventscheme_new.md) |
| 8 | fassetqty | 差异数据 | numeric | 23 | 10 | √ | 0.0000000000 | 差异数据 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | finventorylossamount | 盘亏金额(弃用) | numeric | 19 | 6 | √ | 0.000000 | 盘亏金额(弃用) |
| 14 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fisgenbyconfirm | 是否确认盘点生成 | bpchar | 1 |  | √ | '0' | 是否确认盘点生成 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_inventory_billno |  | fbillno |
| 2 | idx_fa_inventory_forgid |  | forgid,finventschemeid |
| 3 | pk_t_fa_invdiffer |  | fid |

---

## 盘亏盘盈单-反写记录表 t_fa_invdiffer_wb

- **表名称：** 盘亏盘盈单-反写记录表
- **表名：** t_fa_invdiffer_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_invdiffer_wb |  | fentryid |
| 2 | idx_fa_invdiffer_wb_fk |  | fid |
