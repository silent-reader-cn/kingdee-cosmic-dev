# 方案设置-pm_calparam

## 仓库-多选基础资料表 t_pm_assortparamwarehouse

- **表名称：** 仓库-多选基础资料表
- **表名：** t_pm_assortparamwarehouse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pm_assortparamwarehouse |  | fpkid |
| 2 | idx_pm_assort_fbasedataid |  | fbasedataid |
| 3 | idx_pm_assort_fid |  | fid |

---

## 方案设置-主表 t_pm_assortparamplan

- **表名称：** 方案设置-主表
- **表名：** t_pm_assortparamplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenablebomlossrate | BOM损耗率参与需求计算 | bpchar | 1 |  | √ | '0' | BOM损耗率参与需求计算 |
| 3 | fenableavailablestock | 即时库存作为供给 | bpchar | 1 |  | √ | '0' | 即时库存作为供给 |
| 4 | fislastcal | 是否上次计算记录 | bpchar | 1 |  | √ | '0' | 是否上次计算记录 |
| 5 | fenablesafestock | 安全库存作为需求 | bpchar | 1 |  | √ | '0' | 安全库存作为需求 |
| 6 | fenablemateriallist | 使用用料清单计算 | bpchar | 1 |  | √ | '0' | 使用用料清单计算 |
| 7 | fplanname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 8 | fenablelastbomver | 使用最新BOM编码计算 | bpchar | 1 |  | √ | '0' | 使用最新BOM编码计算 |
| 9 | fenablemakenotexpand | 自制件不展开 | bpchar | 1 |  | √ | '0' | 自制件不展开 |
| 10 | fenablelessthanzero | 展示净需求为0的结果 | bpchar | 1 |  | √ | '0' | 展示净需求为0的结果 |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fenableauxpropsum | 辅助属性分组汇总 | bpchar | 1 |  | √ | '0' | 辅助属性分组汇总 |
| 14 | fenableoutsrcnotexpand | 委外件不展开 | bpchar | 1 |  | √ | '0' | 委外件不展开 |
| 15 | flossrateformula | 损耗计算公式 | bpchar | 1 |  | √ | 'A' | 损耗计算公式,枚举: A :标准用料*（1+变动损耗率） B :标准用料/（1-变动损耗率） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_assort_islastcal |  | fislastcal |
| 2 | idx_pm_assort_creatorid |  | fcreatorid |
| 3 | pk_t_pm_assortparamplan |  | fid |
