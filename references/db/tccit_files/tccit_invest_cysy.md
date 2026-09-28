# 投资资产持有收益台账-tccit_invest_cysy

## 投资资产持有收益台账-主表 t_tccit_invest_cysy

- **表名称：** 投资资产持有收益台账-主表
- **表名：** t_tccit_invest_cysy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 投资标的名称 | int8 | 64 |  | √ | 0 | 新增投资资产基础资料 tccit_new_invest_asset_bs |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | finvesttype | 投资性质 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fassettype | 资产类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 12 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fbillno | 资产编号 | varchar | 30 |  | √ | ' ' | 资产编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fassetstatus | 资产状态 | varchar | 50 |  | √ | ' ' | 资产状态,枚举: 0 :持有 1 :处置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_invest_cysy |  | fbillno |
| 2 | pk_tccit_invest_cysy |  | fid |

---

## 新增明细-子表 t_tccit_invest_cysy_ent

- **表名称：** 新增明细-子表
- **表名：** t_tccit_invest_cysy_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmssrje | 免税收入金额 | numeric | 23 | 10 |  | 0 | 免税收入金额 |
| 3 | finvestratio | 投资比例 | numeric | 23 | 10 | √ | 0 | 投资比例 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fbizname | 业务名称 | varchar | 50 |  | √ | ' ' | 业务名称 |
| 7 | fqrsrje | 确认收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 确认收入金额 |
| 8 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 9 | fsfsjms | 是否涉及免税 | varchar | 50 |  | √ | ' ' | 是否涉及免税,枚举: 1 :是 2 :否 |
| 10 | fcysytype | 持有收益类型 | varchar | 50 |  | √ | ' ' | 持有收益类型,枚举: 1 :股息红利 2 :合伙企业分配收入 3 :其他 |
| 11 | fswkjqrsr | 税务/会计确认收入 | varchar | 50 |  | √ | ' ' | 税务/会计确认收入,枚举: 1 :会计确认收入 2 :税务确认收入 |
| 12 | fynse | 合伙企业应纳税所得额 | numeric | 23 | 10 | √ | 0 | 合伙企业应纳税所得额 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_invest_cysy_ent_fk |  | fid |
| 2 | pk_tccit_invest_cysy_ent |  | fentryid |
