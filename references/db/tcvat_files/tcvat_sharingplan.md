# 已废弃-共享方案-tcvat_sharingplan

## 单据体-子表 t_tcvat_sharingplan_rules

- **表名称：** 单据体-子表
- **表名：** t_tcvat_sharingplan_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: income :收入规则 rollout :转出规则 diff :差额扣除规则 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fruleid | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_sharingplan_rules_fk |  | fentryid |
| 2 | t_tcvat_sharingplan_rules_pkey |  | fdetailid |

---

## 单据体-子表 t_tcvat_sharingplan_orgs

- **表名称：** 单据体-子表
- **表名：** t_tcvat_sharingplan_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 税务 | int8 | 64 |  | √ | 0 | [税务组织实体 tctb_org_entity](../tctb_files/tctb_org_entity.md) |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_sharingplan_orgs_pkey |  | fdetailid |
| 2 | idx_tcvat_sharingplan_orgs_fk |  | fentryid |

---

## 已废弃-共享方案-主表 t_tcvat_sharingplan

- **表名称：** 已废弃-共享方案-主表
- **表名：** t_tcvat_sharingplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 400 |  | √ | ' ' | 备注 |
| 2 | fid | 共享方案维护ID | int8 | 64 |  | √ | 0 | 共享方案维护ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 400 |  | √ | ' ' |  |
| 5 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [税务组织实体 tctb_org_entity](../tctb_files/tctb_org_entity.md) |
| 8 | fautoshar | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 9 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 10 | fplanname | fplanname | varchar | 100 |  | √ | ' ' |  |
| 11 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | ftaxpayertype | 适用纳税人类型 | varchar | 30 |  | √ | ' ' | 适用纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fbillno | fbillno | varchar | 60 |  | √ | ' ' |  |
| 21 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_sharingplan_pkey |  | fentryid |
| 2 | idx_t_tcvat_sharingplan |  | fid |

---

## 已废弃-共享方案-多语言表 t_tcvat_sharingplan_l

- **表名称：** 已废弃-共享方案-多语言表
- **表名：** t_tcvat_sharingplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tcvat_sharingplan_l_pkey |  | fpkid |
| 2 | idx_tcvat_sharingplan_l_0 |  | fentryid,flocaleid |
