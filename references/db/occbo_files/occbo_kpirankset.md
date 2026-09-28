# 达成率权重设置-occbo_kpirankset

## 达成率权重设置-多语言表 t_occbo_kpirankset_l

- **表名称：** 达成率权重设置-多语言表
- **表名：** t_occbo_kpirankset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | KPI权重名称 | varchar | 80 |  | √ | ' ' | KPI权重名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_kpirankset_l |  | fpkid |
| 2 | idx_occbo_kpirankset_l |  | fid,flocaleid |

---

## 达成率权重设置-主表 t_occbo_kpirankset

- **表名称：** 达成率权重设置-主表
- **表名：** t_occbo_kpirankset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | KPI权重名称 | varchar | 80 |  | √ | ' ' | KPI权重名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | froleid | 全渠道用户角色 | int8 | 64 |  | √ | 0 | [全渠道用户角色 ocdbd_role](../ocdbd_files/ocdbd_role.md) |
| 6 | fyearid | 考核年度 | int8 | 64 |  | √ | 0 | [营销周期 ocdbd_assess_period](../ocdbd_files/ocdbd_assess_period.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | ftype | 权重类型 | bpchar | 1 |  | √ | 'A' | 权重类型,枚举: A :人员 B :部门 C :省区 D :大区 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | KPI权重编码 | varchar | 80 |  | √ | ' ' | KPI权重编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_kpirankset |  | fid |
| 2 | idx_occbo_kpirankset |  | froleid |

---

## KPI权重-子表 t_occbo_kpirank_entry

- **表名称：** KPI权重-子表
- **表名：** t_occbo_kpirank_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fclosetoprate | 封顶比例% | numeric | 23 | 10 | √ | 0 | 封顶比例% |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fpercentage | 考核权重比例% | numeric | 23 | 10 | √ | 0 | 考核权重比例% |
| 6 | fkpiid | kpi编码 | int8 | 64 |  | √ | 0 | [KPI occbo_kpi_base](../occbo_files/occbo_kpi_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_kpirank_entry |  | fentryid |
| 2 | idx_occbo_kpirank_entry |  | fid,fkpiid |
