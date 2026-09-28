# 智能计算设置-invp_smartcalccfg

## 智能计算设置-主表 t_invp_smartcalccfg

- **表名称：** 智能计算设置-主表
- **表名：** t_invp_smartcalccfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvlevel | finvlevel | int8 | 64 |  | √ | 0 |  |
| 3 | fcalcrulecfg | 因子计算规则 | int8 | 64 |  | √ | 0 | 因子计算规则 invp_calrulecfg |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_smartcalccfg_finvlevel |  | finvlevel |
| 2 | pk_invp_smartcalccfg |  | fid |

---

## 因子取数方案-多选基础资料表 t_invp_smartcalccfg_query

- **表名称：** 因子取数方案-多选基础资料表
- **表名：** t_invp_smartcalccfg_query

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 因子取数方案 invp_queryschema |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_smartcalccfg_query |  | fpkid |
| 2 | idx_invp_smartcalccfg_query_fid |  | fid |
