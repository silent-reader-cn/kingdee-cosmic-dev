# 已废弃-申报共享方案-tcvat_edit_sharingplan

## 共享方案-子表 t_tcvat_sharingplan

- **表名称：** 共享方案-子表
- **表名：** t_tcvat_sharingplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | fremark | varchar | 400 |  | √ | ' ' |  |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fname | fname | varchar | 400 |  | √ | ' ' |  |
| 5 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fautoshar | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fplanname | fplanname | varchar | 100 |  | √ | ' ' |  |
| 11 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 12 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 13 | fstatus | fstatus | varchar | 30 |  | √ | ' ' |  |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 16 | fenable | fenable | varchar | 30 |  | √ | ' ' |  |
| 17 | ftaxpayertype | 文本 | varchar | 30 |  | √ | ' ' | 文本 |
| 18 | fnumber | fnumber | varchar | 60 |  | √ | ' ' |  |
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

## 规则-子表 t_tcvat_sharingplan_rules

- **表名称：** 规则-子表
- **表名：** t_tcvat_sharingplan_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: income :收入规则 rollout :进项转出规则 diff :差额扣除规则 |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
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

## 共享方案-多语言表 t_tcvat_sharingplan_l

- **表名称：** 共享方案-多语言表
- **表名：** t_tcvat_sharingplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 共享方案名 | varchar | 100 |  | √ | ' ' | 共享方案名 |
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

---

## 被共享组织-子表 t_tcvat_sharingplan_orgs

- **表名称：** 被共享组织-子表
- **表名：** t_tcvat_sharingplan_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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

## 已废弃-申报共享方案-主表 t_tcvat_sharingplan_edit

- **表名称：** 已废弃-申报共享方案-主表
- **表名：** t_tcvat_sharingplan_edit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fautoshar | fautoshar | bpchar | 1 |  | √ | '0' |  |
| 4 | fplanname | fplanname | varchar | 100 |  | √ | ' ' |  |
| 5 | fsynsrlx | fsynsrlx | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcvat_sharingplan_edit |  | forgid |
| 2 | t_tcvat_sharingplan_edit_pkey |  | fid |
