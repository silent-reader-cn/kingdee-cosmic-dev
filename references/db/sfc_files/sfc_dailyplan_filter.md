# 日计划查询条件(废弃)-sfc_dailyplan_filter

## 日计划查询条件(废弃)-主表 t_sfc_dailyplan_filter

- **表名称：** 日计划查询条件(废弃)-主表
- **表名：** t_sfc_dailyplan_filter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisallocation | 是否已分配 | bpchar | 1 |  | √ | '0' | 是否已分配 |
| 3 | fprocessgroup | 工序组 | int8 | 64 |  | √ | 0 | 工序组(废弃) mpdm_progroup |
| 4 | fzone | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fsrctype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: |
| 8 | fplantime | 计划时间 | timestamp | 0 |  |  | null | 计划时间 |
| 9 | fplanarea | 计划区域 | int8 | 64 |  | √ | 0 | 计划区域 fmm_planningarea |
| 10 | fworkarea | 工作区域 | int8 | 64 |  | √ | 0 | 工作区域 mpdm_area |
| 11 | fordertaskstatus | 工单任务状态 | varchar | 50 |  | √ | ' ' | 工单任务状态,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 12 | fplanendtime | fplanendtime | timestamp | 0 |  |  | null |  |
| 13 | fproject | 项目 | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 14 | fworkstage | 工作类别 | int8 | 64 |  | √ | 0 | 工作类别 mpdm_workcategories |
| 15 | fplanstarttime | fplanstarttime | timestamp | 0 |  |  | null |  |
| 16 | fprofession | 行业 | int8 | 64 |  | √ | 0 | 树形基础资料模板 mpdm_professiona |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_dailyplanfilter_fuser |  | fuser |
| 2 | pk_sfc_dailyplan_filter |  | fid |

---

## 项目-多选基础资料表 t_sfc_dpf_mulproject

- **表名称：** 项目-多选基础资料表
- **表名：** t_sfc_dpf_mulproject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 项目 pmpd_project |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_dpf_mulproject |  | fpkid |
| 2 | idx_sfc_dpf_mulproject_fk |  | fid |
