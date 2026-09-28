# 使用状态变更单-fa_change_usestatus

## 使用状态变更单-主表 t_fa_changebill

- **表名称：** 使用状态变更单-主表
- **表名：** t_fa_changebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsourceid | fsourceid | int8 | 64 |  | √ | 0 |  |
| 8 | fhasvoucher | fhasvoucher | bpchar | 1 |  | √ | '0' |  |
| 9 | fnewchangetype | fnewchangetype | int8 | 64 |  | √ | 0 |  |
| 10 | fvoucherflag | fvoucherflag | bpchar | 1 |  | √ | 'A' |  |
| 11 | fchangetype | 变更类型 | varchar | 50 |  | √ | 'ASSETVALUE' | 变更类型 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fappliantid | 变更申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsourcetype | 来源方式 | bpchar | 1 |  | √ | '1' | 来源方式,枚举: 1 :移动端移交或领用 2 :手工新增 |
| 17 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 18 | fbillno | 变更单号 | varchar | 30 |  | √ | ' ' | 变更单号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_chabil_fbillno |  | fbillno |
| 2 | t_fa_changebill_pkey |  | fid |
| 3 | idx_fa_chabil_org_comb |  | forgid,fchangedate |

---

## 变更详情分录-子表 t_fa_changebillentry_d

- **表名称：** 变更详情分录-子表
- **表名：** t_fa_changebillentry_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fafterrealinfo | fafterrealinfo | int8 | 64 |  | √ | 0 |  |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fbfrchgdesc | 变更前摘要 | varchar | 100 |  |  | ' ' | 变更前摘要 |
| 5 | freason | 变更理由 | varchar | 255 |  |  | ' ' | 变更理由 |
| 6 | faftchg | 变更后 | varchar | 500 |  |  | ' ' | 变更后 |
| 7 | frealcardid | 卡片编号 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 8 | faftchgdesc | 变更后摘要 | varchar | 100 |  |  | ' ' | 变更后摘要 |
| 9 | fbfrchg | 变更前 | varchar | 500 |  |  | ' ' | 变更前 |
| 10 | fbeforefininfo | 变更前财务信息 | int8 | 64 |  | √ | 0 | 财务卡片变更备份 fa_changebak_fin |
| 11 | fbfrorginval | fbfrorginval | numeric | 19 | 6 | √ | 0.000000 |  |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fafterfininfo | 变更后财务信息 | int8 | 64 |  | √ | 0 | 财务卡片变更备份 fa_changebak_fin |
| 14 | ffincardid | 财务卡片 | int8 | 64 |  | √ | 0 | 财务卡片基础资料 fa_card_fin_base |
| 15 | fentryid | 分录 | int8 | 64 |  | √ | 0 | 分录 |
| 16 | faftorginval | faftorginval | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | faftrealcardid | 变更后实物卡片 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 18 | fbeforerealinfo | fbeforerealinfo | int8 | 64 |  | √ | 0 |  |
| 19 | fdepreuseid | fdepreuseid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_chabilent_d_fentryid |  | fentryid |
| 2 | t_fa_changebillentry_d_pkey |  | fdetailid |
| 3 | idx_fa_chabilent_d_fid |  | fid |
