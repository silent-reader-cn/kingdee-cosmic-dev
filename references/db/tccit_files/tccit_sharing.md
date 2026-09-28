# 所得税共享方案-tccit_sharing

## 所得税共享方案-多语言表 t_tccit_sharing_l

- **表名称：** 所得税共享方案-多语言表
- **表名：** t_tccit_sharing_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
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

## 单据体-子表 t_tccit_sharing_rules

- **表名称：** 单据体-子表
- **表名：** t_tccit_sharing_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftype | 规则类型 | varchar | 30 |  | √ | ' ' | 规则类型,枚举: income :优惠项目取数 |
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
| 1 | idx_tccit_sharing_rules_fk |  | fentryid |
| 2 | t_tccit_sharing_rules_pkey |  | fdetailid |

---

## 单据体-子表 t_tccit_sharing_orgs

- **表名称：** 单据体-子表
- **表名：** t_tccit_sharing_orgs

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
| 1 | idx_tccit_sharing_orgs |  | fentryid |
| 2 | t_tccit_sharing_orgs_pkey |  | fdetailid |

---

## 所得税共享方案-主表 t_tccit_sharing

- **表名称：** 所得税共享方案-主表
- **表名：** t_tccit_sharing

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 共享方案维护ID | int8 | 64 |  | √ | 0 | 共享方案维护ID |
| 2 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 3 | fautoshar | 自动共享 | bpchar | 1 |  | √ | '0' | 自动共享 |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fnumber | 编码 | bpchar | 30 |  | √ | ' ' | 编码 |
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
