# 课程分配-ippm_courseassign

## 学员-多选基础资料表 t_ippm_assigntrainee

- **表名称：** 学员-多选基础资料表
- **表名：** t_ippm_assigntrainee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_assigntrainee |  | fpkid |
| 2 | idx_ippm_assigntrainee |  | fid |

---

## 课程分配-主表 t_ippm_courseassign

- **表名称：** 课程分配-主表
- **表名：** t_ippm_courseassign

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 任务名称 | varchar | 2000 |  | √ | ' ' | 任务名称 |
| 3 | frolecount | 角色数量 | int4 | 32 |  | √ | 0 | 角色数量 |
| 4 | ftraineecount | 学员数量 | int4 | 32 |  | √ | 0 | 学员数量 |
| 5 | fcourselistid | 课程清单 | int8 | 64 |  | √ | 0 | [课程清单 ippm_courselist](../ippm_files/ippm_courselist.md) |
| 6 | fnumber | 任务编码 | varchar | 50 |  | √ | ' ' | 任务编码 |
| 7 | ftotal | 学员总数 | int4 | 32 |  | √ | 0 | 学员总数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ippm_courseassign |  | fcourselistid |
| 2 | pk_t_ippm_courseassign |  | fid |

---

## 角色-多选基础资料表 t_ippm_assignrole

- **表名称：** 角色-多选基础资料表
- **表名：** t_ippm_assignrole

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuserstr | fuserstr | text | 0 |  |  | null |  |
| 3 | fbasedataid | fbasedataid | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 4 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ippm_assignrole |  | fpkid |
| 2 | idx_ippm_assignrole |  | fid |
