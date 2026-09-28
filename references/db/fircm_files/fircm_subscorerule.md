# 审核扣分规则-fircm_subscorerule

## 审核扣分规则-主表 t_fircm_subscorerule

- **表名称：** 审核扣分规则-主表
- **表名：** t_fircm_subscorerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 类别 | int8 | 64 |  | √ | 0 | [审核扣分规则分组 fircm_subscorerulegroup](../fircm_files/fircm_subscorerulegroup.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsublevel | 减分至信用等级 | int8 | 64 |  | √ | 0 | [信用等级 task_creditlevel](../fircm_files/task_creditlevel.md) |
| 7 | fdescription | 描述 | varchar | 250 |  | √ | ' ' | 描述 |
| 8 | fsubscorestr | 每次扣分值 | varchar | 50 |  | √ | ' ' | 每次扣分值 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fsign | fsign | varchar | 2000 |  | √ | ' ' |  |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | ftype | 审核类型 | varchar | 50 |  | √ | ' ' | 审核类型,枚举: 0 :不通过 1 :瑕疵通过 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fsubscore | 减分 | numeric | 19 | 6 | √ | 0 | 减分 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | fflag | 是：降级，否：减分 | bpchar | 1 |  | √ | '1' | 是：降级，否：减分 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fircm_subscorerule_fnumber |  | fnumber |
| 2 | pk_t_fircm_subscorerule |  | fid |

---

## 审核扣分规则-多语言表 t_fircm_subscorerule_l

- **表名称：** 审核扣分规则-多语言表
- **表名：** t_fircm_subscorerule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 250 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 32 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fircm_subscorerule_l |  | fpkid |
| 2 | idx_fircm_subscorerule_l |  | flocaleid |
