# 营销周期使用规则-ocdbd_assesperiod_set

## 分录-子表 t_ocdbd_aperiodset_ee

- **表名称：** 分录-子表
- **表名：** t_ocdbd_aperiodset_ee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdeparmentid | 部门编码 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fperiodgroupid | 营销周期分组 | int8 | 64 |  | √ | 0 | [时间周期分组 ocdbd_timeperiod_group](../ocdbd_files/ocdbd_timeperiod_group.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_aperiodset_ee |  | fentryid |
| 2 | idx_ocdbd_aperiodsetee_fid |  | fid |

---

## 营销周期使用规则-主表 t_ocdbd_aperiodset

- **表名称：** 营销周期使用规则-主表
- **表名：** t_ocdbd_aperiodset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdefaultperiodgroupid | 统一营销周期分组 | int8 | 64 |  | √ | 0 | [时间周期分组 ocdbd_timeperiod_group](../ocdbd_files/ocdbd_timeperiod_group.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ocdbd_aperiodset |  | fdefaultperiodgroupid |
| 2 | pk_ocdbd_aperiodset |  | fid |
