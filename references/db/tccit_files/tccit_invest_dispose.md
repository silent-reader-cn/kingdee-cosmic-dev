# 投资资产处置台账-tccit_invest_dispose

## 处置信息-子表 t_tccit_invest_cz_ent

- **表名称：** 处置信息-子表
- **表名：** t_tccit_invest_cz_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbussidate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 3 | fsycztsxswcl | 适用重组特殊性税务处理 | varchar | 50 |  | √ | ' ' | 适用重组特殊性税务处理,枚举: 1 :是，不适用递延纳税 2 :是，适用递延纳税 3 :否 |
| 4 | fassetlosstype | 资产损失类型 | int8 | 64 |  | √ | 0 | 资产损失备查关系映射(树) tpo_assetlossmap_tree |
| 5 | ftsxswclssje | 特殊性税务处理税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 特殊性税务处理税收金额 |
| 6 | fczzczmjz | 处置资产账面价值 | numeric | 23 | 10 | √ | 0 | 处置资产账面价值 |
| 7 | fczsszbjhxje | 处置损失准备金核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 处置损失准备金核销金额 |
| 8 | fjsjc | 计税基础 | numeric | 23 | 10 | √ | 0.0000000000 | 计税基础 |
| 9 | fczsyzjjrbnsyje | 处置损益直接计入本年损益金额 | numeric | 23 | 10 | √ | 0.0000000000 | 处置损益直接计入本年损益金额 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fzcczsr | 资产处置收入 | numeric | 23 | 10 | √ | 0.0000000000 | 资产处置收入 |
| 12 | fpcsr | 赔偿收入 | numeric | 23 | 10 | √ | 0.0000000000 | 赔偿收入 |
| 13 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fswczsyss | 税务处置收益/损失 | varchar | 50 |  | √ | ' ' | 税务处置收益/损失,枚举: 0 :* 1 :税务处置收益 2 :税务处置损失 |
| 15 | fqshczgxhlsr | 其中：清算或撤资属于股息红利的收入 | numeric | 23 | 10 | √ | 0.0000000000 | 其中：清算或撤资属于股息红利的收入 |
| 16 | ftextfield | ftextfield | varchar | 50 |  | √ | ' ' |  |
| 17 | ftransparty | 交易方 | varchar | 50 |  | √ | ' ' | 交易方 |
| 18 | fssje | 一般税务处理税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 一般税务处理税收金额 |
| 19 | ftranstype | 交易类型 | int8 | 64 |  | √ | 0 | 业务定义分录(树) tpo_tccit_bizdefen_tree |
| 20 | fbusinessname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 21 | fczsl | 减少投资比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减少投资比例 |
| 22 | fjyfsfwglf | 交易方是否为关联方 | varchar | 50 |  | √ | ' ' | 交易方是否为关联方,枚举: 1 :是 2 :否 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_invest_cz_ent_fk |  | fid |
| 2 | pk_tccit_invest_cz_ent |  | fentryid |

---

## 投资资产处置台账-主表 t_tccit_invest_cz

- **表名称：** 投资资产处置台账-主表
- **表名：** t_tccit_invest_cz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 投资标的名称 | int8 | 64 |  | √ | 0 | [新增投资资产基础资料 tccit_new_invest_asset_bs](../tccit_files/tccit_new_invest_asset_bs.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | finvesttype | 投资性质 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 8 | fisalldispose | 是否已全部处置 | varchar | 50 |  | √ | ' ' | 是否已全部处置,枚举: 1 :是 2 :否 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fassettype | 资产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 13 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 14 | fbillno | 资产编号 | varchar | 30 |  | √ | ' ' | 资产编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_invest_cz |  | fid |
| 2 | idx_tccit_invest_cz |  | fbillno |
