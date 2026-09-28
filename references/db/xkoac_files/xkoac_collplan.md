# 经营费用归集方案-xkoac_collplan

## 经营费用归集方案-多语言表 t_xkoac_collplan_l

- **表名称：** 经营费用归集方案-多语言表
- **表名：** t_xkoac_collplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_collplan_l |  | fpkid |
| 2 | idx_collplan_l |  | fid,flocaleid |

---

## 适用经营账簿-多选基础资料表 t_xkoac_collplanbook

- **表名称：** 适用经营账簿-多选基础资料表
- **表名：** t_xkoac_collplanbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营账簿 xkoac_operatingbook](../xkoac_files/xkoac_operatingbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_collplanbook |  | fpkid |
| 2 | idx_xkoac_collplanbook |  | fbasedataid |

---

## 单据体-子表 t_xkoac_collplanentity

- **表名称：** 单据体-子表
- **表名：** t_xkoac_collplanentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frownumber | 行ID | int4 | 32 |  | √ | 0 | 行ID |
| 3 | facctset | 经营科目详细设置 | text | 0 |  |  | null | 经营科目详细设置 |
| 4 | funitsrcdesc | 经营单元来源 | varchar | 100 |  | √ | ' ' | 经营单元来源 |
| 5 | fremark_tag | 备注设置_详情 | text | 0 |  |  | null | 备注设置_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | facctset_tag | 经营科目详细设置_详情 | text | 0 |  |  | null | 经营科目详细设置_详情 |
| 8 | forgsrcdesc | 所属组织来源 | varchar | 100 |  | √ | ' ' | 所属组织来源 |
| 9 | ffilter | 过滤条件设置 | text | 0 |  |  | null | 过滤条件设置 |
| 10 | famountfor | 金额设置 | text | 0 |  |  | null | 金额设置 |
| 11 | funitsrc | 经营单元来源设置 | text | 0 |  |  | null | 经营单元来源设置 |
| 12 | fexpenseitemdesc | 费用项目 | varchar | 100 |  | √ | ' ' | 费用项目 |
| 13 | fremark | 备注设置 | text | 0 |  |  | null | 备注设置 |
| 14 | fsrcdate | 日期来源设置 | varchar | 500 |  | √ | ' ' | 日期来源设置 |
| 15 | fcurrency | 币种设置 | varchar | 500 |  | √ | ' ' | 币种设置 |
| 16 | fexpenseitem | 费用项目设置 | text | 0 |  |  | null | 费用项目设置 |
| 17 | fsrcdatedesc | 日期来源 | varchar | 100 |  | √ | ' ' | 日期来源 |
| 18 | fcurrencydesc | 币种 | varchar | 100 |  | √ | ' ' | 币种 |
| 19 | famountfordesc | 金额 | varchar | 100 |  | √ | ' ' | 金额 |
| 20 | fsourcebillid | 来源单据 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | facctsetdesc | 经营科目 | varchar | 100 |  | √ | ' ' | 经营科目 |
| 22 | forgsrc | 所属组织来源设置 | varchar | 500 |  | √ | ' ' | 所属组织来源设置 |
| 23 | ffilterdesc | 过滤条件 | varchar | 100 |  | √ | ' ' | 过滤条件 |
| 24 | fglaccountid | 总账科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 25 | fremarkdesc | 备注 | varchar | 100 |  | √ | ' ' | 备注 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_collplanentity |  | fentryid |
| 2 | idx_xkoac_collplanentry |  | fid |

---

## 经营费用归集方案-主表 t_xkoac_collplan

- **表名称：** 经营费用归集方案-主表
- **表名：** t_xkoac_collplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fsrcglstatus | 来源凭证状态 | varchar | 50 |  | √ | '1' | 来源凭证状态,枚举: 1 :已审核 2 :已提交 3 :已过账 4 :创建 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fexpensetype | 费用录入方式 | bpchar | 1 |  | √ | '1' | 费用录入方式,枚举: 1 :费用项目 2 :经营科目 |
| 8 | faudittime | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fsrctype | 来源类型 | bpchar | 1 |  | √ | '1' | 来源类型,枚举: 1 :业务单据 2 :总账凭证 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 11 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | faccttblid | 经营科目表 | int8 | 64 |  | √ | 0 | [经营科目表 xkoac_accounttable](../xkoac_files/xkoac_accounttable.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 禁用状态 | bpchar | 1 |  | √ | '1' | 禁用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fgeneratestatus | 生成归集单状态 | bpchar | 1 |  | √ | 'C' | 生成归集单状态,枚举: C :已审核 B :已提交 A :暂存 |
| 18 | fnumber | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fsrcgltableid | 来源总账科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkoac_collplan |  | fid |
| 2 | idx_collplan_fnum |  | fnumber |

---

## 适用经营单元-多选基础资料表 t_xkoac_collplanunit

- **表名称：** 适用经营单元-多选基础资料表
- **表名：** t_xkoac_collplanunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [经营单元 xkoac_unit](../basedata_files/xkoac_unit.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_collplanunit |  | fbasedataid |
| 2 | pk_xkoac_collplanunit |  | fpkid |

---

## 来源总账账簿-多选基础资料表 t_xkoac_collplanglbook

- **表名称：** 来源总账账簿-多选基础资料表
- **表名：** t_xkoac_collplanglbook

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_collplanglbook |  | fbasedataid |
| 2 | pk_xkoac_collplanglbook |  | fpkid |
