# 共享方案-tccit_rule_sharing

## 共享方案-多语言表 t_tccit_sharing_l

- **表名称：** 共享方案-多语言表
- **表名：** t_tccit_sharing_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 共享方案名 | varchar | 50 |  | √ | ' ' | 共享方案名 |
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
| 1 | idx_tccit_sharing_l_0 |  | fentryid,flocaleid |
| 2 | t_tccit_sharing_l_pkey |  | fpkid |

---

## 规则-子表 t_tccit_sharing_rules

- **表名称：** 规则-子表
- **表名：** t_tccit_sharing_rules

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
| 1 | idx_tccit_sharing_rules_fk |  | fentryid |
| 2 | t_tccit_sharing_rules_pkey |  | fdetailid |

---

## 被共享组织-子表 t_tccit_sharing_orgs

- **表名称：** 被共享组织-子表
- **表名：** t_tccit_sharing_orgs

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
| 1 | idx_tccit_sharing_orgs |  | fentryid |
| 2 | t_tccit_sharing_orgs_pkey |  | fdetailid |

---

## 共享方案-主表 t_tccit_sharing_edit

- **表名称：** 共享方案-主表
- **表名：** t_tccit_sharing_edit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsharetype | 共享方案类型 | varchar | 50 |  | √ | ' ' | 共享方案类型,枚举: yj :预缴 hj :汇缴 |
| 4 | fautoshar | fautoshar | bpchar | 1 |  | √ | '0' |  |
| 5 | fplanname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_sharing_edit |  | forgid |
| 2 | t_tccit_sharing_edit_pkey |  | fid |

---

## 共享方案-子表 t_tccit_sharing

- **表名称：** 共享方案-子表
- **表名：** t_tccit_sharing

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fautoshar | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fnumber | fnumber | bpchar | 30 |  | √ | ' ' |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_sharing_fk |  | fid |
| 2 | t_tccit_sharing_pkey |  | fentryid |
