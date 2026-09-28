# 项目标准化设置-plm_pm_standset_project

## 项目变更单据体-多语言表 t_plm_pm_changeset_entry_l

- **表名称：** 项目变更单据体-多语言表
- **表名：** t_plm_pm_changeset_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fchangescope | 变更范围 | varchar | 80 |  | √ | ' ' | 变更范围 |
| 2 | fscopedes | 范围详述 | varchar | 500 |  | √ | ' ' | 范围详述 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_changeset_entry_l_0 |  | fentryid,flocaleid |
| 2 | pk_plm_pm_changeset_entry_l |  | fpkid |

---

## 项目阶段单据体-子表 t_plm_pm_projectphase

- **表名称：** 项目阶段单据体-子表
- **表名：** t_plm_pm_projectphase

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fduration | 计划工期（天） | numeric | 10 | 1 | √ | 0 | 计划工期（天） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fphasename | 名称 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 5 | fendtime | 计划结束时间 | timestamp | 0 |  |  | null | 计划结束时间 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fstarttime | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_projectphase_fk |  | fid |
| 2 | pk_plm_pm_projectphase |  | fentryid |

---

## 气泡图单据体-多语言表 t_plm_pm_standset_entry_l

- **表名称：** 气泡图单据体-多语言表
- **表名：** t_plm_pm_standset_entry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 4 | ftaskgroupname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_standset_entry_l_0 |  | fentryid,flocaleid |
| 2 | pk_plm_pm_standset_entry_l |  | fpkid |

---

## 项目变更单据体-子表 t_plm_pm_changeset_entry

- **表名称：** 项目变更单据体-子表
- **表名：** t_plm_pm_changeset_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangescope | 变更范围 | varchar | 50 |  | √ | ' ' | 变更范围 |
| 3 | fscopedes | 范围详述 | varchar | 50 |  | √ | ' ' | 范围详述 |
| 4 | fischange | 修改必须走变更 | bpchar | 1 |  | √ | '0' | 修改必须走变更 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_changeset_entry_fk |  | fid |
| 2 | pk_plm_pm_changeset_entry |  | fentryid |

---

## 项目标准化设置-主表 t_plm_pm_standset

- **表名称：** 项目标准化设置-主表
- **表名：** t_plm_pm_standset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fitemclasstypefield | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: plm_ipd_project :项目实例 plm_pm_projectcopy :项目副本 plm_pm_projectbaseline :项目基线 plm_pm_projecttpl :项目模板 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fprojectkind | 项目分类 | varchar | 50 |  | √ | ' ' | 项目分类 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_standset |  | fid |
| 2 | idx_plm_pm_standset_m0 |  | fbillno |

---

## 气泡图单据体-子表 t_plm_pm_standset_entry

- **表名称：** 气泡图单据体-子表
- **表名：** t_plm_pm_standset_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftaskgroupname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_standset_entry |  | fentryid |
| 2 | idx_plm_pm_standset_entry_fk |  | fid |
