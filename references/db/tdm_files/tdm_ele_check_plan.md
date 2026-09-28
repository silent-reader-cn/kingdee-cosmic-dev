# 元素核对方案-tdm_ele_check_plan

## 元素核对方案-主表 t_tdm_ele_check_plan

- **表名称：** 元素核对方案-主表
- **表名：** t_tdm_ele_check_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fremark | 备注 | varchar | 256 |  | √ | ' ' | 备注 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcheckrange | 核对周期（单位：天） | int8 | 64 |  | √ | 0 | 核对周期（单位：天） |
| 6 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fplanno | 方案编码 | varchar | 50 |  | √ | ' ' | 方案编码 |
| 8 | fplanname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fplandateend | 核对日期范围.结束 | timestamp | 0 |  |  | null | 核对日期范围.结束 |
| 11 | fplandatestart | 核对日期范围.开始 | timestamp | 0 |  |  | null | 核对日期范围.开始 |
| 12 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 13 | fruntime | 方案最近执行时间 | timestamp | 0 |  |  | null | 方案最近执行时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_ele_check_plan |  | fid |
| 2 | idx_tdm_ele_check_plan |  | fplanno |

---

## 核对元素范围-多选基础资料表 t_tdm_ele_check_plan_ele

- **表名称：** 核对元素范围-多选基础资料表
- **表名：** t_tdm_ele_check_plan_ele

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [元素设置 tdm_element_group](../tdm_files/tdm_element_group.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_ele_check_plan_ele |  | fpkid |
| 2 | idx_tdm_ele_check_plan_ele_fk |  | fid |

---

## 核对组织范围-多选基础资料表 t_tdm_ele_check_plan_orgs

- **表名称：** 核对组织范围-多选基础资料表
- **表名：** t_tdm_ele_check_plan_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_ele_check_plan_orgs_fk |  | fid |
| 2 | pk_tdm_ele_check_plan_orgs |  | fpkid |
