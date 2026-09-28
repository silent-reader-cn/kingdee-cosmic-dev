# 租赁变更单-fa_lease_change_bill

## 租赁变更单-主表 t_fa_lease_change_bill

- **表名称：** 租赁变更单-主表
- **表名：** t_fa_lease_change_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funconfirmchargeb | 变更前未确认融资费用 | numeric | 19 | 6 | √ | 0 | 变更前未确认融资费用 |
| 3 | funconfirmchargea | 变更后未确认融资费用 | numeric | 19 | 6 | √ | 0 | 变更后未确认融资费用 |
| 4 | forgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fleaseliabbefore | 变更前租赁负债现值 | numeric | 19 | 6 | √ | 0 | 变更前租赁负债现值 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fcurrencyafter | 变更后币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | feffectivedate | 变更生效日 | timestamp | 0 |  |  | null | 变更生效日 |
| 10 | faftcontractid | 变更后合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 11 | fchangebakcontractid | 变更备份合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fleaseliaboribefore | 变更前租赁负债原值 | numeric | 19 | 6 | √ | 0 | 变更前租赁负债原值 |
| 14 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fleaseliaboriafter | 变更后租赁负债原值 | numeric | 19 | 6 | √ | 0 | 变更后租赁负债原值 |
| 19 | fleaseliabafter | 变更后租赁负债现值 | numeric | 19 | 6 | √ | 0 | 变更后租赁负债现值 |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fleasecontractid | 原合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 22 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 23 | fbefcontractid | 变更前合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fcurrencybefore | 变更前币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_lease_change_bill |  | fid |
| 2 | idx_fa_leasechange |  | forgid,fleasecontractid,feffectivedate |

---

## 变更项目-多选基础资料表 t_fa_lease_chg_items

- **表名称：** 变更项目-多选基础资料表
- **表名：** t_fa_lease_chg_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [变更项目 fa_change_item](../fa_files/fa_change_item.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_lease_chg_items |  | fpkid |
| 2 | idx_fa_lease_chg_items |  | fid |
