# 其他税费共享方案-totf_edit_sharingplan

## 共享方案-子表 t_totf_sharingplan

- **表名称：** 共享方案-子表
- **表名：** t_totf_sharingplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fautoshar | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 12 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 13 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_sharingplan |  | fentryid |
| 2 | idx_taxc_shareplan_id |  | fid |

---

## 规则-子表 t_totf_sharingplan_rules

- **表名称：** 规则-子表
- **表名：** t_totf_sharingplan_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: income :收入规则 rollout :进项转出规则 diff :差额扣除规则 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
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
| 1 | idx_taxc_share_entry_type_rule |  | fentryid,ftype,fruleid |
| 2 | pk_totf_sharingplan_rules |  | fdetailid |

---

## 被共享组织-子表 t_totf_sharingplan_orgs

- **表名称：** 被共享组织-子表
- **表名：** t_totf_sharingplan_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_sharingplan_orgs |  | fdetailid |
| 2 | idx_taxc_shareplan_org_entryid |  | fentryid |

---

## 共享方案-多语言表 t_totf_sharingplan_l

- **表名称：** 共享方案-多语言表
- **表名：** t_totf_sharingplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 共享方案名 | varchar | 50 |  | √ | ' ' | 共享方案名 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_sharingplan_l |  | fpkid |
| 2 | idx_totf_sharingplan_l_0 |  | fentryid,flocaleid |

---

## 其他税费共享方案-主表 t_totf_sharingplan_edit

- **表名称：** 其他税费共享方案-主表
- **表名：** t_totf_sharingplan_edit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsharetype | 共享方案类型 | varchar | 50 |  | √ | ' ' | 共享方案类型,枚举: sljsjj :水利基金不含税收入 whsyjsf :文化事业建设费应征收入 |
| 4 | fautoshar | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 5 | fplanname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_sharingplan_edit |  | fid |
| 2 | idx_taxc_shareplan_edit_org |  | forgid |
