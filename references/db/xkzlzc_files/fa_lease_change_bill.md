# 租赁变更单-fa_lease_change_bill

## 租赁变更单-主表 t_fa_lease_change_bill

- **表名称：** 租赁变更单-主表
- **表名：** t_fa_lease_change_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fleasecontractid | 原合同 | int8 | 64 |  | √ | 0 | 租赁合同 fa_lease_contract |
| 11 | feffectivedate | 变更生效日 | timestamp | 0 |  |  | null | 变更生效日 |
| 12 | faftcontractid | 变更后合同 | int8 | 64 |  | √ | 0 | 租赁合同 fa_lease_contract |
| 13 | fchangebakcontractid | 变更备份合同 | int8 | 64 |  | √ | 0 | 租赁合同 fa_lease_contract |
| 14 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 15 | fbefcontractid | 变更前合同 | int8 | 64 |  | √ | 0 | 租赁合同 fa_lease_contract |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 变更项目 fa_change_item |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_lease_chg_items |  | fid |
| 2 | pk_t_fa_lease_chg_items |  | fpkid |
